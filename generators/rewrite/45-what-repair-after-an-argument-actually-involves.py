#!/usr/bin/env python3
"""Essay 45 :: what-repair-after-an-argument-actually-involves  (Relationships)

Sources fetched and read on 2 Nov 2026: Gottman and Levenson 1992 and two
1999 papers (Levenson lab copies); Heyman and Slep 2001 (PMC); Stanley,
Bradbury and Markman 2000 (ProQuest abstract); Kim, Capaldi and Crosby 2007
(PMC); the UW 1998 release; the Gottman Institute research FAQ and blog
pages (definitions and practitioner advice, labelled as such); Lewicki,
Polin and Lount 2016 (EKU repository) with the APS summary; Fehr, Gelfand
and Nag 2010 (GGSC copy); McNulty's work via Live Science and the
University of Tennessee.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import newpost, postkit as K

EXT = ' target="_blank" rel="noopener"'
def a(url, text):
    return '<a href="%s"%s>%s</a>' % (url, EXT, text)

REPAIR = "https://www.gottman.com/blog/repair-attempts/"
HORSEMEN = "https://www.gottman.com/?p=1632"
SOOTHE = "https://www.gottman.com/?p=429"
GFAQ = "https://www.gottman.com/about/research/faq/"
REBOUND = "https://bpl.studentorg.berkeley.edu/docs/99-%20Rebound%20from%20marital%20conflict%20and%20divorce%20prediction.pdf"
STABLE = "https://bpl.studentorg.berkeley.edu/docs/58-How%20stable99.pdf"
GL92 = "https://bpl.studentorg.berkeley.edu/docs/41-Marital%20Processes92.pdf"
HEYMAN = "https://pmc.ncbi.nlm.nih.gov/articles/PMC1622921/"
STANLEY = "https://www.proquest.com/docview/219750581"
KIM = "https://pmc.ncbi.nlm.nih.gov/articles/PMC1828692/"
LEWICKI = "https://encompass.eku.edu/fs_research/92"
APS = "https://www.psychologicalscience.org/news/minds-business/effective-apologies-include-six-elements.html"
FEHR = "https://ggsc.berkeley.edu/images/uploads/Fehr_et_al_2010_The_road_to_forgiveness-_A_meta-analytic_synthesis_of_its_situational_and_dispositional_correlates.pdf"
LIVESCI = "https://www.livescience.com/9223-hold-grudge-spouse.html"
UTK = "https://our.tennessee.edu/2011/marriage-psychology"
PERPETUAL = "https://www.gottman.com/?p=446426884"

GOODNEWS = '<a href="/writing/what-your-partner-does-with-your-good-news">what your partner does with your good news</a>'
ESSAY40 = '<a href="/writing/why-reassurance-is-never-enough">why reassurance is never enough</a>'
ESSAY43 = '<a href="/writing/what-the-stoics-meant-by-what-is-up-to-us">what is up to us</a>'
ESSAY42 = '<a href="/writing/what-attachment-styles-actually-measure">the attachment research</a>'

POST = dict(
    slug="what-repair-after-an-argument-actually-involves", num=45, cat="Relationships", read="auto",
    date="2026-11-02",
    gen="rewrite/45-what-repair-after-an-argument-actually-involves.py",
    title="What repair after an argument actually involves, and what the famous numbers miss",
    dek="Couples argue. The research suggests most recover, and that many of their disagreements never get settled at all. What matters is how they come back, and some of the best-known numbers about it are weaker than they sound.",
    takeaway="Repair is whatever stops an argument escalating, and what happens afterwards to restore trust: owning your part, apologising, and, where it is safe, forgiving. In one laboratory study most couples rebounded from conflict, and in another, couples were still discussing the same type of issue four years later in most cases, so the aim is not to end disagreement but to recover from it. Apologies that acknowledge responsibility are judged most effective, and apology is one of the stronger correlates of forgiveness. Forgiveness has limits: in one researcher’s studies, forgiving was associated with the partner’s bad behaviour continuing, and he cautions against forgiving frequent or major offences. Several famous figures, including the 5 to 1 ratio and the very high divorce-prediction rates, describe particular studies and should not be treated as rules.",
    sections=[
        ("What repair is", [
            "Repair is anything that stops an argument from escalating, and whatever happens afterwards to restore trust: acknowledging your part, apologising, and, where it is safe, forgiving. The research suggests most couples do recover from conflict, and that many of their disagreements are never settled, so the skill that matters is coming back, not winning.",
            "HTML:" + K.takeaways([
                "In one laboratory study, most couples were able to rebound from the negativity of a conflict discussion.",
                "Couples followed for four years were mostly still discussing the same type of issue. Disagreement is often permanent; recovery is the skill.",
                "Apologies that acknowledge responsibility were judged most effective in one large study.",
                "Apology is one of the stronger correlates of forgiveness, but forgiving has been associated with a partner’s bad behaviour continuing.",
                "The 5 to 1 ratio and the famous divorce-prediction rates describe particular studies. They are not rules.",
            ]),
            "This essay starts with what the research actually found about conflict and recovery, checks some well-known numbers against their sources, and then looks at the two parts of repair that have the most evidence: apology and forgiveness.",
            "HTML:" + K.callout("definition", "Repair attempt",
                "<p>The term comes from the psychologist John Gottman. The " + a(REPAIR, "Gottman Institute") + ", the organisation that teaches his methods, defines it as any statement or action, silly or otherwise, that prevents negativity from escalating out of control.</p>"),
        ]),
        ("Most couples come back", [
            "Start with the encouraging finding, because it is the one most often left out. In a laboratory study by " + a(REBOUND, "John Gottman and Robert Levenson, published in 1999") + ", couples had a conflict discussion and then a conversation on a pleasant topic. The authors report that most couples were able to rebound from the negativity of marital conflict.",
            "" + a(REBOUND, "The same paper") + " found that how couples behaved in the pleasant conversation after the conflict classified later divorce slightly better than the conflict conversation itself: 92.7% correct compared with 82.6%. The authors are careful about what that means. The two conversations were always held in the same order, so, they write, they cannot draw conclusions about the conversations independent of their order.",
            "HTML:" + K.bars("Divorce classified correctly, by which conversation was used",
                [("Pleasant conversation after the conflict", 92.7, "92.7%"), ("The conflict conversation itself", 82.6, "82.6%")],
                source="Source: Gottman and Levenson (1999), Family Process 38. The two conversations were not counterbalanced, and these are classification rates within one sample."),
            "The useful idea in that result is modest and important: what happens after an argument carries information too. A fight is not only judged by how it went, but by whether the two people can come back to ordinary warmth afterwards.",
        ]),
        ("Many arguments are never settled", [
            "The second finding is less comfortable. In " + a(STABLE, "another 1999 paper") + ", Gottman and Levenson brought couples back to the laboratory four years after a first conflict discussion. Of 79 couples recruited, 42 returned. The authors found that couples were discussing the same type of issue 69% of the time, and new issues only 31% of the time. Their impression was that most marital issues could be called perpetual issues that were never reconciled.",
            "HTML:" + K.table("The 69% figure, and what it measured",
                ["What is often said", "What the study measured"],
                [["69% of couples’ problems are perpetual", "In 42 couples, the conflict discussed four years later was the same type of issue 69% of the time"],
                 ["Perpetual problems come from lasting differences in personality", "Not tested. The authors describe perpetual issues as their impression"],
                 ["Most couples’ problems can never be solved", "A small sample, two laboratory conversations, four years apart"]],
                source='Sources: left column, <a href="' + PERPETUAL + '" target="_blank" rel="noopener">a Gottman Institute article</a>; right column, <a href="' + STABLE + '" target="_blank" rel="noopener">Gottman and Levenson, Family Process 38 (1999)</a>.'),
            "Read at its proper size, the finding is still worth having. Many couples go on disagreeing about the same kinds of things for years, and that is not by itself a sign of failure. If the disagreement is likely to stay, the work is not to end it but to have it without damage, and to recover afterwards.",
        ]),
        ("What escalation looks like", [
            "Gottman’s best-known contribution is a description of the ways conflict turns corrosive, which he called the four horsemen. The " + a(HORSEMEN, "Gottman Institute’s definitions") + " are worth knowing because each has a repair that answers it.",
            "HTML:" + K.table("The four horsemen, as the Gottman Institute defines them",
                ["Pattern", "Definition"],
                [["Criticism", "An attack on a partner at the core of their character, as distinct from a complaint about a behaviour"],
                 ["Contempt", "Treating a partner with disrespect, mocking, ridicule or name-calling, from a position of moral superiority"],
                 ["Defensiveness", "Typically a response to criticism; in effect, a way of blaming the partner"],
                 ["Stonewalling", "Withdrawing from the interaction, shutting down and simply no longer responding"]],
                source='Source: <a href="' + HORSEMEN + '" target="_blank" rel="noopener">Gottman Institute, The Four Horsemen</a>. These are the organisation’s definitions rather than a peer-reviewed paper.'),
            "The same page describes contempt as the single greatest predictor of divorce, but cites no study for it there, so this essay does not repeat it as a finding. The definitions stand on their own as a useful vocabulary: a complaint about what someone did is answerable, an attack on who they are is not.",
        ]),
        ("The famous numbers, checked", [
            "Two numbers from this research are repeated everywhere. Both come from real studies. Neither means what it is usually taken to mean.",
            "The first is the 5 to 1 ratio. In " + a(GL92, "Gottman and Levenson’s 1992 study") + " of 73 married couples, first seen in 1983 and again in 1987, couples whose interactions became more positive over the discussion, whom the authors call regulated, showed positive to negative ratios of approximately 5.0 during a fifteen-minute discussion of a problem in their marriage. Couples on the other path had ratios around one, or below. That is a description of what was observed during conflict conversations. The authors proposed it as a possible set point needing further research, not as advice for daily life.",
            "The second is divorce prediction. Gottman’s group has reported very high rates of predicting which couples would divorce, and the " + a(GFAQ, "Gottman Institute’s own research FAQ") + " acknowledges that the 94% accuracy rate of divorce prediction has become a source of confusion. Other researchers have raised specific concerns.",
            "HTML:" + K.table("What the critics said",
                ["Source", "The concern"],
                [["Heyman and Smith Slep (2001)", "Prediction equations tested only on the data that built them look far better than they are. Using archival survey data, not Gottman’s, an equation with 90% initial accuracy had a positive predictive value of 21% when crossvalidated"],
                 ["Stanley, Bradbury and Markman (2000)", "Questioned the move from a 1998 newlywed study to advice about therapy, citing non-random samples, ambiguity about statistical tests and strong causal inferences from correlational data"],
                 ["Kim, Capaldi and Crosby (2007)", "In 85 at-risk couples, the major findings of Gottman and colleagues failed to replicate"]],
                source='Sources: <a href="' + HEYMAN + '" target="_blank" rel="noopener">Heyman and Slep, Journal of Marriage and the Family (2001)</a>; <a href="' + STANLEY + '" target="_blank" rel="noopener">Stanley, Bradbury and Markman (2000), abstract</a>; <a href="' + KIM + '" target="_blank" rel="noopener">Kim, Capaldi and Crosby, Journal of Marriage and Family (2007)</a>.'),
            "Heyman and Slep’s conclusion applies well beyond Gottman: results without crossvalidation should be interpreted with extreme caution, no matter how impressive they appear. None of this makes the observations worthless. It means they are findings from particular samples, not laws.",
        ]),
        ("The apology", [
            "When an argument has done damage, the most familiar repair is the apology. One well-cited study of what makes one work is " + a(LEWICKI, "a 2016 study by Lewicki, Polin and Lount") + ", which found that not all apologies are viewed equally.",
            "As " + a(APS, "the Association for Psychological Science summarised it") + ", the study tested six components across two experiments with 333 adults and 422 students. Lewicki is quoted as saying the most important component is an acknowledgement of responsibility; asking for forgiveness was the least effective.",
            "HTML:" + K.stages("The six components of an apology tested in the study", [
                ("01", "Expression of regret", "One of the six elements tested."),
                ("02", "Explanation of what went wrong", "One of the six elements tested."),
                ("03", "Acknowledgment of responsibility", "Rated the most important component."),
                ("04", "Declaration of repentance", "One of the six elements tested."),
                ("05", "Offer of repair", "One of the six elements tested."),
                ("06", "Request for forgiveness", "Rated the least effective component."),
            ], source='Sources: <a href="' + APS + '" target="_blank" rel="noopener">Association for Psychological Science (2016)</a>; <a href="' + LEWICKI + '" target="_blank" rel="noopener">Lewicki, Polin and Lount, Negotiation and Conflict Management Research (2016)</a>.'),
            "One caution about scope: these were experiments on apologies after a breach of trust, not studies of couples. The study also found apologies were seen as more effective after a failure of competence than after a failure of integrity. The finding that transfers most naturally is the central one. An apology that says, plainly, I did this and it was mine to do differently, does more than one that asks to be let off.",
        ]),
        ("Forgiveness, and its limits", [
            "A large body of evidence on forgiveness is pulled together in " + a(FEHR, "a 2010 meta-analysis by Fehr, Gelfand and Nag") + " in Psychological Bulletin, which pooled 175 studies and 26,006 participants. Apology was associated with forgiveness at about 0.42, and empathy for the person who caused the harm at about 0.51. Closeness, satisfaction and commitment in the relationship were also associated with forgiving, more weakly.",
            "HTML:" + K.table("What forgiveness is associated with",
                ["Factor", "Correlation with forgiveness"],
                [["Empathy towards the offender", "about 0.51"],
                 ["An apology", "about 0.42"],
                 ["Relationship satisfaction", "about 0.32"],
                 ["Relationship closeness", "about 0.28"],
                 ["Relationship commitment", "about 0.23"]],
                source='Source: <a href="' + FEHR + '" target="_blank" rel="noopener">Fehr, Gelfand and Nag, Psychological Bulletin 136(5), 2010</a>. Correlations across studies, not causal effects.'),
            "The authors conclude that features of the situation account for more of the variation in forgiveness than the personality of the person forgiving. That is a hopeful finding for repair: what happens after the harm, an apology among it, is associated with whether forgiveness follows.",
            "But forgiveness is not always the right repair. The psychologist James McNulty has studied what happens after it. In a week-long diary study of newlywed couples, reported by " + a(LIVESCI, "Live Science") + ", spouses who forgave their partner were almost twice as likely to report that their partner misbehaved again the next day. A four-year study, described by " + a(UTK, "the University of Tennessee") + ", found that aggression stayed relatively stable when a partner was more forgiving, and declined when a partner was less forgiving.",
            "HTML:" + K.callout("warn", "Where repair is the wrong frame",
                "<p>As the University of Tennessee summary puts it, the findings do not suggest forgiveness is always bad. McNulty himself says that forgiving frequent or major offences, such as verbal or physical abuse, is less advisable. If an argument involves threats, intimidation or violence, the question is not how to repair it, and it is worth talking to someone you trust or to a professional.</p>"),
        ]),
        ("Taking a break", [
            "One practical piece of advice is widely repeated and deserves its label. The " + a(SOOTHE, "Gottman Institute advises") + " that when someone in an argument becomes physiologically flooded, which it links to a heart rate above 100 beats per minute, the couple should take a break of around twenty minutes, which it says the body needs to settle.",
            "That is practitioner guidance from the organisation, not a finding from a paper linked here, and the figures should be read that way. The principle is sensible on its face. An argument continued in a state where neither person can listen is unlikely to produce a repair, and coming back to it later is itself a repair, provided someone does come back.",
        ]),
        ("Repair, step by step", [
            "Putting the evidence together gives a sequence that is less dramatic than most advice, and more realistic.",
            "HTML:" + K.decision("Where are we in this argument?",
                ("Is it still escalating?", [
                    ("Yes", "<p>Aim for anything that stops the escalation: a pause, a softer sentence, a break if someone is flooded, with a time agreed to come back.</p>"),
                    ("No", ("Was harm done that needs acknowledging?", [
                        ("Yes", "<p>Apologise for your part, starting with responsibility rather than with a request to be forgiven. Then leave forgiveness to the other person.</p>"),
                        ("No", "<p>Return to ordinary warmth. The research suggests that coming back is part of what counts, and that the disagreement itself may simply recur.</p>"),
                    ])),
                ])),
            "Two other essays on this site meet repair at different points. The apology is yours to give and the forgiveness is not, which is the distinction at the centre of " + ESSAY43 + ". And a repair conversation can quietly turn into the loop described in " + ESSAY40 + ", when what is being asked for after the argument is not repair but proof.", "The other half of the picture is what happens when things go well, which is the subject of " + GOODNEWS + ".",
            "Repair also looks different from person to person, and " + ESSAY42 + " is one way of thinking about why. But no score settles how two people should come back from a particular argument. That is decided in the next conversation, and in whether there is one.",
        ]),
    ],
    note=[
        "Where this essay relies on the Gottman Institute, it says so, and treats its pages as definitions and advice rather than as research findings. The numbers come from the papers, which are linked where they are used.",
    ],
    faqs=[
        ("What is a repair attempt?",
         "A term from John Gottman's work. The Gottman Institute defines it as any statement or action, silly or otherwise, that prevents negativity from escalating out of control."),
        ("Is the 5 to 1 ratio real?",
         "It comes from a real 1992 study of 73 couples, in which couples whose interaction stayed more positive showed positive to negative ratios of approximately 5.0 during a fifteen-minute conflict discussion. It describes what was observed in that setting. It is not a target for everyday life."),
        ("Can researchers predict divorce with 94% accuracy?",
         "Treat the claim with caution. The Gottman Institute's own research FAQ says the 94% figure has become a source of confusion. Other researchers have shown, on a different dataset, that prediction rates of this kind can fall sharply when tested on new data, and one study of 85 couples failed to replicate the major findings."),
        ("Do most couples' arguments ever get resolved?",
         "Often not. In one study of 42 couples seen four years apart, the conflict discussed the second time was the same type of issue 69% of the time. That suggests the important skill is recovering from disagreement rather than ending it."),
        ("Should you always forgive your partner?",
         "No. Apology and empathy are associated with forgiveness, and forgiveness can help repair. But in research by James McNulty, forgiving was associated with the partner’s bad behaviour continuing, and he says forgiving frequent or major offences, such as abuse, is less advisable."),
    ],
    related=[
        ("why-reassurance-is-never-enough", "Why reassurance is never enough, and what to do instead", "Relationships"),
        ("what-the-stoics-meant-by-what-is-up-to-us", "What the Stoics meant by what is up to us, and what it means for love", "Philosophy"),
    ],
)

if __name__ == "__main__":
    newpost.build(POST)
