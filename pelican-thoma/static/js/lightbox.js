/* Lightbox for figures: a click on a figure's image shows it as large as the window
   allows, with its caption. In a gallery, arrow buttons, arrow keys and swiping move
   through its figures and those of the galleries directly before and after it.
   Escape, the close button or a click beside the image close it. Only links to image
   files open here; without JavaScript (or with a modifier key) the link opens the file. */
(function () {
    'use strict';

    if (!document.querySelector('figure > a img') || typeof HTMLDialogElement !== 'function') { return; }

    var TEXT = {
        en: { dialog: 'Image viewer', close: 'Close', prev: 'Previous image', next: 'Next image',
              original: 'Open original file', error: 'The image could not be loaded.' },
        de: { dialog: 'Bildansicht', close: 'Schließen', prev: 'Vorheriges Bild', next: 'Nächstes Bild',
              original: 'Originaldatei öffnen', error: 'Das Bild konnte nicht geladen werden.' }
    };
    var ICONS = {
        close: '<path d="M6 6l12 12M18 6L6 18"/>',
        prev: '<path d="M15 5l-7 7 7 7"/>',
        next: '<path d="M9 5l7 7-7 7"/>',
        original: '<path d="M14 4h6v6M20 4l-9 9M18 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h5"/>'
    };
    var t = TEXT[document.documentElement.lang.slice(0, 2) === 'de' ? 'de' : 'en'];
    var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
    var canMorph = typeof document.startViewTransition === 'function';

    function button(action, extraClass) {
        return '<button type="button" class="lightbox-btn ' + extraClass + '" data-action="' + action + '"' +
            ' aria-label="' + t[action] + '" title="' + t[action] + '">' + icon(action) + '</button>';
    }
    function icon(name) {
        return '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2"' +
            ' stroke-linecap="round" stroke-linejoin="round">' + ICONS[name] + '</svg>';
    }

    var dialog = document.createElement('dialog');
    dialog.className = 'lightbox';
    dialog.setAttribute('aria-label', t.dialog);
    dialog.innerHTML =
        '<div class="lightbox-bar">' +
            '<span class="lightbox-count" aria-live="polite"></span>' +
            '<div class="lightbox-actions">' +
                '<a class="lightbox-btn" data-action="original" aria-label="' + t.original + '" title="' + t.original + '">' + icon('original') + '</a>' +
                button('close', '') +
            '</div>' +
        '</div>' +
        '<div class="lightbox-stage">' +
            '<div class="lightbox-frame"><img class="lightbox-img" alt=""></div>' +
            '<p class="lightbox-error">' + t.error + '</p>' +
            button('prev', 'lightbox-prev') +
            button('next', 'lightbox-next') +
        '</div>' +
        '<div class="lightbox-caption"></div>';
    document.body.appendChild(dialog);

    var count = dialog.querySelector('.lightbox-count');
    var original = dialog.querySelector('[data-action="original"]');
    var bar = dialog.querySelector('.lightbox-bar');
    var stage = dialog.querySelector('.lightbox-stage');
    var frame = dialog.querySelector('.lightbox-frame');
    var img = dialog.querySelector('.lightbox-img');
    var caption = dialog.querySelector('.lightbox-caption');

    var figures = [];   // figures of the open gallery, or the one figure opened
    var index = 0;      // figure shown
    var request = 0;    // counts show() calls, so a slow image cannot overwrite a newer one

    var IMAGE_FILE = /\.(?:png|jpe?g|gif|webp|avif|svg)$/i;

    // the figure's link to its image file, if it has one (some figures link to a web page)
    function imageLink(figure) {
        var link = figure.querySelector(':scope > a[href]');
        var thumb = link && link.querySelector('img');
        if (!thumb) { return null; }
        return IMAGE_FILE.test(link.pathname) || link.href === thumb.currentSrc ? link : null;
    }
    function thumbOf(figure) { return imageLink(figure).querySelector('img'); }
    function hrefOf(figure) { return imageLink(figure).href; }
    function inView(el) {
        var r = el.getBoundingClientRect();
        return r.bottom > 0 && r.top < window.innerHeight;
    }
    function animate() { return !reduceMotion.matches; }

    function show(i, direction) {
        var mine = ++request;
        var figure = figures[i];
        var href = hrefOf(figure);
        var loader = new Image();
        var slow = setTimeout(function () { stage.classList.add('is-loading'); }, 200);

        index = i;
        count.textContent = (i + 1) + ' / ' + figures.length;
        original.href = href;
        loader.src = href;

        function apply(ok) {
            clearTimeout(slow);
            if (mine !== request) { return; }
            var figcaption = figure.querySelector('figcaption');
            stage.classList.remove('is-loading');
            stage.classList.toggle('is-error', !ok);
            img.src = href;
            img.alt = thumbOf(figure).alt;
            if (ok) {
                img.width = loader.naturalWidth;
                img.height = loader.naturalHeight;
            }
            frame.classList.toggle('ai-generated', figure.classList.contains('ai-generated'));
            frame.classList.toggle('ai-modified', figure.classList.contains('ai-modified'));
            caption.replaceChildren();
            if (figcaption) {
                figcaption.childNodes.forEach(function (node) { caption.appendChild(node.cloneNode(true)); });
            }
            caption.hidden = !figcaption;
            if (direction && animate()) {
                frame.animate(
                    [{ opacity: 0, transform: 'translateX(' + (direction * 2.5) + 'rem)' }, { opacity: 1, transform: 'none' }],
                    { duration: 280, easing: 'cubic-bezier(0.2, 0.8, 0.2, 1)' });
            }
            if (figures.length > 1) {
                [i - 1, i + 1].forEach(function (j) {
                    new Image().src = hrefOf(figures[(j + figures.length) % figures.length]);
                });
            }
        }

        // an image already in memory (usually the clicked thumbnail itself) is shown at once
        if (loader.complete && loader.naturalWidth) { apply(true); return Promise.resolve(); }
        return loader.decode().then(function () { apply(true); }, function () { apply(false); });
    }

    function step(direction) {
        if (figures.length > 1) {
            show((index + direction + figures.length) % figures.length, direction);
        }
    }

    // Morph between thumbnail and lightbox image with a view transition where the
    // browser supports it; otherwise, and with reduced motion, switch instantly.
    function morph(from, to, update) {
        if (!canMorph || !animate() || !inView(from)) { return update(); }
        from.style.viewTransitionName = 'lightbox-image';
        var transition = document.startViewTransition(function () {
            from.style.viewTransitionName = '';
            to.style.viewTransitionName = 'lightbox-image';
            return update();
        });
        transition.finished.finally(function () { to.style.viewTransitionName = ''; });
    }

    function isGallery(el) { return el && el.classList.contains('gallery'); }

    // galleries directly after each other (rows of one collection) are paged as one
    function sequenceOf(figure) {
        var gallery = figure.parentElement, first = gallery, all = [];
        if (!isGallery(gallery)) { return [figure]; }
        while (isGallery(first.previousElementSibling)) { first = first.previousElementSibling; }
        for (var g = first; isGallery(g); g = g.nextElementSibling) {
            Array.prototype.forEach.call(g.children, function (el) {
                if (el.tagName === 'FIGURE' && imageLink(el)) { all.push(el); }
            });
        }
        return all;
    }

    function open(figure) {
        figures = sequenceOf(figure);
        dialog.classList.toggle('is-single', figures.length < 2);
        img.removeAttribute('src');   // no stale image from the last gallery
        morph(thumbOf(figure), img, function () {
            var shown = show(figures.indexOf(figure), 0);
            dialog.showModal();
            // wait briefly for the image, so the morph ends on it instead of an empty frame
            return Promise.race([shown, new Promise(function (resolve) { setTimeout(resolve, 400); })]);
        });
    }

    function close() {
        var thumb = thumbOf(figures[index]);
        if (stage.classList.contains('is-error') || !inView(thumb)) {
            dialog.close();
            return;
        }
        morph(img, thumb, function () { dialog.close(); });
    }

    document.addEventListener('click', function (event) {
        var link = event.target.closest('figure > a[href]');
        if (!link || link.closest('.lightbox') || imageLink(link.parentElement) !== link || event.defaultPrevented ||
            event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) { return; }
        event.preventDefault();
        open(link.parentElement);
    });

    var swipedAt = 0;
    dialog.addEventListener('click', function (event) {
        var control = event.target.closest('[data-action]');
        var action = control && control.getAttribute('data-action');
        if (action === 'prev') { step(-1); }
        else if (action === 'next') { step(1); }
        else if (action === 'close') { close(); }
        else if ((event.target === dialog || event.target === stage || event.target === bar) &&
                 Date.now() - swipedAt > 400) { close(); }
    });

    dialog.addEventListener('keydown', function (event) {
        if (event.key === 'ArrowLeft') { step(-1); }
        else if (event.key === 'ArrowRight') { step(1); }
        else if (event.key === 'Escape') { close(); }
        else { return; }
        event.preventDefault();
    });

    // after any close (also the Android back gesture): focus the thumbnail shown last
    dialog.addEventListener('close', function () {
        var link = figures[index] && imageLink(figures[index]);
        if (link) { link.focus({ preventScroll: true }); }
    });

    var start = null;
    stage.addEventListener('pointerdown', function (event) {
        start = event.pointerType === 'mouse' ? null : { x: event.clientX, y: event.clientY };
    });
    stage.addEventListener('pointerup', function (event) {
        if (!start) { return; }
        var dx = event.clientX - start.x, dy = event.clientY - start.y;
        start = null;
        if (Math.abs(dx) > 50 && Math.abs(dx) > 1.5 * Math.abs(dy)) {
            swipedAt = Date.now();
            step(dx < 0 ? 1 : -1);
        }
    });
    stage.addEventListener('pointercancel', function () { start = null; });
})();
