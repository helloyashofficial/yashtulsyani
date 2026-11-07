#!/usr/bin/env python3
"""Essay 41 :: what-the-observer-effect-actually-says  (Physics and time, pillar)

Literal register. Every physics claim is linked to a source fetched and read
on 24 Oct 2026: the Weizmann release and the Nature paper it reports, two
Stanford Encyclopedia of Philosophy entries, and the 2022 Nobel release.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import newpost, postkit as K

EXT = ' target="_blank" rel="noopener"'
WEIZ = '<a href="https://www.sciencedaily.com/releases/1998/02/980227055013.htm"%s>the Weizmann Institute&rsquo;s 1998 press release</a>' % EXT
BUKS = '<a href="https://ideas.repec.org/a/nat/nature/v391y1998i6670d10.1038_36057.html"%s>published in Nature by Buks and colleagues</a>' % EXT
SEPQT = '<a href="https://plato.stanford.edu/entries/qt-issues/"%s>the Stanford Encyclopedia of Philosophy&rsquo;s entry on philosophical issues in quantum theory</a>' % EXT
SEPDEC = '<a href="https://plato.stanford.edu/entries/qm-decoherence/"%s>the Stanford Encyclopedia&rsquo;s entry on decoherence</a>' % EXT
NOBEL = '<a href="https://www.nobelprize.org/prizes/physics/2022/press-release/"%s>the Royal Swedish Academy of Sciences&rsquo; 2022 prize announcement</a>' % EXT
ENT = '<a href="/writing/what-entanglement-is">what quantum entanglement actually is</a>'
ESSAY1 = '<a href="/writing/why-reassurance-is-never-enough">why reassurance is never enough</a>'
UNC = '<a href="/writing/what-the-uncertainty-principle-says">what the uncertainty principle actually says</a>'
BOOKS = '<a href="/books">both books</a>'

POST = dict(
    slug="what-the-observer-effect-actually-says", num=41, cat="Physics and time", read="auto",
    date="2026-10-24",
    gen="rewrite/41-what-the-observer-effect-actually-says.py",
    title="What the observer effect actually says, and what it does not",
    dek="The most quoted result in quantum physics is also the most misread. The observer in the famous experiments is a detector, not a mind, and the real puzzle it points to is stranger than the popular version.",
    takeaway="In quantum physics, observing a system means letting it interact with something that records information about it, and that interaction can destroy interference. The observer is usually an instrument; no consciousness is required, and no mainstream interpretation gives minds a special physical role. Decoherence explains why everyday objects never show quantum interference, but it does not by itself solve the measurement problem, which remains genuinely open. Borrowing this vocabulary for human life is fine, provided you say you are borrowing it.",
    sections=[
        ("What the observer effect is", [
            "In quantum physics, the observer effect is the finding that measuring a system changes what you then see: interference patterns disappear when something records which path a particle took. The observer is whatever does the recording, usually an instrument. Nothing in the effect requires a person, a mind or awareness.",
            "HTML:" + K.takeaways([
                "The observer in the experiments is a detector. The 1998 Weizmann release says so in as many words.",
                "Observation means interaction plus a record. Any physical system that ends up carrying which-path information will do.",
                "Decoherence explains why tables and cats never show interference: the environment is constantly observing them.",
                "The measurement problem is real and unsolved. Decoherence does not solve it on its own.",
                "No mainstream interpretation gives conscious minds a special physical role.",
            ]),
            "That opening paragraph is the whole correction, and the rest of this essay is the evidence for it. (Relativity’s claims about time are a separate subject, set out in <a href=\"/writing/what-it-means-to-call-time-the-fourth-dimension\">what it means to call time the fourth dimension</a>; why time has a direction at all is taken up in <a href=\"/writing/why-time-has-a-direction\">why time has a direction</a>.) It matters on this site because the books borrow quantum vocabulary for human life, and a borrowing is only honest if you know what you are borrowing from.",
            "HTML:" + K.callout("definition", "Observation, in physics",
                "<p>An interaction between a quantum system and something else that leaves the other thing carrying information about the system: which path it took, where it is, how it is spinning. The other thing can be a photon, an electron, a molecule of air or a laboratory detector.</p>"),
        ]),
        ("The experiment everyone quotes", [
            "Many popular accounts of the observer effect, including many that use it to argue that thoughts shape reality, cite one experiment in particular, " + BUKS + " in 1998. Electrons were sent through a device with two possible paths, which produces an interference pattern when the paths cannot be told apart. Next to one path the team placed a detector able to register passing electrons.",
            "The result was clean. The more sensitive the detector, the weaker the interference. The press release that announced it carried the headline that has travelled ever since: observation affects reality.",
            "Read the release itself and the next sentence corrects the headline. In " + WEIZ + ", the observer in the experiment was not human. It was a tiny electronic detector placed beside the electrons&rsquo; path, and the release adds that, apart from detecting the electrons, the detector had no effect on the current. Turn the detector&rsquo;s sensitivity up and there is more watching; more watching means less interference.",
            "HTML:" + K.table("The 1998 experiment, as reported",
                ["Element", "What it was"],
                [["The observed system", "Electrons passing through a double-path interferometer"],
                 ["The observer", "A tiny electronic detector beside one path, not a person"],
                 ["Watching", "The detector registering which path an electron took"],
                 ["The variable", "How sensitive the detector was"],
                 ["The result", "More sensitive detection, weaker interference"]],
                source='Sources: <a href="https://www.sciencedaily.com/releases/1998/02/980227055013.htm" target="_blank" rel="noopener">Weizmann Institute release, 1998</a>; <a href="https://ideas.repec.org/a/nat/nature/v391y1998i6670d10.1038_36057.html" target="_blank" rel="noopener">Buks et al., Nature 391 (1998)</a>.'),
            "So the experiment that is most often quoted for the claim that minds change reality is, on its own terms, an experiment in which no mind was involved. What it shows is real and important: getting information about a quantum system is a physical act with physical consequences. What it does not show is anything about awareness.",
        ]),
        ("What measurement means in physics", [
            "The reason a detector can do what a person was supposed to do is that, in physics, measurement is an interaction. For a detector to register an electron it has to be coupled to it, and the coupling leaves the detector in a state that depends on the electron. Information has moved from one physical system into another.",
            "That transfer is what destroys interference. Interference needs the two paths to be indistinguishable. Once anything in the universe carries a record of which path was taken, the paths are no longer indistinguishable, whether or not anyone ever reads the record.",
            "HTML:" + K.stages("How a measurement removes interference", [
                ("01", "Two possibilities", "The electron is in a state that includes both paths, and the two can interfere."),
                ("02", "Interaction", "Something couples to the electron on one path: a detector, a photon, a molecule."),
                ("03", "A record exists", "That something is now in a state that depends on the path. The two are entangled."),
                ("04", "Interference fades", "The paths are now distinguishable in principle, so the interference pattern weakens or disappears."),
            ], source="A simplified sequence; the sources in the text give the technical account."),
            "Nothing in that sequence mentions a mind. Step three is the important one, and it happens constantly in nature, which leads to the next idea.",
        ]),
        ("Decoherence: the universe is always watching", [
            "If observation is just interaction with a record, then almost everything is being observed almost all the time. Air molecules bounce off objects. Light scatters from them. Each collision carries away a little information about where the object is.",
            "This process has a name. As " + SEPDEC + " describes it, decoherence is the suppression of interference that occurs when a system becomes entangled with its environment, such as stray particles scattering off it. The entry notes that objects on the Earth&rsquo;s surface are very effectively decohered by the air in the atmosphere, and that the timescales involved are often minute. Its example is a speck of dust in air, which loses the relevant interference after about a microsecond of exposure.",
            "This is why nobody sees a table interfere with itself, and why Schr&ouml;dinger&rsquo;s famous cat is never seen to. As the entry puts it, the cat has interacted with so many stray particles: photons, air molecules, dust. Each of those interactions is an observation in the physical sense.",
            "HTML:" + K.callout("note", "Why this matters for the metaphor",
                "<p>If every stray photon is an observer, then the word observer in physics cannot mean a conscious watcher. It means an interaction that leaves a trace. Any argument that needs a mind to be special has to get that from somewhere other than the physics.</p>"),
        ]),
        ("The measurement problem, which is real", [
            "None of this means quantum mechanics is tidy. There is a genuine puzzle at its centre, and it is more interesting than the popular version.",
            "As " + SEPQT + " sets it out, if you apply the ordinary quantum equations to the measuring apparatus itself, you do not get a definite reading. You get an entangled state that includes every possible reading. Yet every experiment ends with one result. The problem of what to make of this is what physicists call the measurement problem.",
            "Decoherence helps, but does not finish the job. It explains why the possible readings stop interfering with each other. It does not explain why one of them is the one you see. The decoherence entry says directly that decoherence as such does not provide a solution to the measurement problem; it has to be combined with an interpretation.",
            "HTML:" + K.table("The main families of answer to the measurement problem",
                ["Approach", "Core idea", "Examples"],
                [["The quantum state is not the whole story", "Something beyond the wave function, or a pragmatic reading of it, settles the outcome", "Copenhagen-style views; de Broglie-Bohm and other hidden-variable theories"],
                 ["Collapse is a physical process", "The equations are modified so that superpositions spontaneously collapse", "GRW and related dynamical collapse theories"],
                 ["Every outcome happens", "The state never collapses; each outcome is realised in its own branch", "Everettian or many-worlds views"]],
                source='Classification follows <a href="https://plato.stanford.edu/entries/qt-issues/" target="_blank" rel="noopener">Myrvold, Stanford Encyclopedia of Philosophy</a>, section 4.2.'),
            "These are serious positions held by serious people, and they disagree. That disagreement is the honest state of the field. It is also where popular writing often slips in a fourth option, as though it were the consensus: that consciousness does the collapsing.",
        ]),
        ("Did anyone serious say consciousness causes collapse?", [
            "Yes, and it is worth being exact about who and how far. According to " + SEPQT + ", Eugene Wigner proposed in 1961 that collapse occurs when a conscious observer becomes aware of a result, and treated it as a real physical process. Fritz London and Edmond Bauer had earlier said a measurement is complete only when its result is observed, though they framed this as a change in what the observer knows rather than a physical process.",
            "John von Neumann is often listed alongside Wigner, sometimes under the label von Neumann-Wigner interpretation. The entry calls the idea that von Neumann required awareness a persistent misconception: neither he nor Dirac took a conscious observer to be necessary for collapse.",
            "And on where the field stands now, the same entry is blunt: none of the mainstream approaches accord any special physical role to conscious observers.",
            "HTML:" + K.table("Who said what about minds and measurement",
                ["Figure", "Position, as the encyclopedia describes it"],
                [["Eugene Wigner (1961)", "Collapse happens when a conscious observer becomes aware of the result, as a physical process"],
                 ["London and Bauer", "Measurement is complete when the result is observed, read as a change in knowledge rather than physics"],
                 ["John von Neumann", "Did not require awareness; the line between observer and observed can be drawn at different places"],
                 ["Mainstream approaches today", "No special physical role for conscious observers"]],
                source='Source: <a href="https://plato.stanford.edu/entries/qt-issues/" target="_blank" rel="noopener">Myrvold, Philosophical Issues in Quantum Theory</a>.'),
            "So the consciousness view exists, has a respectable history, and is not where the field went. Quoting it as what quantum physics says is like quoting one dissenting judgment as the ruling.",
        ]),
        ("What entanglement does and does not mean", [
            "Entanglement is the other quantum word that travels furthest from physics, usually into claims that two people are mysteriously linked. The physics is precise. In " + NOBEL + ", entanglement is described as a state where two particles behave like a single unit even when they are separated, and where what happens to one particle determines what happens to the other.",
            "The prize recognised experiments showing that this correlation is stronger than any theory based on hidden local properties could produce, by violating what are called Bell inequalities. The announcement concludes that quantum mechanics cannot be replaced by a theory that uses hidden variables. (Physicists usually add the word local: hidden variables of the kind those experiments test.)",
            "What the result is about is correlations between measurement outcomes on physical systems. Entanglement itself is not rare: as the decoherence section showed, everyday objects become entangled with their surroundings all the time. That is exactly why a clean, usable correlation between two particular objects is so hard to keep, and why the Nobel experiments needed carefully isolated particles. None of it is about people, feelings or intentions. Two people thinking of each other is not entanglement in this sense, and nothing in the Nobel work suggests it is. The full story of entanglement, from Einstein's objection to the 2015 experiments, is told in " + ENT + ". A related idea, often mixed up with the observer effect, is set out in " + UNC + ".",
        ]),
        ("Three tests for a physics metaphor", [
            "None of this means quantum vocabulary has no place in writing about people. Metaphors are how ideas move between fields, and the books on this site use these words deliberately. The difference between an honest borrowing and a misleading one comes down to three tests.",
            "HTML:" + K.decision("Is this a physics claim or a metaphor?",
                ("Does the sentence say the physics causes the human outcome?", [
                    ("Yes", ("Can you name the physical interaction, and is it one that survives decoherence at human scale?", [
                        ("Yes", "<p>Then it is a physics claim and needs physics evidence. Very few claims about human life pass here.</p>"),
                        ("No", "<p>It is a metaphor presented as a mechanism. Rewrite it to say the structure is similar, not that the physics is at work.</p>"),
                    ])),
                    ("No", "<p>It is a metaphor. That is fine, as long as the writing says so at the point of borrowing, not in a disclaimer at the bottom.</p>"),
                ])),
            "HTML:" + K.table("Common claims, checked",
                ["Claim", "What the physics says"],
                [["Observing something changes reality", "Interacting with a quantum system to gain information about it changes its state. The interaction is physical; no mind is required."],
                 ["Consciousness collapses the wave function", "A minority historical proposal. No mainstream approach gives minds a special physical role."],
                 ["Two people can be entangled", "Entanglement is a correlation between physical systems. Everyday interaction entangles objects with their whole environment, which scrambles any clean correlation between two of them. Nothing links two people's states."],
                 ["Your thoughts create your outcomes", "Not a physics claim at all. Expectations can shape outcomes through behaviour, which is psychology."]],
                source='Sources as cited in the sections above.'),
            "The last row is the bridge back to the rest of this site. Expectations really can shape outcomes, through the ordinary route of what people do. That mechanism is set out, with its evidence, in " + ESSAY1 + ".",
        ]),
        ("What the metaphor is still good for", [
            "Once the physics is stated plainly, the metaphor becomes more useful, not less. The real lesson of the observer effect is that gaining information is not free: to know something about a system you have to interact with it, and the interaction is part of the story.",
            "That is a good description of how people come to know each other. You cannot find out whether someone loves you without asking, watching, testing, and every one of those is an interaction that changes the person being asked. The anxious partner checking for signs of distance is not a neutral instrument. In the language the books borrow, they are part of the system they are measuring.",
            "Said that way, it is a metaphor, and it is labelled as one. The claim is not that physics governs relationships. It is that physics happened to find a precise vocabulary for a pattern that also turns up, by an entirely different mechanism, between people. " + BOOKS.replace(">both books<", ">Both books<") + " hold that line, and this essay exists so that line has something solid behind it.",
        ]),
    ],
    note=[
        "This essay is the literal half of a pair. It deliberately makes no claim about people beyond the last section, so that every essay here that borrows from physics can point to one place where the physics is stated straight.",
    ],
    faqs=[
        ("Does the observer effect mean consciousness changes reality?",
         "No. In the experiments behind the observer effect, the observer is a detector or any physical interaction that records information. The Stanford Encyclopedia of Philosophy notes that no mainstream approach to quantum mechanics gives conscious observers a special physical role."),
        ("Who was the observer in the famous 1998 experiment?",
         "A tiny electronic detector placed next to one of the paths the electrons could take. The Weizmann Institute's own press release states that the observer was not human."),
        ("What is decoherence in simple terms?",
         "Decoherence is the loss of quantum interference when a system becomes entangled with its surroundings, for example through stray air molecules or light scattering off it. It happens extremely quickly for everyday objects, which is why they never show quantum interference."),
        ("Does decoherence solve the measurement problem?",
         "Not on its own. It explains why possible outcomes stop interfering, but not why one particular outcome is observed. It has to be combined with an interpretation of quantum mechanics to address that."),
        ("Can two people be quantum entangled?",
         "Not in any sense that matters for relationships. Entanglement is a correlation between physical systems, and everyday objects are constantly entangled with their surroundings, which is what washes out any clean correlation between two particular things. Using the word for people is a metaphor, and should be labelled as one."),
    ],
    related=[
        ("why-reassurance-is-never-enough", "Why reassurance is never enough, and what to do instead", "Relationships"),
    ],
)

if __name__ == "__main__":
    newpost.build(POST)
