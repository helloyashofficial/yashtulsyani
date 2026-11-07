#!/usr/bin/env python3
"""Essay 69 :: what-the-poincare-conjecture-says  (Fourth dimension)

Sources fetched and read on 7 Nov 2026: Milnor, The Poincare Conjecture
(Clay Mathematics Institute, 2000, revised 2004); the Clay problem page as
mirrored at the Mathematical Institute SANU; Wolfram MathWorld, Poincare
Conjecture; Perelman (2002), arXiv math/0211159; Nature News (Hogan, 2006)
on the Fields Medal; MAA news on the 2010 Clay award; Physics Today (2010)
and the Associated Press via R&D World (2010) on the refusal.
Not used: claims that our universe is shaped like a 3-sphere, which no
fetched source makes; Perelman's private life beyond what the sources say.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import newpost, postkit as K

EXT = ' target="_blank" rel="noopener"'
def a(url, text):
    return '<a href="%s"%s>%s</a>' % (url, EXT, text)

MILNOR = "https://www.claymath.org/wp-content/uploads/2022/06/poincare.pdf"
CLAYM = "https://www.mi.sanu.ac.rs/~zorano/izazovi21vek/poincare.html"
MW = "https://mathworld.wolfram.com/PoincareConjecture.html"
ARX = "https://arxiv.org/abs/math/0211159"
NAT = "https://www.nature.com/news/2006/060821/full/news060821-5.html"
MAA = "https://maa.org/news/perelman-awarded-1-million-prize-for-proving-poincar-conjecture"
PT = "https://physicstoday.aip.org/news/mathematician-turns-down-1-million-prize-for-proving-the-poincare-conjecture"
AP = "https://www.rdworldonline.com/russian-mathematician-rejects-1-million-millennium-prize/"
CLAYCONF = "https://www.claymath.org/resource/the-poincare-conjecture/"

ESSAY44 = '<a href="/writing/what-it-means-to-call-time-the-fourth-dimension">what it means to call time the fourth dimension</a>'
ESSAY64 = '<a href="/writing/what-a-tesseract-is">what a tesseract is</a>'
ESSAY49 = '<a href="/writing/what-flatland-teaches-about-the-fourth-dimension">what Flatland teaches about the fourth dimension</a>'
ESSAY59 = '<a href="/writing/what-physicists-mean-by-extra-dimensions">what physicists mean by extra dimensions</a>'
ESSAY66 = '<a href="/writing/what-the-impostor-phenomenon-is">what the impostor phenomenon is</a>'

POST = dict(
    slug="what-the-poincare-conjecture-says", num=69, cat="Fourth dimension", read="auto",
    date="2026-11-07",
    gen="rewrite/69-what-the-poincare-conjecture-says.py",
    title="What the Poincaré conjecture says, and why it needed four dimensions",
    dek="In 1904 Henri Poincaré asked a deceptively simple question about the shape of three-dimensional spaces. Answering it took almost a century, a detour through higher dimensions, and a reclusive Russian mathematician who solved it and then turned down both the Fields Medal and a million dollars.",
    takeaway="The Poincaré conjecture asks whether every closed three-dimensional space in which every loop can be shrunk to a point must be, topologically, a 3-sphere: the set of points in four-dimensional space at distance one from the origin. Poincaré posed it in 1904, after an earlier, mistaken version. The analogous statements in higher dimensions were proved first, by Stephen Smale and others around 1960 to 1962 for five or more dimensions, and by Michael Freedman in 1982 for four. The three-dimensional case fell to Grigori Perelman, who posted his work online from November 2002, building on Richard Hamilton’s Ricci flow and proving the broader geometrization conjecture of William Thurston. Perelman declined the Fields Medal in 2006 and, in 2010, the Clay Mathematics Institute’s $1 million Millennium Prize, reportedly saying his contribution was no greater than Hamilton’s. The conjecture is about mathematical spaces; whether our universe has this shape is a separate question.",
    sections=[
        ("What the Poincaré conjecture says", [
            "The Poincaré conjecture says that a closed three-dimensional space in which every loop can be shrunk to a point must be a 3-sphere, the three-dimensional analogue of the surface of a ball. It was posed in 1904 and proved by Grigori Perelman in work posted from 2002. It is a statement about mathematical shapes, not about the universe.",
            "HTML:" + K.takeaways([
                "It asks when a three-dimensional space must be a 3-sphere.",
                "The 3-sphere is defined as points in four-dimensional space at distance one from the origin.",
                "Poincaré posed it in 1904, after getting an earlier version wrong.",
                "Higher dimensions were solved first: five and up around 1960, four in 1982.",
                "Perelman proved the three-dimensional case using Hamilton’s Ricci flow.",
                "He declined the Fields Medal in 2006 and the $1 million Clay prize in 2010.",
            ]),
            "This essay is in the literal register, like the others in this series on dimensions. It sets out what the conjecture asks, how it was solved, and what it does and does not say about the space we live in.",
            "HTML:" + K.callout("definition", "The 3-sphere",
                "<p>In " + a(MILNOR, "John Milnor’s official description") + " for the Clay Mathematics Institute: the locus of all points (x, y, z, w) in four-dimensional Euclidean space which have distance exactly 1 from the origin. It is the three-dimensional version of the ordinary sphere’s surface.</p>"),
        ]),
        ("A question about loops", [
            "Topology studies the properties of shapes that survive stretching and bending without tearing. The Clay Institute’s problem description, written by Milnor and preserved on a " + a(CLAYM, "mirror of the original page") + ", explains the key idea with fruit and pastry: “If we stretch a rubber band around the surface of an apple, then we can shrink it down to a point” without tearing it or letting it leave the surface. A surface where every such loop can be shrunk away is called simply connected.",
            "A doughnut is different. The same page imagines a rubber band stretched in the appropriate direction around a doughnut: it cannot be shrunk to a point without breaking the band or the doughnut. So simple connectedness tells an apple’s surface apart from a doughnut’s, however either is squashed or stretched.",
            "Poincaré asked whether the same test works one dimension up. Take a three-dimensional space that is closed, finite and without edges, and suppose every loop in it can be shrunk to a point. In " + a(MILNOR, "Milnor’s formulation") + ", the question is whether such a space must be homeomorphic to the 3-sphere, the same shape up to stretching. " + a(MW, "MathWorld") + " states the conjecture as every simply connected closed three-manifold being homeomorphic to the three-sphere.",
            "Homeomorphic is the technical word for being the same shape in this stretchy sense: one space can be deformed into the other continuously, and back again, without tearing or gluing. A coffee mug and a doughnut are the classic example of two shapes a topologist treats as the same, because each has one hole that no amount of stretching removes.",
        ]),
        ("Why it needs four dimensions", [
            "The difficulty is that the spaces in question cannot be seen. The ordinary sphere is a two-dimensional surface, and to draw it we need three dimensions. The 3-sphere is a three-dimensional space, and the natural way to define it, as in Milnor’s definition, is as a surface in four dimensions: all the points at distance one from the centre of a four-dimensional ball.",
            "According to " + a(MAA, "the Mathematical Association of America") + ", Poincaré’s question concerns three-dimensional shapes that live in four-dimensional space, and because these cannot be visualised directly, he wanted a test that would recognise a 3-sphere however distorted it was. The loop test is that kind of test: it can be checked from the inside, without stepping into the fourth dimension to look.",
            "This is the same move that runs through the other essays here on the fourth dimension. As in " + ESSAY49 + ", a being living inside a space can still reason about its overall shape. A flat being cannot see the ball it lives on, but it can drag loops around and notice that they all shrink.",
            "HTML:" + K.table("Spheres by dimension",
                ["Sphere", "Its own dimension", "Lives naturally in"],
                [["Circle", "1", "A flat plane, 2 dimensions"],
                 ["Ordinary sphere’s surface", "2", "Ordinary space, 3 dimensions"],
                 ["3-sphere", "3", "Four-dimensional space"]],
                source='The 3-sphere definition is from <a href="' + MILNOR + '" target="_blank" rel="noopener">Milnor (Clay Mathematics Institute)</a>.'),
        ]),
        ("Poincaré’s first mistake", [
            "The conjecture began with an error. According to " + a(MILNOR, "Milnor") + ", Poincaré first claimed, in 1900, that a closed space with the same homology as a sphere, a coarser algebraic fingerprint, must actually be a sphere. He then found that this was false. His 1904 paper gave a counterexample, a space assembled from pieces built on the icosahedron, which has the same homology as the 3-sphere yet contains a closed curve that cannot be shrunk to a point.",
            "That discovery is why the loop condition matters. Having seen that the coarser test fails, Poincaré asked, in Milnor’s words, a corresponding question in dimension 3 using the finer test of whether loops can be shrunk. He did not claim to know the answer, and it stayed open for almost a century.",
        ]),
        ("Higher dimensions went first", [
            "One of the strangest parts of the story is that the conjecture was proved in higher dimensions before the three-dimensional case. The question generalises naturally: is every space that looks like a sphere in the relevant sense actually a sphere, in any number of dimensions? " + a(MW, "MathWorld") + " gives the generalised form for n-dimensional spaces.",
            "Stephen Smale announced a proof for high dimensions in 1960, according to " + a(MILNOR, "Milnor") + ", covering five dimensions and above. " + a(MW, "MathWorld") + " records the details: Smale proved the case of seven or more dimensions in 1961 and later extended it to five and above, with Zeeman handling five dimensions in 1961 and Stallings six in 1962. The four-dimensional case, Milnor notes, had to wait twenty years, for the work of Michael Freedman, published in 1982, for which Freedman received the Fields Medal in 1986.",
            "The methods were different in each case. Smale, Milnor explains, built up his spaces by adding handles, attaching simple pieces one at a time and then cancelling them out. Freedman’s four-dimensional proof used non-differentiable methods, working with shapes too rough to allow the smooth tools that succeed in higher dimensions. Neither approach carried over to dimension three.",
            "One loose way to picture why, offered here as an analogy rather than the mathematics, is that extra dimensions leave more room to move things out of each other’s way. Whatever the reason, dimensions three and four turned out to be the hard cases.",
            "HTML:" + K.stages("The conjecture, dimension by dimension", [
                ("1", "1904 · Poincaré", "Asks the three-dimensional question after his 1900 claim fails."),
                ("2", "1960 to 1962 · Five and up", "Smale, with Zeeman and Stallings, settles every dimension from five upward."),
                ("3", "1982 · Four", "Freedman proves the four-dimensional case."),
                ("4", "2002 to 2003 · Three", "Perelman posts the work that settles the original question."),
            ], source='Sources: <a href="' + MILNOR + '" target="_blank" rel="noopener">Milnor</a>; <a href="' + MW + '" target="_blank" rel="noopener">MathWorld</a>; <a href="' + ARX + '" target="_blank" rel="noopener">Perelman (2002)</a>.'),
        ]),
        ("How it was solved", [
            "The route to the three-dimensional case went through a bigger idea. In 1983, Milnor writes, William Thurston conjectured that every compact three-dimensional space can be cut up along spheres and tori into pieces that each carry one of a small number of simple geometric structures. This geometrization conjecture, if true, would imply the Poincaré conjecture.",
            "The tool came from Richard Hamilton, who studied what is called the Ricci flow. In Milnor’s description, the shape’s measurements are required to change with time so that distances decrease in directions of positive curvature, which this essay would compare, loosely, to heat spreading out until a temperature is even. The hope was that any space satisfying Poincaré’s condition would flow into a perfectly round 3-sphere. The difficulty, Milnor notes, is that the flow may develop singularities, places where it breaks down.",
            "Grigori Perelman overcame that difficulty. His first paper, " + a(ARX, "posted to arXiv on 11 November 2002") + ", says in its abstract that it verifies several assertions related to Richard Hamilton’s program for the proof of Thurston geometrization conjecture for closed three-manifolds, and gives a sketch of an eclectic proof of this conjecture. Further papers followed. " + a(MW, "MathWorld") + " notes that the work established the geometrization conjecture, from which the Poincaré conjecture follows immediately, and that it has since been verified.",
        ]),
        ("Two prizes declined", [
            "Recognition followed, and Perelman refused it. In August 2006, at the International Congress of Mathematicians in Madrid, he was awarded the Fields Medal for his work on Ricci flow, but did not accept it. According to " + a(NAT, "Nature News") + ", the president of the International Mathematical Union, John Ball, said “I regret that Dr Perelman has declined to accept,” and that his reasons centred around his feeling of isolation from the mathematical community, and not wanting to be seen as a figurehead. Perelman told The Sunday Telegraph, Nature reported, “I do not think anything that I say can be of the slightest public interest.” The other medallists that year were Andrei Okounkov, Terence Tao and Wendelin Werner.",
            "In 2010, the Clay Mathematics Institute awarded him its $1 million Millennium Prize. According to the " + a(MAA, "MAA") + ", the institute’s press release was dated 18 March 2010, making this the first of its seven Millennium Problems to be solved. The institute later published the lectures from a conference it held to celebrate the resolution, as a " + a(CLAYCONF, "volume") + " with contributions from mathematicians including Michael Atiyah, Simon Donaldson and Gang Tian. The institute’s president, James Carlson, said: “Resolution of the Poincaré conjecture by Grigoriy Perelman brings to a close the century-long quest for the solution.”",
            "Perelman turned that down too. " + a(PT, "Physics Today") + " reported in July 2010 that he had turned down the award and the $1 million prize. The " + a(AP, "Associated Press") + ", citing the Russian news agency Interfax, reported that he considered the decision unfair, and that he believed his contribution to proving the conjecture was no greater than that of the American mathematician Richard Hamilton, who first suggested a programme for the solution.",
        ]),
        ("Is the universe a 3-sphere?", [
            "It is tempting to read the conjecture as a statement about the shape of the cosmos, and popular accounts sometimes do. It is not. The conjecture is a theorem about mathematical spaces: if a closed three-dimensional space passes the loop test, it is a 3-sphere. It says nothing about whether our universe is closed, or finite, or passes the test.",
            "Whether physical space has any particular overall shape is a question for observation, not for topology alone. And the four-dimensional space in which the 3-sphere is drawn is a mathematical convenience; it does not mean there is a fourth spatial direction in the physical world. The essay on " + ESSAY59 + " sets out what physicists have looked for in that regard, and the essay on " + ESSAY44 + " explains why the fourth dimension of relativity is time, a different idea again.",
            "HTML:" + K.callout("warn", "A note on metaphors",
                "<p>The image of shrinking every loop to a point is sometimes borrowed for life, as if every problem could be pulled tight and made to vanish. That is a metaphor, and a loose one. The theorem is about the topology of three-dimensional spaces, and it carries no lesson about people.</p>"),
        ]),
        ("What this does and does not say", [
            "Read plainly, the Poincaré conjecture says that one simple test, whether every loop shrinks to a point, is enough to recognise the 3-sphere among closed three-dimensional spaces. It took almost a century, a detour through higher dimensions, and a new way of letting shapes flow to prove it. It does not tell us the shape of the universe, and it does not require a physical fourth dimension.",
            "Other essays here explore the same territory. " + ESSAY64.replace(">what a tesseract", ">What a tesseract") + " describes another shape that can only be built in four dimensions. The essay on Flatland, linked above, shows how a being can reason about a dimension it cannot see. And " + ESSAY66 + " looks at a very different response to recognition, the feeling of not deserving it, which is not what Perelman described.",
        ]),
    ],
    note=[
        "Perelman’s name is transliterated in different ways; the sources quoted use Grigory, Grigoriy and Grisha. The reasons given for his refusals are as reported by others; he has said little in public himself.",
    ],
    faqs=[
        ("What does the Poincaré conjecture say in simple terms?",
         "That any closed three-dimensional space in which every loop can be shrunk to a point is, up to stretching, the 3-sphere, the three-dimensional analogue of the surface of a ball."),
        ("Why does the Poincaré conjecture involve four dimensions?",
         "Because the 3-sphere is most naturally defined as the set of points in four-dimensional space at distance one from a centre, just as the ordinary sphere’s surface sits in three dimensions."),
        ("Who proved the Poincaré conjecture?",
         "Grigori Perelman, in papers posted online from November 2002, building on Richard Hamilton’s Ricci flow. His work proved Thurston’s broader geometrization conjecture, from which the Poincaré conjecture follows."),
        ("Why did Perelman turn down the prizes?",
         "He declined the 2006 Fields Medal and the 2010 Clay Millennium Prize. Reports said he felt isolated from the mathematical community, did not want to be a figurehead, and considered his contribution no greater than Hamilton’s."),
        ("Does the Poincaré conjecture mean the universe is a sphere?",
         "No. It is a theorem about mathematical spaces. Whether our universe is closed or has any particular shape is a question for observation."),
    ],
    related=[
        ("what-a-tesseract-is", "What a tesseract is, and how one Victorian tried to teach people to see it", "Fourth dimension"),
        ("what-flatland-teaches-about-the-fourth-dimension", "What Flatland teaches about the fourth dimension, and what it does not", "Fourth dimension"),
    ],
)

if __name__ == "__main__":
    newpost.build(POST)
