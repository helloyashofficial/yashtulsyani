#!/usr/bin/env python3
"""Essay 61 :: what-learned-helplessness-actually-showed  (Psychology)

Sources fetched and read on 5 to 6 Nov 2026: Maier and Seligman 1976
(Penn PPC scan) for the design and results of Seligman and Maier 1967;
Overmier and Seligman 1967 (Illinois State copy); Hiroto 1974 and Hiroto
and Seligman 1975 (Appalachian State copies); Abramson, Seligman and
Teasdale 1978 (CORE); Maier and Seligman 2016 (Penn PPC full text);
Baratta, Seligman and Maier 2023 (Frontiers); Abramson, Metalsky and Alloy
1989 (catalogue abstract); Peterson and Seligman 1984 (Penn PPC);
Seligman's Penn biography; CU Boulder tribute to Maier (2026); Seligman in
The Daily Pennsylvanian (2008); New York Review of Books exchange (2016);
APA Monitor (2009).
Not used: the 1967 paper's own abstract and its shock parameters (not
readable); folk parables about elephants and fleas.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import newpost, postkit as K

EXT = ' target="_blank" rel="noopener"'
def a(url, text):
    return '<a href="%s"%s>%s</a>' % (url, EXT, text)

MS76 = "https://ppc.sas.upenn.edu/sites/default/files/lhtheoryevidence.pdf"
OS67 = "https://about.illinoisstate.edu/vfdouga/files/2019/10/overmeier_seligman-_-LH.pdf"
HIROTO = "https://www.appstate.edu/~steelekm/classes/psy5300/Documents/Hiroto1974-learned-helplessness.pdf"
HS75 = "https://www.appstate.edu/~steelekm/classes/psy5300/Documents/Hiroto&amp;Seligman1975-learned-helplessness.pdf"
AST78 = "https://core.ac.uk/download/357200055.pdf"
MS16 = "https://ppc.sas.upenn.edu/sites/default/files/learnedhelplessnessat50.pdf"
MSB23 = "https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2023.1170417/full"
AMA89 = "https://bvbvf1.bib-bvb.de/vufind/PrimoRecord/cdi_proquest_journals_614321725"
PS84 = "https://ppc.sas.upenn.edu/sites/default/files/causalriskfordep.pdf"
SELIGMAN = "https://ppc.sas.upenn.edu/people/martin-ep-seligman"
MAIER = "https://www.colorado.edu/psych-neuro/2026/08/17/remembering-steven-f-maier"
DP = "https://thedp.com/article/2008/08/martin_seligman_data_that_opens_countless_doors_counterpoint"
NYRB = "https://www.nybooks.com/articles/2016/04/21/learned-helplessness-torture-an-exchange/"
MONITOR = "https://www.apa.org/monitor/2009/10/helplessness"

ESSAY42 = '<a href="/writing/what-attachment-styles-actually-measure">what attachment styles actually measure</a>'
ESSAY51 = '<a href="/writing/what-rumination-is">what rumination is</a>'
ESSAY43 = '<a href="/writing/what-the-stoics-meant-by-what-is-up-to-us">what the Stoics meant by what is up to us</a>'

POST = dict(
    slug="what-learned-helplessness-actually-showed", num=61, cat="Psychology", read="auto",
    date="2026-11-06",
    gen="rewrite/61-what-learned-helplessness-actually-showed.py",
    title="What learned helplessness actually showed, and how its discoverers changed their minds",
    dek="Learned helplessness is one of the best-known ideas in psychology: after bad things happen that you cannot control, you stop trying. Fifty years after the first experiments, the two scientists who discovered it concluded that the original explanation had it backward. The passivity is not learned. What can be learned is control.",
    takeaway="In experiments in the 1960s, dogs that had received shocks they could not escape often failed to escape later, when escape was easy; dogs that had been able to stop the same shocks did not. Martin Seligman and Steven Maier explained this as learned helplessness: the animals had learned that nothing they did mattered. The idea was extended to people, reformulated in terms of how people explain bad events, and linked to depression as a risk factor. In 2016, after decades of neuroscience, Maier and Seligman concluded the original theory got it backward: passivity is the default, unlearned response to prolonged bad events, and what animals learn is that they have control, which switches the default off. The finding has a darker history too, in debates about animal research and about how the idea was used.",
    sections=[
        ("What learned helplessness showed", [
            "Learned helplessness showed that after uncontrollable bad events, animals and people often stop trying to escape even when escape becomes possible. The original explanation was that they learned their actions did not matter. Fifty years on, the discoverers concluded the reverse: giving up is the default response, and what is learned is control, which overrides it.",
            "HTML:" + K.takeaways([
                "In the 1960s, dogs given shocks they could not control often failed to escape later, when escape was easy.",
                "Dogs that received the same shocks but could stop them did not show this.",
                "The idea was extended to people, then reformulated around how people explain bad events.",
                "How people explain bad events was later proposed as a risk factor for depression, not a sufficient cause.",
                "In 2016 the discoverers concluded the original theory got it backward: passivity is the default; control is what is learned.",
                "The research has a contested ethical history, from animal welfare to its later misuse.",
            ]),
            "This essay sets out what the experiments did and found, how the theory changed, and what it does and does not say about people. It describes the animal experiments plainly, without softening or dramatising them.",
            "HTML:" + K.callout("definition", "Learned helplessness",
                "<p>In the words of " + a(MS16, "Maier and Seligman") + ", the failure to escape shock induced by uncontrollable aversive events. Whether that failure is actually learned is the question this essay is about.</p>"),
        ]),
        ("The original experiments", [
            "The experiments were run in the mid-1960s at the University of Pennsylvania by Seligman and Maier, who " + a(MS16, "arrived there as first-year graduate students in 1964") + ", and their fellow graduate student Bruce Overmier. The design is set out in a " + a(MS76, "1976 review by Maier and Seligman") + ". Dogs were divided into three groups. An escape group was trained in a hammock to turn off shock by pressing a panel with its nose. A yoked group received shocks identical in number, duration, and pattern to the shocks delivered to the escape group, but nothing it did could stop them. A third group received no shock.",
            "All three groups were then tested in a shuttle box, a two-compartment box in which a dog could escape or avoid shock by jumping over a low barrier. The difference was stark. In the 1967 study the review describes, six of the eight dogs in the yoked group failed completely to escape shock. The dogs that had been able to stop the earlier shocks learned to jump, as did the dogs that had received no shock at all.",
            "HTML:" + K.table("The three-group design",
                ["Group", "First session", "Later, in the shuttle box"],
                [["Escape", "Shocks they could stop by pressing a panel", "Learned to escape"],
                 ["Yoked", "The same shocks, but nothing they did stopped them", "Six of eight failed completely to escape"],
                 ["No shock", "No shocks", "Learned to escape"]],
                source='Source: <a href="' + MS76 + '" target="_blank" rel="noopener">Maier and Seligman (1976)</a>, describing Seligman and Maier (1967).'),
            "The key is the comparison between the first two groups. Both received exactly the same shocks. The only difference was control. That is why the effect was attributed to the uncontrollability of the shocks, not to the shocks themselves.",
        ]),
        ("Not every animal, and not for long", [
            "The effect was strong but not universal. Across their work between 1965 and 1969, the same " + a(MS76, "review") + " reports, the researchers studied about 150 dogs that had received prior inescapable shock, and two thirds, about 100, did not learn to escape. A third did. That is a large effect, but it is not the universal collapse that popular retellings of the experiments often describe.",
            "It could also fade. A companion paper by " + a(OS67, "Overmier and Seligman in 1967") + " found that exposure to inescapable shocks reliably interfered with later escape learning in a new situation, but that the magnitude of interference was found to dissipate rapidly in time, leaving an apparently normal animal after only 48 hours. After a single session, the effect was short-lived.",
        ]),
        ("From dogs to people", [
            "The idea was soon tested in people, using harmless but unpleasant stimuli. In a " + a(HIROTO, "1974 study") + ", Donald Hiroto exposed students to a loud tone; some could switch it off, others had a button that did nothing. Those exposed to the uncontrollable tone later failed to escape the tone in a new task, which the paper describes as a complete replication of learned helplessness in man. People who believed outcomes were down to chance, rather than skill, were more helpless.",
            "A " + a(HS75, "1975 paper by Hiroto and Seligman") + " reported four experiments with college students and found that both insolubility and inescapability produced failure to escape and failure to solve anagrams: unsolvable problems could produce the same effect as an inescapable noise, and the effect carried across tasks. The authors suggested that learned helplessness may be an induced trait.",
        ]),
        ("How people explain bad events", [
            "The human version soon ran into a problem: people do not just register that they lack control; they ask why. In " + a(AST78, "1978") + ", Abramson, Seligman and Teasdale criticised and reformulated the theory. Once people perceive that outcomes do not depend on what they do, they attribute their helplessness to a cause, and that cause can be stable or unstable, global or specific, and internal or external.",
            "The explanation matters, the reformulation argued, because it shapes what follows. The attribution chosen influences whether expectation of future helplessness will be chronic or acute, broad or narrow, and whether helplessness will lower self-esteem or not. Blaming yourself, expecting it to last, and expecting it to spread to everything is the worst combination.",
            "HTML:" + K.table("Three ways to explain a bad event",
                ["Dimension", "One end", "Other end"],
                [["Stable or unstable", "Long-lived or recurrent", "Short-lived or intermittent"],
                 ["Global or specific", "Affects a wide variety of outcomes", "Affects only this one"],
                 ["Internal or external", "About me", "About other people or circumstances"]],
                source='Definitions from <a href="' + AST78 + '" target="_blank" rel="noopener">Abramson, Seligman and Teasdale (1978)</a>.'),
            "In " + a(PS84, "1984") + ", Peterson and Seligman proposed that a habitual explanatory style in which bad events are explained by internal, stable, and global causes is associated with depressive symptoms, and claimed it is a risk factor for later depression when bad events are encountered. They were careful to say that such explanations are not sufficient to produce depressive deficits but rather are risk factors for such deficits. A " + a(AMA89, "1989 revision by Abramson, Metalsky and Alloy") + " went further, proposing a hopelessness theory in which hopelessness is a proximal sufficient cause of a proposed subtype, hopelessness depression, with less weight on the attributions themselves.",
        ]),
        ("Fifty years later: it was backward", [
            "In 2016, Maier and Seligman revisited their discovery in " + a(MS16, "a paper in Psychological Review") + ", drawing on decades of research on what happens in the brain. Their conclusion is unusually blunt for scientists writing about their own most famous idea: “the original theory got it backward.”",
            "In their words: “Passivity in response to shock is not learned. It is the default, unlearned response to prolonged aversive events,” and it is mediated by serotonin-releasing neurons in a brain region called the dorsal raphe nucleus, which in turn inhibits escape. What changes this is control: the passivity can be overcome by learning control, through activity in the medial prefrontal cortex, which detects control and switches off the default.",
            "So the animals in the escape group did not avoid learning helplessness; they learned something extra. As the paper puts it: “So it is the presence of control, not the absence of control, that is detected.” And it concludes that helplessness was not learned in the original experiments, that passivity and heightened anxiety are the default mammalian reaction to prolonged bad events, and that what can be learned is cortical: that bad events will be controllable in the future. The authors suggest that the circuit running from the ventromedial prefrontal cortex to the dorsal raphe nucleus may be usefully thought of as the “hope circuit.”",
            "HTML:" + K.compare("The original theory and the revision", [
                ("1967 theory", ["Animals learn that their actions do not matter"], ["Neuroscience later showed the passivity does not depend on detecting lack of control"], "Helplessness is learned."),
                ("2016 revision", ["Fits the brain data on serotonin and the prefrontal cortex"], ["Mostly from animal studies; human brain evidence is harder to get"], "Passivity is the default; control is learned."),
            ], source='Sources: <a href="' + MS76 + '" target="_blank" rel="noopener">Maier and Seligman (1976)</a>; <a href="' + MS16 + '" target="_blank" rel="noopener">Maier and Seligman (2016)</a>.'),
            "Maier had been saying something similar for years. In a " + a(MONITOR, "2009 APA Monitor article") + " he put it in one sentence: “The default position of the brain is to assume that stress is not controllable.” A " + a(MSB23, "2023 review by Baratta, Seligman and Maier") + " sums up the reversal: in their current account, “control actively leads to protection.”",
        ]),
        ("What it means for depression", [
            "The link to depression is real but limited, and the 2016 paper is careful about it. The " + a(MS16, "authors write") + " that the passivity and heightened anxiety symptoms of learned helplessness map quite well into symptoms of depression, and that the animal model produced eight of the nine symptoms, with the only exception being suicide and suicidal thoughts. They then add that a set of cautions should temper these speculations, chiefly the difficulty of studying the relevant brain circuits in people.",
            "Their suggestion for treatment follows from the reversal. If passivity is the default and control is what can be learned, then building the expectation of control matters more than removing a learned belief. In their words: “We speculate that it is expectations of a better future that most matter in treatment.” It is offered as a speculation, not a finding.",
            "HTML:" + K.callout("warn", "Not medical advice",
                "<p>This essay describes research. If low mood or a sense that nothing you do matters is lasting or getting worse, a doctor or qualified therapist is the right place to start.</p>"),
        ]),
        ("The harder history", [
            "The research has drawn criticism, and its discoverers have addressed some of it. Seligman, writing in " + a(DP, "The Daily Pennsylvanian in 2008") + ", asked himself the question directly, “Could I work in a laboratory that gave shocks to perfectly innocent animals?”, and answered that such research can only be justified if it is likely that the knowledge gained will eliminate vastly more suffering. He added that he gave up animal research more than thirty years earlier, and noted that some now claim the experiments were unnecessary, a claim he called completely wrong.",
            "The idea was also drawn into a later controversy over US interrogation practices. In a " + a(NYRB, "2016 exchange in the New York Review of Books") + ", Seligman wrote that he strongly disapproves of torture and has never aided or abetted it and never would, and that had he known about the methods employed, he would not have discussed learned helplessness with officials. The philosopher Tamsin Shaw, replying, quoted an independent report as saying that investigators did not have enough information to know what Seligman knew or thought at the time. The question remains disputed.",
            "Maier died in July 2026, aged 83. A " + a(MAIER, "tribute from the University of Colorado Boulder") + ", where he was a Distinguished Professor, calls learned helplessness one of the most influential and controversial theories in the history of psychology, and sums up the revision he led: what is detected and learned is the presence, not the absence, of control. Seligman, according to his " + a(SELIGMAN, "University of Pennsylvania biography") + ", went on to be elected president of the American Psychological Association in 1998 and to promote positive psychology as a field of scientific study.",
        ]),
        ("What this does and does not say", [
            "Read carefully, the research supports a clear and somewhat hopeful picture. After prolonged bad events that cannot be controlled, giving up is a natural default, not a character flaw. What protects against it is the experience, and the expectation, of control. How people explain their setbacks shapes how far the effect spreads, and that explanatory style is one risk factor for depression among many. The famous phrase learned helplessness turns out to describe the wrong thing being learned.",
            "Other essays here meet the idea from different directions. " + ESSAY43.replace(">what the Stoics", ">What the Stoics") + " is an ancient attempt to sort what is in our control from what is not. " + ESSAY51.replace(">what rumination", ">What rumination") + " looks at how going over bad events in abstract terms keeps low mood going. And " + ESSAY42 + " looks at another way early experience is thought to shape what people expect from others.",
        ]),
    ],
    note=[
        "The 1967 experiment is described through the authors’ 1976 review, because the original paper could not be read in full. The animal procedures are reported as the sources describe them.",
    ],
    faqs=[
        ("What is learned helplessness?",
         "The failure to escape or avoid bad events after earlier experience of bad events that could not be controlled. It was first described in experiments with dogs in the 1960s and later studied in people."),
        ("What did the learned helplessness experiments involve?",
         "Dogs received electric shocks they either could or could not stop; a third group received none. Later, in a box where they could escape shock by jumping a low barrier, most of the dogs that had been unable to stop the earlier shocks did not escape, while the others did."),
        ("Did the discoverers change their minds?",
         "Yes. In 2016 Maier and Seligman concluded the original theory got it backward: passivity is the default, unlearned response to prolonged bad events, and what animals learn is that they have control, which overrides that default."),
        ("Does learned helplessness cause depression?",
         "Not on its own. A pessimistic way of explaining bad events was proposed as a risk factor for depression, not a sufficient cause, and the 2016 paper treats links to depression as speculation needing caution."),
        ("Is the elephant and rope story about learned helplessness?",
         "It is a popular parable, not part of the research. The scientific work is the series of experiments and papers described in this essay."),
    ],
    related=[
        ("what-rumination-is", "What rumination is, and why thinking it through can make things worse", "Psychology"),
        ("what-the-spotlight-effect-is", "What the spotlight effect is, and why others notice us less than we think", "Psychology"),
    ],
)

if __name__ == "__main__":
    newpost.build(POST)
