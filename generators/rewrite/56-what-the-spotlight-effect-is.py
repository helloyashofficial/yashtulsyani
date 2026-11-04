#!/usr/bin/env python3
"""Essay 56 :: what-the-spotlight-effect-is  (Psychology)

Sources fetched and read on 4 Nov 2026: Gilovich, Medvec and Savitsky
2000, JPSP (full text, scanned copy) with the Kellogg citation page;
Cornell Alumni Magazine 2017; Gilovich, Savitsky and Medvec 1998 (PubMed
abstract and ResearchGate full text); Savitsky, Epley and Gilovich 2001
(library catalogue abstract); Savitsky and Gilovich 2003 (ScienceDirect
abstract); MacInnis, Mackinnon and MacIntyre 2010 (full text); Gilovich
and Savitsky 1999 (APS abstract); Gilovich, Kruger and Medvec 2002
(Kellogg abstract); Brown and Stopa 2007 (Southampton full text); Crosby,
King and Savitsky 2014 (full-text copy); Cornell psychology news 2019.
No independent direct replication of the T-shirt study was found; the
essay says so.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import newpost, postkit as K

EXT = ' target="_blank" rel="noopener"'
def a(url, text):
    return '<a href="%s"%s>%s</a>' % (url, EXT, text)

SPOT = "https://www.psychologyib.com/uploads/1/1/7/5/11758934/the_spotlight_effect_-_ib_psychology.pdf"
SPOTCITE = "https://www.kellogg.northwestern.edu/academics-research/research/detail/2000/the-spotlight-effect-in-social-judgment-an-egocentric-bias/?p=1"
CAM = "https://cornellalumnimagazine.com/things-that-make-you-go-hmm"
TRANS = "https://pubmed.ncbi.nlm.nih.gov/9731312/"
TRANSFULL = "https://www.researchgate.net/publication/13555041_The_Illusion_of_Transparency_Biased_Assessments_of_Others'_Ability_to_Read_One's_Emotional_States"
HARSH = "https://bvbvf1.bib-bvb.de/vufind/PrimoRecord/cdi_proquest_miscellaneous_71045059"
SPEECH = "https://www.sciencedirect.com/science/article/abs/pii/S0022103103000568"
MACINNIS = "https://crisp.org.uiowa.edu/sites/crisp.org.uiowa.edu/files/2020-04/crisp15_4.pdf"
REVIEW99 = "https://www.psychologicalscience.org/journals/current-directions/1467-8721.00039/"
VARIAB = "https://www.kellogg.northwestern.edu/faculty/research/detail/2002/the-spotlight-effect-revisited-overestimating-the-manifest-variability-of"
STOPA = "https://eprints.soton.ac.uk/45092/1/SE_and_IOT.pdf"
MINORITY = "https://frankmcandrew.com/_files/ugd/a6ef2a_37e8b7f1c77b4d1d92834afc095487cd.pdf"
CORNELL = "https://psychology.cornell.edu/news/gilovich-honored-lifetime-research"

ESSAY40 = '<a href="/writing/why-reassurance-is-never-enough">why reassurance is never enough</a>'
ESSAY42 = '<a href="/writing/what-attachment-styles-actually-measure">what attachment styles actually measure</a>'
ESSAY51 = '<a href="/writing/what-rumination-is">what rumination is</a>'
ESSAY46 = '<a href="/writing/what-self-silencing-is">what self-silencing is</a>'

POST = dict(
    slug="what-the-spotlight-effect-is", num=56, cat="Psychology", read="auto",
    date="2026-11-04",
    gen="rewrite/56-what-the-spotlight-effect-is.py",
    title="What the spotlight effect is, and why others notice us less than we think",
    dek="It can feel as if everyone saw the stain, heard the stumble, or noticed the nerves. A set of experiments from Cornell suggests most people are seen and judged less than they believe. The reason is not vanity but where each of us is standing.",
    takeaway="The spotlight effect is the tendency to overestimate how much other people notice our appearance and actions. In the best-known study, published in 2000 by Thomas Gilovich, Medvec and Savitsky, students wearing an embarrassing T-shirt into a room estimated that about half the people there would remember it; about a quarter did. A related bias, the illusion of transparency, is the belief that our inner states, such as nerves or a lie, show more than they do. The researchers explain both as anchoring on our own vivid experience and adjusting too little for other people’s. Telling nervous speakers about the illusion improved their speeches in one study. The effect is not universal, people are still noticed sometimes, and the original findings come mostly from the same research group.",
    sections=[
        ("What the spotlight effect is", [
            "The spotlight effect is the tendency to think other people notice our appearance and actions more than they do. Because our own experience of a moment is vivid, we assume it is just as vivid to everyone else, and we adjust too little for the fact that they are mostly busy with their own.",
            "HTML:" + K.takeaways([
                "Students wearing an embarrassing T-shirt thought about half of the room would notice it. About a quarter did.",
                "The same researchers found people overestimate how much their nerves, lies and disgust show: the illusion of transparency.",
                "The proposed cause is anchoring on your own experience and adjusting too little.",
                "People also overestimate how harshly others judge their blunders.",
                "Telling nervous speakers about the illusion improved their speeches in one study.",
                "It is not that nobody notices you. It is that fewer notice, and less, than it feels.",
            ]),
            "This essay sets out what the experiments did and found, using the researchers’ own figures and caveats. It describes a bias in how people estimate others’ attention, not a treatment for social anxiety. Like the essay on " + ESSAY42 + ", it treats a psychological finding as something with a measured size and known limits, not a label.",
            "HTML:" + K.callout("definition", "The spotlight effect",
                "<p>In the words of " + a(SPOT, "Gilovich, Medvec and Savitsky") + ", the phenomenon that people overestimate the extent to which their actions and appearance are noted by others.</p>"),
        ]),
        ("The T-shirt", [
            "The best-known study is also the simplest. Thomas Gilovich, a psychologist at " + a(CORNELL, "Cornell University") + ", and his colleagues asked students to put on a T-shirt showing a large picture of the singer Barry Manilow, an image the researchers expected to be potentially embarrassing, and then to join a room of other students. Afterwards the person in the shirt was asked how many people in the room could say who was on it.",
            "The " + a(SPOT, "paper") + ", published in 2000 in the Journal of Personality and Social Psychology, reports that the average estimate made by the targets was exactly twice as high as the average accuracy rate of the observers. A footnote gives the figures: the people wearing the shirt estimated 46%; the actual rate was 23%. The study had 15 people wearing the shirt, 64 observers and 30 controls, all Cornell undergraduates.",
            "Gilovich, interviewed by the " + a(CAM, "Cornell Alumni Magazine") + " in 2017, summarised it: the average answer was about half; the reality was less than a quarter. He added that the paper has five or six studies in it, and the one everybody always talks about is the Barry Manilow one.",
            "HTML:" + K.bars("Embarrassing T-shirt: estimated and actual share who noticed",
                [("Wearers’ estimate", 46, "46%"), ("Observers who actually noticed", 23, "23%")],
                source='Source: <a href="' + SPOT + '" target="_blank" rel="noopener">Gilovich, Medvec and Savitsky (2000)</a>, footnote 3. Fifteen students wore the shirt.'),
            "The estimates were not wild. The " + a(SPOT, "paper") + " notes that although the people wearing the shirt overestimated how noticeable it was, their estimates were nonetheless grounded in reality: they were correlated with how many observers actually noticed. They knew roughly what was happening; they just thought it was happening more. Control participants, the paper reports, gave estimates that were clearly much lower than those provided by the wearers themselves.",
        ]),
        ("Not only embarrassment", [
            "The researchers then asked whether the effect was only about embarrassment. In a second study described in the " + a(SPOT, "same paper") + ", students chose a shirt showing a figure they admired, such as Bob Marley, Jerry Seinfeld or Martin Luther King, Jr. They still overestimated how many people would notice: a footnote gives 48% estimated against 8% actual. The authors suggest the low actual rate may reflect a more absorbing task for the observers, so the size of the gap should not be read as fixed.",
            "A third study moved from clothing to behaviour. In the " + a(SPOT, "paper’s account") + ", 193 Cornell undergraduates in 42 groups held a 20-minute discussion of problems facing inner cities. Afterwards, participants thought the other members would rank them higher than they actually did on all six dimensions measured, including speech errors and potentially offensive comments. They believed their good and bad moments stood out more than they did. The authors add a caution: this does not mean people are completely inaccurate about the impressions they make.",
            "HTML:" + K.table("The spotlight studies",
                ["Study", "Situation", "Finding"],
                [["1", "Embarrassing T-shirt", "Wearers estimated 46% would notice; 23% did"],
                 ["2", "Flattering T-shirt", "Wearers estimated 48%; 8% did"],
                 ["3", "Group discussion", "People overestimated how prominent their own comments and slips were"],
                 ["4 and 5", "T-shirt, testing the cause", "Estimates started high and were adjusted down, and less so right after putting the shirt on"]],
                source='Source: <a href="' + SPOT + '" target="_blank" rel="noopener">Gilovich, Medvec and Savitsky (2000)</a>.'),
        ]),
        ("Why it happens", [
            "The researchers’ explanation is anchoring and adjustment. In the " + a(SPOT, "abstract’s words") + ", people appear to anchor on their own rich phenomenological experience and then adjust, insufficiently, to take into account the perspective of others. You start from how loud the moment feels to you and move down from there, but not far enough.",
            "Two further studies in the " + a(SPOT, "paper") + " tested this. In one, with 44 Northwestern undergraduates, 23 of the 30 participants who reported a starting number cited one higher than their final answer: most started high and adjusted downward rather than the reverse. In the other, students who estimated immediately after putting on the shirt guessed that 51% of observers would have noted it, while students who had worn it for 15 minutes first guessed 37%. Once the shirt stopped feeling strange to the wearer, the anchor was lower.",
            "A later paper adds another reason. In " + a(VARIAB, "a 2002 study") + " Gilovich, Kruger and Medvec found that people overestimated how much observers would notice their ups and downs, in appearance, athletic performance and a videogame, and suggested the bias stems in part from a failure to appreciate the extent to which observers are preoccupied with managing their own actions. Everyone in the room is in their own spotlight.",
        ]),
        ("The illusion of transparency", [
            "A companion bias concerns what is inside rather than outside. In " + a(TRANS, "a 1998 paper") + ", Gilovich, Savitsky and Medvec described an illusion of transparency: a tendency for people to overestimate the extent to which others can discern their internal states. People often mistakenly believe that their internal states leak out more than they really do.",
            "In one experiment reported in the " + a(TRANSFULL, "full paper") + ", students took turns answering personal questions, with one of five instructed to lie each round. Liars estimated that an average of 48.8% of the participants would correctly peg them as the liar; only 25.6% did, an accuracy rate indistinguishable from chance. In another, people tasting drinks, some of them foul, while trying to keep a straight face believed their disgust was more apparent than it actually was.",
            "The " + a(TRANS, "abstract") + " adds that a final pair of experiments explores the implications of the illusion of transparency for people’s reluctance to intervene in emergencies. This essay does not report their details, which could not be checked.",
            "HTML:" + K.callout("note", "Two different biases",
                "<p>The spotlight effect is about being noticed: your shirt, your stumble. The illusion of transparency is about your feelings showing: your nerves, your lie. The " + a(REVIEW99, "researchers’ 1999 review") + " treats them as two biases with the same root, anchoring on your own experience.</p>"),
        ]),
        ("Judged less harshly than we fear", [
            "The same group asked a further question: when people are noticed, are they judged as harshly as they expect? In " + a(HARSH, "a 2001 paper") + ", Savitsky, Epley and Gilovich report four studies in which people who imagined a social blunder, experienced a public intellectual failure, or were described in an embarrassing way anticipated being judged more harshly by others than they actually were.",
            "The " + a(HARSH, "abstract") + " explains the gap in similar terms. The people involved were inordinately focused on their misfortunes, and as a result failed to consider the wider range of situational factors that tend to moderate onlookers’ impressions. Observers make allowances, for example for a hard question or a bad day, that the person in the moment does not think of. The authors close by discussing additional mechanisms behind overly pessimistic expectations, and the role such expectations play in producing unnecessary social anxiety.",
        ]),
        ("Does knowing about it help?", [
            "One study tested whether knowing about the bias changes anything. In " + a(SPEECH, "a 2003 paper") + ", Savitsky and Gilovich first showed that people nervous about giving a speech believe their nervousness is more apparent to their audience than it actually is. Then they showed that an awareness of the illusion can improve the quality of a speaker’s performance, from both the speaker’s own perspective and in the eyes of observers.",
            "Later researchers found the illusion outside the laboratory. A " + a(MACINNIS, "2010 study by MacInnis, Mackinnon and MacIntyre") + " reported the existence of the illusion of transparency in a naturalistic public speaking situation, and summarised the 2003 finding as showing that its effects were ameliorated by simply assuring speakers that their anxiety was not as visible as they tend to believe.",
            "HTML:" + K.callout("warn", "Not a treatment",
                "<p>These are studies of speakers in research settings, not of clinical anxiety. Knowing about the spotlight effect may take some of the edge off a nervous moment, but anyone whose social anxiety is getting in the way of daily life should talk to a doctor or a qualified therapist.</p>"),
        ]),
        ("What the research cannot yet say", [
            "The effect has limits that the original paper itself sets out. The " + a(SPOT, "authors write") + " that people do not always overestimate the extent to which their appearance and behaviour are noticed by others, and that something of a reverse spotlight effect might occur when people are not at all conscious of their own behaviour and yet their actions are quite noticeable to others. Their examples include people who wear too much cologne.",
            "It also varies with the situation. A study by " + a(STOPA, "Brown and Stopa") + " in 2007, of students with moderate to high fear of negative evaluation, found higher levels of the spotlight effect under high social-evaluative conditions, and suggested that the effect may be specific to social-evaluative concerns. And a 2014 paper on what its authors call the " + a(MINORITY, "minority spotlight effect") + " found that members of underrepresented groups felt they were the centre of others’ attention when topics related to their group were discussed, despite the fact that the actual gaze of others did not differ.",
            "The studies that extend the idea have their own limits. The " + a(STOPA, "Brown and Stopa") + " sample was 53 female students, a limitation the authors acknowledge. And the " + a(MINORITY, "minority spotlight paper") + " found the effect was not inevitable: in its second study, minority participants’ average estimate of 34.06% was nearly identical to the objectively correct answer of 33%. How much people overestimate attention seems to depend on who they are, where they are and what is being discussed.",
            "HTML:" + K.callout("note", "What was not found",
                "<p>The search for this essay found no independent direct replication of the T-shirt study. Most of the follow-up work comes from the original researchers and their colleagues, and the participants were mostly American university students. That does not make the findings wrong, but it limits how far they can be generalised.</p>"),
        ]),
        ("What this does and does not say", [
            "Read carefully, the research supports a modest and useful claim. When you feel conspicuous, other people are probably noticing less than you think, and judging less harshly, because they are seeing the moment from outside and are mostly occupied with their own. That is not the same as saying nobody notices: in the T-shirt study, about a quarter of the room did.",
            "The practical lesson is to discount the feeling, not to dismiss other people. The vividness of your own experience is real; it is just a poor guide to theirs.",
            "This connects to other essays here. " + ESSAY51.replace(">what rumination", ">What rumination") + " describes how going over an embarrassing moment again and again can keep low mood going. " + ESSAY46.replace(">what self-silencing", ">What self-silencing") + " looks at holding back what you think for fear of how others will react, a fear the spotlight research suggests is often larger than the reaction. And " + ESSAY40 + " looks at a related loop in relationships, where the fear of how one is seen keeps asking to be answered.",
        ]),
    ],
    note=[
        "The T-shirt percentages are from footnote 3 of the 2000 paper; its main text reports the first result as estimates exactly twice the actual rate. The 2001 and 2003 studies are described from their abstracts.",
    ],
    faqs=[
        ("What is the spotlight effect?",
         "The tendency to overestimate how much other people notice your appearance and actions. Thomas Gilovich and colleagues named and tested it in a 2000 paper."),
        ("What was the Barry Manilow T-shirt experiment?",
         "Students wore a T-shirt with a large picture of Barry Manilow into a room of other students, then estimated how many could say who was on it. They estimated 46% on average; 23% actually could."),
        ("What is the illusion of transparency?",
         "The belief that your inner states, such as nervousness or a lie, are more visible to others than they are. In one 1998 study, liars thought nearly half of their group would spot them; about a quarter did, no better than chance."),
        ("Why do people overestimate how much others notice them?",
         "The researchers' explanation is anchoring and adjustment: people start from their own vivid experience of the moment and adjust too little for the fact that others see it from outside and are busy with their own actions."),
        ("Does knowing about the spotlight effect help with nerves?",
         "In one 2003 study, telling nervous speakers about the illusion of transparency improved the quality of their speeches, as judged by themselves and by observers. It is a research finding, not a treatment for anxiety."),
    ],
    related=[
        ("what-rumination-is", "What rumination is, and why thinking it through can make things worse", "Psychology"),
        ("what-attachment-styles-actually-measure", "What attachment styles actually measure, and what they cannot tell you", "Psychology"),
    ],
)

if __name__ == "__main__":
    newpost.build(POST)
