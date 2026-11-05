#!/usr/bin/env python3
"""Essay 59 :: what-physicists-mean-by-extra-dimensions  (Fourth dimension)

Literal register. Sources fetched and read on 5 Nov 2026: MacTutor on
Kaluza; Ravndal (arXiv 1309.4113) on Klein; Symmetry magazine 2005 and
2006; Scientific American "Ask the experts" (Rozali); arXiv abstracts of
Arkani-Hamed, Dimopoulos and Dvali (1998) and Randall and Sundrum (1999);
CERN explainer on extra dimensions; CMS (arXiv 2604.10732, 2026), ATLAS
(arXiv 1606.02265), CMS (arXiv 1706.03794) and ATLAS (arXiv 2102.10874);
Symmetry 2013 on microscopic black holes; Lee et al. 2020 (arXiv
2002.11761) and the University of Washington news release; Physics Today
review of Warped Passages (2005).
Not used: an explicit source for "10 or 11 dimensions" beyond Rozali's
summary; safety arguments about microscopic black holes.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import newpost, postkit as K

EXT = ' target="_blank" rel="noopener"'
def a(url, text):
    return '<a href="%s"%s>%s</a>' % (url, EXT, text)

KALUZA = "https://mathshistory.st-andrews.ac.uk/Biographies/Kaluza/"
KLEIN = "https://arxiv.org/abs/1309.4113"
SYM60PDF = "https://www.symmetrymagazine.org/sites/default/files/legacy/pdfs/200506/60seconds.pdf"
SYM60 = "https://symmetrymagazine.org/article/junejuly-2005/extra-dimensions-0"
SYMSEARCH = "https://www.symmetrymagazine.org/article/december-2005january-2006/search-extra-dimensions"
SCIAM = "https://www.scientificamerican.com/article/extra-dimensional-theorie/"
ADD = "https://www.arxiv.org/abs/hep-ph/9803315"
RS = "https://www.arxiv.org/abs/hep-ph/9905221"
CERN = "https://home.cern/science/physics/extra-dimensions-gravitons-and-tiny-black-holes"
CMS17 = "https://arxiv.org/abs/1705.01403v1"
CMS26 = "https://arxiv.org/pdf/2604.10732"
ATLAS16 = "https://arxiv.org/abs/1606.02265v1"
CMSMONO = "https://arxiv.org/pdf/1706.03794"
ATLAS21 = "https://arxiv.org/pdf/2102.10874"
SYMBH = "https://www.symmetrymagazine.org/article/september-2013/the-hunt-for-microscopic-black-holes"
LEE = "https://arxiv.org/abs/2002.11761"
LEEPDF = "https://arxiv.org/pdf/2002.11761"
UW = "https://phys.washington.edu/news/2020/04/06/experiment-finds-gravity-still-works-down-50-micrometers"
HOSE = "https://physicstoday.aip.org/reviews/warped-passages-unraveling-the-mysteries-of-the-universes-hidden-dimensions"

ESSAY44 = '<a href="/writing/what-it-means-to-call-time-the-fourth-dimension">what it means to call time the fourth dimension</a>'
ESSAY49 = '<a href="/writing/what-flatland-teaches-about-the-fourth-dimension">what Flatland teaches about the fourth dimension</a>'
ESSAY53 = '<a href="/writing/what-entanglement-is">what quantum entanglement actually is</a>'

POST = dict(
    slug="what-physicists-mean-by-extra-dimensions", num=59, cat="Fourth dimension", read="auto",
    date="2026-11-05",
    gen="rewrite/59-what-physicists-mean-by-extra-dimensions.py",
    title="What physicists mean by extra dimensions, and how they look for them",
    dek="Some of the most ambitious theories in physics need more dimensions of space than the three we know. Where would they be, and why can’t we see them? Physicists have answers, and they have built experiments to test them. So far, every test has come back empty.",
    takeaway="Extra dimensions in physics are additional directions of space, beyond the familiar three, proposed to unify the forces. Theodor Kaluza showed in 1921 that a fifth dimension could combine gravity and electromagnetism, and Oskar Klein suggested such a dimension could be curled up too small to see. String theory requires extra dimensions. In 1998 a proposal suggested they might be as large as a millimetre, with gravity spreading into them, which would explain why gravity is so weak, and in 1999 another proposal used a single warped extra dimension. Experiments have looked: the Large Hadron Collider has found no excess of events that extra dimensions would produce, including no microscopic black holes, and precision measurements show Newton’s law of gravity holding down to 52 micrometres, limiting the largest extra dimension to less than 30 micrometres. There is no experimental evidence for extra dimensions, and they have not been ruled out.",
    sections=[
        ("What extra dimensions are", [
            "In physics, extra dimensions are additional directions of space beyond the three we move in, proposed in theories that try to unify the forces of nature. If they exist, they would be curled up very small, or otherwise hidden from everyday experience. Experiments have searched for them in particle collisions and in precise measurements of gravity, and have found nothing so far.",
            "HTML:" + K.takeaways([
                "The idea began in 1921, when Kaluza used a fifth dimension to combine gravity and electromagnetism.",
                "Klein suggested the extra dimension could be curled up too small to notice.",
                "String theory requires extra dimensions.",
                "A 1998 proposal suggested extra dimensions might be large enough to change gravity below a millimetre.",
                "The Large Hadron Collider and tabletop gravity tests have found no sign of them.",
                "They have not been ruled out, only limited in size.",
            ]),
            "This essay is in the literal register, like " + ESSAY44 + ". The extra dimensions here are directions of space, not time, and not a metaphor; any borrowing for human life is kept to one labelled paragraph at the end.",
            "HTML:" + K.callout("definition", "Compactified dimension",
                "<p>A dimension of space that is curled up so small that it cannot be noticed. In the words of a " + a(KLEIN, "historical paper on Oskar Klein") + ", Klein suggested that the extra dimension could be compactified, and would therefore remain unobservable when it is small enough.</p>"),
        ]),
        ("A fifth dimension to unify the forces", [
            "The idea goes back to Theodor Kaluza, a German mathematician and physicist. According to the " + a(KALUZA, "MacTutor history of mathematics archive") + ", Kaluza wrote to Einstein in April 1919 with a way of unifying gravity and electromagnetism by adding a fifth dimension; Einstein encouraged him to publish, and the paper appeared in 1921, communicated by Einstein on 8 December that year. Kaluza described the theory as possessing “virtually unsurpassed formal unity”.",
            "The obvious problem was that nobody sees a fifth dimension. The Swedish physicist Oskar Klein proposed an answer. As Finn Ravndal of the University of Oslo explains in " + a(KLEIN, "a historical paper") + ", the idea had previously been explored by Kaluza, but Klein made it more acceptable by suggesting that the extra dimension “could be compactified and therefore remain unobservable when it is small enough.” Klein’s papers appeared in 1926. The combined idea is now called Kaluza-Klein theory.",
            "A common way to picture a compact dimension comes from a garden hose. A " + a(HOSE, "Physics Today review") + " of a book on the subject makes the comparison: “just as a garden hose appears one-dimensional from a distance large compared to the diameter of the hose”, a dimension curled up small would be invisible on ordinary scales. Up close, the hose has a round direction that cannot be seen from far away.",
        ]),
        ("String theory needs them", [
            "The idea of hidden dimensions returned with string theory. As the physicist Sean Carroll put it in a " + a(SYM60PDF, "short piece for Symmetry magazine") + ": “String theory requires the existence of extra dimensions.”",
            "How many extra dimensions such theories allow is limited by other principles. In a " + a(SCIAM, "Scientific American answer") + ", the physicist Moshe Rozali explains that supersymmetry, a proposed symmetry of nature, limits the number to six or seven extra dimensions in addition to the four dimensions of length, width, height and time, and describes M-theory as a proposal to further unify the cases. He also notes that supersymmetry is still theoretical.",
            "HTML:" + K.callout("warn", "Not proven",
                "<p>String theory is not established physics. It requires extra dimensions, but neither the theory nor the dimensions have been confirmed by experiment. Statements that string theory proves there are ten or eleven dimensions get the order wrong.</p>"),
        ]),
        ("Large extra dimensions and the weakness of gravity", [
            "In 1998 three physicists proposed something bold. In a paper titled " + a(ADD, "The Hierarchy Problem and New Dimensions at a Millimeter") + ", Arkani-Hamed, Dimopoulos and Dvali proposed, in the abstract’s words, “new compact spatial dimensions large compared to the weak scale”, and noted that for the case of two new dimensions, planned sub-millimetre measurements of gravity may observe the transition.",
            "The motivation is a puzzle called the hierarchy problem: why gravity is so much weaker than the other forces. The " + a(CERN, "CERN explainer on extra dimensions") + " sets out one answer: “we don’t feel the full effect of gravity because part of it spreads to extra dimensions.” On this picture, gravity is diluted by spreading where the other forces do not.",
            "A year later Randall and Sundrum proposed a different mechanism. Their 1999 paper, " + a(RS, "A Large Mass Hierarchy from a Small Extra Dimension") + ", describes a new higher-dimensional mechanism for solving the hierarchy problem that relies on the existence of only a single additional dimension; in this essay’s gloss, the large difference in scales comes from the geometry of spacetime, which the abstract calls the background metric.",
            "HTML:" + K.table("Three ideas about extra dimensions",
                ["Proposal", "Year", "Extra dimensions", "Main idea"],
                [["Kaluza-Klein", "1921 and 1926", "One, curled up very small", "Combine gravity and electromagnetism"],
                 ["Large extra dimensions (Arkani-Hamed, Dimopoulos, Dvali)", "1998", "Two or more, possibly up to a millimetre", "Gravity spreads into them, explaining its weakness"],
                 ["Warped extra dimension (Randall, Sundrum)", "1999", "One", "The geometry of spacetime creates the difference in scales"]],
                source='Sources: <a href="' + KALUZA + '" target="_blank" rel="noopener">MacTutor</a>; <a href="' + KLEIN + '" target="_blank" rel="noopener">Ravndal</a>; <a href="' + ADD + '" target="_blank" rel="noopener">Arkani-Hamed, Dimopoulos and Dvali (1998)</a>; <a href="' + RS + '" target="_blank" rel="noopener">Randall and Sundrum (1999)</a>.'),
        ]),
        ("Why gravity is the place to look", [
            "Both proposals are tied closely to gravity, partly because of what they were invented to explain. The 1998 paper took, in its " + a(ADD, "abstract’s words") + ", the weak scale as “the only fundamental short distance scale in nature”, with the gravitational and gauge interactions becoming united at that scale. In plain terms, gravity would be as strong as the other forces at very short distances, and would only look weak at the distances we can measure.",
            "The 1999 warped model predicts its own signature. Its " + a(RS, "abstract") + " notes that there are “fundamental spin-2 excitations with mass of weak scale order”, coupled to ordinary particles with weak-scale rather than gravitational strength.",
            "String theory points the same way. The authors of the 2020 gravity test, in their " + a(LEEPDF, "paper") + ", explain that string theory’s unification of gravity with the other forces “inherently involves extra gravitational space dimensions”, which is one reason to test gravity at the shortest distances possible.",
            "The " + a(CERN, "CERN explainer") + " gives the general principle for why such dimensions could be hidden at all: “if one dimension were to contract to a size smaller than an atom, it would be hidden from our view.”",
        ]),
        ("Looking for them at the LHC", [
            "If extra dimensions are large enough, the Large Hadron Collider at CERN might reveal them. The " + a(CERN, "CERN explainer") + " describes several possible signs. Particles called gravitons, if produced, “would rapidly disappear into extra dimensions”, leaving an imbalance in momentum and energy. There might be heavier versions of particles, called Kaluza-Klein states. And if microscopic black holes appeared in collisions, they would disintegrate rapidly.",
            "None of these has been seen. " + a(SYMSEARCH, "A Symmetry magazine feature") + " of 2005 to 2006 had noted that CERN’s LHC would continue the search once it started running. A 2016 " + a(ATLAS16, "ATLAS search") + " for microscopic black holes, in models with two to six extra dimensions, reported: “No excess of events beyond Standard Model predictions is observed.” A " + a(CMSMONO, "CMS search") + " for events with a single photon and missing energy excluded values of the fundamental Planck scale up to 2.31 to 2.49 TeV, depending on the number of extra dimensions. An " + a(ATLAS21, "ATLAS search published in 2021") + ", using the full dataset of the collider’s second run, found overall agreement between the data and the Standard Model predictions.",
            "An " + a(CMS17, "earlier CMS search") + ", from the start of the collider’s second run, found “No statistically significant excess of events” and excluded such black holes and related objects with masses as high as 9.5 TeV. A " + a(CMS26, "2026 CMS search") + " for microscopic black holes, revised in August 2026 and using data from 2016 to 2018, reports: “No excesses above the standard model background predictions are observed.” In models with large extra dimensions, it excludes such black holes with masses below 8.4 to 11.4 TeV. As John Paul Chou of the CMS experiment told " + a(SYMBH, "Symmetry magazine") + " in 2013: “Scientists are watching, but so far, they haven’t found signs of microscopic black holes.”",
        ]),
        ("Testing gravity on a tabletop", [
            "The other way to look is to measure gravity itself at very short distances. Newton’s law says gravity weakens with the square of the distance. As the " + a(UW, "University of Washington") + " explains, this law, called an inverse-square law, is based purely on geometry, but if the universe has more than three spatial dimensions, the inverse-square law would break.",
            "The Eöt-Wash group at the University of Washington has tested it directly. In a " + a(LEE, "2020 paper") + " (" + a(LEEPDF, "full text") + "), Lee, Adelberger, Cook, Fleischer and Heckel reported measurements at separations between 52 micrometres and 3 millimetres. Their conclusion: “Newtonian gravity gave an excellent fit to our data.”",
            "The same measurement constrains other proposed effects too. The " + a(LEEPDF, "paper") + " reports that any gravitational-strength force of the Yukawa type, a force that switches off beyond a certain range, must have a range less than 38.6 micrometres, and that the dilaton (or a heavy graviton) must be heavier than 5.1 meV and the radion unification mass above 7.1 TeV, quantities tied to string-inspired theories. All of these limits came from data that fit Newton’s law.",
            "That sets a limit on size. In the " + a(LEEPDF, "full paper") + ", the authors conclude that “the largest extra dimension must have a toroidal radius less than 30 µm.” On this essay’s reading, that leaves no room for extra dimensions as large as the millimetre the 1998 proposal raised as a possibility, while much smaller ones remain possible.",
            "HTML:" + K.table("Where the searches stand",
                ["Search", "Result"],
                [["Tabletop gravity, University of Washington (2020)", "Newton’s law holds down to 52 µm; largest extra dimension less than 30 µm"],
                 ["Microscopic black holes, CMS (2026)", "None seen; excluded below 8.4 to 11.4 TeV in large extra dimension models"],
                 ["Missing energy, ATLAS (2021)", "Agreement with the Standard Model"]],
                source='Sources: <a href="' + LEE + '" target="_blank" rel="noopener">Lee et al. (2020)</a>; <a href="' + CMS26 + '" target="_blank" rel="noopener">CMS (2026)</a>; <a href="' + ATLAS21 + '" target="_blank" rel="noopener">ATLAS (2021)</a>.'),
        ]),
        ("What has and has not been ruled out", [
            "The searches do not prove that extra dimensions do not exist. They rule out particular sizes and energy scales in particular models. On this essay’s reading, a curled-up dimension much smaller than the experiments can probe, as in the original Kaluza-Klein idea, would leave no trace in either kind of test.",
            "The honest summary has not changed much since " + a(SYMSEARCH, "a Symmetry magazine feature") + " in the winter of 2005 to 2006 described the field’s “embarrassing dilemma”: “not a single shred of experimental evidence has been found to support their existence.” Two decades and a great deal of data later, the dilemma stands. The window for large extra dimensions has narrowed; the idea itself remains open.",
        ]),
        ("What this does and does not say", [
            "Read literally, extra dimensions are a serious, testable idea in physics with no evidence in their favour so far. They are directions of space, curled up or otherwise hidden, proposed to make the laws of nature simpler or to explain why gravity is weak. They are not time, they are not other worlds or planes of consciousness, and they are not proven.",
            "Here is the one borrowing in this essay, labelled as such. As a metaphor only, the garden hose is a useful reminder that something can look simpler from a distance than it is up close. In physics that is a claim about geometry that experiments are testing; in a life it is only a resemblance, and nothing here suggests the physics governs it.",
            "Other essays here meet the idea from different directions. " + ESSAY49.replace(">what Flatland", ">What Flatland") + " describes the older, imaginative fourth dimension of space, from the novel that first made the idea popular. The essay on time as the fourth dimension, linked above, explains the different sense in which time is a dimension of spacetime. And " + ESSAY53 + " covers another piece of physics that is often borrowed for claims it does not support.",
        ]),
    ],
    note=[
        "Klein’s 1926 papers are cited through Ravndal’s historical account. LHC limits depend on the model assumed, and only figures stated in the linked papers are given.",
    ],
    faqs=[
        ("What are extra dimensions in physics?",
         "Additional directions of space, beyond the familiar three, proposed in theories that try to unify the forces of nature. If they exist, they would be curled up very small or otherwise hidden from everyday experience."),
        ("Is there any evidence for extra dimensions?",
         "No. Particle collider searches and precise measurements of gravity have found no sign of them. They have been limited in size, not ruled out."),
        ("How many dimensions do these theories need?",
         "Theories of this kind are usually described as having ten or eleven dimensions in all. The physicist Moshe Rozali, in a Scientific American explainer, says supersymmetry limits the extra dimensions to six or seven beyond the familiar four. None of these theories has been confirmed by experiment."),
        ("Could the Large Hadron Collider make black holes?",
         "Some extra-dimension models predicted microscopic black holes at the LHC, which would disintegrate rapidly. Searches have found none, and a 2026 CMS search excludes them below about 8.4 to 11.4 TeV in large extra dimension models."),
        ("Is time one of the extra dimensions?",
         "No. Time is the fourth dimension of spacetime in relativity. The extra dimensions proposed in physics are additional dimensions of space, beyond the three we know."),
    ],
    related=[
        ("what-flatland-teaches-about-the-fourth-dimension", "What Flatland teaches about the fourth dimension, and what it does not", "Fourth dimension"),
        ("what-it-means-to-call-time-the-fourth-dimension", "What it means to call time the fourth dimension, and what it does not", "Fourth dimension"),
    ],
)

if __name__ == "__main__":
    newpost.build(POST)
