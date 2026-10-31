/* Large tables. A table wider than the text column scrolls in its own box that fits the
   window: its header rows stick to the top of the box and, if the first column is narrow
   enough, that column sticks to the left, so the labels stay visible in both directions.
   A button above it shows the table in a dialog that fills the window; Escape, the close
   button or a click on a link to a footnote close it again; the arrow, page and Home/End
   keys scroll the table there. Scrolling in the box snaps,
   so a full row and a full column start right after the sticky header and first column.
   A table that is only taller than the window scrolls with the page, and its header rows
   stick below the site header. Without JavaScript a wide table only scrolls sideways. */
(function () {
    'use strict';

    if (typeof HTMLDialogElement !== 'function' || typeof ResizeObserver !== 'function') { return; }

    var TEXT = {
        en: { maximize: 'Maximize', maximizeLabel: 'Show the table in the whole window', close: 'Close', dialog: 'Table' },
        de: { maximize: 'Maximieren', maximizeLabel: 'Tabelle im ganzen Fenster zeigen', close: 'Schließen', dialog: 'Tabelle' }
    };
    var ICONS = {
        maximize: '<path d="M14 4h6v6M10 20H4v-6M20 4l-7 7M4 20l7-7"/>',
        close: '<path d="M6 6l12 12M18 6L6 18"/>'
    };
    var t = TEXT[document.documentElement.lang.slice(0, 2) === 'de' ? 'de' : 'en'];
    // The sticky first column may take at most this share of the visible table width.
    var MAX_STICKY_COLUMN = 0.4;
    var siteHeader = document.querySelector('.site-header');
    var toolsOf = new WeakMap();
    var SCROLL_KEYS = /^(Arrow(Up|Down|Left|Right)|Page(Up|Down)|Home|End)$/;
    var enhanced = [];

    function icon(name) {
        return '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2"' +
            ' stroke-linecap="round" stroke-linejoin="round">' + ICONS[name] + '</svg>';
    }

    function isWide(table) { return table.scrollWidth > table.clientWidth + 1; }

    function isOpaque(color) {
        var m = color.match(/rgba\([^)]*,\s*([\d.]+)\)|\/\s*([\d.]+%?)\s*\)$/);
        if (!m) { return color !== 'transparent'; }
        var alpha = m[1] || m[2];
        return (alpha.slice(-1) === '%' ? parseFloat(alpha) / 100 : parseFloat(alpha)) >= 1;
    }

    // The height the site header covers at the top of the window (it does not stick on small screens).
    function headerHeight() {
        if (!siteHeader || !/sticky|fixed/.test(getComputedStyle(siteHeader).position)) { return 0; }
        return siteHeader.getBoundingClientRect().height;
    }

    // The <thead> rows, else the leading rows that hold only <th> (at most three).
    function headerRows(table) {
        if (table.tHead && table.tHead.rows.length) { return [].slice.call(table.tHead.rows); }
        var rows = [];
        for (var i = 0; i < table.rows.length && rows.length < 3; i++) {
            var row = table.rows[i];
            if (!row.cells.length || [].some.call(row.cells, function (cell) { return cell.tagName !== 'TH'; })) { break; }
            rows.push(row);
        }
        return rows.length < table.rows.length ? rows : [];
    }

    // The cells that start in the first column and span only that column.
    function firstColumnCells(table) {
        var cells = [], covered = 0;
        [].forEach.call(table.rows, function (row) {
            if (covered > 0) { covered--; return; }
            var cell = row.cells[0];
            if (!cell) { return; }
            if (cell.colSpan === 1) { cells.push(cell); }
            covered = Math.max(cell.rowSpan, 1) - 1;
        });
        return cells;
    }

    function layout(table) {
        var wide = isWide(table);
        var boxed = wide || !!table.closest('.table-dialog');
        table.classList.toggle('table-boxed', boxed);
        toolsOf.get(table).hidden = !wide;
        // A box that scrolls must be reachable with the keyboard.
        if (boxed) { table.setAttribute('tabindex', '0'); } else { table.removeAttribute('tabindex'); }

        // In the box the header sticks to its top, otherwise below the site header;
        // 1px beyond the edge, see the CSS.
        var top = (boxed ? 0 : headerHeight()) - 1;
        var rows = headerRows(table);
        rows.forEach(function (row, i) {
            [].forEach.call(row.cells, function (cell) {
                cell.classList.add('sticky-top');
                // the cells that reach down to the last header row carry the separating line
                cell.classList.toggle('sticky-edge', i + Math.max(cell.rowSpan, 1) >= rows.length);
                cell.style.top = top + 'px';
            });
            top += row.offsetHeight;
        });

        var cells = firstColumnCells(table);
        var width = Math.max.apply(null, cells.map(function (cell) { return cell.offsetWidth; }).concat(0));
        var sticky = wide && width <= table.clientWidth * MAX_STICKY_COLUMN;
        if (wide && !sticky && cells.length && !table.classList.contains('first-col-narrow')) {
            // Too wide to stick (on phones): narrow the first column, the resize runs this again.
            // Once narrowed it stays so, or a table on the edge would switch back and forth.
            cells.forEach(function (cell) { cell.classList.add('first-col'); });
            table.classList.add('first-col-narrow');
        }
        cells.forEach(function (cell) { cell.classList.toggle('sticky-left', sticky); });

        // Snapped rows and columns start where the sticky header and first column end,
        // measured to the next row and column, so that their start is a snap position.
        // Sticky cells are positioned, so their offsetLeft counts from the page; the start
        // of the second column is measured on the screen instead.
        var last = rows[rows.length - 1];
        var headerEnd = last ? last.offsetTop + last.offsetHeight : 0;
        var next = cells.map(function (cell) { return cell.nextElementSibling; }).filter(Boolean)[0];
        var columnEnd = next ? next.getBoundingClientRect().left - table.getBoundingClientRect().left -
            table.clientLeft + table.scrollLeft : width;
        table.style.scrollPaddingTop = boxed ? headerEnd + 'px' : '';
        table.style.scrollPaddingLeft = sticky ? columnEnd + 'px' : '';
    }

    function enhance(table) {
        table.classList.add('table-large');
        // Sticky cells need an opaque background, or the scrolled cells shine through.
        var cells = firstColumnCells(table);
        headerRows(table).forEach(function (row) { cells = cells.concat([].slice.call(row.cells)); });
        cells.forEach(function (cell) {
            if (!isOpaque(getComputedStyle(cell).backgroundColor)) { cell.classList.add('sticky-fill'); }
        });
        var tools = document.createElement('div');
        tools.className = 'table-tools';
        tools.innerHTML = '<button type="button" class="table-btn" aria-label="' + t.maximizeLabel + '">' +
            icon('maximize') + '<span>' + t.maximize + '</span></button>';
        tools.firstChild.addEventListener('click', function () { open(table); });
        table.parentNode.insertBefore(tools, table);
        toolsOf.set(table, tools);
        enhanced.push(table);
        new ResizeObserver(function () { layout(table); }).observe(table);
    }

    var dialog, heading, stage, placeholder, current;

    function buildDialog(container) {
        dialog = document.createElement('dialog');
        dialog.className = 'table-dialog';
        dialog.innerHTML =
            '<div class="table-dialog-bar">' +
                '<p class="table-dialog-title"></p>' +
                '<button type="button" class="table-btn" aria-label="' + t.close + '">' + icon('close') + '<span>' + t.close + '</span></button>' +
            '</div>' +
            '<div class="table-dialog-stage"></div>';
        // Inside the article, so the article's own table styles apply in the dialog too.
        container.appendChild(dialog);
        heading = dialog.querySelector('.table-dialog-title');
        stage = dialog.querySelector('.table-dialog-stage');
        dialog.querySelector('button').addEventListener('click', function () { dialog.close(); });
        dialog.addEventListener('close', restore);
        // A footnote link jumps into the article: put the table back before the jump.
        stage.addEventListener('click', function (event) {
            if (event.target.closest('a[href^="#"]')) { restore(); dialog.close(); }
        });
        // The keys scroll the focused element: move the focus to the table (e.g. from
        // the close button) before the browser handles the key.
        dialog.addEventListener('keydown', function (event) {
            if (current && SCROLL_KEYS.test(event.key) && !current.contains(document.activeElement)) {
                current.focus({ preventScroll: true });
            }
        });
    }

    // The heading of the section the table is in names the dialog.
    function sectionTitle(table) {
        var node = table;
        while ((node = node.previousElementSibling || node.parentElement) && !node.classList.contains('article-content')) {
            if (/^H[2-4]$/.test(node.tagName)) {
                var copy = node.cloneNode(true);
                [].forEach.call(copy.querySelectorAll('.deepLink, .header-link'), function (link) { link.remove(); });
                return copy.textContent.trim();
            }
        }
        return '';
    }

    function open(table) {
        if (!dialog) { buildDialog(table.closest('.article-content') || document.body); }
        var title = sectionTitle(table);
        heading.textContent = title;
        dialog.setAttribute('aria-label', title || t.dialog);
        placeholder = document.createElement('div');
        placeholder.className = 'table-placeholder';
        placeholder.style.height = table.offsetHeight + 'px';
        table.parentNode.replaceChild(placeholder, table);
        stage.appendChild(table);
        current = table;
        dialog.showModal();
        table.focus({ preventScroll: true });
    }

    function restore() {
        if (!current) { return; }
        placeholder.parentNode.replaceChild(current, placeholder);
        current = null;
    }

    var candidates = [].filter.call(document.querySelectorAll('.article-content table'), function (table) {
        return !table.classList.contains('transparent');
    });
    function update() {
        // Measure all tables first, then change them, so the page lays out only once.
        candidates.filter(function (table) {
            return !table.classList.contains('table-large') &&
                (isWide(table) || table.offsetHeight > window.innerHeight);
        }).forEach(enhance);
        enhanced.forEach(layout);
    }
    update();
    // Web fonts and images can still change the sizes; a narrower window can make a table too wide.
    window.addEventListener('load', update);
    var pending = false;
    window.addEventListener('resize', function () {
        if (pending) { return; }
        pending = true;
        requestAnimationFrame(function () { pending = false; update(); });
    });
})();
