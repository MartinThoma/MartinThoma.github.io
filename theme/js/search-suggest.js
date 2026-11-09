/* Search suggestions for every search field (form.search[data-suggest]): while typing, a
   dropdown shows the three best title/tag matches from search-titles.json
   (plugins/search_index.py) plus a row for all results. Enter without a chosen
   suggestion submits the form to the full-text search page (search.js).

   Also defines window.ThomaSearch (query parsing and term patterns), which search.js
   uses, so both rank with the same rules. */
(function () {
    'use strict';

    var STOP_WORDS = new Set([
        'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'do', 'for', 'from', 'how', 'i', 'if',
        'in', 'is', 'it', 'my', 'not', 'of', 'on', 'or', 'the', 'to', 'up', 'what', 'when',
        'where', 'which', 'who', 'why', 'with', 'you',
        'auf', 'aus', 'bei', 'das', 'dem', 'den', 'der', 'des', 'die', 'ein', 'eine', 'für',
        'im', 'ist', 'mit', 'nicht', 'oder', 'sind', 'und', 'von', 'was', 'wie', 'zu', 'zum', 'zur'
    ]);

    /* Terms of a query: "quoted phrases" stay together, punctuation around words is
       dropped, common words are ignored unless the query has nothing else. */
    function parse(text) {
        var found = [];
        var token = /"([^"]+)"?|(\S+)/g;
        var match;
        while ((match = token.exec(text))) {
            var term = (match[1] || match[2]).toLowerCase()
                .replace(/^[^\p{L}\p{N}]+|[^\p{L}\p{N}+#]+$/gu, '');
            if (term && found.indexOf(term) < 0) { found.push(term); }
        }
        var meaningful = found.filter(function (term) { return !STOP_WORDS.has(term); });
        return meaningful.length ? meaningful : found;
    }

    /* A term matches at the start of a word; terms of one or two characters only as whole
       words, unless `prefix` is set (the word the user is still typing). */
    function pattern(term, prefix) {
        var source = term.replace(/[.*+?^${}()|[\]\\]/g, '\\$&').replace(/\s+/g, '\\s+');
        var end = term.length <= 2 && !prefix ? '(?![\\p{L}\\p{N}])' : '';
        return '(?<![\\p{L}\\p{N}])' + source + end;
    }

    window.ThomaSearch = { STOP_WORDS: STOP_WORDS, parse: parse, pattern: pattern };

    var LIMIT = 3;
    var MIN_LENGTH = 2;
    var indexes = {};   // URL → promise of the pages
    var counter = 0;

    function load(url) {
        if (!indexes[url]) {
            indexes[url] = fetch(url).then(function (response) {
                if (!response.ok) { throw new Error(response.status + ' ' + response.statusText); }
                return response.json();
            }).then(function (index) { return index.pages; });
            indexes[url].catch(function () { delete indexes[url]; });
        }
        return indexes[url];
    }

    function rank(pages, text) {
        var terms = parse(text);
        if (!terms.length) { return { terms: terms, hits: [] }; }
        var typing = !/[\s"]$/.test(text);
        var regexes = terms.map(function (term, i) {
            return new RegExp(pattern(term, typing && i === terms.length - 1), 'iu');
        });
        var hits = [];
        pages.forEach(function (page) {
            var meta = page.category + ' ' + page.tags.join(' ');
            var score = 0;
            for (var i = 0; i < regexes.length; i++) {
                var inTitle = regexes[i].exec(page.title);
                var inMeta = regexes[i].test(meta);
                if (!inTitle && !inMeta) { return; }
                score += (inTitle ? 10 + (inTitle.index === 0 ? 3 : 0) : 0) + (inMeta ? 4 : 0);
            }
            hits.push({ page: page, score: score });
        });
        hits.sort(function (a, b) {
            return b.score - a.score ||
                (a.page.datetime < b.page.datetime ? 1 : a.page.datetime > b.page.datetime ? -1 : 0);
        });
        return { terms: terms, typing: typing, hits: hits };
    }

    function el(tag, attributes, children) {
        var node = document.createElement(tag);
        Object.keys(attributes || {}).forEach(function (name) {
            if (attributes[name] !== null && attributes[name] !== undefined) {
                node.setAttribute(name, attributes[name]);
            }
        });
        (children || []).forEach(function (child) { node.append(child); });
        return node;
    }

    function marked(text, highlight) {
        var nodes = [];
        var last = 0;
        highlight.lastIndex = 0;
        text.replace(highlight, function (match, offset) {
            nodes.push(text.slice(last, offset), el('mark', {}, [match]));
            last = offset + match.length;
            return match;
        });
        nodes.push(text.slice(last));
        return nodes;
    }

    function attach(form) {
        var input = form.querySelector('input[name="q"]');
        if (!input) { return; }
        var id = 'search-suggest-' + (++counter);
        var siteurl = form.dataset.siteurl || '';
        var listbox = el('div', { class: 'suggest', id: id, role: 'listbox', 'aria-label': 'Suggestions', hidden: '' });
        var live = el('span', { class: 'visually-hidden', role: 'status' });
        form.append(listbox, live);
        input.setAttribute('role', 'combobox');
        input.setAttribute('aria-autocomplete', 'list');
        input.setAttribute('aria-expanded', 'false');
        input.setAttribute('aria-controls', id);
        input.setAttribute('autocomplete', 'off');

        var options = [];
        var active = -1;
        var latest = 0;

        function open() {
            listbox.hidden = false;
            input.setAttribute('aria-expanded', 'true');
        }
        function close() {
            listbox.hidden = true;
            input.setAttribute('aria-expanded', 'false');
            input.removeAttribute('aria-activedescendant');
            active = -1;
        }
        function select(i) {
            options.forEach(function (option, j) { option.setAttribute('aria-selected', String(i === j)); });
            active = i;
            if (i >= 0) {
                input.setAttribute('aria-activedescendant', options[i].id);
                options[i].scrollIntoView({ block: 'nearest' });
            } else {
                input.removeAttribute('aria-activedescendant');
            }
        }

        function allResults(text) {
            var target = new URLSearchParams({ q: text.trim() });
            return el('a', {
                class: 'suggest-all', role: 'option', id: id + '-all', tabindex: '-1',
                href: form.action + '?' + target
            }, [
                el('span', { class: 'suggest-icon', 'aria-hidden': 'true' }),
                el('span', {}, ['All results for ', el('strong', {}, ['“' + text.trim() + '”'])])
            ]);
        }

        function render(rows, text, message) {
            var nodes = rows.slice();
            if (message) { nodes.push(message); }
            nodes.push(allResults(text));
            listbox.replaceChildren.apply(listbox, nodes);
            options = [].slice.call(listbox.querySelectorAll('[role="option"]'));
            select(-1);
            open();
        }

        function row(page, highlight, i) {
            var thumb = page.image
                ? el('img', {
                    class: 'suggest-thumb', src: (form.dataset.images || '') + page.image, alt: '',
                    width: 40, height: 40, loading: 'lazy', decoding: 'async'
                })
                : el('span', { class: 'suggest-thumb is-empty', 'aria-hidden': 'true' });
            return el('a', {
                class: 'suggest-row', role: 'option', id: id + '-' + i, tabindex: '-1',
                href: siteurl + '/' + page.url, lang: page.lang
            }, [
                thumb,
                el('span', { class: 'suggest-text' }, [
                    el('span', { class: 'suggest-title' }, marked(page.title, highlight)),
                    el('span', { class: 'suggest-meta' }, [page.date + ' · ' + page.category])
                ])
            ]);
        }

        function update() {
            var text = input.value;
            var request = ++latest;
            if (text.trim().length < MIN_LENGTH) { close(); live.textContent = ''; return; }
            var pending = setTimeout(function () {
                if (request !== latest) { return; }
                render([], text, el('p', { class: 'suggest-message is-loading' }, ['Searching…']));
            }, 120);
            load(form.dataset.suggest).then(function (pages) {
                clearTimeout(pending);
                if (request !== latest || document.activeElement !== input) { return; }
                var result = rank(pages, text);
                var highlight = new RegExp(result.terms.slice()
                    .sort(function (a, b) { return b.length - a.length; })
                    .map(function (term) { return pattern(term, true); }).join('|'), 'giu');
                var top = result.hits.slice(0, LIMIT);
                var more = result.hits.length - top.length;
                var message = null;
                if (!top.length) {
                    message = el('p', { class: 'suggest-message' }, ['No title matches. Press Enter to search the full text.']);
                } else if (more > 0) {
                    message = el('p', { class: 'suggest-message' }, [
                        more.toLocaleString('en') + ' more ' + (more === 1 ? 'title matches' : 'titles match')
                    ]);
                }
                render(top.map(function (hit, i) { return row(hit.page, highlight, i); }), text, message);
                live.textContent = result.hits.length
                    ? result.hits.length.toLocaleString('en') + (result.hits.length === 1 ? ' article' : ' articles') +
                      ' with a matching title. Use the arrow keys to choose.'
                    : 'No title matches.';
            }, function () {
                clearTimeout(pending);
                close();   // the form still submits to the search page
            });
        }

        input.addEventListener('input', update);
        input.addEventListener('focus', function () {
            load(form.dataset.suggest).catch(function () {});
            if (input.value.trim().length >= MIN_LENGTH) { update(); }
        });
        input.addEventListener('keydown', function (event) {
            if (event.key === 'ArrowDown' || event.key === 'ArrowUp') {
                if (listbox.hidden) { if (input.value.trim().length >= MIN_LENGTH) { update(); } return; }
                event.preventDefault();
                var step = event.key === 'ArrowDown' ? 1 : -1;
                var next = active + step;
                if (next >= options.length) { next = -1; }
                if (next < -1) { next = options.length - 1; }
                select(next);
            } else if (event.key === 'Enter' && !listbox.hidden && active >= 0) {
                event.preventDefault();
                options[active].click();
            } else if (event.key === 'Escape' && !listbox.hidden) {
                event.preventDefault();
                close();
            }
        });
        // keep the focus in the field when a suggestion is pressed, so it is not closed first
        listbox.addEventListener('pointerdown', function (event) { event.preventDefault(); });
        listbox.addEventListener('pointermove', function (event) {
            var option = event.target.closest('[role="option"]');
            if (option) { select(options.indexOf(option)); }
        });
        form.addEventListener('focusout', function (event) {
            if (!form.contains(event.relatedTarget)) { close(); }
        });
    }

    document.querySelectorAll('form.search[data-suggest]').forEach(attach);
})();
