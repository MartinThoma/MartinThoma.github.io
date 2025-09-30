---
layout: post
lang: en
title: German Language
slug: german-language
author: Martin Thoma
date: 2018-02-20 20:00
category: My bits and bytes
tags: Language
featured_image: logos/germany.png
---
[German](https://en.wikipedia.org/wiki/German_language) is one of the many
languages spoken in Europe. I've been told that it also is a quite difficult
one. In this this article I would like to share some funny or interesting
facts about German with you.


## Script

I recently published a [paper about language identification](https://arxiv.org/pdf/1801.07779.pdf).
For this, I collected 1000 paragraphs from random Wikipedia articles, including
the German one. One thing I was interested in is which script defines the language.
While most people will probably say that German is written in the [Latin script](https://en.wikipedia.org/wiki/Latin_script) (so: `A-Z` and `a-z`) with some extra characters (`ß`, `äöü`, `ÄÖÜ`),
I wanted to derive this from the data. So I counted each unicode code point, sorted them descending
by frequency and added characters for some thresholds $\theta$:

* $C_{0.50} = \{\text{SPACE}, e, n, r, i, t\}$: Yes, only 6 characters make up 50% of the texts! And the most common one is one that isn't even mentioned in the usual lists!
* $C_{0.75} = C_{0.50} \cup \{s, a, d, h, u, l, o\}$: We get the remaining vocals
* $C_{0.90} = C_{0.75} \cup \{c, g, m, b, f, ., w, k, z, COMMA, S, v, p, 1\}$: The first capital letter, first punctuation marks and the first digit joins
* $C_{0.99} = C_{0.90} \cup \{ü, D, B, A, ä, M, 0, G, 9, K, F, E, P, W, 2, L, -, H, ö, R, 8, V, I, T, J, N ,), (, 5, y, ß, 6, 7, 4, Z, C, 3\}$: Now we have `a-z` and `äöüß` but not `jqx`. We have `A-C` but not `OQUXY`. We have the punctuation marks `,.()-`, `SPACE` and the digits `0-9`. 64 characters in total
* $C_{1.00}$ contains 247 characters in total, including `їышхдЬСРОВτςεːˈżşśŁğëæâÀ£濱滨春川區区ንሣሞሎیِنمظسرداשלכואҐящчфжбЯЮЩЧУТНИЖЇІφοιαίήέʿʃɛšœňńİēčČýûúøÚÁ¢#`.


## Lower and upper case

One might think that you could actually just write everything in lower case,
without changing the meaning. While this is certainly true for most examples,
there are some where it changes the meaning. With context, of course, you can
still know what was meant.

Example 1:

```text
EN: The spiders
DE: Die Spinnen
DE: Die spinnen!
EN: They are crazy!
```

Example 2:

```text
EN: The captured flea
DE: Der gefangene Floh.
DE: Der Gefangene floh.
EN: The prisoner fled.
```

Example 3: Single words

```text
EN: tremendous | the lawn         | the drink
DE: ungeheuer  | der Rasen        | der Trank
DE: Ungeheuer  |     rasen        |  er trank
EN: monster    | drive (too) fast |  he drank
```


## Punctuation

Just as with lower- and upper case, punctuation doesn't matter too much in most
cases in German. And context is king. But if you are pedantic, ignore the
context or just want to missunderstand the text, the following can be
misunderstood:

Example 1:

```text
EN: We eat, kids. (Talking to the children)
DE: Wir essen, Kinder.
DE: Wir essen Kinder.
EN: We eat kids. (Saying that you eat children as a dish)
```

**Example 2**: This one is actually confusing. Likely also with context.

```text
EN: Professors say, students are doing well.
DE: Professoren sagen, Studenten haben es gut.
DE: Professoren, sagen Studenten, haben es gut.
EN: Professors, students say, are doing well.
```

Example 3:

```text
EN: Don't kill him, release him!
DE: Tötet ihn nicht, freilassen!
DE: Tötet ihn, nicht freilassen!
EN: Kill him, don't release him!
```

Example 4:

```text
EN: We recommend him to follow.
DE: Wir empfehlen ihm, zu folgen.
DE: Wir empfehlen, ihm zu folgen.
EN: We recommend to follow him.
```

Example 5: Even [deepl has problems with this](https://www.deepl.com/translate)

```text
EN: He doesn't want her.
DE: Er will sie nicht.
DE: Er will, sie nicht.
EN: He likes, but she doesn't.
```

## Articles

Where you only have `the` in English, you have `der`, `die`, `das` in German.

```text
EN: It's the table.
DE: Es ist der Tisch.

EN: It's the wallet.
DE: Es ist die Geldbörse.

EN: It's the bread.
DE: Es ist das Brot
```

The concept of [Grammatical gender](https://en.wikipedia.org/wiki/Grammatical_gender) is pretty absurd: `der` is male, `die` is female and `das` is neuter. While you can say "die Anna" und "der Bob",
many words have quite arbitrary grammatical gender:

* the girl: "das Mädchen" - it's neuter
* the box: "die Box" - it's female
* the key: "der Schlüssel" - male

And the article also changes for plural forms:

```text
EN - Singular: the girl    | the box   | the key
EN - Plural  : the girls   | the boxes | the keys
DE - Singular: das Mädchen | die Box   | der Schlüssel
DE - Plural  : die Mädchen | die Boxen | die Schlüssel
```

Of course, it changes with different [grammatical cases](https://en.wikipedia.org/wiki/Grammatical_case):

```text
EN: the key
DE: der Schlüssel

EN: It's    on the key.
DE: Es ist auf dem Schlüssel.

EN: I   give him the key.
DE: Ich gebe ihm den Schlüssel.
```

To summarize: The English word `the` can be translated to 9 different German
words:

<table class="table">
    <tr>
        <th></th>
        <th>Male</th>
        <th>Female</th>
        <th>Neuter</th>
        <th>Plural</th>
    </tr>
    <tr>
        <td>Nominativ</td>
        <td>der&nbsp;</td>
        <td>die</td>
        <td>das</td>
        <td>die</td>
    </tr>
    <tr>
        <td>Genitiv</td>
        <td>den</td>
        <td>die</td>
        <td>das</td>
        <td>die</td>
    </tr>
    <tr>
        <td>Dativ</td>
        <td>dem</td>
        <td>der</td>
        <td>dem</td>
        <td>denen</td>
    </tr>
    <tr>
        <td>Akkussativ</td>
        <td>dessen</td>
        <td>deren</td>
        <td>dessen</td>
        <td>deren</td>
    </tr>
</table>


## Long words

German has crazy long words. The longest one I've seen in 8th grade or so is

```text
DE: Brandrodungswanderhackfeldbau
EN: slash-and-burn migration hackfield cultivation
```

I will add more another day 🙂


## Missing Words

There are some things you cannot easily express with a single word in German:

* **Girlfriend / boyfriend**: You can say "meine feste Freundin" and the word
  "feste" indicates that it's about your partner. And, of course, you can say
  "meine Partnerin", but that also has other meanings (e.g. hiking partner,
  partner at a law firm, ...)
* **Not thirsty**: I think this one is also missing in English. When you are
  hungry and you ate, you say in German "Ich bin satt". But when you are
  thirsty and you drink, you can only negate: "Ich bin nicht mehr durstig".


## Micallenious

* You say "Gesundheit" (directly translated: "health") when somebody sneezes.
  But although it is very close to "get healthy", you don't say it when
  somebody is ill. You can, however, say it when somebody says a complicated
  word.


## See also

* Mark Twain: [The Awful German Language](https://en.wikipedia.org/wiki/The_Awful_German_Language)
