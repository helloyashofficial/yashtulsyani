#!/usr/bin/env python3
"""Essay 49 :: what-flatland-teaches-about-the-fourth-dimension  (Fourth dimension)

Literal register. Sources fetched and read on 3 Nov 2026: the 1884 Seeley
scan of the second edition (Internet Archive); Project Gutenberg 201 for
Part I, the dedication and the preface; Standard Ebooks chapter pages for
Part II (modernised spelling); Lit2Go (USF) for section 18 and the list of
section titles; Banchoff's Abbott materials at Brown; MacTutor; McCarthy
(Expositions, 2007); Mathematics Awareness Month 2000; Peterson (Science
News, 2002); Feiden (1982); Rucker's introduction to Hinton; Crabb (Public
Domain Review, 2015); MathWorld "Hypercube"; Union College 4D notes;
Banchoff (ISR, 1990); Einstein Online "Spacetime"; Symmetry (2005, 2006);
the Brown archive copy of Garnett's 1920 Nature text.
Deliberately not claimed: that Abbott predicted relativity; that Abbott and
Hinton knew each other; who "H. C." in the dedication is; that Hinton
certainly coined "tesseract".
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import newpost, postkit as K

EXT = ' target="_blank" rel="noopener"'
def a(url, text):
    return '<a href="%s"%s>%s</a>' % (url, EXT, text)

SCAN = "https://archive.org/stream/flatlandromanceo1884abbo/flatlandromanceo1884abbo_djvu.txt"
GUT = "https://www.gutenberg.org/cache/epub/201/pg201-images.html"
SE = "https://standardebooks.org/ebooks/edwin-a-abbott/flatland/text/"
SE13, SE16, SE19, SE20, SE22 = (SE + "chapter-13", SE + "chapter-16", SE + "chapter-19", SE + "chapter-20", SE + "chapter-22")
L2G = "https://etc.usf.edu/lit2go/5/flatland/"
L2G18 = "https://etc.usf.edu/lit2go/5/flatland/41/part-2-section-18-how-i-came-to-spaceland-and-what-i-saw-there/"
BANEAA = "https://www.math.brown.edu/tbanchof/EAA32003.pdf"
MACT = "https://mathshistory.st-andrews.ac.uk/Biographies/Abbott/"
MCC = "https://expositions.journals.villanova.edu/index.php/expositions/article/download/55/38/56"
MAM = "https://ww2.amstat.org/mam/00/master/people/abbott/satire.html"
PETER = "https://sciencenews.org/article/stranger-spaceland"
BAN91 = "https://www.math.brown.edu/tbanchof/abbott/Flatland/Publications/1991princeton_intro.shtml"
FEIDEN = "https://www.math.brown.edu/tbanchof/abbott/Flatland/Publications/1982emerson_intro.shtml"
RUCKER = "https://www.rudyrucker.com/pdf/rucker_charles_hinton_intro.pdf"
PDR = "https://publicdomainreview.org/essay/notes-on-the-fourth-dimension"
MW = "https://mathworld.wolfram.com/Hypercube.html"
UNION = "https://www.math.union.edu/~dpvc/math/4D/welcome.html"
ISR = "https://www.math.brown.edu/tbanchof/gc/ISR/ISR.html"
EO = "https://www.einstein-online.info/en/explandict/spacetime/"
SYM06 = "https://www.symmetrymagazine.org/article/december-2005january-2006/search-extra-dimensions"
SYM05 = "https://symmetrymagazine.org/article/junejuly-2005/extra-dimensions-0"
GARNETT = "https://library.brown.edu/cds/flatweb/1920nature.html"

ESSAY44 = '<a href="/writing/what-it-means-to-call-time-the-fourth-dimension">what it means to call time the fourth dimension</a>'
ESSAY48 = '<a href="/writing/why-time-has-a-direction">why time has a direction</a>'
ESSAY41 = '<a href="/writing/what-the-observer-effect-actually-says">the essay on the observer effect</a>'

POST = dict(
    slug="what-flatland-teaches-about-the-fourth-dimension", num=49, cat="Fourth dimension", read="auto",
    date="2026-11-03",
    gen="rewrite/49-what-flatland-teaches-about-the-fourth-dimension.py",
    title="What Flatland teaches about the fourth dimension, and what it does not",
    dek="A Victorian schoolmaster wrote a short novel about a square who lives on a flat plane and is visited by a sphere. It is still the best way in to thinking about a fourth dimension of space. It is not about time, and it did not predict relativity.",
    takeaway="Flatland, published in London in 1884 under the pen name A Square and written by the headmaster Edwin Abbott Abbott, is two books in one. The first half is a satire of a rigid society of shapes, including its treatment of women. The second half is a lesson in thinking about dimensions: a two-dimensional being cannot picture a third dimension, but can reason about it by analogy and can see it in slices. The Square uses the same analogy to guess at a fourth dimension of space and describes, correctly, a figure with sixteen corners and eight cubes for sides: the tesseract. The book's fourth dimension is spatial. Linking it to time came later, from readers of relativity.",
    sections=[
        ("What Flatland teaches", [
            "Flatland teaches that a being cannot picture a dimension beyond its own, but can still reason about one: by analogy, from the pattern of point, line, square and cube, and by watching how a higher shape appears in slices as it passes through a lower world. Its fourth dimension is an extra direction of space, not time.",
            "HTML:" + K.takeaways([
                "Flatland was published in London in 1884 under the pen name A Square. Its author was the headmaster Edwin Abbott Abbott.",
                "The first half is a social satire. Commentators read its treatment of women as targeted at Victorian attitudes, not endorsed.",
                "The second half visits worlds of one, two, three and zero dimensions.",
                "Its central lesson is analogy: from point to line to square to cube, and then one step further.",
                "The Square correctly describes a four-dimensional cube, later called the tesseract.",
                "The book’s fourth dimension is spatial. The link with time came after relativity.",
            ]),
            "This essay is in the literal register, like " + ESSAY41 + ". It reports what the book says, what scholars say about it and what the mathematics says, and keeps any borrowing for human life to one labelled paragraph at the end.",
            "HTML:" + K.callout("definition", "A dimension, in this essay",
                "<p>An independent direction in which something can move or be measured. A line has one, a flat plane two, ordinary space three. A fourth dimension of space would be a fourth direction at right angles to all three. That is a mathematical idea, and nothing in this essay claims such a direction exists.</p>"),
        ]),
        ("A book by A Square", [
            "The title page of the " + a(SCAN, "second edition, published by Seeley in London in 1884") + ", reads Flatland: A Romance of Many Dimensions, With Illustrations by the Author, A Square. A biographical profile of Abbott on the Brown University pages of the mathematician Thomas Banchoff notes that it was " + a(BANEAA, "first published in November 1884, with a second and slightly revised edition appearing a month later") + ".",
            "The author behind the square was Edwin Abbott Abbott. According to " + a(MACT, "the MacTutor biography at the University of St Andrews") + ", he was born in Marylebone on 20 December 1838, was ordained deacon in 1862 and priest in 1863, was headmaster of the City of London School from 1865 to 1889, and died in Hampstead on 12 October 1926.",
            "The book opens with a dedication, which in " + a(GUT, "Project Gutenberg’s text") + " reads “To The Inhabitants of SPACE IN GENERAL And H. C. IN PARTICULAR This Work is Dedicated”. It goes on to hope that, as a humble native of Flatland was initiated into three dimensions, the citizens of Space may aspire “To the Secrets of FOUR FIVE OR EVEN SIX Dimensions”. Who H. C. was, none of the sources consulted for this essay says, and this essay does not guess.",
            "HTML:" + K.callout("note", "Which text is quoted",
                "<p>Part I and the preface are quoted from Project Gutenberg’s text of the second edition. Part II is quoted from Standard Ebooks, whose text modernises spelling, and one passage from Lit2Go’s reproduction of the 1885 Boston edition.</p>"),
        ]),
        ("A world of shapes, and a satire", [
            "The narrator explains his world first. " + a(GUT, "“I call our world Flatland,”") + " he begins, “not because we call it so, but to make its nature clearer to you, my happy readers, who are privileged to live in Space.” Its inhabitants are flat figures that move about on a plane, looking, he says, very much like shadows, only hard and with luminous edges.",
            "Rank in Flatland is geometry. In the same text, Section 3 sets out the order: “Our Women are Straight Lines.” “Our Soldiers and Lowest Classes of Workmen are Triangles with two equal sides.” The middle class are equilateral triangles; the professional men and gentlemen are squares and pentagons, “to which class I myself belong”; the nobility begins with hexagons; and at the top is “the Circular or Priestly order”.",
            "HTML:" + K.table("The order of Flatland",
                ["Rank", "Shape"],
                [["Women", "Straight lines"],
                 ["Soldiers and lowest workmen", "Triangles with two equal sides"],
                 ["Middle class", "Equilateral triangles"],
                 ["Professional men and gentlemen", "Squares and pentagons"],
                 ["Nobility", "Hexagons and upwards"],
                 ["Priests, the highest class", "Circles"]],
                source='Source: <a href="' + GUT + '" target="_blank" rel="noopener">Flatland, Part I, Section 3, Project Gutenberg</a>.'),
            "Section 4, on women, is where modern readers most often stop. The narrator calls women “wholly devoid of brain-power”, quotes “Once a Woman, always a Woman” as a decree of nature, and describes houses with “one entrance in the Eastern side, for the use of Females only.” Read flatly, it is ugly.",
            "Scholars mostly do not read it flatly. A. C. McCarthy, in " + a(MCC, "a review essay in the journal Expositions in 2007") + ", says Victorian readers took the book as “a satire of the more repressive aspects of nineteenth-century British society”, notes that Abbott was “intensely interested in the cause of women’s education”, and observes that the narrator “persists in regarding himself as a unique case of wrongful imprisonment in a system that is otherwise sound.” The " + a(MAM, "Mathematics Awareness Month materials of 2000") + " call Abbott “a firm believer in equality of educational opportunity, across social classes and in particular for women”, and " + a(PETER, "Ivars Peterson in Science News") + " calls the book “a sharply delineated satire”.",
            "Not every reader is fully persuaded. A " + a(FEIDEN, "summary of Karen Feiden’s introduction to a 1982 edition") + " says she calls Abbott “a subtle satirist” while still questioning his treatment of women and the lower classes. And the second-edition preface, headed “By the Editor”, has the Square say he has modified his views on women; Banchoff notes that this preface was " + a(BAN91, "“purportedly written by an editor but actually written by Abbott himself”") + ". McCarthy finds the claimed change of heart unconvincing.",
        ]),
        ("Four worlds", [
            "Part II, titled Other Worlds in " + a(L2G, "the list of sections") + ", is where the book turns to dimensions. The Square meets four worlds in turn. In some he is the one who knows more; in others, the one who knows less.",
            "HTML:" + K.stages("The four worlds of Part II", [
                ("1", "Lineland", "In a dream the Square visits a one-dimensional world whose King cannot conceive of anything off his line, and fails to explain the plane to him."),
                ("2", "Flatland visited", "A Sphere arrives and passes through the plane. The Square sees only a circle that grows, then shrinks, and does not believe in a third dimension."),
                ("3", "Spaceland", "The Sphere lifts the Square out of the plane. He sees his own world from above, every house open to view."),
                ("0", "Pointland", "In a vision they visit a being of no dimensions, who thinks it is the whole universe."),
            ], source='Sections 13 to 20 of Flatland; see <a href="' + L2G + '" target="_blank" rel="noopener">the section titles at Lit2Go</a>.'),
            "In " + a(SE13, "Lineland") + " the Square meets a vast multitude of small straight lines, and to the eye of a Linelander each is only a point. The King tells him, “I am the Monarch of the world.” The Square tries to explain a second dimension and cannot, because the King has no way to picture a direction that is not along his line.",
            "Then the roles are reversed. A Sphere visits Flatland, and all the Square can see is the slice of it that lies in his plane, a circle. The Sphere tries to explain: " + a(SE16, "“I am not a Circle, but an infinite number of Circles”") + ". As it rises out of the plane, “my Circle will become smaller and smaller till it dwindles to a point and finally vanishes”. The Square, who was so patient with the King of Lineland, is no better a pupil.",
            "So the Sphere stops talking and takes him out of the plane. The experience in " + a(L2G18, "Section 18") + " is at first one of horror, and then of seeing: “my native city, with the interior of every house and every creature therein, lay open to my view in miniature.” From a third dimension, the insides of two-dimensional things are as visible as the outside.",
        ]),
        ("The argument from analogy", [
            "The most important chapter, for anyone interested in a fourth dimension, is the one in which the Square starts to argue back. Having seen three dimensions, he asks why there should not be a fourth. His method, in " + a(SE19, "Standard Ebooks’ text of the chapter") + ", is the pattern of what moving figures produce. A moving point produces a line with two terminal points. A moving line produces a square with four. A moving square produces a cube with eight. Then a moving cube, he argues, should produce “a still more divine organization with sixteen terminal points”, “strictly according to Analogy”, bounded by “eight solid Cubes for his perimeter”.",
            "The Square is right. The figure he describes is what is now called a tesseract or four-dimensional hypercube, and " + a(MW, "MathWorld’s entry") + " gives its parts: “A tesseract has 16 polytope vertices, 32 polytope edges, 24 squares, and eight cubes.” The same entry gives the general rule: an n-dimensional cube has 2 to the power n corners, and in general the number of k-dimensional faces is the binomial coefficient of n and k times 2 to the power n minus k.",
            "HTML:" + K.table("Following the analogy",
                ["Figure", "Corners", "Edges", "Squares", "Cubes"],
                [["Point", "1", "0", "0", "0"],
                 ["Line", "2", "1", "0", "0"],
                 ["Square", "4", "4", "1", "0"],
                 ["Cube", "8", "12", "6", "1"],
                 ["Tesseract", "16", "32", "24", "8"]],
                source='Counts from the formula and tesseract figures in <a href="' + MW + '" target="_blank" rel="noopener">Weisstein, “Hypercube”, Wolfram MathWorld</a>.',
                num_cols=(1, 2, 3, 4)),
            "The Sphere’s response is the comic and philosophical centre of the book. The being who has just explained the third dimension to a sceptical square will not hear of a fourth. When the Square first presses him, the Sphere snaps “Pooh! Stuff! Enough of this trifling!” Asked where the land of four dimensions is, he answers, “There is no such land. The very idea of it is utterly inconceivable.” And when the Square appeals to the argument from analogy, the reply is “Analogy! Nonsense: what analogy?”",
            "The lesson is not that a fourth dimension of space exists. It is that the Sphere makes exactly the mistake it scolded the Square for, and the King of Lineland before him: treating the limit of its own imagination as the limit of what is possible. The argument from analogy does not prove anything about the world. It does show that a higher dimension can be thought about consistently, and its properties worked out, by a being that cannot picture it.",
            "Pointland makes the same point from the other end. There the Square and the Sphere find " + a(SE20, "“the realm of Pointland, the abyss of no dimensions”") + ", inhabited by a being who “is himself his own world, his own universe.” The Point is perfectly content, and perfectly unable to learn. The Sphere draws the lesson that “to aspire is better than to be blindly and impotently happy”.",
        ]),
        ("Slices and shadows", [
            "Flatland also gives the two methods mathematicians still use to show four-dimensional shapes to three-dimensional people. The first is slicing. Course notes from " + a(UNION, "Union College on the fourth dimension") + " put it this way: “Flatlanders can understand a sphere as a sequence of circles changing over time.” A cube passing face first through the plane would appear as a square that appears, stays for a while and disappears. In the same way a tesseract passing through our space would appear as a solid that changes, and the notes show such slicing sequences for the hypercube.",
            "The second is the shadow, or projection, which " + a(ISR, "Banchoff") + " also uses. A cube can be drawn on flat paper as a square inside a square with the corners joined; a tesseract can be shown by its shadow in our three dimensions, what Banchoff calls “the shadow of a four-dimensional box”. The Union College notes suggest looking at a sequence of shadows as the shape rotates, rather than a single still one. In the same 1990 article, Banchoff, who uses computer graphics to show such shapes, wrote that “we share with A Square, the protagonist of Flatland, an inability to ‘see’ in a dimension higher than our own”.",
            "HTML:" + K.callout("note", "The cover of this essay",
                "<p>The drawing at the top shows the first method: a sphere crossing a plane, and below it what a Flatlander would see, a point that grows into a circle, reaches its largest size, shrinks and vanishes.</p>"),
        ]),
        ("Hinton and the tesseract", [
            "Flatland was not alone. Charles Howard Hinton had already published an essay called What Is the Fourth Dimension? in 1880 in the Dublin University Magazine, as " + a(RUCKER, "Rudy Rucker records in his introduction to Hinton’s writings") + ". Hinton went further than Abbott in one direction: he tried to train himself to visualise four dimensions directly, and Rucker describes him memorising a block of 46,656 small cubes, 36 on each side, as part of the effort.",
            "The word tesseract is associated with Hinton. Rucker says it is a word Hinton may have coined himself, and " + a(PDR, "Jon Crabb at the Public Domain Review") + " notes that Hinton first used it in his 1888 book A New Era of Thought, spelled tessaract at first. Whether anyone used it earlier, neither source settles.",
            "Hinton knew Abbott’s book. Introducing his own story of a two-dimensional world, A Plane World, he wrote, as " + a(RUCKER, "Rucker quotes") + ", that he would have liked to refer readers to “that ingenious work, ‘Flatland’”, but that Abbott’s aims had been different. That is the extent of the documented link between them; nothing in the sources consulted says the two men collaborated or knew each other.",
        ]),
        ("Not time, not yet", [
            "The most common mistake about Flatland is to treat it as a book about time. Abbott’s fourth dimension is a fourth direction of space, one more step in the pattern of point, line, square and cube. Nothing in the book says that the fourth dimension is time.",
            "The idea that time is the fourth dimension comes from relativity, and is the subject of " + ESSAY44 + ". In spacetime, as " + a(EO, "Einstein Online, from the Max Planck Institute for Gravitational Physics") + ", explains, “three serve to fix its location in three-dimensional space, while the fourth gives the point in time for the event”. As that essay explains, the fourth coordinate does not behave like a fourth direction of space, and it is not what the Square imagined.",
            "The link between the two was made by readers after relativity, not by Abbott. In 1920, in a text printed in Nature and reproduced in " + a(GARNETT, "Brown University’s Flatland archive") + ", William Garnett recalled that “some thirty or more years ago a little jeu d’esprit was written by Dr. Edwin Abbott entitled Flatland”, and that it “did not attract as much attention as it deserved”. Garnett then made the link to time himself: if our space were moving relative to a fourth dimension, “all the changes we experience and assign to the flow of time will be due simply to this movement”. That was Garnett in 1920, not Abbott in 1884. Banchoff, in " + a(BAN91, "his 1991 introduction") + ", notes that when the book was reissued in 1926, with an introduction by Garnett, described as a physicist and a student of Abbott’s, the main stimulus for interest in higher dimensions was relativity theory. MacTutor says only that Flatland predated Einstein’s four-dimensional world by many years. Predating is not predicting.",
            "Crabb, at the Public Domain Review, describes the change in the popular imagination: by the late 1920s, " + a(PDR, "Einsteinian spacetime had more or less replaced the spatial fourth dimension") + ". Extra spatial dimensions have not disappeared from physics; " + a(SYM05, "Symmetry magazine notes") + " that string theory requires them. But the same magazine, in " + a(SYM06, "a feature on the search for them") + ", reported that so far, “not a single shred of experimental evidence has been found to support their existence.” A fourth dimension of space remains, as it was for the Square, a consistent idea rather than an observed fact.",
            "HTML:" + K.table("Three different fourth dimensions",
                ["Idea", "What the fourth dimension is", "Status"],
                [["Flatland (1884) and Hinton (from 1880)", "A fourth direction of space", "A consistent mathematical idea"],
                 ["Relativity", "Time, joined with space as spacetime", "Physical structure, tested by experiment"],
                 ["Extra dimensions in string theory", "Further spatial dimensions", "Required by the theory; no experimental evidence so far"]],
                source='Sources: <a href="' + RUCKER + '" target="_blank" rel="noopener">Rucker</a>; <a href="' + EO + '" target="_blank" rel="noopener">Einstein Online</a>; <a href="' + SYM05 + '" target="_blank" rel="noopener">Symmetry (2005)</a> and <a href="' + SYM06 + '" target="_blank" rel="noopener">(2006)</a>.'),
        ]),
        ("What Flatland does and does not teach", [
            "Read literally, the book teaches three things. A being cannot picture a dimension beyond its own. It can still reason about one, by analogy, and get the right answers, as the Square does with the tesseract. And it can learn to see a higher shape in slices and shadows, as mathematicians still do. The book does not show that a fourth dimension of space exists, it does not say that time is that dimension, and it did not foresee relativity.",
            "The story ends badly for its narrator. In " + a(SE22, "the last chapter") + " his efforts to spread the theory of three dimensions end in a sentence of perpetual imprisonment. Writing later, he says, “Seven years have elapsed and I am still a prisoner,” and hopes his memoir may stir up “a race of rebels who shall refuse to be confined to limited Dimensionality.”",
            "Here is the one borrowing in this essay, labelled as such. As a metaphor only, the Sphere is the most useful figure in the book: someone who can see further than others, explains it well, and then refuses the next step up with “There is no such land.” Most people are the Sphere about something. In the book that is a point about dimensions; in a life it is only a resemblance, and nothing here suggests geometry governs it.",
            "The essay on time as the fourth dimension, linked above, sets out the physics of the other fourth dimension, the one that is time. And " + ESSAY48 + " asks why that dimension, unlike any direction in space, seems to run only one way.",
        ]),
    ],
    note=[
        "Part II of Flatland is quoted from Standard Ebooks, whose text modernises spelling, and Section 18 from Lit2Go’s reproduction of the 1885 Boston edition; other quotations follow Project Gutenberg’s text of the 1884 second edition.",
    ],
    faqs=[
        ("What is Flatland about?",
         "Flatland: A Romance of Many Dimensions (1884) is narrated by a square living in a two-dimensional world. The first half satirises its rigid society of shapes; the second follows the Square's visits to worlds of one, three and zero dimensions, and his attempt to reason about a fourth."),
        ("Who wrote Flatland?",
         "Edwin Abbott Abbott (1838 to 1926), headmaster of the City of London School from 1865 to 1889, published it under the pen name A Square. It first appeared in November 1884, with a slightly revised second edition a month later."),
        ("Is Flatland's fourth dimension time?",
         "No. In Flatland the fourth dimension is a fourth direction of space, reached by extending the pattern of point, line, square and cube. Time became known as the fourth dimension through relativity, and readers began linking the book to it in the 1920s."),
        ("What is a tesseract?",
         "A four-dimensional cube, or hypercube. It has 16 corners, 32 edges, 24 square faces and 8 cubes as its boundary. Flatland's Square describes it by analogy, and Charles Hinton used the word tesseract for it in 1888."),
        ("Is Flatland sexist?",
         "Its narrator is. Most commentators read the treatment of women as satire of Victorian attitudes, noting that Abbott supported women's education, though some readers still question how far the satire succeeds."),
    ],
    related=[
        ("what-it-means-to-call-time-the-fourth-dimension", "What it means to call time the fourth dimension, and what it does not", "Fourth dimension"),
        ("why-time-has-a-direction", "Why time has a direction, and what entropy does and does not explain", "Physics and time"),
    ],
)

if __name__ == "__main__":
    newpost.build(POST)
