/* Marks the contents entry of the section being read with aria-current, while scrolling
   and after a click on an entry. A section is current once its heading has passed the
   upper third of the window. A clicked entry is marked even if the next heading follows
   so closely that it has passed that line too. When the contents scroll on their own
   (long lists in the sidebar), they follow the marked entry; the page does not move.
   In the sidebar, "Hide" closes the contents. That choice is remembered for the sidebar
   only; _includes/toc.html applies it on the next page before the first paint. */
(function () {
    'use strict';

    var toc = document.querySelector('.toc');
    if (!toc) { return; }

    var current = null, clicked = null, pending = false;
    var sidebar = window.matchMedia('screen and (min-width: 64rem)'); // as in thoma.css
    toc.addEventListener('toggle', function () {
        if (toc.open && current) { reveal(current); }
        if (!sidebar.matches) { return; }
        try {
            if (toc.open) { localStorage.removeItem('toc-sidebar'); } else { localStorage.setItem('toc-sidebar', 'closed'); }
        } catch (e) { /* storage blocked: the choice lasts for this page only */ }
    });

    var entries = [];
    toc.querySelectorAll('a[href^="#"]').forEach(function (link) {
        var heading = document.getElementById(decodeURIComponent(link.hash.slice(1)));
        if (heading) { entries.push({ link: link, heading: heading }); }
    });
    if (!entries.length) { return; }

    // Not scrollIntoView: it would scroll the page as well.
    function reveal(link) {
        var box = toc.getBoundingClientRect(), rect = link.getBoundingClientRect();
        if (rect.top < box.top) { toc.scrollTop -= box.top - rect.top + 24; }
        else if (rect.bottom > box.bottom) { toc.scrollTop += rect.bottom - box.bottom + 24; }
    }

    function mark(link) {
        if (link === current) { return; }
        if (current) { current.removeAttribute('aria-current'); }
        current = link;
        if (link) { link.setAttribute('aria-current', 'true'); reveal(link); }
    }

    function update() {
        pending = false;
        if (clicked) { mark(clicked); clicked = null; return; }
        var line = window.innerHeight / 3, found = null;
        for (var i = 0; i < entries.length && entries[i].heading.getBoundingClientRect().top <= line; i++) {
            found = entries[i].link;
        }
        mark(found);
    }

    function schedule() {
        if (!pending) { pending = true; window.requestAnimationFrame(update); }
    }

    toc.addEventListener('click', function (event) {
        var link = event.target.closest('a[href^="#"]');
        if (link) { clicked = link; schedule(); }
    });
    window.addEventListener('scroll', schedule, { passive: true });
    window.addEventListener('resize', schedule);
    window.addEventListener('load', schedule); // web fonts and images may have moved the headings
    update();
})();
