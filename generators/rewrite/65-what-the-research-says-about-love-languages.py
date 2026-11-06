#!/usr/bin/env python3
"""Essay 65 :: what-the-research-says-about-love-languages  (Relationships)

Sources fetched and read on 7 Nov 2026: Impett, Park and Muise (2024),
Current Directions in Psychological Science, abstract on the APS site;
University of Toronto news story on that review (2024); SAGE Perspectives
Q and A with Emily Impett (2025); Mostova, Stolarski and Matthews (2022),
PLOS ONE, full text, and the EurekAlert release; Flicker, Sancier-Barbosa
and Impett (2025), abstract via CiteDrive; abstract of a 2022 qualitative
study (Taylor and Francis, DOI 10.1080/08934215.2022.2113549); Christianity
Today profile of Gary Chapman.
Not used: the original Bunt and Hazelwood (2017) and Egbert and Polk (2006)
papers, which could not be read; they are described only as Mostova and
colleagues describe them. No publication year for the book is given,
because no fetched source states it plainly.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import newpost, postkit as K

EXT = ' target="_blank" rel="noopener"'
def a(url, text):
    return '<a href="%s"%s>%s</a>' % (url, EXT, text)

IPM = "https://www.psychologicalscience.org/journals/current-directions/09637214231217663/"
UOFT = "https://www.utoronto.ca/news/little-evidence-linking-five-love-languages-healthy-relationships-researchers-say"
SAGEQA = "https://www.sagepub.com/explore-our-content/blogs/posts/sage-perspectives/2025/06/04/research-with-impact-q-a-with-emily-impett"
MOST = "https://rcastoragev2.blob.core.windows.net/05f4ea633e3daa2a2df67e27338378ec/PMC9216579.pdf"
EUREKA = "https://www.eurekalert.org/news-releases/956244"
FLICK = "https://www.citedrive.com/en/discovery/revisiting-the-five-love-languages-framework-toward-a-more-flexible-model-of-love-expression/"
QUAL = "https://informahealthcare.com/doi/abs/10.1080/08934215.2022.2113549"
CT = "https://christianitytoday.com/ct/2021/october/gary-chapman-secret-fame-five-love-languages.html"

ESSAY40 = '<a href="/writing/why-reassurance-is-never-enough">why reassurance is never enough</a>'
ESSAY50 = '<a href="/writing/what-your-partner-does-with-your-good-news">what your partner does with your good news</a>'
ESSAY57 = '<a href="/writing/what-aristotle-meant-by-the-three-kinds-of-friendship">what Aristotle meant by the three kinds of friendship</a>'
ESSAY42 = '<a href="/writing/what-attachment-styles-actually-measure">what attachment styles actually measure</a>'

POST = dict(
    slug="what-the-research-says-about-love-languages", num=65, cat="Relationships", read="auto",
    date="2026-11-07",
    gen="rewrite/65-what-the-research-says-about-love-languages.py",
    title="What the research says about love languages, and what it suggests instead",
    dek="Love languages are one of the most popular ideas about relationships: everyone has a main way of feeling loved, there are five of them, and couples do better when they speak each other’s. When researchers tested those claims, the results were mixed at best. One review suggests a better picture: love as a balanced diet.",
    takeaway="Gary Chapman’s The Five Love Languages, which has sold more than 20 million copies according to Christianity Today, grew out of his notes from counselling couples. It makes three central claims: each person has a preferred love language, there are five of them, and couples are more satisfied when partners speak each other’s preferred language. A 2024 review by Emily Impett, Gideon Park and Amy Muise concluded that, collectively, the research does not provide strong empirical support for those three assumptions. One 2022 study did find that couples who better matched each other’s preferences were more satisfied, but it was cross-sectional and could not show cause; a preregistered 2025 study found that less than half of participants had an identifiable primary love language. The reviewers suggest thinking of love as a balanced diet, in which people need a full range of essential nutrients.",
    sections=[
        ("What the research says about love languages", [
            "The research says love languages capture something real, that people value different expressions of care, but does not support the system’s main claims. Most people value all five forms of affection, many do not have one clear favourite, and evidence that matching a partner’s language makes couples happier is weak and mixed.",
            "HTML:" + K.takeaways([
                "Chapman’s idea came from his counselling notes, not from research.",
                "Its three claims: one preferred language each, five languages, and matching helps.",
                "A 2024 review found no strong empirical support for those three claims taken together.",
                "When not forced to choose, people tend to value all five forms of affection.",
                "One 2022 study linked better matching with higher satisfaction, without showing cause.",
                "The reviewers propose love as a balanced diet, not a single language.",
            ]),
            "This essay sets out what the book claims, what the studies found, and where they disagree. It does not tell anyone to stop using the idea; it describes what the evidence can and cannot support.",
            "HTML:" + K.callout("definition", "The five love languages",
                "<p>As listed in a " + a(MOST, "2022 study") + ": Acts of Service, Physical Touch, Words of Affirmation, Quality Time and Gifts. In Chapman’s framework, each person feels most loved through one of them.</p>"),
        ]),
        ("Where the idea came from", [
            "The love languages came out of a pastor’s office, not a laboratory. According to a " + a(CT, "Christianity Today profile") + ", Gary Chapman, a lifelong conservative Southern Baptist, has pastored Calvary Baptist Church in Winston-Salem for five decades and counselled couples there. His training, the profile notes, ran from Moody Bible Institute and Wheaton College to a PhD from Southwestern Baptist Theological Seminary and a master’s degree in anthropology from Wake Forest University. After more than a decade of counselling, the profile says, he went back through twelve years of notes and concluded that unhappy couples were simply attempting to show one another love in ways their partners did not receive.",
            "The book that followed sold 8,500 copies in its first year, the profile reports, and has since sold more than 20 million copies worldwide and been printed in 57 languages. By 2024, " + a(UOFT, "University of Toronto News") + " could describe it as having been out for 30-odd years and having sold millions of copies.",
            "Its appeal is easy to see. The " + a(IPM, "2024 review") + " by Emily Impett, Gideon Park and Amy Muise suggests the framework enables people to identify important relationship needs and provides an intuitive metaphor that resonates with people. Those are real strengths, and the reviewers acknowledge them. The question the research asks is narrower: whether the specific claims the book makes about those needs hold up when they are measured.",
        ]),
        ("Three claims, tested", [
            "The 2024 review, published in Current Directions in Psychological Science, set out to check three assumptions in the book: that each person has a preferred love language, that there are five love languages, and that couples are more satisfied when partners speak one another’s preferred language. Its overall conclusion is that the research, collectively, does not provide strong empirical support for the book’s three central assumptions.",
            "According to " + a(UOFT, "University of Toronto News") + ", the review looked at ten existing studies, and Impett is quoted as saying: “None of the 10 studies supported Chapman’s claims.” That is a strong statement, and as the sections below show, at least one study found something closer to support for one of the claims. The fair summary is that the evidence is weak and inconsistent, not that every finding points the same way.",
            "HTML:" + K.table("The three assumptions and the evidence",
                ["Assumption", "What studies found"],
                [["Each person has one preferred language", "When not forced to choose, people tend to value all five; in one 2025 study, under half had a clear primary one"],
                 ["There are exactly five", "Some support for the five, and evidence for other ways of expressing love"],
                 ["Matching makes couples happier", "Mixed: one 2022 study found a link; other studies did not, and none shows cause"]],
                source='Sources: <a href="' + IPM + '" target="_blank" rel="noopener">Impett and others (2024)</a>; <a href="' + FLICK + '" target="_blank" rel="noopener">Flicker and others (2025)</a>; <a href="' + MOST + '" target="_blank" rel="noopener">Mostova and others (2022)</a>.'),
        ]),
        ("Does everyone have one?", [
            "Part of the answer depends on how the question is asked. The standard way to find your love language is Chapman’s quiz, and according to " + a(UOFT, "University of Toronto News") + ", the researchers note that it forces trade-offs that don’t occur in real life: you must pick one expression of love over another, even if you value both.",
            "When people are not forced to choose, the picture changes. In a " + a(SAGEQA, "2025 interview with SAGE") + ", Impett said that people tend to value all five forms of affection. A preregistered study of 499 people in long-term, cohabiting relationships, by " + a(FLICK, "Sharon Flicker, Flavia Sancier-Barbosa and Impett") + ", published in 2025, found that less than half of participants had an identifiable primary love language.",
            "That does not mean preferences do not exist. Some people do care more about time together, others about help with the chores. It means that sorting everyone into one of five boxes loses much of the detail, and that most people want more than one kind of care.",
        ]),
        ("Are there five?", [
            "The evidence on the number five is genuinely mixed. A 2022 study that analysed 648 open-ended responses from 324 college-aged participants, according to its " + a(QUAL, "abstract") + ", found substantial support for Chapman’s Five Love Languages, as well as evidence for a novel, sixth love language.",
            "Other research points to things the five leave out. University of Toronto News reports that the reviewers found inconsistent evidence for the five, and that Chapman’s model leaves out things like supporting a partner’s personal goals. In the 2025 study, the abstract reports that verbal affirmations, encouragement for individual pursuits, support during difficult times, and accountability stood out as especially strong predictors of relationship quality. Only the first of those is clearly one of Chapman’s five.",
            "Impett has suggested why. Chapman’s framework, she told " + a(SAGEQA, "SAGE") + ", was based on a narrow group, so it may miss other ways of showing love, such as supporting a partner’s autonomy.",
        ]),
        ("Does speaking the same language help?", [
            "This is the claim that matters most to couples, and the one with the most conflicting results. The strongest positive finding comes from a 2022 study in PLOS ONE by " + a(MOST, "Olha Mostova, Maciej Stolarski and Gerald Matthews") + ". They surveyed 100 heterosexual couples and found that people whose partners expressed love in their preferred ways reported higher relationship and sexual satisfaction, and that both satisfaction measures were negatively associated with mismatch, for men and for women.",
            "The authors are careful about what this shows. The study was an online, cross-sectional, self-report survey, and they call for research to establish the direction of causality. In the " + a(EUREKA, "press release") + ", they add that the study only included heterosexual couples, and that dimensional assessment may be preferable to typologizing love languages. They also describe their study as the first to find empirical support for the matching hypothesis, contrasting it with earlier studies that found no significant effect of matching, and attribute the difference to measuring matching on a scale rather than by category.",
            "Some details of the study are worth knowing. The couples had been together for between six months and 24 years, according to the " + a(EUREKA, "release") + ", and the sample was culturally mixed, with 31 nationalities, most often Ukrainian and Polish; the authors note that this mix might have been a confounding variable. They had also expected that more empathic partners would be better at speaking each other’s language, but that idea was only partly supported, and they concluded that the benefits of matching did not appear to run through empathy. Women scored higher than men on most of the scales for feeling loved.",
            "The same " + a(MOST, "paper") + " summarises earlier attempts to test the idea, and they are not encouraging. It reports that one earlier study found no significant effect of matching on relationship quality; that another found that sharing the same primary language did not lead to relationship satisfaction, although women’s self-regulation improved partners’ satisfaction when their languages were misaligned; and that a third found no statistically significant differences in behaviour after couples learned their partner’s love language. Knowing the language, in that last study, did not change what people did.",
            "The 2025 study points the other way. Its " + a(FLICK, "abstract") + " reports that, among people who did have a primary love language, satisfaction with a partner’s expression of that behaviour was no stronger a predictor of relationship quality than satisfaction with the other behaviours. And Impett, summing up the review for " + a(UOFT, "University of Toronto News") + ", put it bluntly: “There’s no support for this matching effect,” adding that people are happier when they receive any of these expressions of love.",
            "HTML:" + K.compare("Two readings of the matching evidence", [
                ("Matching helps", ["One 2022 study of 100 couples found a link with satisfaction"], ["Cross-sectional, so cause is unknown"], "Possible, not shown."),
                ("Any care helps", ["Fits the 2024 review and the 2025 study"], ["Still mostly correlational evidence"], "Better supported."),
            ], source='Sources: <a href="' + MOST + '" target="_blank" rel="noopener">Mostova and others (2022)</a>; <a href="' + FLICK + '" target="_blank" rel="noopener">Flicker and others (2025)</a>; <a href="' + IPM + '" target="_blank" rel="noopener">Impett and others (2024)</a>.'),
        ]),
        ("A balanced diet, not a language", [
            "The reviewers offer an alternative picture. In the words of their " + a(IPM, "abstract") + ", love can be more appropriately understood as a balanced diet in which people need a full range of essential nutrients to cultivate lasting love. Impett put it more simply to " + a(SAGEQA, "SAGE") + ": “Love isn’t a language; it’s more like a balanced diet.”",
            "On this view, relationships need a mix of affection, practical support, gratitude and quality time, and meeting those needs over time matters more than a quiz score. University of Toronto News adds companionship and emotional support to the list of essential needs. The point is not that one kind of care is better than another, but that a relationship short on any of them is missing something, however fluent it is in the rest. A partner who brings flowers but never asks how the week went is offering one nutrient and withholding others.",
            "This changes the practical advice. The love languages suggest finding your partner’s one language and speaking it well. The balanced-diet view suggests paying attention to the whole range, and in particular to forms of care the five leave out, such as backing a partner’s goals and being there during hard times.",
        ]),
        ("What is still useful", [
            "None of this makes the love languages useless. Impett told " + a(SAGEQA, "SAGE") + " that “We acknowledge they’ve helped many people reflect on their relationships,” and that the goal of the review was not to tear down the love languages entirely. Asking what makes a partner feel cared for, and noticing that it may not be what you would want yourself, is good advice whatever the evidence says about the five categories.",
            "Chapman has taken the research calmly. Asked about psychologists who challenge the theory, he told " + a(CT, "Christianity Today") + ": “I welcome the results they discover in their own research.”",
            "HTML:" + K.callout("warn", "A note on using the idea",
                "<p>Treating a quiz result as a fixed fact about a partner can narrow what each person offers and expects. The evidence above suggests holding the five categories loosely, as a starting point for a conversation, not as a rule about what love has to look like.</p>"),
        ]),
        ("What this does and does not say", [
            "Read carefully, the research does not say love languages are nonsense. It says the strong version, one language each, exactly five, and matching as the key to happiness, is not well supported, while the underlying point, that people differ in what makes them feel cared for, is reasonable. The best-supported advice is broader: offer a range of care, ask rather than assume, and notice the needs the five leave out.",
            "Other essays here look at the same question from different angles. " + ESSAY50.replace(">what your partner", ">What your partner") + " describes research on one specific, well-studied form of care: how a partner responds to good news. " + ESSAY40.replace(">why reassurance", ">Why reassurance") + " looks at what a partner’s words can and cannot fix. And " + ESSAY57 + " sets out a much older account of what holds close relationships together.",
        ]),
    ],
    note=[
        "Earlier studies that found no matching effect are described here as Mostova and colleagues describe them, because the original papers could not be read. Impett is a co-author of both the 2024 review and the 2025 study.",
    ],
    faqs=[
        ("Are love languages backed by science?",
         "Only partly. A 2024 review concluded that the research does not provide strong empirical support for the book’s three central assumptions, though people clearly do value different expressions of care."),
        ("Does everyone have a primary love language?",
         "Not necessarily. When not forced to choose, people tend to value all five, and in a 2025 study of 499 people in long-term relationships, less than half had an identifiable primary love language."),
        ("Do couples who share a love language do better?",
         "The evidence is mixed. One 2022 study of 100 couples found that better matching went with higher satisfaction, but it could not show cause, and other studies have found no matching effect."),
        ("What is the balanced diet idea of love?",
         "The 2024 review’s alternative: love is like a balanced diet in which people need a full range of essential nutrients, such as affection, practical support, gratitude and time, rather than one preferred language."),
        ("Where did the five love languages come from?",
         "From Gary Chapman’s counselling work. According to Christianity Today, he reviewed twelve years of notes from counselling couples and concluded that unhappy couples were showing love in ways their partners did not receive."),
    ],
    related=[
        ("what-your-partner-does-with-your-good-news", "What your partner does with your good news, and why it may matter more than you think", "Relationships"),
        ("what-the-michelangelo-phenomenon-says", "What the Michelangelo phenomenon says about how partners shape each other", "Relationships"),
    ],
)

if __name__ == "__main__":
    newpost.build(POST)
