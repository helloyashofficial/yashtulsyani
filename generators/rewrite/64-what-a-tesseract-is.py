#!/usr/bin/env python3
"""Essay 64 :: what-a-tesseract-is  (Fourth dimension)

Sources fetched and read on 7 Nov 2026: Hinton, A New Era of Thought (1888)
and The Fourth Dimension (1904, 1906 edition), Project Gutenberg; Wolfram
MathWorld, Tesseract and Hypercube; Science Fiction Encyclopedia entry on
Hinton; Princeton Alumni Weekly (Graham, 2019); Public Domain Review essay
(Crabb) and collection page on the 1904 plates; Metropolitan Museum of Art
collection page for Dali's Crucifixion (Corpus Hypercubus); History of
Information entry on the painting.
Not used: claims about Hinton's later life that no fetched source states;
the boundary counts of the tesseract's chapter in A New Era of Thought,
which could not be read.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import newpost, postkit as K

EXT = ' target="_blank" rel="noopener"'
def a(url, text):
    return '<a href="%s"%s>%s</a>' % (url, EXT, text)

NEWERA = "https://gutenberg.org/cache/epub/60607/pg60607-images.html"
FOURTH = "https://gutenberg.org/cache/epub/67153/pg67153-images.html"
MWT = "https://mathworld.wolfram.com/Tesseract.html"
MWH = "https://mathworld.wolfram.com/Hypercube.html"
SFE = "https://sf-encyclopedia.com/entry/hinton_c_h"
PAW = "https://paw.princeton.edu/article/charles-howard-hinton-he-wrote-science-fiction-genre-existed"
PDR = "https://publicdomainreview.org/essay/notes-on-the-fourth-dimension"
PDRV = "https://publicdomainreview.org/collections/views-of-the-tesseract-1904/"
MET = "https://metmuseum.org/art/collection/search/488880"
HOI = "https://www.historyofinformation.com/detail.php?id=4922"

ESSAY44 = '<a href="/writing/what-it-means-to-call-time-the-fourth-dimension">what it means to call time the fourth dimension</a>'
ESSAY49 = '<a href="/writing/what-flatland-teaches-about-the-fourth-dimension">what Flatland teaches about the fourth dimension</a>'
ESSAY59 = '<a href="/writing/what-physicists-mean-by-extra-dimensions">what physicists mean by extra dimensions</a>'
ESSAY63 = '<a href="/writing/what-time-dilation-is">what time dilation is</a>'
ESSAY41 = '<a href="/writing/what-the-observer-effect-actually-says">what the observer effect actually says</a>'

POST = dict(
    slug="what-a-tesseract-is", num=64, cat="Fourth dimension", read="auto",
    date="2026-11-07",
    gen="rewrite/64-what-a-tesseract-is.py",
    title="What a tesseract is, and how one Victorian tried to teach people to see it",
    dek="A tesseract is a cube taken one dimension further: a four-dimensional figure with 16 corners and 8 cubes for sides. The word was coined by Charles Howard Hinton, a Victorian mathematician who believed that, with enough practice with coloured cubes, people could learn to picture it. What you see in the famous rotating images is not the tesseract itself, but its shadow.",
    takeaway="A tesseract, or four-dimensional hypercube, is to a cube what a cube is to a square. According to MathWorld it has 16 vertices, 32 edges, 24 squares and 8 cubes. The word was coined by Charles Howard Hinton (1853 to 1907), who first used it in his 1888 book A New Era of Thought, spelled tessaract, and who designed sets of coloured cubes to train readers to sense four-dimensional space. Hinton’s method rested on an analogy: a flat being could learn about a cube by watching it pass through its plane as a series of square sections. The rotating pictures of a tesseract are projections into three dimensions, much as a drawing of a cube is a projection onto paper. The tesseract is a well-defined mathematical object; whether space has a fourth spatial direction is a separate question, and the fourth dimension of relativity is time.",
    sections=[
        ("What a tesseract is", [
            "A tesseract is the four-dimensional version of a cube. Just as a cube is built from squares, a tesseract is built from cubes: eight of them, joined so that each square face is shared by two. It cannot be built in our three-dimensional space, but it can be described exactly, and drawn as a shadow.",
            "HTML:" + K.takeaways([
                "A tesseract is to a cube what a cube is to a square.",
                "It has 16 corners, 32 edges, 24 square faces and 8 cubic cells.",
                "The word was coined by Charles Howard Hinton, who first used it in 1888.",
                "Hinton designed coloured cubes to train people to sense four-dimensional space.",
                "The familiar rotating images are projections, the tesseract’s shadow in three dimensions.",
                "The tesseract is mathematics. The fourth dimension of physics is time, a different idea.",
            ]),
            "This essay is in the literal register, like " + ESSAY41 + ". It sets out what the mathematics says and what Hinton actually wrote, and keeps anything else to clearly labelled asides.",
            "HTML:" + K.callout("definition", "Tesseract",
                "<p>In " + a(MWT, "MathWorld’s") + " definition, the tesseract is the hypercube in four-dimensional space, also called the 8-cell or octachoron.</p>"),
        ]),
        ("Building up from a point", [
            "The easiest way to understand a tesseract is to build up to it. Take a point and drag it in a straight line: it traces a line segment. Drag the segment at right angles to itself and it sweeps out a square. Drag the square at right angles to its own plane and it sweeps out a cube. Each step uses a new direction, at right angles to all the previous ones.",
            "The tesseract is the next step: a cube dragged in a fourth direction, at right angles to all three of the directions we know. We cannot point in that direction, but the pattern tells us what the result must contain. The corners double at each step, from one to two to four to eight, so the tesseract has sixteen. " + a(MWT, "MathWorld") + " gives the full count: the tesseract has 16 vertices, 32 edges, 24 squares, and 8 cubes.",
            "HTML:" + K.table("Building the tesseract",
                ["Shape", "Dimensions", "Corners", "Made by dragging"],
                [["Point", "0", "1", "Nothing"],
                 ["Line segment", "1", "2", "A point"],
                 ["Square", "2", "4", "A line segment"],
                 ["Cube", "3", "8", "A square"],
                 ["Tesseract", "4", "16", "A cube"]],
                source='Corner counts double at each step; the tesseract’s full count is from <a href="' + MWT + '" target="_blank" rel="noopener">MathWorld</a>.'),
            "The same reasoning appears in a famous novel of 1884, in which a square living on a flat plane works out what a four-dimensional figure must look like; the essay on " + ESSAY49 + " follows that argument step by step.",
        ]),
        ("The man who named it", [
            "The word tesseract came from Charles Howard Hinton. According to the " + a(SFE, "Encyclopedia of Science Fiction") + ", he was born in London on 6 June 1853 and died in Washington, District of Columbia, on 30 April 1907. The " + a(PDR, "Public Domain Review") + " notes that he first used the word in his 1888 book A New Era of Thought, where he spelled it tessaract.",
            "His life was eventful. The same encyclopedia records an 1886 conviction and three-day sentence for bigamy, after which he was in Japan from 1887 and in the USA from 1892. A " + a(PDRV, "Public Domain Review collection page") + " adds that he had married Mary Ellen Boole in 1880 and Maud Florence in 1883.",
            "In the United States, according to the " + a(PAW, "Princeton Alumni Weekly") + ", he became an instructor in mathematics at Princeton in 1893 and taught there until 1897. The magazine also records that he invented a gunpowder-powered baseball-pitching machine, which stopped being used, in a contemporary’s words, on account of the fear it inspired in the batters.",
            "He wrote steadily about the fourth dimension throughout. The " + a(SFE, "encyclopedia") + " lists two collections of what he called Scientific Romances, in 1884 and 1896, then The Fourth Dimension in 1904 and An Episode of Flatland in 1907, the year of his death. The 1888 book’s contents already include a chapter on the Genesis of a Tessaract and its Representation in Three-space; the " + a(FOURTH, "1904 book") + ", which reached a second edition in 1906, works up through chapters on The Analogy of a Plane World and A Four-Dimensional Figure to The Simplest Four-Dimensional Solid, and ends with appendices called The Models and A Language of Space.",
        ]),
        ("Learning to see with cubes", [
            "Hinton did not want only to describe four-dimensional space. He wanted to feel it. His introduction to " + a(NEWERA, "A New Era of Thought") + " states the goal: “The task was to obtain a sense of the properties of higher space, or space of four dimensions.” The book’s preface, signed by the editors Alicia Boole and H. John Falk, explains the practical side: “Coloured models can easily be made by covering Kindergarten cubes with white paper.”",
            "The idea was that, by memorising arrangements of coloured cubes and learning how they would fit together if a fourth direction were available, a reader could build up an intuition for four-dimensional shapes, much as we come to know a room by moving around it. The " + a(PAW, "Princeton Alumni Weekly") + " notes that, years earlier, he had taught the Boole children geometry with wooden cubes.",
            "The cubes gained a reputation of their own. According to the " + a(PDR, "Public Domain Review") + ", people who used them reported disturbing or addictive experiences, and it was rumoured that some particularly ardent adherents of the cubes had even gone mad. The rumour is a rumour; it shows how strange the exercise seemed, not what it did.",
            "His 1904 book carried the method into print, with plates showing what Hinton called views of the tessaract. The " + a(PDRV, "Public Domain Review") + ", which reproduces them, singles out the coloured frontispiece in particular, and describes the images as offering a glimpse into the theory of four-dimensional space. They are diagrams for study, meant to be worked through slowly with the models to hand, rather than pictures to be taken in at a glance.",
            "For Hinton the project was more than geometry. In A New Era of Thought he wrote that “both in science and in conduct there are self elements”, and that getting rid of self elements means a truer apprehension of the facts. The Public Domain Review describes him as as much hyperspace philosopher as scientist, who hoped that recognising the fourth dimension would lead to a more peaceful and selfless society. That hope was his, and it was not something the mathematics could deliver.",
        ]),
        ("What a flat being would see", [
            "Hinton’s method rests on an analogy that runs through all writing on the fourth dimension. Imagine a being that lives on a flat plane and can perceive only what lies in it. A cube passing through the plane would appear to it, in the words of Hinton’s 1904 book " + a(FOURTH, "The Fourth Dimension") + ", “as a square object”: a square that appears, persists while the cube passes through, and vanishes.",
            "To understand the cube, the flat being would have to think of it as a series of sections, each like the square which forms its base, all rigidly connected together. Hinton then makes the step up. We can then consider a four-dimensional body as consisting of a series of sections, each parallel to our space, he writes, and suggests imagining the simplest four-dimensional body, one which begins as a cube.",
            "A tesseract passing through our space would therefore appear as a cube that appears, lasts, and disappears. As Hinton puts it, the flat being’s position holds for us too: “To see the whole he must relinquish part of that which he has, and take the whole portion by portion.”",
        ]),
        ("What the rotating pictures show", [
            "The images most people know, a cube inside a larger cube with the corners joined, turning in strange ways, are not pictures of a tesseract as it is. They are projections. " + a(MWH, "MathWorld") + " labels one such figure as “a projection of the tesseract in three-space.” A drawing of a cube on paper works the same way: the square faces become slanted shapes, and some look smaller than others, because three dimensions have been flattened into two.",
            "In the common cube-within-a-cube picture, the small inner cube and the large outer cube are both cells of the tesseract, as are the six shapes that join them. All eight are really equal cubes; they look different only because of the projection, as the far face of a drawn cube looks smaller than the near one. When the image rotates, the tesseract is turning in four dimensions, and its shadow seems to turn inside out.",
            "There is another way to show a tesseract: unfold it. A cube can be cut along some of its edges and laid flat as six squares in a cross shape, and " + a(MWH, "MathWorld") + " gives the number of distinct nets of the cube as 11. A tesseract can be unfolded into eight cubes in three-dimensional space, and the same sequence gives 261 distinct ways of doing it.",
            "HTML:" + K.compare("Two ways to show a tesseract in our space", [
                ("Projection", ["Shows how the cells connect"], ["Distorts sizes and angles"], "A shadow of the whole."),
                ("Net", ["Every cube appears at its true size"], ["Shows the pieces apart, not joined"], "The whole, unfolded."),
            ], source='Sources: <a href="' + MWH + '" target="_blank" rel="noopener">MathWorld, Hypercube</a>; <a href="' + MWT + '" target="_blank" rel="noopener">MathWorld, Tesseract</a>.'),
        ]),
        ("Dalí’s hypercube", [
            "The best-known unfolded tesseract hangs in a museum. Salvador Dalí’s " + a(MET, "Crucifixion (Corpus Hypercubus)") + ", painted in 1954 and in the Metropolitan Museum of Art in New York, shows Christ, in the Met’s words, levitating before a hypercube, a geometric, multidimensional form. The museum notes that the artist’s wife, Gala, poses as a devotional figure.",
            "The " + a(HOI, "History of Information") + " describes the cross in the painting as the polyhedron net of a tesseract. Read that way, the painting uses the unfolded tesseract as an image of something beyond ordinary space. That is Dalí’s symbolism, not a claim of the mathematics.",
            "Hinton’s ideas reached many other artists and writers. The " + a(PAW, "Princeton Alumni Weekly") + " lists Crowley, Lovecraft, Borges, Moore, L’Engle and Nolan among those his work influenced, and the " + a(PDR, "Public Domain Review") + " traces the spread of fourth-dimensional ideas over about thirty years to the Cubists and Duchamp.",
        ]),
        ("Space, or time?", [
            "A tesseract is a precise mathematical object, and four-dimensional geometry is routine mathematics; the " + a(MWH, "MathWorld entry on hypercubes") + " carries on to five dimensions and beyond, with a projection of the 5-hypercube among its figures. Whether physical space has a fourth spatial direction is a separate question, and the essay on " + ESSAY59 + " sets out how physicists have looked for extra dimensions and what they have found so far.",
            "The fourth dimension that is part of established physics is a different thing again. In relativity it is time, and the essay on " + ESSAY44 + " explains why that fourth coordinate does not behave like a fourth direction of space. A tesseract is not a picture of spacetime, and nothing about Hinton’s cubes bears on the physics of time.",
            "HTML:" + K.callout("warn", "A metaphor, labelled as one",
                "<p>The flat being’s situation is often borrowed for human life: we see only sections of something larger, portion by portion. That is a metaphor, and it should be read as one. Hinton used the analogy to teach geometry, and to express a philosophical hope; it is not evidence that there is a hidden dimension to experience.</p>"),
        ]),
        ("What this does and does not say", [
            "Read literally, a tesseract is the next shape in a sequence that runs from point to line to square to cube: sixteen corners, eight cubes, and a shadow in our space that looks like a cube inside a cube. The man who named it believed people could learn to sense it directly, and built a strange and memorable method for trying. Whether anyone succeeded is something the sources do not say.",
            "Other essays here explore the same territory. The essay on Flatland, linked above, follows the flat-world analogy in the novel that made it famous. " + ESSAY63.replace(">what time dilation", ">What time dilation") + " looks at the measured physics of time that the fourth dimension of relativity describes. And the essay on time as the fourth dimension, linked above, explains how that idea differs from Hinton’s.",
        ]),
    ],
    note=[
        "Hinton spelled the word tessaract; the modern spelling is tesseract. Biographical dates are from the Encyclopedia of Science Fiction, Princeton Alumni Weekly and Public Domain Review as linked.",
    ],
    faqs=[
        ("What is a tesseract in simple terms?",
         "A four-dimensional cube. A cube is made of six squares; a tesseract is made of eight cubes. It has 16 corners, 32 edges and 24 square faces."),
        ("Who invented the word tesseract?",
         "Charles Howard Hinton, a British mathematician and writer, who first used it, spelled tessaract, in his 1888 book A New Era of Thought."),
        ("What are Hinton cubes?",
         "Sets of coloured cubes Hinton designed so that readers could memorise arrangements and build an intuition for four-dimensional space. His 1888 book explains how to make them from Kindergarten cubes covered with paper."),
        ("Are the rotating tesseract images real?",
         "They are projections, the tesseract’s shadow in three dimensions shown on a flat screen. Like a drawing of a cube, they distort sizes and angles, so the eight equal cubes look different."),
        ("Is the fourth dimension of a tesseract the same as time?",
         "No. A tesseract has four directions of space. In relativity the fourth dimension is time, which behaves differently from a direction of space."),
    ],
    related=[
        ("what-flatland-teaches-about-the-fourth-dimension", "What Flatland teaches about the fourth dimension, and what it does not", "Fourth dimension"),
        ("what-physicists-mean-by-extra-dimensions", "What physicists mean by extra dimensions, and how they look for them", "Fourth dimension"),
    ],
)

if __name__ == "__main__":
    newpost.build(POST)
