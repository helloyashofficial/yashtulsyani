#!/usr/bin/env python3
"""Essay 50 :: what-your-partner-does-with-your-good-news  (Relationships)

Sources fetched and read on 3 Nov 2026: Gable, Reis, Impett and Asher 2004
(full text, Reis lab copy) and PubMed record; Gable and Reis 2010 (full
text, Reis lab copy); Gable, Gonzaga and Strachman 2006 (PubMed abstract
only); Peters, Reis and Gable 2018 (Gable lab citation page, abstract
fragments only); Sim et al. 2024 (University of Minnesota abstract); Pagani
et al. 2015 (Universita Cattolica abstract); Woods et al. 2015 (UT
Southwestern abstract); De Netto, Quek and Golden 2021 (Frontiers);
Reivich, Seligman and McBride 2011 (full text); Novotney, APA Monitor 2009;
Steenkamp, Nash and Litz 2013 (full text, BU lab copy).
Langston 1994 could not be read; what he found is reported through Gable's
accounts and attributed to them. No meta-analysis was found; the essay says
so rather than claiming none exists.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import newpost, postkit as K

EXT = ' target="_blank" rel="noopener"'
def a(url, text):
    return '<a href="%s"%s>%s</a>' % (url, EXT, text)

G04 = "https://www.sas.rochester.edu/psy/people/faculty/reis_harry/assets/pdf/GableReisImpettAsher_2004.pdf"
PAG13 = "https://publires.unicatt.it/it/publications/actively-dealing-with-good-fortune-a-confirmatory-factor-analysis-7/"
GUO = "https://www.sbp-journal.com/index.php/sbp/article/view/7234"
G04PM = "https://pubmed.ncbi.nlm.nih.gov/15301629/"
GR10 = "https://www.sas.rochester.edu/psy/people/faculty/reis_harry/assets/pdf/GableReis_2010.pdf"
G06 = "https://pubmed.ncbi.nlm.nih.gov/17059309/"
PRG18 = "https://labs.psych.ucsb.edu/gable/shelly/node/716"
SIM = "https://experts.umn.edu/en/publications/cross-cultural-differences-in-supportive-responses-to-positive-ev/"
PAGANI = "https://publires.unicatt.it/it/publications/when-good-things-happen-explicit-capitalization-attempts-of-posit-8/"
WOODS = "https://utsouthwestern.elsevierpure.com/en/publications/im-so-excited-for-you-how-an-enthusiastic-responding-intervention"
DENETTO = "https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2021.767908/pdf"
MRT = "https://cns.org/Assets/61659458-0c72-4295-9832-018698f5a662/637002600373370000/reivich-seligman-and-mcbride-master-resilience-training-in-the-u-s-army-pdf"
MONITOR = "https://www.apa.org/monitor/2009/12/army-program"
STEEN = "https://sites.bu.edu/litzlab/files/2023/05/Posttraumatic-stress-disorder-prevention-in-troops-Review-of-the-comprehensive-soldier-fitness-program.pdf"

MICHEL = '<a href="/writing/what-the-michelangelo-phenomenon-says">what the Michelangelo phenomenon says</a>'
ESSAY40 = '<a href="/writing/why-reassurance-is-never-enough">why reassurance is never enough</a>'
ESSAY45 = '<a href="/writing/what-repair-after-an-argument-actually-involves">what repair after an argument involves</a>'
ESSAY42 = '<a href="/writing/what-attachment-styles-actually-measure">what attachment styles actually measure</a>'

POST = dict(
    slug="what-your-partner-does-with-your-good-news", num=50, cat="Relationships", read="auto",
    date="2026-11-03",
    gen="rewrite/50-what-your-partner-does-with-your-good-news.py",
    title="What your partner does with your good news, and why it may matter more than you think",
    dek="Most advice about relationships is about the hard moments. A line of research that began in the 1990s looks at the easy ones: what happens when one person shares good news and the other responds. The findings are striking, and more tentative than they are usually made to sound.",
    takeaway="Telling someone about a good thing that happened to you, which psychologists call capitalization, is linked to more positive mood than the event alone explains. How the listener responds matters. Shelly Gable and colleagues sort responses into four kinds, active or passive and constructive or destructive, and in their 2004 studies only the active-constructive kind, enthusiastic and engaged, was linked to better relationship quality; quiet, understated support was linked to worse outcomes. A 2006 study found responses to good news were more closely related to relationship well-being two months later than responses to bad news. Most of this evidence is correlational and based on how people perceive their partner, the quiet style seems to work differently across cultures, and one training study did not change relationship satisfaction.",
    sections=[
        ("Why good news is a test", [
            "When one partner shares good news, the other’s response is linked to how the relationship is doing. In a set of studies published in 2004, only enthusiastic, engaged responses went with better relationship quality, and quietly pleased ones went with worse. The research is mostly correlational, so it shows a pattern worth paying attention to, not a rule.",
            "HTML:" + K.takeaways([
                "Sharing good news is linked to feeling better than the news alone accounts for. Psychologists call the sharing capitalization.",
                "Responses fall into four kinds: active or passive, constructive or destructive.",
                "In the 2004 studies only the active-constructive kind, enthusiastic and curious, was linked to better relationship quality.",
                "Quiet, understated support was linked to worse outcomes in those studies, though later work finds this varies across cultures.",
                "Responses to good news predicted relationship well-being two months later more closely than responses to bad news, in one study of dating couples.",
                "Most of the evidence is correlational and based on perception. One training programme did not change relationship satisfaction.",
            ]),
            "This essay sets out where the idea came from, what the main studies did and found, and how far the findings have held up. It quotes the researchers’ own caveats, because the popular version of this research usually leaves them out.",
            "HTML:" + K.callout("definition", "Capitalization, in this essay",
                "<p>In the words of " + a(G04, "Gable and her colleagues") + ", the process of informing another person about the occurrence of a personal positive event and thereby deriving additional benefit from it.</p>"),
        ]),
        ("Where the idea came from", [
            "The term comes from C. A. Langston, writing in 1994. His paper could not be read for this essay, so his findings are reported here as Shelly Gable and her colleagues describe them. In their " + a(G04, "2004 paper") + ", they write that in two daily experience studies Langston found that when people shared the news of a positive event with others or celebrated the event in some way, they experienced greater positive affect, beyond increases associated with the valence of the positive event itself. “He called this capitalization,” they write.",
            "Gable and Harry Reis later explained that they had narrowed the word. In " + a(GR10, "a 2010 review chapter") + ", they note that Langston first defined capitalization as the process of reflecting on personal good fortune and other positive events, and that they have come to use the term to refer to an interpersonal strategy: telling someone. Langston coined the word; the focus on the person listening is Gable and Reis’s.",
            "Why should telling someone add anything? Gable and Reis, in the " + a(GR10, "same chapter") + ", list the mechanisms Langston proposed: sharing may work to enhance memorability, to maximize the event’s personal significance, and to gain value (status) in the eyes of others. Retelling a good thing makes it more vivid, makes it feel more real, and lets someone else see it. Each of those depends on the listener, which is where Gable’s research begins.",
            "That focus is what made the idea interesting for relationships. Capitalization asks about the other half of ordinary life: the promotion, the good mark, the small win at the end of the day, and what happens when it is brought home.",
        ]),
        ("Four ways to respond", [
            "Gable and her colleagues sorted responses along two lines, adapting Rusbult’s earlier model of how people respond to a partner’s negative behaviour. A response can be active or passive, and constructive or destructive. In the " + a(G04, "2004 paper") + " the four kinds are illustrated as active-constructive responses (e.g., enthusiastic support), passive-constructive responses (e.g., quiet, understated support), active-destructive responses (e.g., quashing the event), and passive-destructive responses (e.g., ignoring the event).",
            "The questionnaire they built, the Perceived Responses to Capitalization Attempts scale, asks people to rate statements that each follow the stem “When I tell my partner about something good that has happened to me…”. Its items show the four styles more vividly than any definition.",
            "HTML:" + K.table("The four responses, in the questionnaire’s own words",
                ["Response", "Example item"],
                [["Active-constructive", "“My partner often asks a lot of questions and shows genuine concern about the good event.”"],
                 ["Passive-constructive", "“My partner says little, but I know he/she is happy for me.”"],
                 ["Active-destructive", "“He/she points out the potential down sides of the good event.”"],
                 ["Passive-destructive", "“My partner often seems disinterested.”"]],
                source='Items from Table 2 of <a href="' + G04 + '" target="_blank" rel="noopener">Gable, Reis, Impett and Asher (2004)</a>.'),
            "The scale has 12 items, three for each kind. In their " + a(GR10, "2010 chapter") + ", Gable and Reis report that its four subscales showed good reliability, with alphas from 0.66 to 0.87, and that it predicted actual behaviour in the laboratory for both men and women. Later studies of " + a(PAG13, "239 couples") + " and of " + a(GUO, "1,213 Chinese students") + " found the same four-part structure.",
            "HTML:" + K.callout("note", "Why the passive-constructive response is the surprise",
                "<p>Three of the four kinds are easy to judge: enthusiasm sounds good, and criticism or indifference sound bad. The interesting one is the quiet, pleased response. It is meant kindly, and many people would count it as support.</p>"),
        ]),
        ("What the 2004 studies found", [
            "The " + a(G04, "2004 paper") + ", in the Journal of Personality and Social Psychology, reports four studies: a daily diary study of 154 undergraduates, a study of 59 dating couples, a study of 89 married couples, and a further diary study of 94 undergraduates. The abstract, as " + a(G04PM, "PubMed records it") + ", describes four studies of the intrapersonal and interpersonal consequences of seeking out others when good things happen.",
            "The first finding was about the person sharing. In the " + a(G04, "authors’ words") + ", telling others about positive events was associated with increased daily positive affect and well-being, above and beyond the impact of the positive event itself. In the fourth study, the more different people participants told about a positive event, the higher their positive mood and life satisfaction.",
            "The second finding was about the listener. In " + a(G04, "the dating couples") + ", active-constructive responses were positively correlated with commitment, satisfaction, intimacy and trust, and the other three kinds were mostly negatively correlated with them. In the married couples, only active-constructive responses were positively associated with better relationship quality.",
            "HTML:" + K.table("The four 2004 studies",
                ["Study", "Who took part", "Main finding"],
                [["1", "154 undergraduates, daily diary", "Sharing good news linked to more positive mood than the event alone"],
                 ["2", "59 dating couples", "Active-constructive responses linked to commitment, satisfaction, intimacy and trust; the other three, mostly negatively"],
                 ["3", "89 married couples", "Only active-constructive responses linked to better relationship quality"],
                 ["4", "94 undergraduates", "Telling more people linked to higher mood and life satisfaction"]],
                source='Source: <a href="' + G04 + '" target="_blank" rel="noopener">Gable, Reis, Impett and Asher (2004)</a>, Journal of Personality and Social Psychology 87.'),
            "The quiet response did not come out well. " + a(G04, "The authors write") + " that they did not offer a strong prediction about passive-constructive responses, which, in all three studies, were associated with poorer intrapersonal and interpersonal outcomes. A partner who is pleased but says little is, on this evidence, not experienced the way they intend.",
        ]),
        ("Good news compared with bad", [
            "A " + a(G06, "2006 study by Gable, Gonzaga and Strachman") + " went beyond questionnaires. Seventy-nine dating couples were videotaped discussing a recent positive event and a recent negative event, the person sharing rated how understood, validated and cared for they felt, and observers coded how the listener responded. Two months later, according to the abstract, responses to positive event discussions were more closely related to relationship well-being and break-up than responses to the negative ones.",
            "" + a(G06, "The authors conclude") + " that the findings point to the recurrent, but often overlooked, role that positive emotional exchanges play in building relationship resources. Only the abstract of this study could be read for this essay, so its effect sizes and the number of break-ups are not reported here.",
            "The comparison is the point. Support in a crisis is what people usually mean by being there for someone, and it matters. This study suggests that being there when things go right is at least as closely tied to how a relationship fares. It is also the more frequent test: " + a(GR10, "Gable and Reis") + " note that the frequency of positive events outweighs the frequency of negative events, about three positive to every one negative event.",
        ]),
        ("What the research cannot yet say", [
            "The original authors were candid about the limits. In the " + a(G04, "2004 paper") + " they note that they focused on the participant’s perception of the partner’s response without examining interaction directly, that the couple data were collected concurrently, and that they are unable to ascertain whether perceived responsiveness leads to relationship well-being, if relationship health leads to greater perceived responsiveness, or both. A happy couple may simply see each other’s responses more generously.",
            "Later work adds three complications. First, culture. A 2024 study of 915 European American, East Asian and South Asian participants, as " + a(SIM, "its abstract on the University of Minnesota research portal") + " reports, found that passive-constructive responses went with lower responsiveness and satisfaction for European Americans and East Asians, but with higher responsiveness and satisfaction for South Asians. A study of young adults in Malaysia, " + a(DENETTO, "published in 2021") + ", notes that findings on the passive-constructive response seem contradictory across the literature and that its impact is still not completely clear.",
            "Second, how the news is shared. In a diary study of 49 married couples, " + a(PAGANI, "Pagani and colleagues") + " found that simply disclosing a positive event was not linked to gains in self-esteem or relationship quality, while being explicit when disclosing it to the partner was. The sharer’s part matters as well as the listener’s. Gable and Reis, in their " + a(GR10, "2010 chapter") + ", note that people with low self-esteem, rather than basking in success, are more likely to worry about its potential pitfalls, and suggest this may make it harder for them to benefit from sharing good news.",
            "Third, training. An intervention that taught enthusiastic responding, reported by " + a(WOODS, "Woods and colleagues in 2015") + ", found no significant differences in reported relationship satisfaction or gratitude expression; its effects showed up only in how people perceived their partner: more gratitude received, and a partner they thought more satisfied.",
            "The original researchers have themselves qualified the quiet response. In their " + a(GR10, "2010 chapter") + ", Gable and Reis write that evidence for passive-constructive responses is more mixed, and that in certain circumstances they are beneficial. They also warn that unsuccessful attempts at sharing are likely to have detrimental consequences: telling someone good news is a small risk, and a poor response has a cost of its own.",
            "HTML:" + K.callout("warn", "What was not found",
                "<p>No meta-analysis of this research, and no large pre-registered replication, turned up in the search for this essay. That is not the same as saying none exists. It does mean the findings rest on a modest number of studies, most of them correlational.</p>"),
            "The field is still developing its theory. A " + a(PRG18, "2018 review by Peters, Reis and Gable") + " describes capitalization as a social process that affects both capitalizers and responders, and proposes a model of how the two sides interact.",
        ]),
        ("From the laboratory to an Army classroom", [
            "The idea travelled further than most findings in relationship science. When the US Army introduced resilience training for its soldiers, active constructive responding was part of it. " + a(MRT, "Reivich, Seligman and McBride, writing in 2011") + ", describe the skill as based on the work of Shelly Gable, list the four styles, and explain that each style is role-played and practised in small groups. The " + a(MONITOR, "APA’s Monitor magazine reported in 2009") + " that soldiers learn the importance of active and constructive responding, a positive psychology technique.",
            "" + a(MRT, "That paper") + " reports the non-commissioned officers’ reactions to the course, not whether the skill changed their relationships; the authors note that the comments represent only their immediate evaluation of the programme. The wider programme has been criticised. A " + a(STEEN, "2013 review by Steenkamp, Nash and Litz") + " argued that the programme’s own evaluation, which was not peer reviewed, showed at best very small differences between the trained and control groups, which call into question the incremental value of the program. That criticism does not single out this skill, but it is a reason not to cite the Army as evidence that the technique works.",
        ]),
        ("What this does and does not say", [
            "Taken together, the research supports a modest and useful claim. How people respond to a partner’s good news is linked to how the relationship is doing, enthusiastic engagement is the response most consistently linked to good outcomes, and quiet approval may land as less than it is meant to be, at least in some cultures. It does not show that learning a technique will fix a relationship, and it does not supply a script.",
            "Read practically, the questionnaire items describe what engagement looks like: asking questions, showing interest in the details, letting the other person tell it fully. The items describe genuine concern, not a performance of excitement.",
            "This connects to three other essays here. The pattern in " + ESSAY40 + " is the hard-times version of the same question, about what a partner’s response can and cannot give. " + ESSAY45.replace(">what repair", ">What repair") + " covers the moments after things go wrong, which this research suggests are only half the picture. And " + ESSAY42 + " looks at another set of questionnaires that measure how people perceive their partners, with similar limits.",
            "A related line of research, on how partners help each other grow towards their own ideals, is set out in " + MICHEL + ".",
        ]),
    ],
    note=[
        "Langston’s 1994 paper and the full text of the 2006 study could not be read; both are described through the sources linked where they appear.",
    ],
    faqs=[
        ("What is capitalization in relationships?",
         "Telling another person about something good that happened to you, and getting extra benefit from sharing it. The term comes from C. A. Langston (1994); Shelly Gable and Harry Reis narrowed it to the interpersonal sense and studied how partners respond."),
        ("What is active constructive responding?",
         "One of four ways of responding to good news described by Gable and colleagues in 2004: enthusiastic and engaged, for example asking questions about the event. The others are passive-constructive (quiet support), active-destructive (pointing out downsides) and passive-destructive (ignoring it)."),
        ("Is quiet support bad for a relationship?",
         "In the 2004 studies, quiet, understated support was linked to poorer outcomes. Later research suggests this varies: a 2024 study found it went with higher satisfaction for South Asian participants, unlike European American and East Asian participants."),
        ("Does responding enthusiastically make relationships last?",
         "Not proven. The studies are mostly correlational and based on how people perceive their partner. One 2006 study of 79 dating couples linked responses to good news with relationship well-being and break-up two months later, and one training study did not change relationship satisfaction."),
        ("Is the good news research used outside psychology?",
         "Yes. Active constructive responding was taught in the US Army's resilience training, as described in a 2011 paper, though that paper reports no evidence about its effects and the wider programme has been criticised."),
    ],
    related=[
        ("why-reassurance-is-never-enough", "Why reassurance is never enough, and what to do instead", "Relationships"),
        ("what-repair-after-an-argument-actually-involves", "What repair after an argument actually involves, and what the famous numbers miss", "Relationships"),
    ],
)

if __name__ == "__main__":
    newpost.build(POST)
