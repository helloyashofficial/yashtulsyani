#!/usr/bin/env python3
"""Essay 70 :: what-the-four-horsemen-research-showed  (Relationships)

Sources fetched and read on 7 to 8 Nov 2026: Gottman Institute articles on
the four horsemen and their antidotes; Gottman and Levenson (2000), Journal
of Marriage and the Family, lab copy; Gottman and Levenson (2002), Family
Process, lab copy; University of Washington News (2000); Heyman and Slep
(2001), Journal of Marriage and the Family; abstract of a study of 136
satisfied newlywed couples (PsycINFO record dated 2011).
Not used: the popular claims that Gottman can predict divorce with over 90
per cent accuracy in minutes, except where a fetched paper states a figure.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import newpost, postkit as K

EXT = ' target="_blank" rel="noopener"'
def a(url, text):
    return '<a href="%s"%s>%s</a>' % (url, EXT, text)

GHORSE = "https://www.gottman.com/blog/the-four-horsemen-recognizing-criticism-contempt-defensiveness-and-stonewalling/embed/"
GANTI = "https://www.gottman.com/blog/the-four-horsemen-the-antidotes/"
GL2000 = "https://bpl.studentorg.berkeley.edu/docs/61-Timing of Divorce00.pdf"
GL2002 = "https://bpl.studentorg.berkeley.edu/docs/66-Two Factor Model02.pdf"
UW = "https://www.washington.edu/news/2000/09/11/marital-researchers-now-can-predict-not-only-which-couples-will-divorce-but-when-they-will-split/"
HS = "https://pmc.ncbi.nlm.nih.gov/articles/PMC1622921"
NEWLY = "https://www.healthymarriageinfo.org/news/why-do-even-satisfied-newlyweds-eventually-go-on-to-divorce"

ESSAY40 = '<a href="/writing/why-reassurance-is-never-enough">why reassurance is never enough</a>'
ESSAY45 = '<a href="/writing/what-repair-after-an-argument-actually-involves">what repair after an argument involves</a>'
ESSAY60 = '<a href="/writing/what-the-demand-withdraw-pattern-is">what the demand-withdraw pattern is</a>'
ESSAY66 = '<a href="/writing/what-the-impostor-phenomenon-is">what the impostor phenomenon is</a>'
ESSAY43 = '<a href="/writing/what-the-stoics-meant-by-what-is-up-to-us">what the Stoics meant by what is up to us</a>'

POST = dict(
    slug="what-the-four-horsemen-research-showed", num=70, cat="Relationships", read="auto",
    date="2026-11-08",
    gen="rewrite/70-what-the-four-horsemen-research-showed.py",
    title="What the four horsemen research showed, and how well it predicts divorce",
    dek="Criticism, contempt, defensiveness and stonewalling: John Gottman’s four horsemen are a widely known idea in relationship psychology, often repeated with the claim that he can predict divorce with near-perfect accuracy. The research behind them is real. The prediction claims are weaker than they sound.",
    takeaway="The four horsemen are criticism, contempt, defensiveness and stonewalling, four ways of handling conflict that the psychologist John Gottman found to predict divorce in his laboratory studies. In a 14-year study of 79 couples, Gottman and Robert Levenson found that negative affect during conflict, including the four horsemen, predicted early divorcing but not later divorcing; couples who divorced later were marked more by a lack of positive emotion. The paper’s abstract reports 93 per cent accuracy, but the models were not tested on a separate sample of couples. Richard Heyman and Amy Smith Slep showed in 2001 that when a divorce-prediction equation is tested on new couples, accuracy drops sharply. The horsemen are a useful description of conflict that tends to go badly, and the Gottman Institute pairs each with an antidote. They are not a reliable test of whether a particular couple will divorce.",
    sections=[
        ("What the four horsemen research showed", [
            "The four horsemen research showed that couples who met conflict with criticism, contempt, defensiveness and stonewalling were more likely to divorce, especially early. It did not show that these behaviours can tell, for any given couple, whether they will split. The famous high accuracy figures come from small samples and models not tested on new couples.",
            "HTML:" + K.takeaways([
                "The four horsemen are criticism, contempt, defensiveness and stonewalling.",
                "In a 14-year study of 79 couples, negative conflict predicted early, not later, divorce.",
                "Later divorce was linked more to a lack of positive emotion than to fighting.",
                "High accuracy figures came from small samples, not tested on new couples.",
                "A 2001 study showed prediction accuracy falls sharply on new couples.",
                "The horsemen describe risky conflict; they are not a divorce test.",
            ]),
            "This essay sets out what the four behaviours are, what the main studies found, and why the prediction claims need more care than they usually get. The practical side, how couples recover after a fight, is covered in the essay on " + ESSAY45 + ".",
            "HTML:" + K.callout("definition", "The four horsemen",
                "<p>Criticism, contempt, defensiveness and stonewalling, as described by the " + a(GHORSE, "Gottman Institute") + ". The name borrows the four horsemen of the apocalypse, a metaphor for the end of times in the New Testament, for communication styles that can predict the end of a relationship.</p>"),
        ]),
        ("The four behaviours", [
            "The " + a(GHORSE, "Gottman Institute") + " defines each one. Criticism “is an attack on your partner at the core of their character,” and it says the important thing is to learn the difference between expressing a complaint and criticizing. A complaint is about a specific behaviour; a criticism is about who the person is.",
            "Contempt is when we treat others with disrespect, mock them with sarcasm, ridicule, call them names. The Institute calls it the single greatest predictor of divorce. Defensiveness, it says, “is really a way of blaming your partner”: answering a complaint with a counter-complaint or an excuse.",
            "Stonewalling “occurs when the listener withdraws from the interaction, shuts down”. The Institute links it to being physiologically flooded, in a state where, in its words, “we may not even be in a physiological state where we can discuss things rationally.” That connects the horsemen to the body, not just to words.",
            "HTML:" + K.table("The horsemen and their antidotes",
                ["Horseman", "What it looks like", "Suggested antidote"],
                [["Criticism", "Attacking character, not behaviour", "Complain without blame, with a gentle start-up"],
                 ["Contempt", "Mockery, sarcasm, disrespect", "Build a culture of appreciation and respect"],
                 ["Defensiveness", "Blaming back, making excuses", "Accept responsibility, even for part of the conflict"],
                 ["Stonewalling", "Withdrawing, shutting down", "Take a break and practise physiological self-soothing"]],
                source='Sources: <a href="' + GHORSE + '" target="_blank" rel="noopener">Gottman Institute, the four horsemen</a>; <a href="' + GANTI + '" target="_blank" rel="noopener">Gottman Institute, the antidotes</a>.'),
        ]),
        ("The 14-year study", [
            "The best-known evidence comes from a study by John Gottman and Robert Levenson, " + a(GL2000, "published in 2000") + " in the Journal of Marriage and the Family. According to " + a(UW, "University of Washington News") + ", they followed 79 couples from Bloomington, Indiana, from 1983, for 14 years, and 22 of them, 28 per cent, divorced.",
            "Each couple had two recorded conversations in the laboratory, described in the paper as an events-of-the-day discussion after being apart for at least eight hours, and a discussion of a problem area of continuing disagreement. The researchers coded the emotions they showed, including the four horsemen.",
            "The key finding was that timing mattered. In the paper’s words, “Negative affect during conflict predicted early divorcing, but it did not predict later divorcing.” The discussion notes that negative codes such as contempt, criticism, defensiveness, and stonewalling were successful in predicting divorce, but these predicted the divorces that came early. Couples who divorced later were distinguished more by a lack of positive affect.",
            "The numbers behind this were small. According to the " + a(GL2000, "paper") + ", nine couples divorced early, on average 7.4 years after marrying, and thirteen later, on average 13.9 years after. A model using the negative interaction codes, including the four horsemen, classified 83.5 per cent of couples correctly for early divorce; one based on positive affect classified 88.5 per cent correctly for later divorce, and 75 per cent using the positive interaction codes alone. The paper also reports 95 per cent accuracy in telling early from later divorcers, but among the divorced couples only.",
            "Gottman described the two groups to " + a(UW, "University of Washington News") + " in vivid terms. “Couples in the early divorce group are openly contesting and fighting with each other,” he said, while those who split later, often when their children were young teenagers, were cool, suppressed their emotions, and seemed, in his words, “alienated and avoidant.”",
        ]),
        ("Two ways marriages end", [
            "Gottman and Levenson followed this up in a " + a(GL2002, "2002 paper in Family Process") + " that tried to build a model of when couples divorce. Its sample was the 21 couples of the 79 who divorced over 14 years. One factor, the amount of unregulated volatile positive and negative affect in the marriage, predicted a short marriage for the divorcing couples. The other, roughly, was emotional flatness: little affect of any kind, linked with later divorce.",
            "The authors were explicit that this was exploratory. The abstract describes it as an attempt to create a post hoc model, and the analyses rested on only 21 divorces. That is a hypothesis, not a settled finding.",
            "The two-route picture is still useful, because it corrects a common reading of the horsemen. A marriage does not have to be full of fighting to be in trouble. One that has gone quiet and distant can be at risk too, for different reasons, and the four horsemen will not show it.",
        ]),
        ("The 93 per cent claim", [
            "The abstract of the " + a(GL2000, "2000 paper") + " states: “The model predicted divorce with 93% accuracy.” Figures of this kind are behind the widely repeated idea that Gottman can tell which couples will divorce. The results section reports several analyses with their own classification rates, and no test on a separate sample of couples: each rate comes from the same couples the model was built on.",
            "That matters, because a model fitted to a set of data will almost always describe that data better than it predicts new cases. The paper also notes a limitation of its design: the order of conversations was not randomized or counterbalanced.",
            "In 2001, " + a(HS, "Richard Heyman and Amy Smith Slep") + " tested this problem directly in the same journal, in a paper titled The Hazards of Predicting Divorce Without Crossvalidation. They wrote that studies suggest couples’ eventual divorce can be very accurately predicted, but that accuracy and predictive value drops precipitously during crossvalidation, and concluded that results without crossvalidation should be interpreted with extreme caution. They also noted that, as of their writing, no published study predicting divorce with general population couples had cross-validated its results.",
            "Their target was partly an earlier Gottman study, published in 1998, which they said had received an extraordinary degree of professional and popular attention. That study reported 80 per cent correct divorce prediction, but, Heyman and Slep argued, did not break the figure down into how many divorcing and non-divorcing couples it caught, rested on only 60 couples, a sample small enough to raise concerns about overfitting.",
            "Their own demonstration, using survey data rather than Gottman’s laboratory design, makes the point concrete. An equation built on one half of their sample classified 90 per cent of couples correctly. Applied to the other half, it classified 69 per cent correctly, and of the couples it flagged as heading for divorce, only 29 per cent actually fitted that description. Reweighted to a more realistic 16 per cent divorce rate, that figure fell to about 21 per cent.",
            "HTML:" + K.compare("Two ways to read the prediction figures", [
                ("Same-sample accuracy", ["Shows the measures are strongly related to divorce"], ["Not tested on new couples, so it likely overstates"], "Describes the sample."),
                ("New-sample accuracy", ["The honest test of a prediction"], ["Much lower in Heyman and Slep’s demonstration"], "What a couple can rely on."),
            ], source='Sources: <a href="' + GL2000 + '" target="_blank" rel="noopener">Gottman and Levenson (2000)</a>; <a href="' + HS + '" target="_blank" rel="noopener">Heyman and Slep (2001)</a>.'),
        ]),
        ("Base rates and false alarms", [
            "Heyman and Slep also raised a subtler problem. Even a test that is right 80 per cent of the time will flag many couples wrongly if divorce is not very common in the group being tested. Applying an 80 per cent sensitivity and specificity to a 16 per cent divorce rate, they estimated that only about 43 per cent of couples told they were likely to divorce would actually be on that path; a couple given that verdict would be wrong more than half the time.",
            "This is not a criticism of the horsemen as a description. Heyman and Slep said their own equation was clearly capturing real relations among the variables. It is a criticism of turning that relationship into a forecast about one couple. The horsemen tell you something about risk on average, not about destiny. Heyman and Slep put the distinction directly about their own equation: it “does not hold the key to answering the question ‘Who will get divorced?’”",
        ]),
        ("Other evidence on conflict", [
            "The broad idea that how couples handle conflict matters has support beyond Gottman’s laboratory. One study, " + a(NEWLY, "summarised in its abstract") + ", identified 136 couples reporting stably high levels of relationship satisfaction in the first four years of marriage and compared those who had divorced by the ten-year follow-up with those who stayed married.",
            "Even among these happy couples, those who later divorced had displayed more negative communication, emotion, and social support as newlyweds. No significant differences were found in the other areas the study looked at, in satisfaction, or in positive behaviours. The authors suggest that these couples’ many strengths may mask their potent interpersonal liabilities: feeling good about a relationship does not guarantee that conflict is being handled well.",
        ]),
        ("What to do with the horsemen", [
            "Used as a checklist for one’s own behaviour, the horsemen are practical. The " + a(GANTI, "Gottman Institute") + " pairs each with an antidote: complain without blame by using a soft or gentle start-up; build a culture of appreciation and respect; accept responsibility, even if only for part of the conflict; and, when flooded, practise physiological self-soothing, which it says should mean a break of at least twenty minutes. Its other article on the horsemen suggests using that time to do something alone that soothes you, and returning to the conversation once ready.",
            "Its suggested wording is plain. In place of stonewalling: “I’m feeling overwhelmed and I need to take a break. Can you give me twenty minutes and then we can talk?” The Institute also describes a magic ratio of five or more positive interactions for every one negative interaction, a figure it presents as necessary for a relationship to succeed.",
            "HTML:" + K.callout("warn", "A note on using it",
                "<p>Spotting a horseman in a partner can become a new kind of criticism. The research describes patterns between two people, measured on average across many couples. It is better used to notice one’s own part in a pattern than as a verdict on someone else, and it is not a substitute for help from a qualified couples therapist where conflict is serious.</p>"),
        ]),
        ("What this does and does not say", [
            "Read carefully, the four horsemen research shows that criticism, contempt, defensiveness and stonewalling during conflict are associated with divorce, especially early divorce, and that a lack of warmth matters too. It does not show that anyone can predict, with 90 per cent accuracy, whether a particular couple will stay together. The honest version is less dramatic and more useful: these are patterns worth changing, not signs of fate.",
            "Other essays here look at the same ground from different angles. " + ESSAY60.replace(">what the demand", ">What the demand") + " describes one pattern in which one partner pushes and the other withdraws, close kin to stonewalling. " + ESSAY40.replace(">why reassurance", ">Why reassurance") + " looks at a loop in which asking for comfort keeps the worry going. And " + ESSAY43 + " sets out an older way of separating what is in our power in a conflict from what is not.",
        ]),
    ],
    note=[
        "The 93 per cent figure is quoted from the 2000 paper’s abstract. The descriptions of the horsemen and antidotes are the Gottman Institute’s; the Institute teaches Gottman’s methods commercially.",
    ],
    faqs=[
        ("What are the four horsemen in relationships?",
         "Criticism, contempt, defensiveness and stonewalling, four ways of handling conflict that John Gottman’s research linked to divorce. The Gottman Institute calls contempt the single greatest predictor."),
        ("Can Gottman really predict divorce with over 90 per cent accuracy?",
         "Not in the way the claim suggests. High figures came from small samples and were not tested on new couples. When a prediction equation was tested on new couples in a 2001 study, accuracy dropped sharply."),
        ("Do the four horsemen predict all divorces?",
         "No. In a 14-year study, negative conflict predicted early divorce but not later divorce. Couples who split later were marked more by a lack of positive emotion than by fighting."),
        ("What are the antidotes to the four horsemen?",
         "According to the Gottman Institute: a gentle start-up instead of criticism, a culture of appreciation instead of contempt, taking responsibility instead of defensiveness, and self-soothing breaks instead of stonewalling."),
        ("What is stonewalling?",
         "Withdrawing from a conversation and shutting down. The Gottman Institute links it to being physiologically flooded and suggests a break of at least twenty minutes."),
    ],
    related=[
        ("what-repair-after-an-argument-actually-involves", "What repair after an argument actually involves, and what the famous numbers miss", "Relationships"),
        ("what-the-demand-withdraw-pattern-is", "What the demand-withdraw pattern is, and why it feeds itself", "Relationships"),
    ],
)

if __name__ == "__main__":
    newpost.build(POST)
