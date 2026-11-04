#!/usr/bin/env python3
"""Essay 46 :: what-self-silencing-is  (Psychology)

Sources fetched and read on 3 Nov 2026: Jack and Ali (OUP blog extract,
2010); the STSS scale record (Jack and Dill 1992); a published table quoting
an STSS item; Ussher and Perz 2010; Lutz-Zois et al. 2013; Harper, Dickson
and Welsh 2006 (abstract); Little et al. 2011; Shulman et al. 2018;
MacDonald 2001 (dissertation); Butler et al. 2003; Gross and John 2003;
Impett et al. 2012 and 2014; Le and Impett 2013; Sahdev 2026 (preprint,
labelled). The 2021 meta-analysis could not be opened, so none of its
figures are used.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import newpost, postkit as K

EXT = ' target="_blank" rel="noopener"'
def a(url, text):
    return '<a href="%s"%s>%s</a>' % (url, EXT, text)

JACK = "https://blog.oup.com/2010/03/silencing-the-self/"
STSS = "https://emerge.ucsd.edu/?p=25862"
ITEM = "https://pmc.ncbi.nlm.nih.gov/articles/PMC4135315/table/T1"
USSHER = "https://researchers.westernsydney.edu.au/en/publications/gender-differences-in-self-silencing-and-psychological-distress-i/"
LUTZ = "https://ecommons.udayton.edu/psy_fac_pub/9"
HARPER = "https://ojp.gov/ncjrs/virtual-library/abstracts/self-silencing-and-rejection-sensitivity-adolescent-romantic"
LITTLE = "https://digitalcommons.oberlin.edu/faculty_schol/2565"
SHULMAN = "https://cris.haifa.ac.il/en/publications/changes-in-self-silencing-from-adolescence-to-emerging-adulthood-/"
MACD = "https://ruor.uottawa.ca/items/45a26f1c-be6b-4423-b39d-d28a13c298a9"
BUTLER = "https://experts.arizona.edu/en/publications/the-social-consequences-of-expressive-suppression/"
GROSS = "https://pubmed.ncbi.nlm.nih.gov/12916575/"
IMPETT12 = "https://sources.mandala.library.virginia.edu/node/22871"
IMPETT14 = "https://labsites.rochester.edu/lelab/wp-content/uploads/2020/06/Impett-et-al.-2014-The-costs-of-perceived-partner-suppression-during-relationship-sacrifice.pdf"
LE13 = "https://www.psychologicalscience.org/journals/psychological-science/0956797613475365/"
SAHDEV = "https://www.researchsquare.com/article/rs-10798157"

RUMINATION = '<a href="/writing/what-rumination-is">what rumination is</a>'
ESSAY42 = '<a href="/writing/what-attachment-styles-actually-measure">what attachment styles actually measure</a>'
ESSAY40 = '<a href="/writing/why-reassurance-is-never-enough">the essay on reassurance seeking</a>'
ESSAY43 = '<a href="/writing/what-the-stoics-meant-by-what-is-up-to-us">what is up to us</a>'
SHRINK = '<a href="/books/nobody-has-to-shrink">Nobody has to shrink</a>'

POST = dict(
    slug="what-self-silencing-is", num=46, cat="Psychology", read="auto",
    date="2026-11-03",
    gen="rewrite/46-what-self-silencing-is.py",
    title="What self-silencing is, and what keeping the peace can cost",
    dek="Not saying the thing, so that the evening stays calm, can look like kindness. Psychologists have a name and a scale for it, and the research on what it does over time is clearer than the advice that circulates about it.",
    takeaway="Self-silencing means holding back your own thoughts, feelings and needs to avoid conflict and keep a relationship. The idea comes from Dana Crowley Jack, who built it from depressed women's own accounts and measured it with a 31-item scale. The research links it to depression, mostly through correlations measured at one time, with some studies following people over months or years. It is not only a women's pattern: men often score as high or higher, though the silence can mean something different to them. In couples, hiding what you feel during sacrifices tracks with lower satisfaction later, but not for everyone. The useful distinction is between choosing not to raise something and routinely making yourself smaller to keep the peace.",
    sections=[
        ("What self-silencing is", [
            "Self-silencing is holding back your own thoughts, feelings and needs in a close relationship to avoid conflict or the risk of losing the other person. The research treats it as a pattern of beliefs about how to keep a relationship, measured by a questionnaire, and it has been linked repeatedly to depression.",
            "HTML:" + K.takeaways([
                "The idea comes from the psychologist Dana Crowley Jack, who built it from depressed women’s own accounts.",
                "It is measured by a 31-item questionnaire with four parts, from judging yourself by others’ standards to keeping a public self apart from a private one.",
                "The research links it to depressive symptoms; most of that evidence is correlational, and some of it follows people over time.",
                "Men often score as high as women or higher. What the silence means to them can differ.",
                "Hiding what you feel when you give something up for a partner tracks with lower satisfaction later, though not for everyone.",
            ]),
            "This essay sets out where the idea came from, what the questionnaire measures, what the evidence does and does not show, and where holding back is ordinary judgement rather than a problem.",
            "HTML:" + K.callout("definition", "Self-silencing",
                "<p>Not saying, doing or showing things you think would contradict a partner’s wishes, so as to protect the relationship. In Dana Crowley Jack’s account, it rests on beliefs about how intimacy has to be kept, not on a single decision to stay quiet.</p>"),
        ]),
        ("Where the idea came from", [
            "The concept comes from the psychologist Dana Crowley Jack, who developed it from depressed women’s own accounts of their relationships. In " + a(JACK, "a blog extract by Jack and Alisha Ali") + ", co-editors of Silencing the Self Across Cultures (2010), Jack describes women who would silence or suppress certain thoughts, feelings and actions that they thought would contradict their partner’s wishes, and argues that these beliefs create vulnerability to depression by directing women to defer to the needs of others.",
            "To study the idea, Jack and Dill published the Silencing the Self Scale in 1992. As " + a(STSS, "the scale’s record") + " sets out, it has 31 statements, each rated on a five-point scale from disagree to agree, giving a total between 31 and 155. Jack and Ali note that the statements came directly from depressed women’s accounts and were worded to be gender neutral.",
            "HTML:" + K.table("The four parts of the Silencing the Self Scale",
                ["Subscale", "Items", "What it is about"],
                [["Externalized self-perception", "1 to 6", "Judging yourself by outside standards"],
                 ["Care as self-sacrifice", "7 to 15", "Putting others’ needs before your own"],
                 ["Silencing the self", "16 to 24", "Holding back what you think or feel to protect the relationship"],
                 ["Divided self", "25 to 31", "An outward self that differs from what you feel inside"]],
                source='Sources: <a href="' + STSS + '" target="_blank" rel="noopener">scale record (Jack and Dill, Psychology of Women Quarterly 16, 1992)</a>; <a href="' + JACK + '" target="_blank" rel="noopener">Jack and Ali (2010)</a>. Descriptions summarised.'),
            "One item, as quoted in " + a(ITEM, "a published study that used the scale") + ", gives the flavour: “I don’t speak my feelings in an intimate relationship when I know they will cause disagreement.” Most people will recognise that sentence as true of themselves sometimes. The scale is about how often, and how much it organises the relationship.",
        ]),
        ("What the research links it to", [
            "The central finding is an association with depression. Across many studies, people who score higher on self-silencing tend to report more depressive symptoms. That is a correlation, and on its own it cannot say which comes first: silence could feed low mood, low mood could make people quieter, or both could share a cause.",
            "Some studies follow people over time, which helps. In " + a(LITTLE, "a study of 209 adolescent dating couples") + ", published in 2011, self-silencing predicted increases in depressive symptoms from the first measurement to the second. That points in one direction for that group. It is one study, in young couples, and it does not rule out the reverse.",
            "Much of the rest of the evidence is measured at a single point. A " + a(SAHDEV, "2026 systematic review of studies in women") + ", posted as a preprint that has not yet been peer reviewed, describes the evidence as converging on a consistent positive relationship, and notes that most studies are cross-sectional, which limits causal inference.",
            "HTML:" + K.callout("note", "What this essay leaves out",
                "<p>A 2021 meta-analysis pooled studies of self-silencing and depression. Its published abstract could not be opened for this essay, and its figures circulate mainly on secondary sites, so none of them are repeated here.</p>"),
        ]),
        ("Not only women", [
            "Because the idea began with women’s accounts, it is often described as a women’s pattern. The scores do not bear that out. In " + a(USSHER, "a 2010 study of informal cancer carers") + " by Ussher and Perz, with 329 women and 155 men, the men reported greater self-silencing than the women. The women reported more depression and anxiety, and both were correlated with self-silencing.",
            "Other studies agree on the scores and add detail. In " + a(HARPER, "a study of 211 adolescents and their partners") + ", boys reported more self-silencing than girls. In " + a(LUTZ, "a 2013 study of 247 college students") + ", women scored higher on judging themselves by outside standards, men scored higher on care as self-sacrifice, and that self-sacrifice subscale was negatively correlated with depression in men and unrelated to it in women.",
            "HTML:" + K.table("Self-silencing and gender, as reported",
                ["Study", "Who", "Finding"],
                [["Ussher and Perz (2010)", "329 women and 155 men caring for someone with cancer", "Men reported more self-silencing; women reported more depression and anxiety"],
                 ["Harper, Dickson and Welsh (2006)", "211 adolescents and their partners", "Boys reported more self-silencing than girls"],
                 ["Lutz-Zois and colleagues (2013)", "247 college students", "Women higher on outside standards; men higher on self-sacrifice"]],
                source='Sources: <a href="' + USSHER + '" target="_blank" rel="noopener">Ussher and Perz, Psychology of Women Quarterly 34 (2010)</a>; <a href="' + HARPER + '" target="_blank" rel="noopener">Harper et al., Journal of Youth and Adolescence 35 (2006)</a>; <a href="' + LUTZ + '" target="_blank" rel="noopener">Lutz-Zois et al., Personality and Individual Differences 55 (2013)</a>.'),
            "What may differ is the meaning. In interviews in the Ussher and Perz study, women tended to describe silencing themselves as something they had to do to cope, while men tended to describe it as an ordinary part of being a man, and saw voicing their own needs as weakness. The same score can sit on different reasons.",
        ]),
        ("What silence does inside a relationship", [
            "The closest evidence on couples comes from research on hiding emotions. In " + a(IMPETT12, "a study by Impett and colleagues") + ", couples took part in a laboratory session, kept a diary for fourteen days and were followed up three months later. People who suppressed their emotions when they made a sacrifice for their partner reported decreases in relationship satisfaction, and more thoughts about breaking up three months later. In the laboratory and diary parts of the study, feeling less authentic helped explain those costs.",
            "A " + a(IMPETT14, "later study of 80 couples") + " looked at the other side. When people believed their partner was hiding feelings while making a sacrifice, they saw that partner as less authentic, and that went with poorer relationship quality three months on.",
            "Self-silencing as Jack defined it has also been followed over years. In " + a(SHULMAN, "a study") + " that followed 144 adolescents from 16 to 23, self-silencing at 16 predicted more concealment in relationships seven years later, and changes in self-silencing were related to later concealment, partner support and relationship certainty.",
            "Couples have been studied too. In " + a(MACD, "a 2001 doctoral study of 85 couples") + ", silencing one’s needs and feelings within the relationship was associated with an increase in women’s depressive symptoms.",
            "HTML:" + K.table("Hiding what you feel: what the studies measured",
                ["Study", "Design", "Finding"],
                [["Impett and colleagues (2012)", "Couples; lab session, 14-day diary, 3-month follow-up", "Suppression during sacrifice predicted lower satisfaction and more thoughts of breaking up"],
                 ["Impett and colleagues (2014)", "80 couples", "A partner seen as suppressing was seen as less authentic; poorer relationship quality 3 months later"],
                 ["Shulman and colleagues (2018)", "144 adolescents followed from 16 to 23", "Self-silencing at 16 predicted more concealment at 23"],
                 ["Butler and colleagues (2003)", "Pairs of women who had not met, discussing an upsetting topic", "Suppression disrupted the conversation and raised the other person’s blood pressure"]],
                source='Sources as linked in the text. <a href="' + BUTLER + '" target="_blank" rel="noopener">Butler et al., Emotion 3 (2003)</a>.'),
            "It is easy to read the last row as being about couples. It is not. In " + a(BUTLER, "the 2003 study by Butler and colleagues") + ", the pairs were strangers. Suppression disrupted communication, reduced rapport and magnified blood pressure responses in the suppressor’s partner in the conversation. It is a striking finding about what hiding emotion does to an exchange, but it was measured between people who had just met. A " + a(GROSS, "2003 set of studies by Gross and John") + " found that habitually suppressing emotion was associated with worse interpersonal functioning and lower well-being.",
        ]),
        ("When holding back is not a mistake", [
            "None of this means every unsaid thought is a wound. Ordinary tact, choosing a better moment and letting small things go are part of living with anyone. The research is about a pattern, not a single silence.",
            "There is also a real exception. In " + a(LE13, "a study by Le and Impett") + ", people with a more interdependent sense of self, who define themselves more through their relationships, experienced boosts in well-being and relationship quality when they suppressed negative emotions during a sacrifice. The authors describe this as a condition under which suppression may be beneficial.",
            "HTML:" + K.decision("Is this a silence I am choosing, or one I am keeping?",
                ("Would saying it put you or someone else at risk?", [
                    ("Yes", "<p>Then silence may be protecting you, and this essay is not the right frame. Talk to someone you trust outside the relationship.</p>"),
                    ("No", ("Is it something small that you can genuinely let go of?", [
                        ("Yes", "<p>That is ordinary judgement. Not every reaction needs to be said.</p>"),
                        ("No", ("Have you held back things like this many times before?", [
                            ("Yes", "<p>That is the pattern the research describes. Consider saying one true thing about it, plainly and once.</p>"),
                            ("No", "<p>Then it is a single choice. Notice whether it stays a single choice.</p>"),
                        ])),
                    ])),
                ])),
            "The distinction that matters, then, is between choosing not to raise something and routinely making yourself smaller to keep the peace. The first is judgement. The second is what the studies keep finding costs something.",
        ]),
        ("Silence and reassurance, two ends of one fear", [
            "Self-silencing has an opposite that this site has already written about. " + ESSAY40.replace(">the essay on reassurance seeking<", ">The essay on reassurance seeking<") + " describes asking again and again for proof that a relationship is safe. Self-silencing tries to keep it safe by asking for nothing at all. One says too much and the other too little, and both are trying to manage the other person’s reaction before it happens.",
            "That is where an older idea is useful. In the language of " + ESSAY43 + ", what you say and how you say it are yours; how the other person responds is not. Silencing yourself to control that response puts effort on the side of the line where it cannot work, and gives up the part that was yours.",
            "The research on attachment points the same way. Fear of rejection is one of the two dimensions described in " + ESSAY42 + ", and self-silencing is one of the things that fear can lead people to do. A score does not decide the behaviour; the behaviour is the part that can change.",
            "Silencing is about what goes unsaid. Its inward counterpart, going over the same feelings and problems without getting anywhere, is the subject of " + RUMINATION + ".",
        ]),
        ("What to try instead", [
            "This essay found no tested intervention for self-silencing, so what follows is drawn from the findings above rather than proven by them. The most consistent thread is authenticity: in the Impett studies, hiding emotion made people feel less authentic (2012) and made partners seem less authentic (2014).",
            "HTML:" + K.stages("Speaking without making it a crisis", [
                ("01", "Notice the pattern", "Not every silence, just the ones that repeat: the same need, unsaid, again."),
                ("02", "Say one true thing", "Small and specific: what you feel and what you would like, not a case for the prosecution."),
                ("03", "Say it once", "Repeating it for reassurance is the opposite trap. Let the answer be the other person’s."),
                ("04", "Notice how it lands", "See how a stated need is received. If every one is met with punishment, that is information too."),
            ], source="The essay’s suggestions, drawn from the studies cited; not a tested intervention."),
            SHRINK + ", one of the books on this site, turns the mirror both ways, as its own page puts it: a chapter for the person being made small, and a harder one for the person doing it. This essay is the research underneath one half of that: what it costs, over time, to keep making yourself smaller so that nothing has to be said.",
        ]),
    ],
    note=[
        "Where a finding comes from one study, a single age group, strangers rather than couples, a dissertation or a preprint, the essay says so where it is used. One relevant meta-analysis is not cited because its abstract could not be checked.",
    ],
    faqs=[
        ("What is self-silencing?",
         "Holding back your own thoughts, feelings and needs in a close relationship to avoid conflict or the risk of losing the other person. The idea comes from the psychologist Dana Crowley Jack and is measured with the 31-item Silencing the Self Scale."),
        ("Is self-silencing linked to depression?",
         "Yes, consistently, though mostly through correlations measured at one time. One study of 209 adolescent dating couples found that self-silencing predicted later increases in depressive symptoms, which suggests a direction for that group but does not rule out the reverse."),
        ("Do men self-silence too?",
         "Yes. Men scored higher on self-silencing in two studies, including one of 155 men and 329 women caring for someone with cancer, and higher on one part of the scale in a third. Interviews in that study suggested the silence can mean something different to men than to women."),
        ("Is it always bad to hide your feelings from a partner?",
         "No. Ordinary tact and choosing your moment are part of any relationship, and one study found that people with a more interdependent sense of self benefited from suppressing negative emotions during a sacrifice. The costs show up when hiding becomes a habit, especially around giving things up for a partner."),
        ("What is the Silencing the Self Scale?",
         "A 31-item questionnaire published by Jack and Dill in 1992. It has four parts: judging yourself by outside standards, care as self-sacrifice, silencing the self, and a divided self."),
    ],
    related=[
        ("what-attachment-styles-actually-measure", "What attachment styles actually measure, and what they cannot tell you", "Psychology"),
        ("why-reassurance-is-never-enough", "Why reassurance is never enough, and what to do instead", "Relationships"),
    ],
)

if __name__ == "__main__":
    newpost.build(POST)
