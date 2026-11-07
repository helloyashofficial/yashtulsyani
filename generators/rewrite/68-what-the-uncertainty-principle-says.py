#!/usr/bin/env python3
"""Essay 68 :: what-the-uncertainty-principle-says  (Physics and time)

Sources fetched and read on 7 Nov 2026: Heisenberg (1927), English
translation as NASA TM-77379 (1983), via the nLab copy and the NTRS record;
Stanford Encyclopedia of Philosophy, The Uncertainty Principle (Hilgevoord
and Uffink, revised 2016); Erhart and others (2012), arXiv copy of the Nature Physics
paper; Vienna University of Technology release on it (EurekAlert);
University of Toronto News (2012) on Rozema and others, Physical Review
Letters; Busch, Lahti and Werner (2013), Physical Review Letters, arXiv
abstract.
Not used: numerical values of Planck's constant (no primary source fetched);
claims about consciousness or observers, which the physics does not make.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import newpost, postkit as K

EXT = ' target="_blank" rel="noopener"'
def a(url, text):
    return '<a href="%s"%s>%s</a>' % (url, EXT, text)

HEIS = "https://ncatlab.org/nlab/files/Heisenberg-ActualContent.pdf"
NTRS = "https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/19840008978.pdf"
SEP = "https://plato.stanford.edu/ENTRIES/qt-uncertainty/"
ERH = "https://arxiv.org/pdf/1201.1833"
TUW = "https://www.eurekalert.org/pub_releases/2012-01/vuot-ayc011612.php"
UOFT = "https://utoronto.ca/news/u-t-scientists-cast-doubt-uncertainty-principle"
BLW = "https://www.arxiv.org/abs/1306.1565"

ESSAY41 = '<a href="/writing/what-the-observer-effect-actually-says">what the observer effect actually says</a>'
ESSAY53 = '<a href="/writing/what-entanglement-is">what entanglement is</a>'
ESSAY63 = '<a href="/writing/what-time-dilation-is">what time dilation is</a>'
ESSAY62 = '<a href="/writing/what-spinoza-meant-by-hope-and-fear">what Spinoza meant by hope and fear</a>'

POST = dict(
    slug="what-the-uncertainty-principle-says", num=68, cat="Physics and time", read="auto",
    date="2026-11-07",
    gen="rewrite/68-what-the-uncertainty-principle-says.py",
    title="What the uncertainty principle actually says, and what it does not",
    dek="The uncertainty principle is often summed up as “measuring something disturbs it.” That is how Heisenberg first explained it in 1927, but it is only part of the story. The modern form is about the spread of a quantum state itself, and experiments in 2012 showed that measurement need not disturb as much as Heisenberg’s original formula suggested.",
    takeaway="In 1927 Werner Heisenberg argued that, for pairs of quantities such as position and momentum, the more precisely one is determined, the less precisely the other can be known. He illustrated this with a thought experiment in which observing an electron with light disturbs it. The same year, Kennard gave the first mathematically exact form, an inequality on the statistical spreads of the two quantities, which Robertson generalised in 1929. That version is not about disturbance at all: it describes how sharply a quantum state can define both quantities at once. In 2012, experiments in Vienna and Toronto found that a Heisenberg-style trade-off between measurement error and disturbance can be beaten; in the Vienna experiment, a more general relation proposed by Masanao Ozawa held. Other physicists showed that, with different definitions, a Heisenberg-type error-disturbance relation can be proved. Either way, the intrinsic uncertainty of quantum states remains. None of this concerns consciousness.",
    sections=[
        ("What the uncertainty principle says", [
            "The uncertainty principle says that some pairs of quantities, such as a particle’s position and momentum, cannot both be sharply defined at once. The more narrowly one is pinned down, the more spread out the other must be. In its standard modern form it is a statement about quantum states, not about clumsy instruments.",
            "HTML:" + K.takeaways([
                "Heisenberg proposed it in 1927, illustrating it with light disturbing an electron.",
                "Kennard gave the first exact form the same year, about statistical spreads.",
                "That form concerns how sharply a state defines two quantities, not disturbance.",
                "In 2012, experiments showed measurement can disturb less than Heisenberg’s formula implied.",
                "Other physicists proved a Heisenberg-type trade-off using different definitions.",
                "Nothing in it involves consciousness or minds.",
            ]),
            "This essay is in the literal register, like " + ESSAY41 + ". It sets out what Heisenberg wrote, what the later mathematics says, and what the experiments found, and keeps any borrowing for human life to one labelled box near the end.",
            "HTML:" + K.callout("definition", "Uncertainty relation",
                "<p>In the form due to Kennard (1927), described in the " + a(SEP, "Stanford Encyclopedia of Philosophy") + ": the product of the standard deviations of position and momentum is at least ħ/2, where ħ is the reduced Planck constant. Standard deviation measures how spread out a quantity’s possible values are.</p>"),
        ]),
        ("Heisenberg’s 1927 paper", [
            "The principle comes from a 1927 paper by Werner Heisenberg in the Zeitschrift für Physik. Its English translation, issued by NASA in 1983 as " + a(NTRS, "Technical Memorandum 77379") + ", states the core claim in its abstract: “Canonically conjugated variables are determined simultaneously only with a characteristic uncertainty.” Position and momentum are the standard example of such a pair. In the mathematics of the theory, the paper ties this to the fact that the two quantities do not commute: multiplying them in one order gives a different result from multiplying them in the other, as expressed in the relation Pq − qP = h/2πi.",
            "Heisenberg made the idea concrete with a thought experiment, often called the gamma-ray microscope. To see where an electron is, you must shine light on it, and to locate it very precisely you need light of very short wavelength. But such light carries a large kick, and when it scatters off the electron it changes the electron’s momentum by an amount that cannot be fully controlled. In the " + a(HEIS, "NASA translation") + ": “That is, the more precisely the position is determined, the more imprecisely will the impulse be known, and vice-versa.” Impulse is the translation’s word for momentum.",
            "Heisenberg drew strong conclusions from this. The paper says that the classical “orbit” of an electron “only comes into being by our observing it,” and that “quantum mechanics once and for all establishes the invalidity of the law of causality.” The law he meant is stated in the paper as “If we know the present precisely, we can calculate the future,” and his point was that the premise fails: the present cannot be known precisely in all its parameters. These sentences have been widely debated, and they are Heisenberg’s interpretation, not the only one physicists hold.",
        ]),
        ("Not quite a disturbance story", [
            "Heisenberg’s microscope makes uncertainty sound like a practical problem: we disturb things when we look at them. That reading was challenged at once. According to the " + a(SEP, "Stanford Encyclopedia of Philosophy") + ", Niels Bohr objected that it is not the change in the electron’s momentum that matters, but that this change cannot be precisely determined in the same experiment. For Bohr the limit lay in what any single experimental arrangement can define, not in a nudge.",
            "Heisenberg himself did not settle on one name for the idea. The encyclopedia notes that his favourite terms were Ungenauigkeitsrelationen, inaccuracy relations, and Unbestimmtheitsrelationen, indeterminacy relations. The two words point in different directions: one suggests our measurements are imprecise, the other that the quantities themselves are not fully determined.",
            "The English word uncertainty blurs the difference, and much popular confusion starts there. It sounds as if the particle has an exact position and momentum that we simply cannot find out. In the standard modern reading, that is not what the mathematics says.",
        ]),
        ("The exact form: spreads, not nudges", [
            "The first mathematically exact formulation, the " + a(SEP, "encyclopedia") + " records, is due to Kennard in 1927: an inequality stating that the product of the standard deviations of position and momentum is at least ħ/2. In 1929, Robertson generalised it to any pair of observables, with the size of the bound set by how the two fail to commute.",
            "This version says nothing about measuring devices. It concerns the spreads of the probability distributions that a quantum state assigns to the two quantities. Prepare many particles in the same state, measure position on some and momentum on others, and the spreads in the two sets of results cannot both be made arbitrarily small. The encyclopedia distinguishes these statements about the spreads of the probability distributions from disturbance-type relations, which ask “how much one variable is disturbed by the accurate measurement of another.”",
            "So there are really two questions under one name. One is about states: how sharply can a quantum state define two quantities at once? The other is about measurements: how accurately can you measure one quantity without disturbing another? Kennard’s inequality answers the first. Heisenberg’s microscope was an attempt to answer the second.",
            "HTML:" + K.table("Two questions under one name",
                ["Question", "About", "Classic answer"],
                [["How sharply can a state define both?", "The quantum state itself", "Kennard 1927, Robertson 1929"],
                 ["How much does measuring one disturb the other?", "The measuring process", "Heisenberg’s 1927 microscope argument"]],
                source='Source: <a href="' + SEP + '" target="_blank" rel="noopener">Stanford Encyclopedia of Philosophy, The Uncertainty Principle</a>.'),
        ]),
        ("The 2012 experiments", [
            "The measurement question was tested directly in 2012. A Vienna team led by Yuji Hasegawa, working with the Japanese theorist Masanao Ozawa, used neutrons. Rather than position and momentum, the " + a(TUW, "release") + " explains, they measured the spin of neutrons in two different directions, which obey an uncertainty relation of the same kind. Their " + a(ERH, "paper in Nature Physics") + " reports a neutron optical experiment that records the error of a spin-component measurement and the disturbance it causes. In its words, “The results confirm that both error and disturbance completely obey the new, more general relation,” the one Ozawa had proposed, “but violate the old one in a wide range of an experimental parameter.”",
            "The Vienna University of Technology " + a(TUW, "release") + " is careful about what that means. “The uncertainty principle is of course still true,” it says, but the uncertainty “does not always come from the disturbing influence of the measurement.” Hasegawa is quoted: “The smaller the error in one measurement, the larger the disturbance of the other - this rule still holds.” What failed was Heisenberg’s particular formula for the trade-off, not the existence of a trade-off.",
            "Later that year, a group at the University of Toronto reached a similar conclusion with single photons. According to " + a(UOFT, "University of Toronto News") + ", Lee Rozema and colleagues in Aephraim Steinberg’s group used weak measurements, gentle enough to barely affect the system, and found that “the disturbance induced by the measurement is less than Heisenberg’s precision-disturbance relation would require.” Each weak measurement told them very little on its own; “Each shot only gave us a tiny bit of information about the disturbance,” Rozema said, but repeating the experiment many times built up a reliable picture. “The results force us to adjust our view of exactly what limits quantum mechanics places on measurement,” Rozema said. The article stresses that the quantum world remains uncertain.",
        ]),
        ("A disagreement about definitions", [
            "Not everyone accepted that Heisenberg had been shown wrong. In a 2013 paper in Physical Review Letters titled " + a(BLW, "Proof of Heisenberg’s error-disturbance relation") + ", Paul Busch, Pekka Lahti and Reinhard Werner argued that “Heisenberg-type inequalities can be proven that describe a trade-off between the precision of a position measurement” and the disturbance it causes to momentum.",
            "The difference lies in how error and disturbance are defined. Busch, Lahti and Werner use measures that are properties of the measuring device, which they call state independent and which give worst-case estimates across all states. With those definitions, a relation of Heisenberg’s form holds.",
            "The disagreement is largely about which quantities best capture Heisenberg’s idea. The fair summary is that the measurement side of the uncertainty principle is subtler than the textbook microscope story, and that whether Heisenberg’s formula is violated depends on how its terms are made precise. The state side, Kennard’s inequality, is not in dispute.",
            "HTML:" + K.compare("Was Heisenberg’s measurement trade-off wrong?", [
                ("Yes, as stated", ["Vienna and Toronto results, 2012", "In Vienna, Ozawa’s more general relation held"], ["Uses state-dependent definitions"], "The formula needs revising."),
                ("No, if defined differently", ["A 2013 proof with device-based, worst-case measures"], ["Answers a slightly different question"], "A trade-off of his form holds."),
            ], source='Sources: <a href="' + ERH + '" target="_blank" rel="noopener">Erhart and others (2012)</a>; <a href="' + UOFT + '" target="_blank" rel="noopener">University of Toronto News (2012)</a>; <a href="' + BLW + '" target="_blank" rel="noopener">Busch, Lahti and Werner (2013)</a>.'),
        ]),
        ("Scale, time and the name", [
            "The bound in Kennard’s inequality is set by Planck’s constant, which is extremely small. For objects of everyday size, the spreads it requires are extremely small, which is why a thrown ball seems to have a perfectly definite position and speed. The principle matters for electrons and atoms.",
            "Time is a special case. Heisenberg also discussed an uncertainty relation between energy and time, and it is often quoted alongside the position and momentum version. But the " + a(SEP, "Stanford Encyclopedia") + " notes that the status of the time variable in his illustrations is “not at all clear,” and that “most physical systems do not have a time operator.” That gives the relation between energy and time a different status from the one between position and momentum, and it has to be interpreted with more care, which matters for anyone reading it as a statement about time itself.",
            "Is it even a principle? The philosopher Popper argued, according to the encyclopedia, that since the relations follow from the rest of quantum theory, they cannot be a principle. The encyclopedia’s authors reply that the argument is correct but misses the point: many statements in physics are called principles even though they are in fact derivable from other statements in the theory. The name has stuck either way.",
            "It also does not mean that measurement in daily life is hopeless, or that anything can happen. Quantum mechanics still makes statistical predictions. What it denies is that both members of certain pairs of quantities can be sharp at the same time.",
        ]),
        ("What it does not mean", [
            "The uncertainty principle is often stretched beyond its subject. It does not say that observation by a conscious mind changes reality; Heisenberg’s disturbance came from light hitting an electron, and the modern inequality concerns quantum states, with no observer in it. It does not say that everything is uncertain, or that knowledge in general is impossible. And it does not apply to people, decisions or relationships.",
            "HTML:" + K.callout("warn", "A metaphor, labelled as one",
                "<p>People sometimes borrow the uncertainty principle to say that you cannot study something without changing it, or that precision about one thing costs precision about another. As a figure of speech that is harmless, but it is a metaphor, not physics. The principle concerns specific pairs of quantities in quantum systems, and it gives no support to claims about minds, people or the observer creating reality.</p>"),
        ]),
        ("What this does and does not say", [
            "Read plainly, the uncertainty principle has two parts. One is firm and mathematical: a quantum state cannot sharply define both position and momentum. The other, about how much measuring one disturbs the other, turned out to be subtler than Heisenberg’s microscope suggested, and physicists still debate how best to state it. Neither part involves consciousness, and neither licenses the idea that reality is whatever we expect.",
            "Other essays here follow the same physics. The essay on the observer effect, linked above, explains what measurement does in quantum mechanics and what it does not. " + ESSAY53.replace(">what entanglement", ">What entanglement") + " describes correlations that Einstein found troubling. And " + ESSAY62 + " looks at a philosopher who held that everything follows necessarily from its causes, a view Heisenberg’s 1927 paper rejected for physics.",
        ]),
    ],
    note=[
        "Heisenberg’s words are quoted from the 1983 NASA translation of his 1927 paper. The symbols in Kennard’s inequality follow the Stanford Encyclopedia of Philosophy.",
    ],
    faqs=[
        ("What does the uncertainty principle say in simple terms?",
         "That some pairs of quantities, such as position and momentum, cannot both be sharply defined at once: the more narrowly one is pinned down, the more spread out the other must be."),
        ("Is the uncertainty principle just about measurement disturbing things?",
         "No. Heisenberg first explained it that way, but its standard exact form, due to Kennard in 1927, is about the spreads of quantities in a quantum state, whatever is done to measure them."),
        ("Was Heisenberg’s uncertainty principle proved wrong?",
         "No. Experiments in 2012 found that Heisenberg’s specific formula for the trade-off between measurement error and disturbance can be beaten under one set of definitions, but the uncertainty of quantum states remains, and a 2013 paper proved a Heisenberg-type relation under other definitions."),
        ("Why don’t we notice uncertainty in everyday life?",
         "Because the limit is set by Planck’s constant, which is extremely small. For everyday objects the required spreads are extremely small."),
        ("Does the uncertainty principle mean the observer creates reality?",
         "No. It involves no conscious observer. Heisenberg’s example involved light hitting an electron, and the modern inequality is a property of quantum states."),
    ],
    related=[
        ("what-the-observer-effect-actually-says", "What the observer effect actually says, and what it does not", "Physics and time"),
        ("what-entanglement-is", "What quantum entanglement actually is, and what it is not", "Physics and time"),
    ],
)

if __name__ == "__main__":
    newpost.build(POST)
