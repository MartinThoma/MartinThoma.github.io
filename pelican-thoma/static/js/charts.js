/* Bar charts from plain HTML tables (progressive enhancement).

   Write a table with class "bar-chart": the first column holds the labels, the second
   the values. Without JavaScript (feed readers, print) the table stays as it is; with
   JavaScript it becomes a horizontal bar chart, and a button switches to the table.

   <figure class="chart">
   <table class="bar-chart" data-unit="charging stations">
     <thead><tr><th>Charging power</th><th>Charging stations</th></tr></thead>
     <tbody>
       <tr><td>up to 21 kW</td><td>870</td></tr>
       <tr class="highlight"><td>44 kW</td><td>8630</td></tr>
     </tbody>
   </table>
   <figcaption>…</figcaption>
   </figure>

   Options (attributes of the table):
     data-unit="…"      unit for tooltips and screen readers, e.g. "charging stations"
     data-sort="desc"   sort the bars ("asc" or "desc"); default: table order
     data-approx        values are approximate: shown as "≈ 870"
     data-no-share      don't show the share of the total in the tooltip
     data-total="19658" the total for the shares, if it is not the sum of the rows
                        (rounded values, or rows that don't cover everything)
   A row with class "highlight" is drawn in the accent color, all others muted.
   Values may use "," or "." as thousands separators and "%" or units after the number.
   Labels are shown in the language of the page (lang="de" → German number format). */
