#!/usr/bin/env python3
"""Essay 55 :: what-the-michelangelo-phenomenon-says  (Relationships)

Sources fetched and read on 4 Nov 2026: Rusbult, Finkel and Kumashiro 2009,
Current Directions in Psychological Science (full text, Northwestern copy;
APS abstract page); Rusbult, Kumashiro, Kubacka and Finkel 2009, JPSP
(full text, Northwestern and Goldsmiths copies); Buehler, Weidmann,
Kumashiro and Grob 2019 (Goldsmiths record); Buehler, Finkenauer and Grob
2020 (Utrecht full text); Eli Finkel's Rusbult archive and Science News
obituary (2010); Quote Investigator on the "chip away" attribution.
The 1999 paper that named the phenomenon is described through the 2009
review, because its abstract could only be read in a garbled index copy.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import newpost, postkit as K

EXT = ' target="_blank" rel="noopener"'
def a(url, text):
    return '<a href="%s"%s>%s</a>' % (url, EXT, text)

REVIEW = "https://faculty.wcas.northwestern.edu/eli-finkel/documents/47_RusbultFinkelKumashiro2009_CDir.pdf"
PART = "https://faculty.wcas.northwestern.edu/eli-finkel/documents/43_RusbultKumashiroKubackaFinkel2009_JPSP.pdf"
PARTGOLD = "https://eprints-gro.gold.ac.uk/5364/1/Rusbult%20et%20al%202009%20ideal%20similarity.pdf"
AGE = "https://research.gold.ac.uk/23164"
SWISS = "https://dspace.library.uu.nl/bitstream/1874/408072/1/1_s2.0_S0092656620300313_main.pdf"
ARCHIVE = "https://elifinkel.squarespace.com/rusbult/home"
SCINEWS = "https://www.sciencenews.org/?p=5659"
SELFEXP = "https://www.frontiersin.org/articles/10.3389/fpsyg.2019.02399/pdf"
QI = "https://quoteinvestigator.com/2014/06/22/chip-away/"

ESSAY40 = '<a href="/writing/why-reassurance-is-never-enough">why reassurance is never enough</a>'
ESSAY50 = '<a href="/writing/what-your-partner-does-with-your-good-news">what your partner does with your good news</a>'
ESSAY46 = '<a href="/writing/what-self-silencing-is">what self-silencing is</a>'

POST = dict(
    slug="what-the-michelangelo-phenomenon-says", num=55, cat="Relationships", read="auto",
    date="2026-11-04",
    gen="rewrite/55-what-the-michelangelo-phenomenon-says.py",
    title="What the Michelangelo phenomenon says about how partners shape each other",
    dek="Close partners change each other over time. A line of research named after a sculptor asks whether they help each other become who each wants to be, or something else. The answer turns on a detail that is easy to miss: whose ideal the shaping is aimed at.",
    takeaway="The Michelangelo phenomenon, first described in a 1999 paper by Drigotas, Rusbult and colleagues, describes how close partners shape each other’s selves. When a partner sees you in ways that fit your own ideal self and treats you in ways that bring out that ideal, you tend to move towards it, and both your personal well-being and the relationship tend to benefit. The key condition is that the affirmation is aimed at your ideals, not the partner’s: shaping someone towards the partner’s own ideal, which researchers call the Pygmalion phenomenon, is associated with worse outcomes. Most studies measure associations rather than run experiments, drawn mainly from American and Dutch samples, and an independent Swiss study in 2020 did not find affirmation predicting movement towards the ideal self.",
    sections=[
        ("What the Michelangelo phenomenon is", [
            "The Michelangelo phenomenon is the process by which close partners shape each other’s selves. Research suggests that when a partner sees and treats you in ways that fit the person you want to become, you tend to move towards that ideal, and both you and the relationship tend to do better, though one independent test did not find that link. The condition is that it is your ideal, not theirs.",
            "HTML:" + K.takeaways([
                "The phenomenon was first described in a 1999 paper by Drigotas, Rusbult and colleagues.",
                "Your ideal self is your own dreams and aspirations: the skills and traits you hope to have.",
                "Partners can affirm it in how they see you and in how they behave towards you.",
                "Affirmation is linked to moving towards your ideal and to better personal and couple well-being.",
                "Shaping someone towards the partner’s own ideal, the Pygmalion phenomenon, is linked to worse outcomes.",
                "Most studies measure associations rather than run experiments, and one independent study did not find the central link.",
            ]),
            "This essay sets out where the idea came from, what the research found and what it leaves open. It quotes the researchers’ own definitions, because the popular version of this idea tends to drop the condition that matters most.",
            "HTML:" + K.callout("definition", "The ideal self",
                "<p>" + a(REVIEW, "Rusbult, Finkel and Kumashiro") + " start from the observation that people have dreams and aspirations, and define the ideal self as “the constellation of skills, traits, and resources that an individual ideally wishes to acquire”.</p>"),
        ]),
        ("A sculptor’s image", [
            "The name comes from a description of how Michelangelo saw his work. As " + a(REVIEW, "Rusbult, Finkel and Kumashiro") + " put it in a 2009 review, “Michelangelo Buonarroti described sculpting as a process whereby the artist releases an ideal figure from the block of stone in which it slumbers.” The sculptor’s task, they write, is simply to chip away at the stone so as to reveal the ideal form. They cite the art historian Gombrich for this account, and illustrate it with one of Michelangelo’s unfinished captive figures.",
            "Two well-known lines are often attached to Michelangelo in this context: that he saw an angel in the marble and carved until he set him free, and that sculpting means chipping away everything that does not look like the statue. Neither has a verified source: " + a(QI, "Quote Investigator") + " found no substantive evidence that Michelangelo or any other great sculptor made the chip-away remark, and traces a similar angel story to an 1883 essay about an unnamed sculptor; and the researchers themselves paraphrase his idea rather than quoting him.",
            "In the research, the sculptor is the partner, and the stone is a person’s current self. A close partner, the review argues, can help release the ideal figure that is already there.",
        ]),
        ("The researchers and the first studies", [
            "The phenomenon was named in a 1999 paper by Drigotas, Rusbult, Wieselquist and Whitton in the Journal of Personality and Social Psychology, as the " + a(REVIEW, "2009 review") + " records in its references. The review summarises what those and later studies found: when a partner affirms the target’s ideal self, the target moves closer to it, and enjoys enhanced personal well-being, including greater life satisfaction and psychological health, as well as enhanced couple well-being, including greater adjustment and probability of persistence.",
            "According to " + a(ARCHIVE, "a tribute archive kept by her collaborator Eli Finkel") + ", she took her PhD at the University of North Carolina at Chapel Hill in 1978, taught there from 1986, and moved to VU University Amsterdam in 2004; her investment model is described there as one of the most well-known and influential theoretical frameworks in the area of close relationships. " + a(SCINEWS, "Science News") + " reported that she died on 27 January 2010, aged 57, and quoted the psychologist William Ickes calling the Michelangelo phenomenon the capstone to her brilliant career.",
        ]),
        ("Two kinds of affirmation", [
            "The research distinguishes two ways a partner can affirm someone’s ideal self. The " + a(REVIEW, "2009 review") + " defines them. Partner perceptual affirmation describes the extent to which a partner, consciously or unconsciously, perceives the person in ways that are compatible with the person’s ideal self. Partner behavioural affirmation describes the extent to which a partner, consciously or unconsciously, behaves in ways that elicit ideal-congruent behaviours from them.",
            "HTML:" + K.table("Perceptual and behavioural affirmation",
                ["", "Perceptual affirmation", "Behavioural affirmation"],
                [["What it is", "Seeing the person as compatible with their ideal", "Acting in ways that bring out their ideal"],
                 ["Example, for someone who wants to be more confident speaking", "Thinking of them as capable of it", "Giving them chances to speak, and responding well when they do"]],
                source='Definitions from <a href="' + REVIEW + '" target="_blank" rel="noopener">Rusbult, Finkel and Kumashiro (2009)</a>; the example is an illustration, not from a study.'),
            "Both can happen without anyone meaning them to. That is part of the point: partners shape each other through ordinary daily interaction, not only through deliberate encouragement.",
        ]),
        ("What the studies found", [
            "One study described in the " + a(REVIEW, "review") + " is unusually direct. The researchers videotaped married partners while they discussed a goal relevant to each person’s ideal self, and four months later asked whether the goals had been achieved. When partners were more affirming during the goal-relevant conversations, the people whose goals were discussed were more likely to achieve their ideal-self goals.",
            "A larger set of studies, published in " + a(PART, "a 2009 paper by Rusbult, Kumashiro, Kubacka and Finkel") + ", asked how this happens. Its abstract reports that across four studies employing diverse designs, when partners possess key elements of one another’s ideal selves, each affirms the other, each moves closer to his or her ideal self, and couple well-being is enhanced. The studies included " + a(PARTGOLD, "187 newly committed couples in the Chapel Hill community") + ", students at VU University Amsterdam, and a six-month study of 69 Northwestern University students in dating relationships.",
            "That six-month study also tracked who stayed together. Twenty-six participants broke up during the study, and the mean level of ideal similarity, how far each partner already had qualities from the other’s ideal self, was greater in relationships that persisted than in those that ended. The same paper reports that partner affirmation predicted significant change over time in people’s movement towards their ideal.",
            "HTML:" + K.table("Some of the evidence",
                ["Study", "Who", "Finding"],
                [["Goal conversations", "Married couples, followed up after four months", "More affirming partners, more ideal-self goals achieved"],
                 ["Ideal similarity, study 1", "187 newly committed couples", "Ideal similarity linked to affirmation, movement towards ideals and couple well-being"],
                 ["Six-month follow-up", "69 students in dating relationships", "Affirmation predicted change over time; ideal similarity higher in couples who stayed together"]],
                source='Sources: <a href="' + REVIEW + '" target="_blank" rel="noopener">Rusbult, Finkel and Kumashiro (2009)</a>; <a href="' + PARTGOLD + '" target="_blank" rel="noopener">Rusbult, Kumashiro, Kubacka and Finkel (2009)</a>.'),
        ]),
        ("Why shared ideals help", [
            "The 2009 paper on " + a(PART, "ideal similarity") + " asked a further question: what makes affirmation easier? Its answer is that it helps when a partner already has some of what you aspire to. The paper defines ideal similarity as the extent to which a partner possesses attitudes and traits that are part of one’s ideal self.",
            "On the " + a(PART, "paper’s account") + ", when partners possess key elements of one another’s ideal selves, each person affirms the other by eliciting important aspects of the other’s ideals. To illustrate, and this example is not from the paper: a partner who is already calm under pressure does not have to try to bring calm out in someone who wants it, because ordinary life together gives them chances to show it.",
            "The paper opens with a line often attributed to Elizabeth Barrett Browning: “I love you for the part of me that you bring out.” The " + a(PART, "authors themselves") + " note that its provenance is ambiguous, so it is best read as an epigraph that captures the idea, not as a sourced quotation.",
            "The six-month study adds the result about who stayed together: ideal similarity was higher in the relationships that lasted. That finding is about ideal similarity, not about affirmation as such, and it comes from one small sample of 69 students, but it fits the larger picture.",
        ]),
        ("Whose ideal: the Pygmalion problem", [
            "The most important finding is a condition. Affirmation only helps when it is aimed at the right target. The " + a(REVIEW, "2009 review") + " contrasts the Michelangelo phenomenon with what it calls the Pygmalion phenomenon: a partner who perceives and behaves towards the person in ways that are consistent with the partner’s own ideals. Research, the review says, reveals that the Pygmalion phenomenon is negatively associated with diverse indices of personal and couple well-being.",
            "The review’s conclusion is plain: “To be effective, partner affirmation must be oriented toward key elements of the target’s ideal self.” And: “In short, it is unwise to foist one’s own ideal-self representations onto others.”",
            "HTML:" + K.callout("warn", "Not a licence to change someone",
                "<p>The research does not say partners should mould each other. It says the opposite: helping someone become who they want to be is linked to good outcomes, and pushing them towards who you want them to be is linked to bad ones. The difference is whose dreams are being served.</p>"),
                    ]),
        ("What the research cannot yet say", [
            "The most important complication comes from outside the original group. A 2020 study by " + a(SWISS, "Bühler, Finkenauer and Grob") + " recruited 163 couples from the German-speaking parts of Switzerland and followed them over time, with 113 couples in the main analyses. It did not find the central link: the authors write that “we did not find partner perceptual affirmation and partner behavioral affirmation to serve as significant predictors” of movement towards the ideal self.",
            "The same study offers, as one possible explanation for the patterns it did find, that a satisfying relationship is a context that makes partners more likely to move toward their ideal self. Growth may help the relationship, the relationship may help growth, or both may follow from something else. The authors also note that their hypotheses were not preregistered. One study does not overturn a body of work, but it is the kind of independent test the idea most needs, and it did not simply confirm it.",
            "The samples have been fairly narrow. The " + a(PART, "original studies") + " drew mainly on American communities and universities and on students in Amsterdam. A " + a(AGE, "2019 study of 505 adults aged 18 to 90") + " notes that prior research has primarily focused on young adult samples; it found the model held across ages, with perceptual affirmation becoming more important for relationship satisfaction with increasing age.",
            "Some measures have been imperfect. The " + a(PART, "2009 ideal similarity paper") + " notes that some of its indices exhibited only moderate reliability, which means the true relationships may be stronger or weaker than the reported ones.",
            "The idea is also not limited to romantic partners. The " + a(REVIEW, "2009 review") + " reports a study of pairs of friends that found sizable across-friend associations, and lists open questions for future work: how clearly a person needs to have articulated their goals, whether affirmation works differently when it is conscious or unconscious, and how it applies to ought-self goals, which the review glosses as duties and responsibilities, as opposed to ideals.",
            "HTML:" + K.callout("note", "What was not found",
                "<p>Apart from the 2020 Swiss study above, the search for this essay found no published failed replication or major critique. That is not the same as there being none, and much of the supporting evidence comes from Rusbult and her collaborators.</p>"),
        ]),
        ("What this does and does not say", [
            "Read carefully, the research supports a promising idea with a sharp condition and an open question. In the original studies, when the shaping helped each person move towards their own ideals, both people and the relationship tended to do better, and when one partner pushed the other towards an image of their own, the opposite tended to follow. An independent test did not find the first link, so the idea is best held as well supported by its originators and not yet settled.",
            "The idea sits alongside another well-known account of how relationships change people. The self-expansion model, as a " + a(SELFEXP, "2019 review by Branand, Mashek and Aron") + " describes it, holds that “close relationships provide opportunities to expand the self”: each partner comes to experience the other’s resources, perspectives and identities as to some extent their own, the other being, in the model’s terms, included in the self. The Michelangelo research adds a direction to that expansion: towards the person each partner wants to be.",
            "In practice, that means knowing what the other person actually wants to become, rather than assuming, and noticing whether encouragement serves their aims or yours. Asking is part of affirming.",
            "Other essays here meet the idea at different points. " + ESSAY50.replace(">what your partner", ">What your partner") + " looks at one everyday moment where affirmation happens: how someone responds when good things happen to you. " + ESSAY46.replace(">what self-silencing", ">What self-silencing") + " describes the opposite of becoming more yourself in a relationship: holding back what you think to keep the peace. And " + ESSAY40 + " looks at what happens when one partner needs the other to keep confirming who they are.",
        ]),
    ],
    note=[
        "The 1999 paper that named the phenomenon is described through the 2009 review that summarises it, because only a garbled copy of its abstract could be read.",
    ],
    faqs=[
        ("What is the Michelangelo phenomenon?",
         "The process by which close partners shape each other's selves. When a partner sees and treats you in ways that fit your own ideal self, you tend to move towards that ideal, and personal and relationship well-being tend to improve. It was first described in a 1999 paper by Drigotas, Rusbult and colleagues."),
        ("What is the Pygmalion phenomenon in relationships?",
         "A partner perceiving and behaving towards you in ways that fit the partner's own ideals rather than yours. Research reviewed in 2009 found it negatively associated with personal and couple well-being."),
        ("What is partner affirmation?",
         "A partner seeing you in ways compatible with your ideal self (perceptual affirmation) and acting in ways that bring out ideal-congruent behaviour (behavioural affirmation). Both can happen without either person intending them."),
        ("Did Michelangelo say he saw the angel in the marble?",
         "There is no verified source for that line, or for the line about chipping away everything that does not look like the statue. The researchers paraphrase Michelangelo's view of sculpting through the art historian Gombrich rather than quoting him."),
        ("Does a supportive partner cause personal growth?",
         "Not proven. Some longitudinal studies found affirmation predicted later movement towards ideals, but an independent 2020 study of Swiss couples did not find that link, and suggested a satisfying relationship may itself make growth more likely."),
    ],
    related=[
        ("what-your-partner-does-with-your-good-news", "What your partner does with your good news, and why it may matter more than you think", "Relationships"),
        ("why-reassurance-is-never-enough", "Why reassurance is never enough, and what to do instead", "Relationships"),
    ],
)

if __name__ == "__main__":
    newpost.build(POST)
