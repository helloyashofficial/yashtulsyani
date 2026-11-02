#!/usr/bin/env python3
"""
add-page-schema.py --- writes page JSON-LD between PAGE-SCHEMA markers.

Ported in role from FSDM's script of the same name. The Person and Book
facts are defined ONCE here and written into every block that needs them,
so the home, about and work pages can never describe two different people.

Yoast owns WebSite, WebPage, Article and BreadcrumbList, and its own Person.
Every node here uses a fragment @id Yoast never claims (#yash, #profilepage,
#book, #books). Facts must mirror what the page visibly says: a
fact-check on 24 Oct 2026 removed numberOfPages and two topics the pages
never state.

Each target block must carry exactly one marker pair:
  <!-- PAGE-SCHEMA:BEGIN --> ... <!-- PAGE-SCHEMA:END -->
"""
import json, re, sys
import ytconf as C

U = C.url
PERSON_REF = {"@id": C.PERSON_ID}

PERSON = {
    "@type": "Person",
    "@id": C.PERSON_ID,
    "name": "Yash Tulsyani",
    "url": U("/about"),
    "jobTitle": "Head of Growth Marketing",
    "worksFor": [
        {"@type": "Organization", "name": "BetterBugs"},
        {"@type": "Organization", "name": "QAble Testlab"},
    ],
    "knowsAbout": ["Relationships", "Psychology", "Philosophy", "Philosophy of time",
                   "Quantum mechanics as metaphor", "Organic search"],
    "sameAs": ["https://linkedin.com/in/yashtulsyani",
               "https://fullstackdigitalmarketer.com/"],
}

BOOKS = [
    {
        "@type": "Book",
        "@id": U("/books/nobody-has-to-shrink") + "#book",
        "name": "Nobody Has to Shrink",
        "alternativeHeadline": "A Handbook for Secure Love",
        "url": U("/books/nobody-has-to-shrink"),
        "author": PERSON_REF,
        "inLanguage": "en",
        "dateCreated": "2026",
        "creativeWorkStatus": "Unpublished",
        "about": ["Neglect", "Self-worth", "Emotional independence", "Secure love"],
    },
    {
        "@type": "Book",
        "@id": U("/books/the-thing-you-were-afraid-of") + "#book",
        "name": "The Thing You Were Afraid Of",
        "alternativeHeadline": "A Quantum Philosophy of Love, Insecurity, Validation and the Reality We Create",
        "url": U("/books/the-thing-you-were-afraid-of"),
        "author": PERSON_REF,
        "inLanguage": "en",
        "dateCreated": "2026",
        "creativeWorkStatus": "Unpublished",
        "about": ["Love", "Insecurity", "Validation", "Relationships"],
    },
]

GRAPHS = {
    "02-home.html": [PERSON],
    "23-work.html": [PERSON],
    "25-about.html": [
        {"@type": "ProfilePage", "@id": U("/about") + "#profilepage",
         "url": U("/about"), "mainEntity": PERSON_REF},
        PERSON,
    ],
    "20-books.html": [
        {"@type": "ItemList", "@id": U("/books") + "#books", "name": "Books by Yash Tulsyani",
         "itemListOrder": "https://schema.org/ItemListOrderDescending",
         "numberOfItems": len(BOOKS),
         "itemListElement": [{"@type": "ListItem", "position": i + 1, "item": b}
                             for i, b in enumerate(BOOKS)]},
    ],
    "22-book-nobody-has-to-shrink.html": [BOOKS[0]],
    "21-book-afraid-of.html": [BOOKS[1]],
}

B, E = "<!-- PAGE-SCHEMA:BEGIN -->", "<!-- PAGE-SCHEMA:END -->"


def render(graph):
    doc = json.dumps({"@context": "https://schema.org", "@graph": graph}, indent=2, ensure_ascii=False)
    doc = doc.replace("&", "\\u0026").replace("<", "\\u003c").replace(">", "\\u003e")
    return '%s\n<script type="application/ld+json">\n%s\n</script>\n%s' % (B, doc, E)


def main():
    for name, graph in GRAPHS.items():
        p = C.BLOCKS / name
        s = p.read_text(encoding="utf-8")
        if s.count(B) != 1 or s.count(E) != 1:
            sys.exit("%s: needs exactly one PAGE-SCHEMA marker pair" % name)
        s2 = re.sub(re.escape(B) + ".*?" + re.escape(E), lambda m: render(graph), s, flags=re.S)
        p.write_text(s2, encoding="utf-8")
        print("page schema: %-36s %s" % (name, [g["@type"] for g in graph]))


if __name__ == "__main__":
    main()
