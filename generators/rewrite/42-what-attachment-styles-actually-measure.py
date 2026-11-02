#!/usr/bin/env python3
"""Essay 42 :: what-attachment-styles-actually-measure  (Psychology, pillar)

Every research claim is linked to a source fetched and read on 2 Nov 2026:
Hazan and Shaver 1987 (scan of the published article), Bartholomew and
Horowitz 1991 (PubMed abstract), Brennan, Clark and Shaver 1998 and the
ECR-R and ECR-RS pages (Fraley's lab), Morales-Vives et al. 2021 (PMC),
Fraley and Shaver 2000, Shaver and Mikulincer (draft chapter), Fraley et
al. 2015, Pinquart, Feussner and Ahnert 2013, Fraley 2019, and Fraley et
al. 2011 (ECR-RS abstract).
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import newpost, postkit as K

EXT = ' target="_blank" rel="noopener"'
def a(url, text):
    return '<a href="%s"%s>%s</a>' % (url, EXT, text)

HS87_URL = "https://www.psychologywizard.net/uploads/2/6/6/4/26640833/hazanshaver1987.pdf"
BH91_URL = "https://pubmed.ncbi.nlm.nih.gov/1920064/"
BCS98_URL = "https://labs.psychology.illinois.edu/~rcfraley/measures/brennan.html"
MV21_URL = "https://pmc.ncbi.nlm.nih.gov/articles/PMC8266088"
ECRR_URL = "https://labs.psychology.illinois.edu/~rcfraley/measures/ecrr.htm"
F15_URL = "https://www.nathanwhudson.com/vita/pdf/Fraley%20et%20al.,%202015.pdf"
FS00_URL = "https://adultattachment.faculty.ucdavis.edu/wp-content/uploads/sites/66/2015/09/Fraley_2000_Adult-romantic-attachment.pdf"
SM_URL = "https://adultattachment.faculty.ucdavis.edu/wp-content/uploads/sites/66/2015/09/Shaver_2006_Attachment-theory-individual-psychodynamics-and-relationship-functioning.pdf"
PFA_URL = "https://www.lieselotte-ahnert.de/files/65/pinquart-feussner-ahnert-2012.pdf"
F19_URL = "https://library.scottbarrykaufman.com/uploads/2019/01/Fraley-2019.pdf"
RS_URL = "https://experts.illinois.edu/en/publications/the-experiences-in-close-relationships-relationship-structures-qu/"
RSM_URL = "https://labs.psychology.illinois.edu/~rcfraley/measures/relstructures.htm"
F11_URL = "https://digitalcommons.iwu.edu/psych_scholarship/19"

ESSAY40 = '<a href="/writing/why-reassurance-is-never-enough">the essay on reassurance seeking</a>'
ESSAY41 = '<a href="/writing/what-the-observer-effect-actually-says">the word observer in physics</a>'
SHRINK = '<a href="/books/nobody-has-to-shrink">Nobody has to shrink</a>'

POST = dict(
    slug="what-attachment-styles-actually-measure", num=42, cat="Psychology", read="auto",
    date="2026-11-02",
    gen="rewrite/42-what-attachment-styles-actually-measure.py",
    title="What attachment styles actually measure, and what they cannot tell you",
    dek="Secure, anxious, avoidant: the labels are everywhere, and they began as a newspaper quiz. The research has since moved a long way from boxes, and what it found is more useful than any label.",
    takeaway="Attachment research measures two things: how much a person worries about being rejected or abandoned, and how uncomfortable they are with closeness and depending on others. The familiar styles are shorthand for regions on those two scales. Large studies find that people are spread continuously along them rather than sorted into types, that the link from infancy to adulthood is weak over long spans, and that the same person can be more or less secure with different people. Read a result as a position that can move, in a particular relationship, not as a verdict on who you are.",
    sections=[
        ("What attachment styles measure", [
            "Attachment styles measure two things: how much you worry that people close to you will reject or leave you, which researchers call anxiety, and how uncomfortable you are with closeness and depending on others, which they call avoidance. Secure, anxious and avoidant are names for regions on those two scales, not types of people.",
            "HTML:" + K.takeaways([
                "The three famous styles began in 1987 as one multiple-choice question in a newspaper love quiz.",
                "Later research replaced the boxes with two continuous scales: anxiety and avoidance.",
                "Large taxometric studies find people spread along those scales, not clustered into types.",
                "Attachment security is only moderately stable, and no significant stability was found across intervals longer than fifteen years.",
                "People can be more secure in one relationship than another, and relationship-specific measures generally predict outcomes better than general ones.",
            ]),
            "That is a narrower and more hopeful finding than the version that circulates, in which everyone has a style, the style was set in childhood, and the style explains the relationship. This essay goes through where the labels came from, what replaced them, and what a result can and cannot tell you.",
            "HTML:" + K.callout("definition", "Attachment, in this research",
                "<p>The pattern of expectations and feelings a person brings to close relationships about whether others will be there when needed. In adults it is usually measured by questionnaire, as two scores: attachment anxiety and attachment avoidance.</p>"),
        ]),
        ("Where the three styles came from", [
            "The categories began with infants. In Mary Ainsworth&rsquo;s laboratory procedure, the Strange Situation, a young child is briefly separated from a parent and then reunited. As " + a(F19_URL, "Chris Fraley&rsquo;s 2019 review in the Annual Review of Psychology") + " describes it, some children, labelled avoidant, may not show clear signals of distress at the separation; others, labelled anxious-resistant, are distressed and hard to settle; secure children are visibly upset by the separation and easily soothed when the parent returns.",
            "In 1985 two researchers, Cindy Hazan and Phillip Shaver, asked whether adult romantic love might follow the same patterns. Their method, reported in " + a(HS87_URL, "the 1987 paper in the Journal of Personality and Social Psychology") + ", was a love quiz printed in a local newspaper, the Rocky Mountain News, on 26 July 1985. They analysed the first 620 of more than 1,200 replies: 205 from men and 415 from women, aged 14 to 82.",
            "The attachment measure was a single question: which of three short paragraphs best describes your feelings? Readers were asked to choose one. That choice was the attachment style. Of the 620, 574 chose a single paragraph; the rest left the question blank or ticked more than one.",
            "<strong>Secure.</strong> &ldquo;I find it relatively easy to get close to others and am comfortable depending on them and having them depend on me. I don&rsquo;t often worry about being abandoned or about someone getting too close to me.&rdquo;",
            "<strong>Avoidant.</strong> &ldquo;I am somewhat uncomfortable being close to others; I find it difficult to trust them completely, difficult to allow myself to depend on them. I am nervous when anyone gets too close, and often, love partners want me to be more intimate than I feel comfortable being.&rdquo;",
            "<strong>Anxious/ambivalent.</strong> &ldquo;I find that others are reluctant to get as close as I would like. I often worry that my partner doesn&rsquo;t really love me or won&rsquo;t want to stay with me. I want to merge completely with another person, and this desire sometimes scares people away.&rdquo;",
            "Those are the original 1987 wordings, quoted from " + a(HS87_URL, "the published paper") + ".",
            "In the newspaper sample, " + a(HS87_URL, "56% chose the secure paragraph") + ", 25% the avoidant one and 19% the anxious one. A second study of 108 undergraduates gave almost the same split: 56%, 23% and 20%. The authors noted that these figures were similar to proportions from American studies of infants and mothers, which they cited as 62% secure, 23% avoidant and 15% anxious.",
            "HTML:" + K.bars("Self-classified attachment style, 1987 newspaper sample (574 who chose one paragraph)",
                [("Secure", 56, "56%"), ("Avoidant", 25, "25%"), ("Anxious/ambivalent", 19, "19%")],
                source="Source: Hazan and Shaver (1987), Study 1. A self-selected sample of newspaper readers answering one forced-choice question."),
            "Those percentages are still quoted, often as if they described the population. They describe the readers of one newspaper in 1985 who chose to send in a love quiz, two thirds of them women, each answering one question.",
        ]),
        ("What the original authors warned", [
            "The 1987 paper is more careful than its reputation. Hazan and Shaver wrote that it was unlikely their single-item measure captured exactly what had been coded from watching infants with their mothers, and that it would be naive to think a style adopted in infancy remains unchanged through life.",
            "They also pointed to a problem with the measure itself: each of their answer alternatives included more than one issue or dimension. A reader who was comfortable depending on others but often worried about being left had no paragraph that fitted.",
            "And they warned against the reading that later became popular. In their words, they had probably overemphasised the degree to which attachment style and attachment-related feelings are traits rather than products of unique person-situation interactions. The links they found between memories of parents and current attachment type were, in their words, statistically significant but not strong.",
            "HTML:" + K.callout("note", "Why this matters",
                "<p>The first adult attachment study already said the three boxes were a rough tool, that each box mixed more than one thing, and that style might depend on the situation as much as the person. The research that followed took those warnings seriously. Much popular writing did not.</p>"),
        ]),
        ("From three boxes to two scales", [
            "The first change was to notice that the boxes were built from two separate questions. In 1991 Kim Bartholomew and Leonard Horowitz proposed four patterns, defined, as " + a(BH91_URL, "their abstract puts it") + ", by combining a person&rsquo;s image of themselves (positive or negative) with their image of others (positive or negative).",
            "The second change was larger. Kelly Brennan, Catherine Clark and Phillip Shaver gathered most of the existing self-report attachment measures: " + a(BCS98_URL, "482 items meant to assess 60 named constructs") + ". Analysed together, those 60 scales reduced to two essentially independent factors, which they called anxiety and avoidance. Their questionnaire built on that result, the Experiences in Close Relationships scale, has 36 items, 18 for each.",
            "The questionnaires most used in research today, such as the revised Experiences in Close Relationships scale, score these two dimensions. " + a(MV21_URL, "A 2021 paper in PLoS ONE") + " summarises them as anxiety, meaning fear of abandonment and hypervigilance towards romantic partners, searching for signs of rejection, and avoidance, meaning reluctance to get close to others.",
            "HTML:" + K.table("The four regions of the two-dimensional space",
                ["Region", "Anxiety", "Avoidance"],
                [["Secure", "Low", "Low"],
                 ["Preoccupied", "High", "Low"],
                 ["Dismissing", "Low", "High"],
                 ["Fearful", "High", "High"]],
                source='Source: <a href="' + MV21_URL + '" target="_blank" rel="noopener">Morales-Vives et al., PLoS ONE (2021)</a>, describing Bartholomew and Horowitz&rsquo;s four-category model on the two dimensions.'),
            "Read this way, the old anxious style sits roughly in the preoccupied corner, and the old avoidant style was hiding two different patterns: people who keep their distance and feel fine about it, and people who keep their distance because they fear being hurt. Treating those as one style lost the difference.",
        ]),
        ("Are they types at all?", [
            "A table with four corners still invites you to put people in corners. The obvious next question is whether people actually cluster there, or whether the corners are just labels on a smooth surface. Statisticians have a family of methods for this, called taxometric analysis, designed to tell whether a set of scores reflects distinct types or continuous variation.",
            "The largest taxometric studies have pointed the same way. Reviewing early work, " + a(FS00_URL, "Fraley and Shaver wrote in 2000") + " that Fraley and Waller&rsquo;s analyses indicated categorical models are inappropriate for studying variation in romantic attachment, and that the data were more consistent with a dimensional model.",
            "A large test came in 2015. " + a(F15_URL, "Fraley, Hudson, Heffernan and Segal") + " analysed two samples of about 2,300 and 2,400 people, looking at attachment in general and within specific relationships. They concluded that individual differences in adult attachment are continuously distributed, with the findings for friendships a little more ambiguous. Their recommendation was blunt: they no longer think it is defensible to use categorical measures in adult attachment research, and they advise against cutting continuous scores into categories, because that can misrepresent the nature of the differences.",
            "Phillip Shaver, one of the two people who started this research, said the same thing in his own later writing. In " + a(SM_URL, "a chapter with Mario Mikulincer") + ", he described attachment styles as regions in a continuous two-dimensional space, and warned that using category names as shorthand can encourage people to think in types.",
            "The question is not entirely closed. Some researchers still argue for combining the two approaches; " + a(MV21_URL, "the 2021 PLoS ONE paper") + ", for example, reports that there is still no consensus and found two broad profiles in its own data, an insecure one and a normal-range one. But the large taxometric studies, and the people who built the main questionnaires, point towards dimensions.",
            "HTML:" + K.compare("Two ways to read an attachment result", [
                ("As a type", [], ["Treats people in the same box as the same", "Hides how far someone is from the boundary", "Invites the question of which one you are"], "Not supported by the taxometric evidence."),
                ("As two scores", ["Keeps every difference in both dimensions", "Shows how close to the middle someone sits", "Lets a score move without a change of identity"], [], "How the research now measures it."),
            ], source='Sources: <a href="' + F15_URL + '" target="_blank" rel="noopener">Fraley et al. (2015)</a>; <a href="' + ECRR_URL + '" target="_blank" rel="noopener">Fraley&rsquo;s ECR-R page</a>.'),
            "Even the most widely used questionnaire comes with the same instruction. " + a(ECRR_URL, "Fraley&rsquo;s page for the revised Experiences in Close Relationships scale") + " says variation in attachment is best modelled with dimensions rather than categories, and strongly recommends against classifying people on the basis of their continuous scores.",
        ]),
        ("How stable is attachment?", [
            "The popular account usually adds that your style was set in childhood. The evidence for that is weaker than the claim.",
            "One large review of the question is " + a(PFA_URL, "a 2013 meta-analysis by Pinquart, Feu&szlig;ner and Ahnert") + ", which combined 127 papers covering more than 21,000 attachments, followed over intervals from two weeks to 29 years. Overall, security at one point correlated with security at the next at about 0.39, which the authors describe as medium-sized stability. But stability fell as the gap grew, and no significant stability was found in intervals longer than fifteen years; only 18 results covered spans that long.",
            "HTML:" + K.table("Attachment stability, as measured",
                ["Comparison", "Correlation"],
                [["Attachment security, all intervals pooled (infancy to early adulthood)", "about 0.39: medium stability"],
                 ["Intervals longer than 15 years", "about 0.14: not significant"],
                 ["Infant Strange Situation to adult romantic security (one unpublished study)", "0.17: weak"]],
                source='Sources: <a href="' + PFA_URL + '" target="_blank" rel="noopener">Pinquart, Feußner and Ahnert, Attachment and Human Development (2013)</a>; <a href="' + FS00_URL + '" target="_blank" rel="noopener">Fraley and Shaver (2000)</a>, reporting Steele, Waters, Crowell and Treboux (1998, unpublished).'),
            "Fraley&rsquo;s 2019 review reaches the same conclusion from a different direction. Longitudinal studies do find associations between early caregiving and adult attachment, but, as " + a(F19_URL, "the review puts it") + ", these associations are not strong, and they are not necessarily consistent across ways of measuring. Many people, despite having supportive caregiving experiences, are insecure in their adult relationships. The reverse is also true.",
            "What adult attachment does look like, in studies that track it closely, is a stable core with movement around it. In " + a(F11_URL, "a 2011 study by Fraley, Vicary, Brumbaugh and Roisman") + ", one sample was assessed daily for 30 days and another weekly for a year, and the results were most consistent with what the authors call a prototype model: a stable factor underlying temporary variations in attachment. The 2019 review adds that attachment is more stable in established relationships, such as those with parents, than in romantic ones, and lists breakups among the experiences linked to change. Fraley and Shaver noted earlier that attachment anxiety has been shown to decrease over time, while avoidance has not.",
        ]),
        ("One person, several attachments", [
            "The last finding is the one most often left out. Attachment is not only something a person has; it is also something that differs between relationships.",
            "The questionnaire built to measure this, " + a(RS_URL, "the Experiences in Close Relationships, Relationship Structures questionnaire") + ", asks " + a(RSM_URL, "the same nine questions") + " about a mother, a father, a romantic partner and a best friend. Its authors describe people as holding distinct working models in different relationships. They also found that relationship-specific measures generally predict both personal and interpersonal outcomes better than general ones, while the broader measures predict personality traits better.",
            "HTML:" + K.stages("What a single attachment score leaves out", [
                ("01", "Which relationship", "Security with a parent, a partner and a friend can differ, and each is measured separately."),
                ("02", "Which dimension", "Anxiety and avoidance vary independently. One label compresses two numbers into one word."),
                ("03", "How far from the middle", "Most people are not at the extremes. A category hides how close someone is to the boundary."),
                ("04", "When", "Scores move over days, weeks and years, around a more stable core."),
            ], source='Sources: <a href="' + RS_URL + '" target="_blank" rel="noopener">Fraley et al., Psychological Assessment (2011)</a>; <a href="' + F11_URL + '" target="_blank" rel="noopener">Fraley et al., Journal of Personality and Social Psychology (2011)</a>; <a href="' + F19_URL + '" target="_blank" rel="noopener">Fraley (2019)</a>.'),
            "So the honest answer to the question of what your attachment style is begins with another question: with whom? Fraley&rsquo;s review notes that, in one line of work, romantic relationship outcomes were correlated only with relationship-specific representations. How secure you feel with this partner tells you more about this relationship than a general label does.",
        ]),
        ("Reading your own result", [
            "None of this makes attachment research useless for understanding yourself. It makes it more precise. A few habits follow directly from what the research found.",
            "HTML:" + K.decision("What is this result telling me?",
                ("Is it a single label, such as anxious or avoidant?", [
                    ("Yes", ("Can you find the two underlying scores?", [
                        ("Yes", "<p>Read the scores instead of the label. Two numbers, each on a scale, say far more than one word.</p>"),
                        ("No", "<p>Treat the label as a rough region, not a type. The research recommends against classifying people this way.</p>"),
                    ])),
                    ("No", ("Does it say which relationship it is about?", [
                        ("Yes", "<p>Good. That is the measure most likely to tell you something about that relationship.</p>"),
                        ("No", "<p>It is a general picture. Ask how it compares with how you feel with one specific person.</p>"),
                    ])),
                ])),
            "Three readings are worth keeping. First, high anxiety and high avoidance are different problems, and a label that hides which one you have hides the useful part. Second, a score is a position on the day you answered, in the relationship you were thinking of; the research expects it to move. Third, a score does not explain a relationship on its own. The questions are about expectations and feelings, and what changes relationships is what people do with them.",
            "That last point is where this essay meets " + ESSAY40 + ". The anxiety dimension describes a person scanning for signs of rejection. Reassurance seeking is one of the things such a person may do about it, and it has its own loop and its own evidence. The two overlap, but they are not the same thing: a score describes the fear, and the behaviour is something that can be changed directly.",
        ]),
        ("What the labels are still good for", [
            "The words secure, anxious and avoidant will not disappear, and they do not need to. As shorthand for regions they are useful, and they give people a way to talk about patterns they recognise. The mistake is treating a region as an identity.",
            "There is a parallel elsewhere on this site. Like " + ESSAY41 + ", which means something far narrower in the research than in popular use, the word style carries more certainty in conversation than it does in the studies. The research describes two dimensions, measured in a particular relationship, at a particular time, with a stable core and room to move.",
            "Security, read that way, is a direction rather than a box: lower anxiety, lower avoidance, with someone in particular. " + SHRINK + ", one of the books on this site, is described as a handbook for secure love. This essay is the evidence behind using the word secure as something people can move towards, rather than something they either have or do not.",
        ]),
    ],
    note=[
        "Everything here comes from the research literature, linked in the text. Where a figure comes from a single sample, a self-selected one or an unpublished study, the essay says so at the point it is used.",
    ],
    faqs=[
        ("What are the two dimensions of attachment?",
         "Attachment anxiety, which is worry about rejection and abandonment and watchfulness for signs of it, and attachment avoidance, which is discomfort with closeness and with depending on others. Brennan, Clark and Shaver found that dozens of earlier attachment scales reduced to these two largely independent factors."),
        ("Are attachment styles real types of people?",
         "The weight of evidence says no. Large taxometric studies, including Fraley and colleagues in 2015, find that people are spread continuously along the anxiety and avoidance dimensions rather than falling into distinct types. The style names are shorthand for regions of that space, though some researchers still argue for combining types and dimensions."),
        ("Can your attachment style change?",
         "Yes. A 2013 meta-analysis found medium stability overall but no significant stability over intervals longer than fifteen years, and studies that track adults closely find a stable core with variation around it. People can also be more or less secure in different relationships."),
        ("How many people are securely attached?",
         "There is no single answer, because the number depends on how attachment is measured and where the cut-off is drawn. The often quoted 56% comes from a 1987 newspaper love quiz with a self-selected sample answering one question. With continuous measures, which researchers now recommend, there is no natural cut-off at all."),
        ("Is anxious attachment the same as reassurance seeking?",
         "No. Attachment anxiety is a score describing worry about rejection and abandonment. Reassurance seeking is a behaviour, repeatedly asking for confirmation, that people high in anxiety may show. They overlap, but the behaviour has its own pattern and can be changed directly."),
    ],
    related=[
        ("why-reassurance-is-never-enough", "Why reassurance is never enough, and what to do instead", "Relationships"),
        ("what-the-observer-effect-actually-says", "What the observer effect actually says, and what it does not", "Physics and time"),
    ],
)

if __name__ == "__main__":
    newpost.build(POST)
