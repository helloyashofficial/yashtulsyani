#!/usr/bin/env python3
"""Essay 51 :: what-rumination-is  (Psychology)

Sources fetched and read on 4 Nov 2026: Nolen-Hoeksema, Wisco and
Lyubomirsky 2008, "Rethinking rumination" (full text, academia.edu copy);
Watkins 2008 (Exeter repository manuscript, full text); Nolen-Hoeksema,
Parker and Larson 1994 (full text); the Loma Prieta abstract (Scilit
record); Lyubomirsky and Tkach chapter (author's site, full text);
Treynor, Gonzalez and Nolen-Hoeksema 2003 (Springer, abstract);
Whitmer and Gotlib 2011 (full text); NovoPsych's reproduction of the
Ruminative Responses Scale (secondary, for item wording); Watkins and
Moulds 2005 (abstract); Johnson and Whisman 2013 (PMC); Aldao,
Nolen-Hoeksema and Schweizer 2010 (PubMed abstract); McLaughlin and
Nolen-Hoeksema 2011 (PMC); Rose 2002 (abstract); Watkins et al. 2011
(full text); Yale News obituary 2013.
Not used: the original 1993 and 1995 Lyubomirsky papers (reported through
the chapter); any mindfulness trial (none read).
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import newpost, postkit as K

EXT = ' target="_blank" rel="noopener"'
def a(url, text):
    return '<a href="%s"%s>%s</a>' % (url, EXT, text)

RETHINK = "https://www.academia.edu/1028279/Rethinking_rumination"
WATKINS = "https://ore.exeter.ac.uk/repository/bitstream/10871/11162/2/watkinsconstructiveunconstructiveRT.pdf"
NPL94 = "https://www.researchgate.net/profile/Louise-Parker-2/publication/15151833_Ruminative_Coping_With_Depressed_Mood_Following_Loss/links/53f4f4b00cf22be01c3efc96/Ruminative-Coping-With-Depressed-Mood-Following-Loss.pdf"
LOMA = "https://scilit.net/publications/b67677b1341ab4100bbb41277fcfafd1"
LT = "https://sonjalyubomirsky.com/wp-content/uploads/2024/07/Lyubomirsky-Tkach-2004.pdf"
TREYNOR = "https://link.springer.com/content/pdf/10.1023/a:1023910315561.pdf"
WG = "https://web.stanford.edu/group/mood/cgi-bin/wordpress/wp-content/uploads/2012/02/whitmer_gotlib_CTR_2011.pdf"
RRS = "https://novopsych.com/wp-content/uploads/2026/08/ruminative-responses-scale-rrs-blank-form-pdf-survey-questions-items.pdf"
WM05 = "https://scilit.com/publications/91a16854b667eb9d4f7f74036049ee2e"
JW13 = "https://pmc.ncbi.nlm.nih.gov/articles/PMC3786159"
ALDAO = "https://pubmed.ncbi.nlm.nih.gov/20015584/"
MCL = "https://pmc.ncbi.nlm.nih.gov/articles/PMC3042543"
ROSE = "https://scilit.com/publications/1a8bd19677792a60015231e97ca11c8f"
RFCBT = "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/8A7837A95E24712C034EB101FD53F41A/S0007125000258352a.pdf/ruminationfocused_cognitivebehavioural_therapy_for_residual_depression_phase_ii_randomised_controlled_trial.pdf"
YALE = "https://news.yale.edu/2013/01/07/memoriam-susan-nolen-hoeksema"

ESSAY42 = '<a href="/writing/what-attachment-styles-actually-measure">what attachment styles actually measure</a>'
ESSAY46 = '<a href="/writing/what-self-silencing-is">what self-silencing is</a>'
ESSAY40 = '<a href="/writing/why-reassurance-is-never-enough">why reassurance is never enough</a>'

POST = dict(
    slug="what-rumination-is", num=51, cat="Psychology", read="auto",
    date="2026-11-04",
    gen="rewrite/51-what-rumination-is.py",
    title="What rumination is, and why thinking it through can make things worse",
    dek="Going over a problem again and again feels like working on it. A long line of research suggests that, for people who are already low, it often keeps the low mood going instead. It also suggests that not all repetitive thinking is the same, and the difference is useful.",
    takeaway="Rumination is thinking repetitively about your feelings and problems: why you feel this way, what it means, what will follow. Susan Nolen-Hoeksema proposed that this response to low mood makes it worse and longer. Studies support that in several ways: people who ruminated before an earthquake were more depressed after it, rumination predicted new episodes of depression in a community sample, and in experiments rumination worsened mood in people who were already low but not in others, and worsened their problem solving. Later work split rumination into brooding, which goes with more depression, and reflection, which predicted less over time, and found that abstract, evaluative thinking is the harmful kind while concrete, experiential thinking is not. Most of the evidence shows prediction rather than proof of cause, and a therapy aimed at rumination has had encouraging early results.",
    sections=[
        ("What rumination is", [
            "Rumination is repetitive thinking about your own feelings and problems: why you feel this way, what it says about you, what will happen next. Research suggests that, in people who are already low, it tends to deepen and prolong the low mood and to make problems look harder to solve. Not all repetitive thought does this; the brooding, abstract kind is the problem.",
            "HTML:" + K.takeaways([
                "Rumination is thinking perseveratively about your feelings and problems, in the words of Nolen-Hoeksema and colleagues.",
                "People who ruminated more before the Loma Prieta earthquake were more depressed afterwards.",
                "In experiments, rumination worsened mood in people who were already low, but not in others, and worsened their problem solving.",
                "Brooding goes with more depression. Reflection went with more at the time but predicted less over time.",
                "Abstract thinking about causes and meanings is the unhelpful kind; concrete, moment-by-moment attention is not.",
                "Most of the evidence is prediction, not proof of cause. A therapy aimed at rumination has had promising early results.",
            ]),
            "This essay sets out what the research means by rumination, what the main studies found, and what they leave open. It is about how the research describes a habit of thought, not a guide to treating depression; anyone struggling with low mood should talk to a doctor or another qualified professional.",
            "HTML:" + K.callout("definition", "Rumination, in this essay",
                "<p>Defined by " + a(RETHINK, "Nolen-Hoeksema, Wisco and Lyubomirsky") + " as the process of thinking perseveratively about one’s feelings and problems.</p>"),
        ]),
        ("The response styles theory", [
            "Much of the research on rumination traces back to Susan Nolen-Hoeksema, a psychologist who later chaired the psychology department at Yale. According to " + a(YALE, "Yale’s obituary") + ", she received her doctorate from the University of Pennsylvania in 1986, wrote books including Women Who Think Too Much, and died in January 2013 at the age of 53.",
            "Her idea, first set out in 1991, was that the way people respond to feeling low affects how long the low lasts. Her original definition, as " + a(WATKINS, "Watkins quotes it") + ", described rumination as behaviors and thoughts that focus one’s attention on one’s depressive symptoms and on the implications of these symptoms. Someone who responds to sadness by asking why they feel this way, what is wrong with them and where it will lead is ruminating. Someone who responds by doing something absorbing is distracting themselves.",
            "The prediction was that the first response would make depression worse and longer. In the " + a(RETHINK, "2008 review") + " she wrote with Wisco and Sonja Lyubomirsky, the theory is summarised as holding that rumination exacerbates and prolongs distress, particularly depression. One of the routes it describes is practical: rumination in the context of a low mood seems to interfere with good problem solving.",
            "HTML:" + K.callout("note", "Why it feels useful",
                "<p>Rumination usually feels like an attempt to understand, not like a habit. That may be part of why it is hard to notice from the inside.</p>"),
        ]),
        ("An earthquake, by chance", [
            "Some early evidence came from an accident of timing. Nolen-Hoeksema and Morrow had measured mood and response styles in a group of students " + a(LOMA, "14 days before the Loma Prieta earthquake") + ". According to the abstract, 137 students were followed up 10 days and 7 weeks after it.",
            "The abstract reports that students who already had elevated symptoms and a ruminative style before the earthquake had more depression and stress symptoms at both follow-ups, and that students who ruminated more about the earthquake in the first 10 days were still more likely to have high symptoms 7 weeks later. Writing in " + a(NPL94, "1994") + ", Nolen-Hoeksema and her colleagues summarised it: people with a more ruminative style before the earthquake were more depressed afterwards, even after taking into account pre-earthquake levels of distress.",
            "A larger study pointed the same way. The " + a(RETHINK, "2008 review") + " reports that in a sample of approximately 1,300 adults randomly drawn from the community, rumination scores predicted new onsets of major depressive episodes over the following year, among people who were not already depressed. The 1994 study, of 253 bereaved adults, found that people with a more ruminative style were more depressed six months after the loss, even after controlling for initial depression and other factors.",
            "HTML:" + K.table("Three studies that followed people over time",
                ["Study", "Who", "What rumination predicted"],
                [["Loma Prieta earthquake study (1991)", "137 students, measured before the earthquake", "More depression and stress symptoms 10 days and 7 weeks after"],
                 ["Bereavement (1994)", "253 bereaved adults", "More depression at 6 months, after controlling for initial levels"],
                 ["Community sample (2000)", "About 1,300 adults", "New episodes of major depression over the next year"]],
                source='Sources: <a href="' + LOMA + '" target="_blank" rel="noopener">Loma Prieta abstract</a>; <a href="' + NPL94 + '" target="_blank" rel="noopener">Nolen-Hoeksema, Parker and Larson (1994)</a>; <a href="' + RETHINK + '" target="_blank" rel="noopener">Nolen-Hoeksema, Wisco and Lyubomirsky (2008)</a>.'),
            "Studies like these show that rumination comes before worse outcomes, which is stronger than showing that the two go together. They do not on their own prove that rumination causes them. For that, the research turned to experiments.",
        ]),
        ("What the experiments show", [
            "In the laboratory, researchers ask some participants to spend a few minutes thinking about themselves and their feelings, and others to think about neutral things. A chapter by " + a(LT, "Lyubomirsky and Tkach") + " gives examples of each: a rumination prompt such as “Think about the kind of person you are”, and a distraction prompt such as “Think about the size of the Statue of Liberty”.",
            "The result depends on who is ruminating. The " + a(RETHINK, "2008 review") + " reports that the rumination induction significantly increases dysphoric mood in dysphoric participants, but not in nondysphoric participants. Dysphoric here means already in a low mood. For someone feeling fine, thinking about themselves for a few minutes did not measurably lower mood; for someone already low, it made things worse.",
            "Rumination also seems to make problems look harder. The review notes that inducing dysphoric participants to ruminate prompts them to appraise their problems as overwhelming and unsolvable. In one study described by " + a(LT, "Lyubomirsky and Tkach") + ", dysphoric students who ruminated generated less effective solutions to hypothetical problems.",
            "One finding may help explain why the habit persists. The same chapter reports that dysphoric ruminators recognised that pleasant, distracting activities would lift their mood, but were unwilling to do them. Knowing what would help is not the same as doing it.",
            "Distraction has limits too. Lyubomirsky and Tkach note that effective distractions do not include inherently dangerous or self-destructive activities. In the " + a(RETHINK, "2008 review") + ", pleasant or neutral distraction is presented as a way to lift mood enough to then tackle the problem, not as a permanent escape from it.",
        ]),
        ("Brooding and reflection", [
            "Not all repetitive self-focused thinking turned out to be the same. In " + a(TREYNOR, "a 2003 analysis") + ", Treynor, Gonzalez and Nolen-Hoeksema identified two components within the standard rumination questionnaire, reflective pondering and brooding, which the abstract says differentially relate to depression.",
            "Later researchers describe the two clearly. In " + a(WG, "a 2011 paper") + ", Whitmer and Gotlib summarise Treynor’s definitions: brooding as passive and judgmental pondering of one’s mood, and reflection as contemplative, intentional pondering of one’s mood with a focus on problem solving.",
            "HTML:" + K.table("Brooding and reflection, in the questionnaire’s words",
                ["Component", "Example items"],
                [["Brooding", "“Think ‘What am I doing to deserve this?’” · “Think ‘Why do I always react this way?’”"],
                 ["Reflection", "“Analyze recent events to try to understand why you are depressed” · “Go away by yourself and think about why you feel this way”"]],
                source='Items from the Ruminative Responses Scale, as reproduced by <a href="' + RRS + '" target="_blank" rel="noopener">NovoPsych</a>; components from <a href="' + TREYNOR + '" target="_blank" rel="noopener">Treynor, Gonzalez and Nolen-Hoeksema (2003)</a>.'),
            "The findings were different for each. The " + a(RETHINK, "2008 review") + " reports that brooding was positively correlated with depression both at the time and over one year, and that, although reflective pondering was associated with more depression at the time, it was associated with less depression over time. " + a(WG, "Whitmer and Gotlib") + " summarise it the same way: reflection was associated with concurrent symptoms but predicted lower levels of depression over time.",
            "One possible reading, which is interpretation rather than a finding: reflection may start when someone is already low, which is why it shows up alongside symptoms, but it is aimed at understanding and doing something, which may be why it helps later. Brooding is judgement without a way forward.",
        ]),
        ("Abstract and concrete thinking", [
            "The psychologist Watkins took the distinction further. In a " + a(WATKINS, "2008 review in Psychological Bulletin") + ", he argues that repetitive thought can have constructive or unconstructive consequences, and that which it has depends on three things: the valence of what is being thought about, the context in which it happens, and the level of construal, meaning whether the thinking is abstract or concrete.",
            "Abstract thinking, in Watkins’s description, is an evaluative mindset focused on the causes, meanings and implications of events: why did this happen, what does it say about me. Concrete thinking attends to the specifics of what happened and how it felt, moment by moment. Watkins reports an experiment by Ehring and colleagues in which abstract rumination resulted in slower recovery of negative affect than concrete rumination or distraction.",
            "The difference also affects problem solving. In a study of " + a(WM05, "40 depressed patients and 40 never-depressed people") + ", Watkins and Moulds found that concrete self-focus improved problem solving in the depressed patients compared with abstract self-focus. Their conclusion was that the particular way of focusing on symptoms, rather than focusing on symptoms as such, determines the effects of rumination on social problem solving.",
            "HTML:" + K.table("Two ways of thinking about the same bad day",
                ["Abstract (unhelpful when low)", "Concrete (less harmful)"],
                [["Why does this always happen to me?", "What exactly happened, in what order?"],
                 ["What does this say about who I am?", "What did I notice and feel at each point?"],
                 ["Where is this going to lead?", "What is the next specific thing I could do?"]],
                source='Illustrations of the distinction described by <a href="' + WATKINS + '" target="_blank" rel="noopener">Watkins (2008)</a>; the questions are examples, not items from a study.'),
        ]),
        ("Who ruminates, and what else it is linked to", [
            "The " + a(RETHINK, "2008 review") + " notes that several studies have found women more likely to ruminate, and that the difference in rumination has been found to account for part of the gender difference in depression in some studies. The size of the difference is modest. A " + a(JW13, "2013 meta-analysis by Johnson and Whisman") + " of 59 samples and more than 14,000 people found women scored higher, and the authors note that the effect sizes were small in magnitude.",
            "Rumination is not only linked to depression. A " + a(ALDAO, "2010 meta-analysis") + " by Aldao, Nolen-Hoeksema and Schweizer combined 241 effect sizes from 114 studies of how people regulate emotions. It found that rumination had a large association with symptoms of anxiety, depression, eating and substance-related disorders, compared with medium to large for avoidance, problem solving and suppression, and small to medium for reappraisal and acceptance. A " + a(MCL, "2011 study") + " by McLaughlin and Nolen-Hoeksema, of 1,065 adolescents and 1,317 adults, found rumination helped explain why depression and anxiety so often occur together.",
            "It can also be shared. A 2002 study by A. J. Rose described " + a(ROSE, "co-rumination") + " between friends as extensively discussing and revisiting problems, speculating about problems, and focusing on negative feelings. In the study, of 608 children in grades 3 to 9, co-rumination was linked both to close, high-quality friendships and to symptoms of depression and anxiety. Talking a problem over with a friend can be support or a shared loop, depending on how it is done.",
        ]),
        ("What helps", [
            "If rumination keeps low mood going, interrupting it should help. The research points to a few approaches. Brief distraction with neutral or pleasant activities, which the " + a(RETHINK, "2008 review") + " mentions as one way of helping people prone to rumination. Shifting from abstract to concrete thinking, as in " + a(WM05, "Watkins’s experiments") + ". And therapies designed to target the habit directly.",
            "An early direct test was a small trial of rumination-focused cognitive behavioural therapy. In " + a(RFCBT, "a 2011 trial led by Watkins") + ", 42 people with residual depression were randomly allocated to usual treatment, or usual treatment plus up to 12 sessions of the therapy. The authors report that adding it significantly improved residual symptoms and remission rates, and that the effect was mediated by change in rumination.",
            "The trial is an early one. Its authors note that it lacked an attentional control group, so it cannot show whether the effects came from the specific content of the therapy or from therapy in general. It is a reason for optimism, not a settled result.",
            "HTML:" + K.callout("warn", "Not medical advice",
                "<p>This essay describes research. It is not a treatment plan. If low mood is lasting, getting worse or making daily life hard, a doctor or a qualified therapist is the right place to start.</p>"),
        ]),
        ("What this does and does not say", [
            "Read carefully, the research supports a clear but bounded claim. Repetitive, abstract, self-judging thought about feelings and problems predicts worse and longer low mood, worsens mood and problem solving in people already low in experiments, and is linked to anxiety as well as depression. Not all thinking about problems is harmful: reflection aimed at understanding, and concrete attention to what actually happened, look different. The evidence for rumination as a cause is strongest in the short term in the laboratory; over longer periods it is mostly prediction.",
            "The practical lesson is not to stop thinking about problems. It is to notice when thinking has stopped going anywhere, when it has become the same abstract questions about why and what it means, and to treat that as a signal to do something else for a while, or to switch to the concrete.",
            "This connects to other essays here. " + ESSAY46.replace(">what self-silencing", ">What self-silencing") + " looks at another inward pattern that often goes with low mood: holding back what you think and feel to keep the peace. " + ESSAY40.replace(">why reassurance", ">Why reassurance") + " describes a loop between partners that has a similar shape: going back again and again for an answer that does not settle anything. And " + ESSAY42 + " looks at another way psychologists measure inner habits through questionnaires, with similar limits.",
        ]),
    ],
    note=[
        "The original 1993 and 1995 experiments by Lyubomirsky and Nolen-Hoeksema are described through a review chapter by Lyubomirsky and Tkach. The questionnaire items are quoted from a reproduction of the scale, not the original paper.",
    ],
    faqs=[
        ("What is rumination in psychology?",
         "Repetitive thinking about your own feelings and problems: why you feel this way, what it means, and what will follow. Nolen-Hoeksema, Wisco and Lyubomirsky (2008) define it as thinking perseveratively about one's feelings and problems."),
        ("Does rumination cause depression?",
         "The evidence shows it predicts depression. In studies that followed people over time, rumination predicted more depression after an earthquake, after bereavement, and new episodes over a year. In experiments it worsened mood in people already low, but not in others. Prediction is not the same as proof of cause."),
        ("What is the difference between brooding and reflection?",
         "Brooding is passive, judgemental pondering of your mood, such as asking why you always react this way. Reflection is intentional pondering aimed at understanding and problem solving. Brooding goes with more depression; reflection went with more depression at the time but predicted less over time."),
        ("Is thinking about your problems always bad?",
         "No. Research by Watkins suggests the abstract kind, focused on causes, meanings and implications, is the unhelpful one, while concrete attention to what actually happened and how it felt is not, and can help problem solving."),
        ("Do women ruminate more than men?",
         "On average, slightly. A 2013 meta-analysis of more than 14,000 people found women scored higher on rumination, with small effect sizes. Some studies find the difference helps explain why women are more often depressed."),
    ],
    related=[
        ("what-self-silencing-is", "What self-silencing is", "Psychology"),
        ("what-attachment-styles-actually-measure", "What attachment styles actually measure, and what they cannot tell you", "Psychology"),
    ],
)

if __name__ == "__main__":
    newpost.build(POST)
