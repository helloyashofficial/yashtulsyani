#!/usr/bin/env python3
"""Essay 53 :: what-entanglement-is  (Physics and time)

Literal register. Sources fetched and read on 4 Nov 2026: SEP "The
Einstein-Podolsky-Rosen Argument in Quantum Theory"; SEP "Quantum
Entanglement and Information"; Cambridge Core record of Schrödinger 1935;
Mermin, "Is the Moon there when nobody looks?", Physics Today (reprint PDF);
SEP "Bell's Theorem", Summer 2006 archive; Nobel Prize in Physics 2022 press
release and popular information; Hensen et al. 2015 (arXiv abstract);
Giustina et al. 2015 (arXiv abstract); Shalm et al. 2015 (ADS abstract);
Yin et al. 2017 (arXiv abstract) and Physics Today news; Fedrizzi and
Malik in The Conversation and the Heriot-Watt long read; SEP "The Role of
Decoherence in Quantum Mechanics"; Bobroff 2019 (phys.org reprint).
No source was found in which a physicist addresses claims that people are
entangled directly; the essay does not attribute such a statement.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import newpost, postkit as K

EXT = ' target="_blank" rel="noopener"'
def a(url, text):
    return '<a href="%s"%s>%s</a>' % (url, EXT, text)

SEPEPR = "https://plato.stanford.edu/ENTRIES/qt-epr/"
SEPENT = "https://plato.stanford.edu/ENTRIES/qt-entangle/"
SCHR = "https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/abs/discussion-of-probability-relations-between-separated-systems/C1C71E1AA5BA56EBE6588AAACB9A222D"
MERMIN = "https://aip.brightspotcdn.com/PTO.v78.i1.28_1.online.pdf"
SEPBELL = "https://plato.stanford.edu/archives/sum2006/entries/bell-theorem/index.html"
NOBEL = "https://nobelprize.org/prizes/physics/2022/press-release/"
NOBELPOP = "https://www.nobelprize.org/prizes/physics/2022/popular-information/"
HENSEN = "https://arxiv.org/abs/1508.05949"
GIUSTINA = "https://arxiv.org/abs/1511.03190v2"
SHALM = "https://ui.adsabs.harvard.edu/abs/2015PhRvL.115y0402S"
MICIUS = "https://arxiv.org/abs/1707.01339"
MICIUSPT = "https://physicstoday.aip.org/news/satellite-distributed-entanglement"
CONV = "https://theconversation.edu.au/four-common-misconceptions-about-quantum-physics-192062"
HW = "https://www.hw.ac.uk/uk/research/long-read/common-misconceptions-about-quantum.htm"
SEPDEC = "https://plato.stanford.edu/ENTRiES/qm-decoherence/"
BOBROFF = "https://phys.org/news/2019-04-common-myths-quantum-physics.pdf"

ESSAY41 = '<a href="/writing/what-the-observer-effect-actually-says">what the observer effect actually says</a>'
ESSAY48 = '<a href="/writing/why-time-has-a-direction">why time has a direction</a>'
ESSAY44 = '<a href="/writing/what-it-means-to-call-time-the-fourth-dimension">what it means to call time the fourth dimension</a>'

POST = dict(
    slug="what-entanglement-is", num=53, cat="Physics and time", read="auto",
    date="2026-11-04",
    gen="rewrite/53-what-entanglement-is.py",
    title="What quantum entanglement actually is, and what it is not",
    dek="Entanglement is the quantum idea most often borrowed for talk about souls and lovers. In physics it is something precise: a correlation between measurements that no ordinary explanation can match. It cannot send a message, and it does not survive in anything as large and warm as a person.",
    takeaway="Entanglement is a state in which two particles behave like a single unit even when separated, so that measurements on them are correlated in ways no theory based on local hidden properties can reproduce. Einstein, Podolsky and Rosen argued in 1935 that this showed quantum mechanics was incomplete; Schrödinger, the same year, named the phenomenon and called it the characteristic trait of the theory. J. S. Bell showed in 1964 that the question could be tested, experiments led by John Clauser, Alain Aspect and Anton Zeilinger, recognised by the 2022 Nobel Prize, found the correlations quantum mechanics predicts, and three experiments in 2015 closed the main loopholes together. Entanglement cannot be used to send signals faster than light, it underpins quantum cryptography and teleportation of quantum states, and in large warm objects like people it is destroyed almost instantly by decoherence.",
    sections=[
        ("What entanglement is", [
            "Entanglement is a state in which two or more particles behave like a single system even when they are far apart. Measure them and the results are correlated more strongly than any explanation based on properties fixed in advance could allow. It cannot be used to send a message, and it is quickly destroyed in large, warm objects.",
            "HTML:" + K.takeaways([
                "In the words of the Nobel committee, entangled particles behave like a single unit even when they are separated.",
                "Einstein, Podolsky and Rosen argued in 1935 that this showed quantum mechanics was incomplete.",
                "Schrödinger named it the same year and called it the characteristic trait of quantum mechanics.",
                "Bell showed in 1964 how to test the question; experiments since then side with quantum mechanics.",
                "Entanglement cannot carry a message faster than light.",
                "In anything as large and warm as a person, it is destroyed almost instantly.",
            ]),
            "This essay is in the literal register, like " + ESSAY41 + ", which touched on entanglement briefly. It sets out what the physics says, how it was tested and what it rules out, and keeps any borrowing for human life to one labelled paragraph at the end.",
            "HTML:" + K.callout("definition", "Entanglement, in this essay",
                "<p>The " + a(NOBEL, "Nobel Prize press release of 2022") + " describes entangled quantum states as ones where two particles behave like a single unit even when they are separated. Everything in this essay is about particles and the outcomes of measurements on them, not about people.</p>"),
        ]),
        ("Einstein’s objection", [
            "The story starts with an argument against quantum mechanics. In 1935 Einstein, Podolsky and Rosen published a paper in Physical Review titled Can quantum-mechanical description of physical reality be considered complete? The " + a(SEPEPR, "Stanford Encyclopedia of Philosophy") + " sets out its reasoning.",
            "The argument rests on a criterion of what is real: “If, without in any way disturbing a system, we can predict with certainty the value of a physical quantity, then there exists an element of reality corresponding to that quantity.” Take two particles that have interacted and then separated. Measuring one lets you predict a property of the other with certainty, without touching it. So, the authors argued, that property must have been real all along.",
            "But quantum mechanics does not assign the property a definite value before measurement. If the property was real and the theory leaves it out, the theory is missing something. The conclusion, in the encyclopedia’s summary, is that the quantum mechanical description of systems by state vectors is incomplete.",
        ]),
        ("Schrödinger’s word", [
            "Erwin Schrödinger replied the same year. In a paper published in October 1935 in the Proceedings of the Cambridge Philosophical Society, recorded by " + a(SCHR, "Cambridge University Press") + " as Discussion of Probability Relations between Separated Systems, he gave the phenomenon its name.",
            "According to the " + a(SEPENT, "Stanford Encyclopedia’s entry on entanglement") + ", Schrödinger coined the term to describe this peculiar connection between quantum systems, and wrote of it: “I would not call that one but rather the characteristic trait of quantum mechanics, the one that enforces its entire departure from classical lines of thought.”",
            "Einstein and Schrödinger saw the same feature from opposite sides. For Einstein it was a sign the theory was unfinished. For Schrödinger it was the heart of what made the theory new.",
        ]),
        ("Spooky action at a distance", [
            "Einstein’s most quoted phrase about entanglement is not in the 1935 paper. It comes from a letter to Born in March 1947, which the physicist N. David Mermin quotes in " + a(MERMIN, "a well-known Physics Today essay") + ": Einstein could not seriously believe in the quantum theory, he wrote, because it cannot be reconciled with the idea that physics should represent a reality in time and space, free from spooky actions at a distance.",
            "Mermin explains what Einstein meant: the spooky actions, spukhafte Fernwirkungen in German, are the acquisition of a definite value by a property of one system as a result of a measurement made on another, distant one. Einstein found that unacceptable. The question was whether nature agreed.",
            "HTML:" + K.callout("warn", "A date often got wrong",
                "<p>The phrase spooky action at a distance is often attributed to the 1935 paper. It is from Einstein’s 1947 letter to Born, as " + a(MERMIN, "Mermin") + " records.</p>"),
        ]),
        ("Bell’s test", [
            "For almost thirty years the disagreement seemed beyond the reach of experiment. Then the physicist J. S. Bell, in a 1964 paper titled On the Einstein-Podolsky-Rosen paradox, showed it could be tested. The " + a(SEPBELL, "Stanford Encyclopedia’s entry on Bell’s theorem") + " states the result: no physical theory which is realistic and also local in a specified sense can agree with all of the statistical implications of quantum mechanics.",
            "Put simply, if particles carried hidden instructions set when they were created, and if nothing done to one could affect the other faster than light, then the correlations between measurements on them would have to stay below a certain limit, a Bell inequality. Quantum mechanics predicts correlations above that limit. An experiment could decide between them.",
            "The experiments came over the following decades, and the " + a(NOBEL, "2022 Nobel Prize in Physics") + " went to three of the people who did them: John Clauser, Alain Aspect and Anton Zeilinger, “for experiments with entangled photons, establishing the violation of Bell inequalities and pioneering quantum information science.” Of Clauser’s measurements, the press release says they supported quantum mechanics by clearly violating a Bell inequality, which means that quantum mechanics cannot be replaced by a theory that uses hidden variables.",
            "Each experiment left some room for doubt, known as loopholes. The press release notes that some loopholes remained after Clauser’s work, and that Aspect closed an important one by switching the measurement settings after an entangled pair had left its source, so the setting that existed when they were emitted could not affect the result.",
            "HTML:" + K.table("Closing the loopholes: three experiments in 2015",
                ["Team", "What was entangled", "Reported result"],
                [["Delft (Hensen and colleagues)", "Electron spins 1.3 km apart", "245 trials; S = 2.42 against a local limit of 2"],
                 ["Vienna (Giustina and colleagues)", "Photons", "Probability under local realism no more than 3.74 × 10⁻³¹"],
                 ["NIST (Shalm and colleagues)", "Photons", "Adjusted p value as small as 2.3 × 10⁻⁷"]],
                source='Sources: abstracts of <a href="' + HENSEN + '" target="_blank" rel="noopener">Hensen et al.</a>, <a href="' + GIUSTINA + '" target="_blank" rel="noopener">Giustina et al.</a> and <a href="' + SHALM + '" target="_blank" rel="noopener">Shalm et al.</a> (2015).'),
            "Two loopholes mattered most. The locality loophole is the possibility that something about one measurement reached the other in time to influence it; the answer is to separate the stations far enough, and choose the settings late enough, that no signal at light speed could connect them. The detection loophole is the possibility that the particles actually detected are not a fair sample of all those produced. The Delft team, in their " + a(HENSEN, "abstract") + ", write that their spatial separation ensured the required locality conditions and that efficient spin readout avoids the fair sampling assumption, the detection loophole. Their test used the standard CHSH form of Bell’s inequality, S ≤ 2, and found S = 2.42 ± 0.20.",
            "In 2015 three groups closed the main loopholes at once. The Delft experiment, reported by " + a(HENSEN, "Hensen and colleagues") + ", entangled electron spins at stations separated by 1.3 km and found a violation in 245 trials. Teams in " + a(GIUSTINA, "Vienna") + " and at " + a(SHALM, "NIST in the United States") + " reported photon experiments with very small probabilities that local realism could explain their results.",
            "The distances have grown since. In 2017, " + a(MICIUS, "Yin and colleagues") + " used the Micius satellite to distribute entangled photons to two ground stations 1203 km apart and found a Bell violation under strict locality conditions. According to " + a(MICIUSPT, "Physics Today") + ", the satellite orbits at about 500 km.",
        ]),
        ("What entanglement cannot do", [
            "The most common misunderstanding is that entanglement lets one particle send an instant message to the other. It does not. The " + a(SEPBELL, "Stanford Encyclopedia") + " notes that several researchers have shown that this kind of connection cannot be used to send messages superluminally, faster than light, between the two measuring stations.",
            "The reason is that each person’s results, taken alone, look random. Mermin, describing an idealised version of the experiment in " + a(MERMIN, "his essay") + ", writes that the statistical pattern at one detector is entirely random. The correlation only appears when the two records are brought together and compared, which requires ordinary communication at or below the speed of light.",
            "Physicists Alessandro Fedrizzi and Mehul Malik make the point bluntly in " + a(CONV, "The Conversation") + ": “The idea that measuring one entangled card changes the state of the other is not true.” Such a change, they add, would mean communication faster than the speed of light, something forbidden by Einstein’s theories. In a " + a(HW, "Heriot-Watt University article") + " they note that a common misconception is that entanglement might be used for faster-than-light communication.",
            "HTML:" + K.table("What entanglement does and does not do",
                ["Claim", "Status"],
                [["Measurements on entangled particles are correlated beyond any local hidden-variable limit", "Confirmed by experiment"],
                 ["Measuring one particle sends a signal to the other", "False: each side’s results alone are random"],
                 ["Entanglement allows faster-than-light communication", "False"],
                 ["Quantum teleportation moves objects", "False: it moves a quantum state, and needs ordinary communication"]],
                source='Sources: <a href="' + SEPBELL + '" target="_blank" rel="noopener">Stanford Encyclopedia, Bell’s theorem</a>; <a href="' + CONV + '" target="_blank" rel="noopener">Fedrizzi and Malik</a>; <a href="' + SEPENT + '" target="_blank" rel="noopener">Stanford Encyclopedia, entanglement and information</a>.'),
        ]),
        ("What entanglement is used for", [
            "Entanglement is no longer only a puzzle. The " + a(NOBEL, "2022 press release") + " quotes the committee chair, Anders Irbäck: “It has become increasingly clear that a new kind of quantum technology is emerging.” It notes that Zeilinger’s group demonstrated quantum teleportation, which makes it possible to move a quantum state from one particle to one at a distance. The " + a(NOBELPOP, "Nobel popular information") + " dates the first such experiment to 1997.",
            "Teleportation is less dramatic than its name. The " + a(SEPENT, "Stanford Encyclopedia") + " explains that the receiver reconstructs the state on the basis of just two bits of classical information sent by the sender. Nothing travels faster than light, and no object is moved.",
            "Entanglement is also used for secure communication. The same entry explains that it can make quantum cryptography secure through what is called the monogamy of entangled correlations: no third party can share entanglement correlations between the two people communicating, so an eavesdropper leaves a trace.",
        ]),
        ("Why people are not entangled", [
            "Entanglement is not rare. As the " + a(SEPDEC, "Stanford Encyclopedia’s entry on decoherence") + " explains, objects become entangled with their surroundings all the time, and that is exactly what destroys the clean quantum behaviour seen in isolated particles. The entry notes that middle-sized objects on the Earth’s surface are very effectively decohered by the air in the atmosphere, and interference is typically very well suppressed between localised states of macroscopic objects.",
            "For people, that settles the matter. Fedrizzi and Malik, in " + a(CONV, "The Conversation") + ", note that the kind of quantum behaviour seen in small, isolated systems generally won’t apply to big creatures such as cats or a human. The experiments above took great care to isolate single photons or single electron spins precisely because anything larger loses its quantum coherence almost at once.",
            "That has not stopped the word from travelling. The physicist Julien Bobroff, in " + a(BOBROFF, "an article on common myths") + ", describes a kind of quantum mysticism in which a pseudo-New Age spirituality finds its credentials in scientific jargon. Claims that two people are entangled, or that entanglement explains a bond between them, borrow the word without the physics. None of the experiments above tested anything about people, and nothing in them suggests it.",
        ]),
        ("What this does and does not say", [
            "Read literally, entanglement is one of the best-tested and strangest results in physics. Measurements on separated particles are correlated in ways no local explanation based on pre-set properties can match, the effect has been confirmed over more than a thousand kilometres, and it cannot be used to send a message. How to interpret it is still debated, as the " + a(SEPENT, "Stanford Encyclopedia") + " entries linked here show; the experiments settle what happens, not what it means.",
            "Here is the one borrowing in this essay, labelled as a metaphor. Two people who have shared a great deal can find that they respond to the same events in matching ways, even when apart, without anything passing between them at the time: the match was built by their history together. That is a resemblance to the physics, not an instance of it, and the resemblance is closer to Einstein’s hidden instructions than to entanglement, which is exactly what Bell’s test ruled out for particles. Nothing in the physics says anything about people.",
            "Three other essays here carry the physics further. The observer-effect essay, linked above, explains measurement and decoherence. " + ESSAY44.replace(">what it means", ">What it means") + " covers the relativity behind the speed-of-light limit that entanglement does not break. And " + ESSAY48 + " asks why, if the basic laws barely distinguish past and future, time still seems to run one way.",
        ]),
    ],
    note=[
        "Quoted figures for the 2015 and 2017 experiments are from the papers’ abstracts. Einstein’s 1947 letter is quoted through Mermin’s essay, and Schrödinger’s 1935 sentence through the Stanford Encyclopedia of Philosophy.",
    ],
    faqs=[
        ("What is quantum entanglement in simple terms?",
         "A state in which two particles behave like a single unit even when they are separated, so that measurements on them are correlated more strongly than any explanation based on properties fixed in advance can allow."),
        ("Can entanglement be used to send messages faster than light?",
         "No. Each side's results, taken alone, are random. The correlation only shows up when the two sets of results are compared, which needs ordinary communication. Several researchers have shown entanglement cannot be used to signal faster than light."),
        ("Did Einstein call entanglement spooky action at a distance?",
         "Yes, but not in the famous 1935 paper. The phrase comes from a letter he wrote to Born in March 1947, quoted by N. David Mermin."),
        ("What did the 2022 Nobel Prize in Physics recognise?",
         "Experiments by John Clauser, Alain Aspect and Anton Zeilinger with entangled photons, establishing the violation of Bell inequalities and pioneering quantum information science."),
        ("Can people be entangled?",
         "Not in the physics sense. Large, warm objects interact constantly with their surroundings, which destroys quantum coherence almost at once. The experiments that show entanglement isolate single photons or electrons with great care."),
    ],
    related=[
        ("what-the-observer-effect-actually-says", "What the observer effect actually says, and what it does not", "Physics and time"),
        ("why-time-has-a-direction", "Why time has a direction, and what entropy does and does not explain", "Physics and time"),
    ],
)

if __name__ == "__main__":
    newpost.build(POST)
