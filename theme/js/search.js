/* Search page (templates/search.html). Loads search.json (plugins/search_index.py) and
   renders the results for ?q=…&page=….

   Matching: terms match at the start of a word ("test" finds "testing"); terms of one or
   two characters ("R", "AI") only as whole words; "quoted phrases" as a whole. Common
   words are ignored unless the query has nothing else. Articles containing all terms come
   first, ranked by title, category/tag and text hits; if none contains all terms, the
   articles containing any of them are shown with a note. */
(function () {
    'use strict';

    var root = document.getElementById('search');
    if (!root) { return; }

    var PER_PAGE = 20;
    var EXCERPT_LENGTH = 240;
    var STOP_WORDS = new Set([
        'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'do', 'for', 'from', 'how', 'i', 'if',
        'in', 'is', 'it', 'my', 'not', 'of', 'on', 'or', 'the', 'to', 'up', 'what', 'when',
        'where', 'which', 'who', 'why', 'with', 'you',
        'auf', 'aus', 'bei', 'das', 'dem', 'den', 'der', 'des', 'die', 'ein', 'eine', 'für',
        'im', 'ist', 'mit', 'nicht', 'oder', 'sind', 'und', 'von', 'was', 'wie', 'zu', 'zum', 'zur'
    ]);

    var params = new URLSearchParams(location.search);
    var query = (params.get('q') || '').trim();
    var requestedPage = Math.max(1, parseInt(params.get('page'), 10) || 1);

    var heading = root.querySelector('[data-heading]');
    var status = root.querySelector('[data-status]');
    var output = root.querySelector('[data-results]');
    root.querySelector('input[name="q"]').value = query;

    if (!query) { return; }
    root.querySelectorAll('[data-intro]').forEach(function (node) { node.hidden = true; });
    document.title = '“' + query + '” · ' + document.title;

    var terms = parse(query);
    output.setAttribute('aria-busy', 'true');
    output.replaceChildren(skeleton());

    fetch(root.dataset.index)
        .then(function (response) {
            if (!response.ok) { throw new Error(response.status + ' ' + response.statusText); }
            return response.json();
        })
        .then(function (index) { show(search(index.pages)); }, fail)
        .finally(function () { output.removeAttribute('aria-busy'); });

    /* ---------- query ---------- */

    function parse(text) {
        var found = [];
        var token = /"([^"]+)"|(\S+)/g;
        var match;
        while ((match = token.exec(text))) {
            var term = (match[1] || match[2]).toLowerCase()
                .replace(/^[^\p{L}\p{N}]+|[^\p{L}\p{N}+#]+$/gu, '');
            if (term && found.indexOf(term) < 0) { found.push(term); }
        }
        var meaningful = found.filter(function (term) { return !STOP_WORDS.has(term); });
        return meaningful.length ? meaningful : found;
    }

    function pattern(term) {
        var source = term.replace(/[.*+?^${}()|[\]\\]/g, '\\$&').replace(/\s+/g, '\\s+');
        var end = term.length <= 2 ? '(?![\\p{L}\\p{N}])' : '';
        return '(?<![\\p{L}\\p{N}])' + source + end;
    }

    function count(text, regex) {
        var hits = text.match(regex);
        return hits ? hits.length : 0;
    }

    /* ---------- ranking ---------- */

    function search(pages) {
        var regexes = terms.map(function (term) { return new RegExp(pattern(term), 'giu'); });
        var phrase = terms.length > 1 ? query.toLowerCase() : null;
        var hits = [];
        pages.forEach(function (page) {
            var meta = page.category + ' ' + page.tags.join(' ');
            var matched = 0;
            var score = 0;
            regexes.forEach(function (regex) {
                var inTitle = count(page.title, regex);
                var inMeta = count(meta, regex);
                var inText = count(page.text, regex);
                if (inTitle || inMeta || inText) { matched += 1; }
                score += inTitle * 20 + Math.min(inMeta, 1) * 8 + Math.min(inText, 20);
            });
            if (!matched) { return; }
            if (phrase && page.title.toLowerCase().indexOf(phrase) >= 0) { score += 15; }
            hits.push({ page: page, matched: matched, score: score });
        });
        var all = hits.filter(function (hit) { return hit.matched === terms.length; });
        var list = all.length ? all : hits;
        list.sort(function (a, b) {
            return b.matched - a.matched || b.score - a.score ||
                (a.page.datetime < b.page.datetime ? 1 : a.page.datetime > b.page.datetime ? -1 : 0);
        });
        return { hits: list, partial: !all.length && hits.length > 0 };
    }

    /* ---------- rendering ---------- */

    function el(tag, attributes, children) {
        var node = document.createElement(tag);
        Object.keys(attributes || {}).forEach(function (name) {
            if (attributes[name] !== null && attributes[name] !== undefined) {
                node.setAttribute(name, attributes[name]);
            }
        });
        (children || []).forEach(function (child) {
            node.append(child);
        });
        return node;
    }

    function plural(n, word) {
        return n.toLocaleString('en') + ' ' + word + (n === 1 ? '' : 's');
    }

    function show(result) {
        var total = result.hits.length;
        if (!total) { return empty(); }

        var pages = Math.ceil(total / PER_PAGE);
        var page = Math.min(requestedPage, pages);
        var first = (page - 1) * PER_PAGE;
        var highlight = new RegExp(terms.slice().sort(function (a, b) { return b.length - a.length; })
            .map(pattern).join('|'), 'giu');

        heading.textContent = plural(total, 'search result');
        status.textContent = plural(total, 'search result') + ' for “' + query + '”' +
            (pages > 1 ? ', page ' + page + ' of ' + pages : '') + '.';

        var children = [];
        if (result.partial) {
            children.push(el('p', { class: 'search-note' }, [
                'No article contains all of the words. These contain at least one of them.'
            ]));
        }
        children.push(el('ol', { class: 'results', start: first + 1 },
            result.hits.slice(first, first + PER_PAGE).map(function (hit) { return row(hit.page, highlight); })));
        if (pages > 1) { children.push(pagination(page, pages)); }
        output.replaceChildren.apply(output, children);
    }

    function row(page, highlight) {
        var thumb = page.image
            ? el('img', {
                class: 'result-thumb', src: root.dataset.images + page.image, alt: '',
                width: 72, height: 72, loading: 'lazy', decoding: 'async'
            })
            : el('span', { class: 'result-thumb is-empty', 'aria-hidden': 'true' });
        return el('li', { class: 'result', lang: page.lang }, [
            thumb,
            el('div', { class: 'result-body' }, [
                el('h2', { class: 'result-title' }, [
                    el('a', { href: root.dataset.siteurl + '/' + page.url }, [page.title])
                ]),
                el('p', { class: 'result-meta' }, [
                    el('time', { datetime: page.datetime }, [page.date]), ' · ' + page.category
                ]),
                el('p', { class: 'result-excerpt' }, excerpt(page.text, highlight))
            ])
        ]);
    }

    /* The passage around the first hit, cut at word boundaries, hits in <mark>. */
    function excerpt(text, highlight) {
        highlight.lastIndex = 0;
        var hit = highlight.exec(text);
        var start = 0;
        if (hit && hit.index > 80) { start = text.lastIndexOf(' ', hit.index - 60) + 1; }
        var end = start + EXCERPT_LENGTH;
        if (end < text.length) {
            var space = text.lastIndexOf(' ', end);
            end = space > start ? space : end;
        } else {
            end = text.length;
        }
        var passage = text.slice(start, end);
        var nodes = start > 0 ? ['… '] : [];
        var last = 0;
        highlight.lastIndex = 0;
        passage.replace(highlight, function (match, offset) {
            nodes.push(passage.slice(last, offset), el('mark', {}, [match]));
            last = offset + match.length;
            return match;
        });
        nodes.push(passage.slice(last));
        if (end < text.length) { nodes.push(' …'); }
        return nodes;
    }

    function pageLink(number, label, attributes) {
        var target = new URLSearchParams({ q: query });
        if (number > 1) { target.set('page', number); }
        return el('a', Object.assign({ href: '?' + target }, attributes), [label]);
    }

    function pagination(page, pages) {
        var items = [];
        if (page > 1) { items.push(pageLink(page - 1, 'Previous', { class: 'step', rel: 'prev' })); }
        var shown = [1, page - 1, page, page + 1, pages].filter(function (n, i, all) {
            return n >= 1 && n <= pages && all.indexOf(n) === i;
        }).sort(function (a, b) { return a - b; });
        shown.forEach(function (n, i) {
            if (i && n - shown[i - 1] > 1) { items.push(el('span', { class: 'gap', 'aria-hidden': 'true' }, ['…'])); }
            items.push(pageLink(n, String(n), {
                'aria-current': n === page ? 'page' : null,
                'aria-label': 'Page ' + n
            }));
        });
        if (page < pages) { items.push(pageLink(page + 1, 'Next', { class: 'step', rel: 'next' })); }
        return el('nav', { class: 'pagination', 'aria-label': 'Result pages' }, items);
    }

    function skeleton() {
        var rows = [];
        for (var i = 0; i < 4; i++) {
            rows.push(el('li', { class: 'result is-loading' }, [
                el('span', { class: 'result-thumb' }),
                el('div', { class: 'result-body' }, [
                    el('span', { class: 'bone bone-title' }), el('span', { class: 'bone bone-meta' }),
                    el('span', { class: 'bone' }), el('span', { class: 'bone bone-short' })
                ])
            ]));
        }
        return el('ol', { class: 'results', 'aria-hidden': 'true' }, rows);
    }

    function browseLinks() {
        return [
            'Or browse ', el('a', { href: root.dataset.tags }, ['all tags']),
            ' and ', el('a', { href: root.dataset.archives }, ['the archive']), '.'
        ];
    }

    function empty() {
        heading.textContent = 'No search results';
        status.textContent = 'No search results for “' + query + '”.';
        output.replaceChildren(el('div', { class: 'search-panel' }, [
            el('p', {}, ['No article matches ', el('strong', {}, ['“' + query + '”']), '. You could:']),
            el('ul', {}, [
                el('li', {}, ['check the spelling,']),
                el('li', {}, ['use fewer or more general words,']),
                el('li', {}, ['search in English: most articles are English.'])
            ]),
            el('p', {}, browseLinks())
        ]));
    }

    function fail(error) {
        heading.textContent = 'Search is unavailable';
        status.textContent = 'The search index could not be loaded.';
        output.replaceChildren(el('div', { class: 'search-panel' }, [
            el('p', {}, ['The search index could not be loaded (' + error.message + '). ',
                el('a', { href: location.href }, ['Try again']), '.']),
            el('p', {}, browseLinks())
        ]));
    }
})();
