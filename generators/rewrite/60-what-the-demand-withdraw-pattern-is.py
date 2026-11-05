#!/usr/bin/env python3
"""Essay 60 :: what-the-demand-withdraw-pattern-is  (Relationships)

Sources fetched and read on 5 Nov 2026: Christensen and Heavey 1990
(Scilit abstract; reference confirmed in Ross et al. 2019); Holley, Sturm
and Levenson 2010 (PMC full text); Ross, Karney, Nguyen and Bradbury 2019
(full text, UCLA); Crenshaw, Christensen et al. 2016 (PMC); Schrodt, Witt
and Shimkowski 2014 (abstract) and ScienceDaily release; Heavey, Layne and
Christensen 1993 (Nova abstract); Christensen et al. 2006 (catalogue
abstract); Gottman Institute blog on stonewalling; Gottman and Levenson
2000 (full text, Berkeley); UCLA IBCT site; Christensen et al. 2004
(PubMed abstract); UCLA 2010 release and APA Monitor 2011; Baucom et al.
2011 (PMC); UCLA faculty page.
Not used: Christensen 1988 and Christensen and Shenk 1991 as primary sources
(not readable); the "100 bpm" flooding figure (not in a primary source).
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import newpost, postkit as K

EXT = ' target="_blank" rel="noopener"'
def a(url, text):
    return '<a href="%s"%s>%s</a>' % (url, EXT, text)

CH90 = "https://scilit.com/publications/710c12d311425c79b2842f8b54f14573"
HOLLEY = "https://pmc.ncbi.nlm.nih.gov/articles/PMC3014221"
ROSS = "https://marriage.psych.ucla.edu/wp-content/uploads/sites/213/2020/05/psp-pspi0000158.pdf"
CRENSHAW = "https://pmc.ncbi.nlm.nih.gov/articles/PMC5346477"
SCHRODT = "https://informahealthcare.com/doi/full/10.1080/03637751.2013.813632"
SCIDAILY = "https://www.sciencedaily.com/releases/2014/08/140804122903.htm"
HEAVEY93 = "https://scholars.nova.edu/en/publications/gender-and-conflict-structure-in-marital-interaction-a-replicatio-3/"
CROSS = "https://searchworks.jioinstitute.edu.in/articles/edb__22615455"
STONEWALL = "https://gottman.com/blog/the-four-horsemen-stonewalling"
GL2000 = "https://bpl.studentorg.berkeley.edu/docs/61-Timing%20of%20Divorce00.pdf"
IBCT = "https://ibct.psych.ucla.edu/about"
IBCT04 = "https://pubmed.ncbi.nlm.nih.gov/15065953/"
UCLA10 = "https://www.sciencedaily.com/releases/2010/04/100419151119.htm"
MONITOR = "https://www.apa.org/monitor/2011/01/christensen"
BAUCOM = "https://pmc.ncbi.nlm.nih.gov/articles/PMC3339273/"
UCLA = "https://www.psych.ucla.edu/faculty-page/achriste/"

ESSAY40 = '<a href="/writing/why-reassurance-is-never-enough">why reassurance is never enough</a>'
ESSAY45 = '<a href="/writing/what-repair-after-an-argument-actually-involves">what repair after an argument involves</a>'
ESSAY51 = '<a href="/writing/what-rumination-is">what rumination is</a>'

POST = dict(
    slug="what-the-demand-withdraw-pattern-is", num=60, cat="Relationships", read="auto",
    date="2026-11-05",
    gen="rewrite/60-what-the-demand-withdraw-pattern-is.py",
    title="What the demand-withdraw pattern is, and why it feeds itself",
    dek="One partner raises a problem and pushes for change. The other goes quiet, changes the subject or leaves the room. The pushing gets harder, and so does the retreat. Relationship researchers have studied this loop for decades, and the most useful finding is about who ends up in which role.",
    takeaway="The demand-withdraw pattern is a common way couples get stuck in conflict: one partner tries to discuss a problem, criticises and asks for change, and the other avoids the discussion. A meta-analysis of 74 studies found it associated, moderately overall, with worse relationship, communication and well-being outcomes, in both directions, and described the links as reciprocal rather than causal. Women are more often in the demanding role on average, but research suggests the role follows the issue: whoever wants the change tends to demand, and the same pattern appears in gay and lesbian couples. The pattern is thought to feed itself, with withdrawal inviting more insistent demands and those inviting more withdrawal. Its effects are not uniform, and therapy that helps couples identify the patterns that get them stuck has shown benefits.",
    sections=[
        ("What the pattern is", [
            "The demand-withdraw pattern is a loop in couple conflict: one partner raises a problem, criticises and asks for change, and the other avoids the discussion. Each response tends to provoke more of the other. Research suggests it is linked to lower satisfaction, and that the role a person takes depends more on who wants the change than on who they are.",
            "HTML:" + K.takeaways([
                "One partner demands change; the other avoids the discussion.",
                "A meta-analysis of 74 studies linked the pattern to worse relationship and communication outcomes.",
                "The link was about as strong whichever partner demanded.",
                "Whoever wants the change tends to demand, in men and women, and in same-sex couples.",
                "Researchers believe the pattern is self-perpetuating: withdrawal invites more demands, which invite more withdrawal.",
                "Its effects are not uniform, and the links are associations, not proven causes.",
            ]),
            "This essay sets out what the research found and where it is still uncertain. It is meant to help people recognise the pattern, not to assign blame to the partner in either role.",
            "HTML:" + K.callout("definition", "Demand and withdraw",
                "<p>As " + a(HOLLEY, "Holley, Sturm and Levenson") + " summarise the classic description, the pattern is characterised by one partner trying to discuss problems, criticising or blaming their partner, and requesting or demanding change, while the other partner tries to avoid discussion of the problem.</p>"),
        ]),
        ("Where the idea came from", [
            "Much of the research on the pattern comes from Andrew Christensen, a Distinguished Research Professor in the " + a(UCLA, "UCLA Department of Psychology") + " whose research interests include conflict in couples and couples therapy; " + a(HOLLEY, "later researchers") + " trace the classic description of the pattern to his work.",
            "In a 1990 study, Christensen and Heavey observed " + a(CH90, "31 couples in two conflict discussions") + ", each about a change one of the partners wanted. The abstract reports that wife-demand and husband-withdraw interaction was more likely than the reverse overall, but only when discussing a change the wife wanted. Both husband and wife were more likely to be demanding when discussing a change they wanted.",
            "The same study found a gender difference, but not the one usually assumed: men were overall more withdrawn than women, but women were not overall more demanding than men.",
        ]),
        ("How researchers measure it", [
            "There are two main ways to study the pattern. One is to watch it happen: couples are asked to discuss a real disagreement and their behaviour is rated. The " + a(HEAVEY93, "1993 study") + " described below, for example, had couples take part in two videotaped discussions.",
            "The other is to ask. The Communication Patterns Questionnaire asks each partner how they and their partner typically behave when a problem comes up. A " + a(CRENSHAW, "paper by Crenshaw, Christensen and colleagues") + ", published online in 2016, reports, citing earlier work, that all four scales of a revised version of the questionnaire distinguished distressed from non-distressed couples, and notes that it is widely used.",
            "Both methods have limits. Observed discussions are short and staged; questionnaires depend on how people see their own relationship. The findings below draw on both, which is one reason to take the overall pattern seriously.",
        ]),
        ("Who demands depends on the issue", [
            "The most useful finding in this research is that the roles follow the issue. A 1993 replication by " + a(HEAVEY93, "Heavey, Layne and Christensen") + ", with 29 married couples, found that when discussing the wives’ issues, wives were more demanding and husbands more withdrawing.",
            "A later study widened the test. In " + a(HOLLEY, "a 2010 study of 63 heterosexual, gay and lesbian couples") + ", Holley, Sturm and Levenson found that the demand-withdraw pattern was seen regardless of type of couple, and concluded that men and women are not inherently different in their tendencies to demand and withdraw. The more change one person wants relative to their partner, they write, the more likely that person is to demand while the partner withdraws, regardless of the sex of the partners.",
            "Why, then, do women demand more often on average? The same authors suggest the pattern may result from social conventions that afford men greater power and women less power: on this reading, the partner who is more satisfied with how things are has less reason to push for change.",
            "HTML:" + K.callout("warn", "Not a fixed trait",
                "<p>The popular version, that women nag and men withdraw, is not what the research shows. On average women are more often in the demanding role, but the role follows the issue and who wants the change, and the same pattern appears in couples of the same sex.</p>"),
        ]),
        ("What the pattern is linked to", [
            "The largest summary of the evidence is a " + a(SCHRODT, "2014 meta-analysis by Schrodt, Witt and Shimkowski") + ", which reviewed 74 studies with 14,255 participants. It found a moderate, meaningful relationship between demand-withdraw and overall outcomes, a correlation of .360. The links were stronger for relational outcomes (.423) and communication outcomes (.418) than for demographic (.239) and well-being outcomes (.249).",
            "Two details stand out. The direction did not matter much: wife-demand and husband-withdraw had a correlation of .380 with outcomes, and husband-demand and wife-withdraw .392. And the links were stronger in distressed or clinical samples (.413) than in others (.345).",
            "HTML:" + K.table("Demand-withdraw and outcomes in the 2014 meta-analysis",
                ["Outcome or group", "Correlation"],
                [["All outcomes", ".360"],
                 ["Relational outcomes", ".423"],
                 ["Communication outcomes", ".418"],
                 ["Well-being outcomes", ".249"],
                 ["Wife demands, husband withdraws", ".380"],
                 ["Husband demands, wife withdraws", ".392"]],
                source='Source: <a href="' + SCHRODT + '" target="_blank" rel="noopener">Schrodt, Witt and Shimkowski (2014)</a>, Communication Monographs, abstract. 74 studies, 14,255 participants.'),
            "The authors are careful about what this means. They describe the effects as reciprocal associations rather than causal links: a struggling relationship may produce the pattern as much as the pattern produces the struggle. A " + a(SCIDAILY, "press release") + " about the study adds that it is also a very hard pattern to break, and quotes Schrodt: “It’s a real, serious sign of distress in the relationship.”",
        ]),
        ("Why it feeds itself", [
            "The pattern is usually described as a loop. Ross, Karney, Nguyen and Bradbury, in a " + a(ROSS, "2019 paper") + ", put it this way: the demand-withdraw pattern is believed to be self-perpetuating, with disengagement inviting increasingly insistent requests for change, thus evoking even greater avoidance and defensiveness from the partner. Note the word believed: it is the field’s understanding of the mechanism, not a measured fact.",
            "Part of what keeps the loop going is how each partner sees it. In the " + a(SCIDAILY, "same press release") + ", Schrodt explains that partners get locked in this pattern, largely because they each see the other as the cause. To give this essay’s own illustration: the person demanding sees withdrawal as the problem, and the person withdrawing sees the demands as the problem. Both are describing the same loop from different points in it.",
            "HTML:" + K.stages("How the loop turns", [
                ("01", "A request", "One partner raises something they want to change."),
                ("02", "A retreat", "The other avoids the discussion, goes quiet or changes the subject."),
                ("03", "More pressure", "Feeling unheard, the first partner pushes harder or criticises."),
                ("04", "More retreat", "Feeling attacked, the second partner withdraws further."),
            ], source='A simplified description following <a href="' + ROSS + '" target="_blank" rel="noopener">Ross et al. (2019)</a>, who note that the pattern is believed to be self-perpetuating.'),
            "A related idea comes from John Gottman’s work. The " + a(STONEWALL, "Gottman Institute") + " describes stonewalling as what happens when the listener shuts down because they feel overwhelmed or physiologically flooded, and recommends that a break from the argument should last at least twenty minutes, since it will take that much time for your bodies to physiologically calm down. Withdrawal, on this view, is sometimes less a tactic than a body overloaded. The institute also says that men are consistently more likely to stonewall than women, and that when women stonewall, it is quite predictive of divorce; these are its statements, not figures from a study linked here.",
        ]),
        ("What it predicts", [
            "Studies that followed couples over time suggest the pattern matters for the future of a relationship, though the evidence is mixed in an important way. In the " + a(HEAVEY93, "1993 study") + ", wife-demand and husband-withdraw interaction predicted a decline in wives’ satisfaction a year later, while husband-demand and wife-withdraw interaction predicted an increase in wives’ satisfaction.",
            "Gottman and Levenson, in a " + a(GL2000, "2000 study following couples for 14 years") + ", built a measure of the wife-demand and husband-withdraw pattern from criticism and stonewalling, and found it predicted both earlier divorcing and later divorcing, with correlations of .32 and .27. The " + a(CRENSHAW, "paper by Crenshaw, Christensen and colleagues") + " summarises the wider literature: higher levels of demand-withdraw behaviour are associated with greater relationship distress and with a greater likelihood of divorce.",
            "The pattern is also not always harmful. The " + a(ROSS, "2019 study") + " replicated the harmful effects of the pattern on wives’ satisfaction among relatively affluent couples, while documenting benefits of it among relatively disadvantaged couples. Its authors suggest that men’s withdrawal appears to be maladaptive when couples have resources and capacities to enact desired changes, but may be adaptive when those resources and capacities are lacking. One way to read that, which is this essay’s gloss: when a problem cannot be solved, stepping back from it may protect the relationship.",
        ]),
        ("Across cultures", [
            "The pattern is not only an American one. A " + a(CROSS, "2006 study by Christensen and colleagues") + " of 363 participants in Brazil, Italy, Taiwan and the United States found that woman-demand and man-withdraw communication was significantly more likely than the reverse, and that differences between partners in desire for closeness versus independence were associated with more demand-withdraw communication.",
            "Across all four countries, the same study found, constructive communication was positively associated with relationship satisfaction, whereas demand-withdraw communication was negatively associated with it. The pattern, and its link to satisfaction, travelled across very different cultures.",
            "The same study adds a clue about why the roles fall as they do. The abstract notes that some evidence suggested women wanted greater closeness versus independence in their relationships than did men. Combined with the finding that differences in that desire were associated with more of the pattern, one possible reading, which is this essay’s interpretation, is that the partner who wants more connection pushes and the partner who is content with less steps back.",
        ]),
        ("What helps", [
            "Because both partners are inside the loop, approaches that help them see it from outside seem promising. Integrative Behavioral Couple Therapy, developed by Christensen and the late Neil S. Jacobson, aims, according to its " + a(IBCT, "UCLA site") + ", to integrate the twin goals of acceptance and change, partly by helping couples identify the patterns that get them stuck.",
            "It has been tested in a large trial. In " + a(IBCT04, "a 2004 study") + " of 134 seriously and chronically distressed married couples, 71% of couples receiving this therapy and 59% receiving a traditional behavioural couple therapy were reliably improved or recovered. At five years, the " + a(MONITOR, "APA Monitor reported") + ", about half the couples in each group still showed clinically significant improvement, and the difference between the two therapies had disappeared. None of the sources linked here says the therapy targets the demand-withdraw pattern specifically.",
            "Five years on, the picture was mixed but encouraging. A " + a(UCLA10, "UCLA release") + " on the follow-up reported that about half the couples were significantly improved, about a quarter were separated or divorced, and about a quarter were unchanged. A " + a(BAUCOM, "2011 analysis of the same trial") + " records that 98 of the 134 couples, 73.1%, were still married at five years. For couples who began seriously distressed, that is a meaningful result, though not a cure.",
            "HTML:" + K.callout("note", "Not a substitute for help",
                "<p>This essay describes research. Couples who feel stuck in this loop, or in any pattern that is causing distress, may benefit from working with a qualified couples therapist. Withdrawal that is about fear or safety is a different matter from the pattern described here.</p>"),
        ]),
        ("What this does and does not say", [
            "Read carefully, the research supports a clear and useful picture. The demand-withdraw loop is common, it is linked to worse outcomes in either direction, and the roles in it depend largely on who wants the change. That makes it a pattern between two people, not a flaw in one of them. The causal story is less certain than the loop makes it feel, and the pattern is not harmful in every circumstance.",
            "In practice, this essay’s suggestion, drawing on the research above, is naming the loop together rather than blaming the other person for their part in it, and noticing which role each person tends to take on which issue. The person withdrawing may need a break to calm down; the person demanding may need to know the issue will actually be returned to.",
            "Other essays here meet the pattern at different points. " + ESSAY45.replace(">what repair", ">What repair") + " covers what helps after an argument, including breaks and returning to the issue. " + ESSAY40.replace(">why reassurance", ">Why reassurance") + " describes another loop with a similar shape, where asking again brings less relief each time. And " + ESSAY51 + " looks at the inward version of going round in circles.",
        ]),
    ],
    note=[
        "The 2014 meta-analysis is described from its abstract, notes and press release. Correlations describe associations across studies, not effects on any one couple.",
    ],
    faqs=[
        ("What is the demand-withdraw pattern?",
         "A pattern in couple conflict where one partner tries to discuss a problem, criticises and asks for change, and the other avoids the discussion. Each response tends to provoke more of the other."),
        ("Is it always the woman who demands?",
         "No. Women are more often in the demanding role on average, but research suggests the role follows the issue: whoever wants the change tends to demand. A 2010 study found the same pattern in gay and lesbian couples."),
        ("Is the demand-withdraw pattern bad for relationships?",
         "A 2014 meta-analysis of 74 studies found it associated, moderately overall, with worse relationship, communication and well-being outcomes, whichever partner demanded. The authors describe the links as associations rather than proven causes, and one 2019 study found benefits among some disadvantaged couples."),
        ("Why is the pattern so hard to break?",
         "It is believed to be self-perpetuating: withdrawal invites more insistent demands, which invite more withdrawal. Partners also tend to see each other as the cause, which keeps each in their role."),
        ("Does couples therapy help with demand-withdraw?",
         "Integrative Behavioral Couple Therapy aims to help couples identify the patterns that get them stuck. In a trial of 134 distressed couples, most improved, and about half still showed clinically significant improvement five years later."),
    ],
    related=[
        ("what-repair-after-an-argument-actually-involves", "What repair after an argument actually involves, and what the famous numbers miss", "Relationships"),
        ("why-reassurance-is-never-enough", "Why reassurance is never enough, and what to do instead", "Relationships"),
    ],
)

if __name__ == "__main__":
    newpost.build(POST)