(function () {
    'use strict';

    var lang = (document.documentElement.lang || 'en').slice(0, 2);
    var de = lang === 'de';
    var fmt = new Intl.NumberFormat(de ? 'de-DE' : 'en-US', { maximumFractionDigits: 2 });
    var pct = new Intl.NumberFormat(de ? 'de-DE' : 'en-US', { style: 'percent', maximumFractionDigits: 1 });
    var text = de
        ? { table: 'Tabelle', chart: 'Diagramm', total: 'von insgesamt' }
        : { table: 'Table', chart: 'Chart', total: 'of' };

    function parseValue(raw) {
        // "8,630" / "8.630" / "8 630" / "44 %" / "1,5" → number
        var s = raw.replace(/[\s  ]/g, '').replace(/[^\d.,\-]/g, '');
        if (/^-?\d{1,3}([.,]\d{3})+$/.test(s)) { return parseFloat(s.replace(/[.,]/g, '')); }
        return parseFloat(s.replace(',', '.'));
    }

    function niceStep(max) {
        // a step of 1, 2 or 5 × 10^n that gives about 4 to 6 gridlines
        var rough = max / 5;
        var power = Math.pow(10, Math.floor(Math.log10(rough)));
        var f = rough / power;
        return (f <= 1 ? 1 : f <= 2 ? 2 : f <= 5 ? 5 : 10) * power;
    }

    function el(tag, cls, content) {
        var node = document.createElement(tag);
        if (cls) { node.className = cls; }
        if (content !== undefined) { node.textContent = content; }
        return node;
    }

    function build(table) {
        var rows = [].map.call(table.tBodies[0] ? table.tBodies[0].rows : [], function (tr) {
            return {
                label: tr.cells[0].textContent.trim(),
                value: parseValue(tr.cells[1].textContent),
                highlight: tr.classList.contains('highlight')
            };
        }).filter(function (r) { return !isNaN(r.value); });
        if (!rows.length) { return; }

        var sort = table.dataset.sort;
        if (sort === 'desc') { rows.sort(function (a, b) { return b.value - a.value; }); }
        if (sort === 'asc') { rows.sort(function (a, b) { return a.value - b.value; }); }

        var unit = table.dataset.unit || '';
        var approx = table.hasAttribute('data-approx') ? '≈ ' : '';
        var total = table.dataset.total ? parseValue(table.dataset.total)
            : rows.reduce(function (s, r) { return s + r.value; }, 0);
        var showShare = !table.hasAttribute('data-no-share') && rows.every(function (r) { return r.value >= 0; });
        var max = Math.max.apply(null, rows.map(function (r) { return r.value; }));
        var step = niceStep(max);
        var axisMax = Math.ceil(max / step) * step;
        var anyHighlight = rows.some(function (r) { return r.highlight; });
        var caption = table.caption ? table.caption.textContent.trim() : '';
        var head = table.tHead && table.tHead.rows[0] ? table.tHead.rows[0].cells : null;

        var view = el('div', 'bar-chart-view');
        view.setAttribute('role', 'group');
        if (caption) { view.setAttribute('aria-label', caption); }
        view.style.setProperty('--grid-step', (step / axisMax * 100) + '%');

        var tooltip = el('div', 'chart-tooltip');
        tooltip.setAttribute('aria-hidden', 'true');
        var plot = el('div', 'chart-plot');

        rows.forEach(function (r) {
            var share = showShare && total > 0 ? r.value / total : null;
            var valueText = approx + fmt.format(r.value);
            var width = axisMax > 0 ? r.value / axisMax * 100 : 0;

            var label = el('div', 'chart-label', r.label);
            var track = el('div', 'chart-track');
            var bar = el('div', 'chart-bar' + (anyHighlight && !r.highlight ? ' muted' : ''));
            bar.style.setProperty('--w', width + '%');
            var value = el('span', 'chart-value' + (width > 82 ? ' inside' : ''), valueText);
            value.style.setProperty('--w', width + '%');
            track.appendChild(bar);
            track.appendChild(value);

            var row = el('div', 'chart-row');
            row.tabIndex = 0;
            row.setAttribute('aria-label', r.label + ': ' + valueText + (unit ? ' ' + unit : '') +
                (share !== null ? ' (' + pct.format(share) + ')' : ''));
            row.appendChild(label);
            row.appendChild(track);
            plot.appendChild(row);

            function show(event) {
                tooltip.textContent = '';
                tooltip.appendChild(el('strong', null, valueText + (unit ? ' ' + unit : '')));
                tooltip.appendChild(el('span', null, r.label));
                if (share !== null) {
                    tooltip.appendChild(el('span', 'muted-text', pct.format(share) + ' ' + text.total + ' ' + fmt.format(total)));
                }
                var box = view.getBoundingClientRect();
                var rowBox = row.getBoundingClientRect();
                var half = tooltip.offsetWidth / 2;
                var x = event && event.clientX ? event.clientX - box.left : track.offsetLeft + track.offsetWidth * width / 100;
                tooltip.style.left = Math.min(Math.max(x, half), box.width - half) + 'px';
                tooltip.style.top = (rowBox.top - box.top) + 'px';
                tooltip.classList.add('visible');
                row.classList.add('active');
            }
            function hide() { tooltip.classList.remove('visible'); row.classList.remove('active'); }
            row.addEventListener('pointermove', show);
            row.addEventListener('pointerleave', hide);
            row.addEventListener('focus', show);
            row.addEventListener('blur', hide);
        });

        // value axis below the bars
        var axis = el('div', 'chart-axis');
        axis.appendChild(el('div', 'chart-label'));
        var ticks = el('div', 'chart-ticks');
        for (var t = 0; t <= axisMax + step / 2; t += step) {
            var tick = el('span', null, fmt.format(t));
            tick.style.left = (t / axisMax * 100) + '%';
            ticks.appendChild(tick);
        }
        axis.appendChild(ticks);
        plot.appendChild(axis);
        // on narrow screens, label only every other gridline so the numbers don't collide
        if ('ResizeObserver' in window) {
            new ResizeObserver(function () {
                var widest = Math.max.apply(null, [].map.call(ticks.children, function (s) { return s.offsetWidth; }));
                var gap = ticks.offsetWidth / Math.max(ticks.children.length - 1, 1);
                // the last label is right-aligned, so it reaches 1.5 widths towards its neighbour
                ticks.classList.toggle('sparse', widest * 1.5 + 8 > gap);
            }).observe(ticks);
        }
        if (head && head[1]) { plot.appendChild(el('div', 'chart-axis-title', head[1].textContent.trim())); }

        view.appendChild(plot);
        view.appendChild(tooltip);

        var tools = el('div', 'table-tools chart-tools');
        var toggle = el('button', 'table-btn', text.table);
        tools.appendChild(toggle);
        toggle.type = 'button';
        toggle.setAttribute('aria-pressed', 'false');
        toggle.addEventListener('click', function () {
            var tableShown = table.classList.toggle('chart-table-visible');
            view.hidden = tableShown;
            toggle.textContent = tableShown ? text.chart : text.table;
            toggle.setAttribute('aria-pressed', String(tableShown));
        });

        table.classList.add('chart-enhanced');
        table.parentNode.insertBefore(view, table);
        table.parentNode.insertBefore(tools, view);

        // grow the bars once when the chart scrolls into view
        if ('IntersectionObserver' in window && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
            view.classList.add('pending');
            var io = new IntersectionObserver(function (entries) {
                if (entries[0].isIntersecting) { view.classList.remove('pending'); io.disconnect(); }
            }, { threshold: 0.25 });
            io.observe(view);
        }
    }

    [].forEach.call(document.querySelectorAll('table.bar-chart'), build);
})();
