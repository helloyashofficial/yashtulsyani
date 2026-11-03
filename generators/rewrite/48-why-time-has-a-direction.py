#!/usr/bin/env python3
"""Essay 48 :: why-time-has-a-direction  (Physics and time)

Literal register. Sources fetched and read on 3 Nov 2026: Callender, SEP
"Thermodynamic Asymmetry in Time" (Spring 2025 archive); Werndl, SEP
"Philosophy of Statistical Mechanics" (Summer 2026 archive); the 1980 Nobel
Prize press release; Ben-Naim (arXiv 1705.01467) quoting Eddington, with
Eddington's 1928 edition details confirmed from the Gutenberg text;
Goldstein (arXiv cond-mat/0105242); Lebowitz (arXiv math-ph/0010018),
including his quotation of Feynman. Eddington and Feynman are quoted
through these papers because their books could not be read in full.
Penrose's estimate is described without a figure because two sources give
different exponents.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import newpost, postkit as K

EXT = ' target="_blank" rel="noopener"'
def a(url, text):
    return '<a href="%s"%s>%s</a>' % (url, EXT, text)

CALL = "https://plato.stanford.edu/archives/spr2025/entries/time-thermo/"
WERNDL = "https://plato.stanford.edu/archives/sum2026/entries/statphys-statmech/"
NOBEL = "https://www.nobelprize.org/prizes/physics/1980/press-release/"
BENNAIM = "https://arxiv.org/pdf/1705.01467"
EDD = "https://gutenberg.org/cache/epub/72963/pg72963-images.html"
GOLD = "https://arxiv.org/pdf/cond-mat/0105242"
LEB = "https://arxiv.org/pdf/math-ph/0010018"

ESSAY41 = '<a href="/writing/what-the-observer-effect-actually-says">what the observer effect actually says</a>'
ESSAY44 = '<a href="/writing/what-it-means-to-call-time-the-fourth-dimension">the essay on time as the fourth dimension</a>'
ESSAY47 = '<a href="/writing/why-we-blame-the-people-we-love">why we blame the people we love</a>'

POST = dict(
    slug="why-time-has-a-direction", num=48, cat="Physics and time", read="auto",
    date="2026-11-03",
    gen="rewrite/48-why-time-has-a-direction.py",
    title="Why time has a direction, and what entropy does and does not explain",
    dek="The basic laws of physics barely care which way time runs. Eggs still break and never unbreak. The standard explanation runs through entropy, and it ends with an assumption about the beginning of the universe that physicists are still arguing about.",
    takeaway="The fundamental laws of motion are, with a small exception in the weak interaction, the same run forwards or backwards, yet everyday processes only go one way. The usual explanation is the second law of thermodynamics: entropy, which Boltzmann tied to how many microscopic arrangements fit a given large-scale state, tends to increase. That only explains the arrow if entropy was low in the past, so the account needs an extra assumption, the Past Hypothesis, that the universe began in an extremely low-entropy state. Whether that assumption is a law, a brute fact or something needing explanation is still debated, and philosophers doubt that every arrow of time reduces neatly to entropy.",
    sections=[
        ("Why time has a direction", [
            "Time seems to have a direction because of entropy: large collections of particles tend to move from rare arrangements to common ones, and almost never the reverse. That explains the arrow only if the universe began in a very rare, low-entropy state, an assumption physicists call the Past Hypothesis, and why it did is still an open question.",
            "HTML:" + K.takeaways([
                "The basic laws of motion are, with one small exception, indifferent to the direction of time.",
                "Arthur Eddington named the one-way property time’s arrow, in a book published in 1928.",
                "Boltzmann tied entropy to counting: how many microscopic arrangements fit what we see at large scale.",
                "Entropy increase is overwhelmingly likely, not strictly certain, which answers two famous objections.",
                "The account needs a low-entropy beginning, the Past Hypothesis. Its status is still debated.",
                "Whether memory, causation and the other arrows all reduce to entropy is doubtful.",
            ]),
            "This essay is in the literal register, like " + ESSAY41 + ". It states the physics and the open questions as the sources state them, and borrows nothing for human life except in one labelled paragraph at the end.",
            "HTML:" + K.callout("definition", "Entropy, in this essay",
                "<p>A measure of how many microscopic arrangements of a system are compatible with its large-scale state. A state that can be realised in vastly more ways has higher entropy. The word disorder is a common gloss, but, as later sections show, it can mislead.</p>"),
        ]),
        ("Laws that do not care which way", [
            "The puzzle starts with the laws themselves. As " + a(CALL, "Craig Callender’s entry in the Stanford Encyclopedia of Philosophy") + " puts it, the problem is usually said to arise because fundamental physics is time symmetric, or more precisely, time reversal invariant. Loosely, a theory has that property if its laws don’t care about the direction of time.",
            "A film of two billiard balls colliding looks equally possible run backwards. The same is true, as far as the basic equations go, for planets in orbit and for most of what happens inside atoms. In its " + a(NOBEL, "1980 prize announcement") + ", the Royal Swedish Academy of Sciences explains the principle as the fundamental laws not changing when all motions are reversed, and notes that this symmetry is valid for processes governed by electromagnetic, gravitational and strong forces.",
            "There is one known exception. The same announcement records the discovery, by James Cronin and Val Fitch, of violations of fundamental symmetry principles in the decay of neutral K-mesons, and concludes that perfect symmetry by time reversal is not always true. Callender notes that weak interactions between quarks and leptons can violate time symmetry, but that these violations don’t appear to be responsible for thermodynamic behaviour. The everyday arrow has to come from somewhere else.",
            "HTML:" + K.table("Time symmetry in the basic forces",
                ["Force", "Same run backwards?"],
                [["Electromagnetic", "Yes"],
                 ["Gravitational", "Yes"],
                 ["Strong", "Yes"],
                 ["Weak", "Not always: violations seen in neutral K-meson decays, too slight to explain the everyday arrow"]],
                source='Sources: <a href="' + NOBEL + '" target="_blank" rel="noopener">Nobel Prize in Physics 1980, press release</a>; <a href="' + CALL + '" target="_blank" rel="noopener">Callender, Stanford Encyclopedia of Philosophy</a>.'),
        ]),
        ("Eddington names the arrow", [
            "The phrase comes from the astronomer Arthur Eddington. His book The Nature of the Physical World, based on his Gifford Lectures of 1927, was " + a(EDD, "published in November 1928") + ". In it, as quoted by " + a(BENNAIM, "Arieh Ben-Naim") + ", he proposed: “Let us draw an arrow arbitrarily.” If, following the arrow, we find more and more of the random element in the state of the world, the arrow points towards the future. He then wrote: “I shall use the phrase ‘time’s arrow’ to express this one-way property of time which has no analogue in space.”",
            "Eddington was emphatic about the law behind it. The law that entropy always increases, the second law of thermodynamics, holds, he wrote, “the supreme position among the laws of Nature”. A theory that contradicted Maxwell’s equations might survive; one that went against the second law, he said, had no hope.",
            "HTML:" + K.callout("note", "Why space has no arrow",
                "<p>Eddington’s point was that nothing in physics picks out left from right, or up from down, the way the second law picks out earlier from later. That is the sense in which time’s one-way property has no analogue in space.</p>"),
        ]),
        ("Entropy as counting", [
            "The second law in its classical form says, in Callender’s words, that in the spontaneous evolution of a thermally closed system the entropy can never decrease, and that it attains its maximum value at equilibrium. Heat flows from hot to cold, never the reverse.",
            "Ludwig Boltzmann’s insight was to explain this by counting. As " + a(WERNDL, "Charlotte Werndl’s entry on the philosophy of statistical mechanics") + " sets out, Boltzmann entropy is a property of a large-scale state, defined by the size of the region of possible microscopic states that produce it. The bigger that region, the higher the entropy, and the equilibrium state is the one with the largest region.",
            "HTML:" + K.stages("Why entropy goes up, in four steps", [
                ("01", "Large-scale states", "We see temperature, pressure, where the gas is: a handful of numbers."),
                ("02", "Many microscopic states each", "Each of those large-scale states can be produced by a huge number of exact arrangements of particles."),
                ("03", "Very unequal counts", "Spread-out states can be produced in overwhelmingly more ways than gathered-up ones."),
                ("04", "Drift towards the common", "A system wandering among its arrangements almost always ends up in the large-scale state with the most of them."),
            ], source='A simplified account of Boltzmann’s approach, following <a href="' + WERNDL + '" target="_blank" rel="noopener">Werndl</a> and <a href="' + GOLD + '" target="_blank" rel="noopener">Goldstein (2001)</a>.'),
            "Shuffle a new deck of cards and it is almost never back in order. Nothing forbids the ordered deck; there are simply vastly more shuffled orders. Boltzmann’s second law is that idea applied to the particles of a gas, where the numbers are so large that almost never becomes never in practice.",
        ]),
        ("Two objections, and the answer", [
            "Boltzmann’s account met two famous objections. The first, as Werndl records, is Loschmidt’s reversibility objection, first put forward by Loschmidt in 1876: since the laws of motion are reversible, for every motion that raises entropy there is a reversed motion that lowers it.",
            "The second is Zermelo’s recurrence objection, first put forward by Zermelo in 1896. It rests on Poincaré’s result that systems of this kind must, at some point, return arbitrarily close to their initial state. In Callender’s words, recurrence means that every solution will at some point have its entropy decrease if we wait long enough.",
            "HTML:" + K.table("The two classic objections",
                ["Objection", "First raised", "The point"],
                [["Reversibility", "Loschmidt, 1876", "Reversed motions are just as lawful, so entropy-lowering motions exist"],
                 ["Recurrence", "Zermelo, 1896, using Poincaré’s result", "Given long enough, a system returns close to its starting state"]],
                source='Sources: <a href="' + WERNDL + '" target="_blank" rel="noopener">Werndl</a>; <a href="' + CALL + '" target="_blank" rel="noopener">Callender</a>.'),
            "The answer is that the second law, understood Boltzmann’s way, is about likelihood. A decrease in entropy is not impossible; it is, as Callender’s entry puts it, tremendously unlikely. The reversed motions exist, but they are an unimaginably small fraction of all motions. The recurrences come, but on timescales far beyond anything that matters. Sheldon Goldstein, in " + a(GOLD, "a 2001 account of Boltzmann’s approach") + ", argues that neither objection is a genuine conflict with Boltzmann’s analysis.",
        ]),
        ("The Past Hypothesis", [
            "There is a catch, and it is the deepest part of the story. If entropy-raising and entropy-lowering motions are equally lawful, the same counting argument that says entropy will rise in the future also says it should have been higher in the past. Run backwards, the most likely history of a half-melted ice cube is one in which it was more melted earlier.",
            "We know that is false: the past had lower entropy. To get the right answer, the account needs an extra assumption about the beginning. Callender describes it as the cosmological posit that the universe began in an extremely tiny section of its available phase space, and notes that the philosopher David Albert, in 2000, called this the Past Hypothesis.",
            "Richard Feynman had made the same point decades earlier. In his 1960s lectures published as The Character of Physical Law, as " + a(LEB, "Joel Lebowitz quotes him") + ", it is necessary to add to the physical laws the hypothesis that in the past the universe was more ordered, in the technical sense, than it is today, to make an understanding of the irreversibility.",
            "The low-entropy beginning has a surprising feature. Lebowitz notes that in a universe dominated, like ours, by gravity, a uniform density corresponds to a state of very low entropy. Gravity makes matter clump, and clumped states have more entropy. So a smooth, evenly spread early universe, which might look like maximum disorder, was in fact extraordinarily special. Roger Penrose estimated just how special, and his estimate is quoted by Goldstein and by Lebowitz; the two give the exponent differently, so no figure is repeated here.",
            "HTML:" + K.compare("What the Past Hypothesis is, according to whom", [
                ("A law", ["Treats the low-entropy start as part of physics itself", "Needs no further explanation"], ["Unusual: a law about one moment rather than about change"], "Defended by some, including Callender."),
                ("A brute fact, or something to explain", ["Keeps laws as rules for change"], ["Leaves the most important fact about the universe unexplained", "Earman thinks it not even coherent enough to be false"], "Defended by others, including Price."),
            ], source='Source: <a href="' + CALL + '" target="_blank" rel="noopener">Callender, Stanford Encyclopedia of Philosophy</a>, and <a href="' + WERNDL + '" target="_blank" rel="noopener">Werndl</a>, on the positions.'),
        ]),
        ("The other arrows", [
            "Entropy is not the only way time seems to point. Callender’s entry lists several. There is a knowledge arrow: roughly put, we know more about the past than the future. A causal arrow: causes typically occur before their effects. A radiative arrow, in which waves spread out from their sources rather than converging on them. A cosmological arrow, the most obvious being the expansion of the universe. And a psychological arrow, which the entry calls controversial and actually many different asymmetries.",
            "Boltzmann suggested long ago that these are all explained by the direction of increasing entropy. Callender is cautious: a straightforward reduction of these arrows to entropy, he writes, is probably not in the cards. In one newer view, it is the low-entropy past itself that is basic, and the thermodynamic arrow is just one of its consequences, alongside the others.",
            "Some of the arrows are closer to entropy than others. On the radiative arrow, the entry reports that most agree the asymmetry of waves is ultimately thermodynamic, but after that matters are contested. The cosmological arrow invites a stranger thought. Gold proposed that if the universe ever stopped expanding and began to contract, then at the maximum radius the thermodynamic arrow would flip, so that entropy would decrease in the contracting phase. The idea is a speculation rather than a result, and it shows how tightly the account ties the direction of time to the state of the universe as a whole.",
            "The knowledge arrow shows how that works. Callender notes that the highly constrained early state is what causes there to be macroscopic traces of the past in the present, but not traces of the future. Footprints, photographs and memories are records, and records point backwards because the past was special and the future is not.",
        ]),
        ("What this does and does not say", [
            "Read literally, the account is modest. The laws mostly do not care which way time runs; the arrow comes from statistics plus a special beginning; and why the beginning was special is unsettled. It says nothing about consciousness, meaning or fate.",
            "Here is the one borrowing in this essay, labelled as such. As a metaphor only, the asymmetry of records is apt for people: the past leaves traces and the future leaves none, which is part of why the past feels fixed and the future open. In physics that is a fact about entropy and a low-entropy start; in a life it is only a resemblance, and nothing in this essay suggests the physics governs it.",
            "Two other essays here carry the thread on. " + ESSAY44.replace(">the essay on time as the fourth dimension<", ">The essay on time as the fourth dimension<") + " explains why relativity leaves open whether past and future are as real as the present. And " + ESSAY47 + " asks what a fixed future would mean for blame, and finds that the answer has less to do with physics than with how people treat each other.",
        ]),
    ],
    note=[
        "Eddington and Feynman are quoted through scholarly papers that cite them, because their books could not be read in full for this essay; the papers are linked where the quotations appear.",
    ],
    faqs=[
        ("Why does time only go forward?",
         "The basic laws of motion mostly work the same in both directions. The one-way character comes from entropy: systems move from states that can be realised in few ways to states that can be realised in vastly more ways. That explains the arrow only if the universe began in a very low-entropy state, which physicists call the Past Hypothesis."),
        ("Who coined the phrase arrow of time?",
         "The astronomer Arthur Eddington, in The Nature of the Physical World, published in 1928 and based on his 1927 Gifford Lectures. He used time's arrow for the one-way property of time which, he wrote, has no analogue in space."),
        ("Is entropy the same as disorder?",
         "Not exactly. In Boltzmann's account, entropy measures how many microscopic arrangements fit a given large-scale state. Disorder is a loose gloss that can mislead: because of gravity, a smooth, evenly spread universe is a state of very low entropy, not high."),
        ("Can entropy ever decrease?",
         "Not impossibly, but almost never. On Boltzmann's account a decrease in a closed system is tremendously unlikely rather than forbidden, which is how his view answers the objections raised by Loschmidt in 1876 and Zermelo in 1896."),
        ("What is the Past Hypothesis?",
         "The assumption that the universe began in an extremely low-entropy state. The philosopher David Albert named it in 2000; Richard Feynman had made the point earlier. Philosophers still disagree about whether it is a law, a brute fact or something that needs explaining."),
    ],
    related=[
        ("what-it-means-to-call-time-the-fourth-dimension", "What it means to call time the fourth dimension, and what it does not", "Fourth dimension"),
        ("what-the-observer-effect-actually-says", "What the observer effect actually says, and what it does not", "Physics and time"),
    ],
)

if __name__ == "__main__":
    newpost.build(POST)
