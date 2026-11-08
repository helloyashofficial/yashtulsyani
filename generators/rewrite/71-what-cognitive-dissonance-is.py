#!/usr/bin/env python3
"""Essay 71 :: what-cognitive-dissonance-is  (Psychology)

Sources fetched and read on 8 Nov 2026: Festinger and Carlsmith (1959),
Journal of Abnormal and Social Psychology, full text at Classics in the
History of Psychology (York University); APS Observer (2024) and the
Sabanci University repository record of Vaidis and others (2024),
Advances in Methods and Practices in Psychological Science; TIME essay
(Goldwag, 2024) on When Prophecy Fails; Kelly (2026), Journal of the
History of the Behavioral Sciences, author copy; Woodyard (1972),
Psychonomic Science, abstract and references.
Not used: Festinger's 1957 book, which could not be read; the details of
Bem's 1967 paper beyond its title, which could not be read.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import newpost, postkit as K

EXT = ' target="_blank" rel="noopener"'
def a(url, text):
    return '<a href="%s"%s>%s</a>' % (url, EXT, text)

FC = "https://www.yorku.ca/pclassic/Festinger/index.htm"
APS = "https://www.psychologicalscience.org/observer/multilab-replication-cognitive-dissonance"
VAID = "https://research.sabanciuniv.edu/id/eprint/49125/"
TIME = "https://time.com/6960441/ufo-cultists-political-paranoia-essay"
KELLY = "https://gwern.net/doc/psychology/cognitive-bias/2025-kelly.pdf"
WOOD = "https://link.springer.com/article/10.3758/BF03332824"

ESSAY42 = '<a href="/writing/what-attachment-styles-actually-measure">what attachment styles actually measure</a>'
ESSAY66 = '<a href="/writing/what-the-impostor-phenomenon-is">what the impostor phenomenon is</a>'
ESSAY61 = '<a href="/writing/what-learned-helplessness-actually-showed">what learned helplessness actually showed</a>'
ESSAY47 = '<a href="/writing/why-we-blame-the-people-we-love">why we blame the people we love</a>'

POST = dict(
    slug="what-cognitive-dissonance-is", num=71, cat="Psychology", read="auto",
    date="2026-11-08",
    gen="rewrite/71-what-cognitive-dissonance-is.py",
    title="What cognitive dissonance is, and how well the classic evidence holds up",
    dek="Cognitive dissonance is the idea that when what we do clashes with what we believe, we tend to change the belief. It rests on famous studies: students paid a dollar to lie, and a group that expected the end of the world. Recent work has put both under strain.",
    takeaway="Cognitive dissonance is the discomfort Leon Festinger proposed arises when a person’s actions and beliefs conflict, and which they may reduce by changing their private opinion. In Festinger and James Carlsmith’s 1959 experiment, Stanford students who were paid one dollar to tell a waiting student that a dull task was enjoyable later rated the task as more enjoyable than students paid twenty dollars. The earlier book When Prophecy Fails described a group that kept believing after its prophecy of the end of the world failed; a 2026 archival study argues its central claims were false. In 2024 a replication across 39 labs in 19 countries, with 4,898 participants, found that writing a counterattitudinal essay did shift attitudes, but that having a choice about writing it, the key ingredient in the theory, made no difference. The idea remains useful; its classic evidence is weaker than textbooks suggest.",
    sections=[
        ("What cognitive dissonance is", [
            "Cognitive dissonance is the uncomfortable tension that, according to Leon Festinger’s theory, arises when a person holds beliefs and behaviours that conflict. The theory predicts that people often reduce it by changing a belief to fit what they have done, especially when they had little outside reason for doing it.",
            "HTML:" + K.takeaways([
                "Festinger proposed that conflict between action and belief creates pressure to change the belief.",
                "In 1959, students paid one dollar to lie about a dull task later rated it as more enjoyable than those paid twenty.",
                "When Prophecy Fails described believers holding on after a failed prophecy; a 2026 study argues its central claims were false.",
                "A 2024 replication across 39 labs found essay-writing shifted attitudes, but choice made no difference.",
                "The idea remains plausible; much of its classic evidence is weaker than its fame.",
            ]),
            "This essay sets out what the theory says, what the founding experiment actually found, and what has happened when researchers looked again.",
            "HTML:" + K.callout("definition", "Cognitive dissonance",
                "<p>The tension that, in Festinger’s theory, follows when a person does or says something contrary to private opinion. As " + a(FC, "Festinger and Carlsmith") + " put it in 1959, “One way in which the dissonance can be reduced is for the person to change his private opinion.”</p>"),
        ]),
        ("The question Festinger asked", [
            "Leon Festinger and James Carlsmith opened their " + a(FC, "1959 paper") + " in the Journal of Abnormal and Social Psychology with a simple question: “What happens to a person’s private opinion if he is forced to do or say something contrary to that opinion?”",
            "The theory gave a two-part answer, which the paper set out in its summary. First, there will be a tendency for him to change his opinion so as to bring it into correspondence with what he has done or said. Second, the stronger the pressure that produced the behaviour, the weaker that tendency. A large reward or a strong threat explains the behaviour on its own, so there is less need to change one’s mind. A small reward does not, so the mind has to do the work.",
            "That second prediction is what made the theory interesting. Common sense, and much of the psychology of the time, suggested that paying people more would make them like what they were paid for more. Dissonance theory predicted the reverse.",
        ]),
        ("The one-dollar experiment", [
            "The experiment, as the " + a(FC, "paper") + " describes it, used seventy-one male students in the introductory psychology course at Stanford University. Each spent an hour on deliberately dull tasks, half an hour on each: putting 12 spools onto a tray, emptying the tray, refilling it with spools, and then turning pegs on a board a quarter turn clockwise, one after another.",
            "Afterwards, the experimenter asked some students to help by telling the next participant, who was waiting outside, that the tasks had been fun. The waiting student was actually an undergraduate hired for this role. The participant was to say something like: “It was very enjoyable, I had a lot of fun, I enjoyed myself.” Some were offered a dollar for doing so, others twenty dollars. A control group did the tasks without being asked to say anything.",
            "Later, in what looked like a separate interview, everyone rated how enjoyable the tasks had been. The control group’s average rating was −0.45, slightly negative. The twenty-dollar group’s was −0.05, close to the control group. The one-dollar group’s was +1.35, clearly positive. The paper reports that the difference between the one-dollar and twenty-dollar groups was significant at the .03 level.",
            "HTML:" + K.table("How enjoyable were the tasks?",
                ["Group", "Average rating", "Reading"],
                [["Control, no lie", "−0.45", "Slightly negative"],
                 ["Paid $20 to say it was fun", "−0.05", "About the same as control"],
                 ["Paid $1 to say it was fun", "+1.35", "Clearly positive"]],
                source='Source: <a href="' + FC + '" target="_blank" rel="noopener">Festinger and Carlsmith (1959)</a>. Ratings ran from −5 to +5.'),
        ]),
        ("Reading the result carefully", [
            "The result is striking, and the authors wrote that it strongly corroborates the theory. But the details are worth knowing. The " + a(FC, "paper") + " says the data from 11 of the 71 participants had to be discarded, mostly because they grew suspicious, refused the money, or otherwise broke the cover story. The final comparison, in the paper’s words, left 20 participants in each of the three conditions.",
            "The interpretation the authors favoured is easy to state. On this reasoning, twenty dollars was a sufficient reason on its own for telling a small lie, so those students had no need to persuade themselves of anything. One dollar was not enough to explain the lie away. On the theory, those students resolved the tension by coming to believe, a little, that the tasks had not been so bad after all.",
            "Only one of the four interview questions showed a clear effect. Participants were also asked how much they had learned, how scientifically important the experiment was, and whether they would take part in a similar one. The paper notes that the willingness to take part results do not yield high levels of statistical significance, and the learning question showed only negligible differences.",
            "None of this means the result was wrong. It means the most famous experiment in the field was small, with a difference significant at a level that would be treated cautiously today, and with one clear outcome among several measured.",
        ]),
        ("When prophecy failed", [
            "The theory’s other famous illustration came earlier, from a 1956 book, When Prophecy Fails, by Festinger, Henry Riecken and Stanley Schachter. According to a " + a(TIME, "2024 essay in TIME") + ", it followed a small Chicago-based group, the Seekers, led by Dorothy Martin, called Mrs Marian Keech in the book, who predicted the world would end on 21 December 1954. Festinger sent observers to join the group and take notes.",
            "The book’s story, as TIME summarises it, is that when the prophecy failed, the more casual members drifted away, but the core members doubled down on their belief and on spreading it. That became a classic example of dissonance reduction: people who had given up a great deal for a belief found a way to keep it.",
            "A 2026 archival study disputes that story. Writing in the Journal of the History of the Behavioral Sciences, the independent scholar " + a(KELLY, "Thomas Kelly") + " used newly unsealed papers of Festinger’s to argue that the book’s central claims are false, and that the authors knew they were false. Kelly reports that the group actively proselytized well before the prophecy failed, contrary to the book’s account, and that it did not increase its efforts afterwards.",
            "Kelly also describes the observers as far from passive. He reports that Riecken, under the name Brother Henry, was treated as a spiritual figure by the group and later admitted he had precipitated key events. These are Kelly’s findings and interpretations; they are recent, and how other historians respond remains to be seen. But they mean the book can no longer be cited as clean evidence for the theory.",
            "Kelly’s evidence comes largely from a box of Festinger’s papers at the Bentley Historical Library that had only recently been unsealed, along with university archives, a UFO collection and published UFO magazines. He also reports that another observer performed fake automatic writing for a group member, and that Dorothy Martin herself told a UFO magazine in 1955 that she “really didn’t expect to be picked up physically by the saucerman.” Martin, he writes, later renamed herself Sister Thedra and kept teaching, but never mentioned the failed prophecy to her later followers.",
        ]),
        ("The 2024 replication", [
            "The most direct recent test was a large replication of the induced-compliance paradigm, the experimental family the one-dollar study belongs to. According to its " + a(VAID, "abstract") + ", the study, led by David Vaidis and published in 2024 in Advances in Methods and Practices in Psychological Science, involved 39 labs from 19 countries, 14 languages and 4,898 participants.",
            "The design, as the " + a(APS, "Association for Psychological Science") + " describes it, was a constructive, not exact, replication of a 1983 study by Croyle and Cooper: it kept the logic of that study while updating the materials for many countries and languages. Students wrote an essay supporting a tuition increase, which most opposed. Some were given a choice about writing it, others were simply told to, and a control group wrote a neutral essay.",
            "The result split in two. Writing the counterattitudinal essay did shift attitudes compared with the neutral essay. But choice made no difference: there was no significant attitude difference between the high-choice and low-choice groups. “In other words, we did not replicate the effect of choice on attitude change,” Vaidis told the APS. The authors write that the findings call into question whether the induced-compliance paradigm offers solid evidence for cognitive dissonance, at least in the form it has usually taken.",
            "HTML:" + K.compare("What the 2024 replication found", [
                ("Supported", ["Writing an essay against your view shifted attitudes"], ["Does not show why"], "Saying it moves you a little."),
                ("Not supported", ["Choice was meant to be the key ingredient"], ["No difference between high and low choice"], "The theory’s signature prediction failed here."),
            ], source='Sources: <a href="' + VAID + '" target="_blank" rel="noopener">Vaidis and others (2024)</a>; <a href="' + APS + '" target="_blank" rel="noopener">APS Observer (2024)</a>.'),
        ]),
        ("Other explanations", [
            "Dissonance was never the only possible explanation for these results. From the late 1960s, a rival account, self-perception theory, associated with the psychologist Bem and his 1967 paper " + a(WOOD, "Self-perception: An alternative interpretation of cognitive dissonance phenomena") + ", proposed that people may simply infer their attitudes from their own behaviour, much as an observer would, without any inner discomfort being involved.",
            "Researchers spent years trying to tell the two accounts apart, with mixed results. One 1972 study, by H. D. Woodyard, reported results it interpreted as consistent with cognitive dissonance theory predictions and nonsupportive of self-perception theory assumptions. The 2024 replication does not settle that old argument either. Its finding that writing the essay shifted attitudes regardless of choice fits several explanations.",
            "The authors of the replication were careful not to declare the theory dead. In the " + a(APS, "APS article") + ", Sleegers, one of its authors, noted that “Many of the established findings from the cognitive dissonance literature stem from papers that are decades old,” and the team’s stated aim was to prompt more research and a reassessment, not to close the question.",
        ]),
        ("What it is still good for", [
            "As an everyday idea, cognitive dissonance points at something real: people do explain their own choices to themselves, and those explanations can drift towards whatever makes the choice look sensible. What the evidence questions is the specific mechanism, discomfort that is reduced by changing a belief, and the specific conditions, such as low reward and free choice, said to strengthen it.",
            "A practical version of the idea survives the doubts. When you notice yourself defending a decision more fiercely the more it cost you, or describing something you were pushed into as something you wanted all along, it is worth asking whether the account is a reason or a repair. That question does not depend on which psychological mechanism turns out to be right.",
            "HTML:" + K.callout("warn", "A note on using the term",
                "<p>Calling someone’s view “just cognitive dissonance” is a way of dismissing it without engaging it. The research describes a tendency measured on average in experiments; it does not tell you why a particular person believes what they do, and it applies to the person using the term as much as to anyone else.</p>"),
        ]),
        ("What this does and does not say", [
            "Read carefully, the evidence supports a modest version of the idea: saying or doing something against one’s view can shift that view a little. It does not, on current evidence, support the stronger textbook claims that small rewards reliably produce more change than large ones, that free choice is essential, or that a failed prophecy makes believers more fervent.",
            "Other essays here look at related ground. " + ESSAY66.replace(">what the impostor", ">What the impostor") + " describes another famous idea whose evidence turned out more mixed than its reputation. " + ESSAY61.replace(">what learned", ">What learned") + " follows a theory its own founders reversed. " + ESSAY47.replace(">why we blame", ">Why we blame") + " asks how we explain other people’s actions. And " + ESSAY42 + " looks at how much a psychological label depends on how it is measured.",
        ]),
    ],
    note=[
        "The 1959 ratings use the scale described in the paper, from −5 to +5. Kelly’s 2026 findings are his own and are presented as such.",
    ],
    faqs=[
        ("What is cognitive dissonance in simple terms?",
         "The discomfort, in Leon Festinger’s theory, of acting against what you believe, which people may reduce by changing the belief to match what they did."),
        ("What was the one-dollar experiment?",
         "A 1959 study in which Stanford students paid one dollar to tell another student a dull task was enjoyable later rated it as more enjoyable than students paid twenty dollars."),
        ("Has cognitive dissonance been replicated?",
         "Partly. A 2024 replication across 39 labs found that writing an essay against one’s view shifted attitudes, but having a choice about writing it, a key prediction of the theory, made no difference."),
        ("Is When Prophecy Fails accurate?",
         "A 2026 archival study by Thomas Kelly argues that the book’s central claims are false, including that the group proselytized more after its prophecy failed, and that the observers influenced events."),
        ("Is cognitive dissonance real?",
         "People do sometimes adjust their views to fit what they have done, but the specific mechanism and conditions the theory proposed have weaker support than textbooks often suggest."),
    ],
    related=[
        ("what-the-impostor-phenomenon-is", "What the impostor phenomenon is, and why it was never meant to be a syndrome", "Psychology"),
        ("what-learned-helplessness-actually-showed", "What learned helplessness actually showed, and how its discoverers changed their minds", "Psychology"),
    ],
)

if __name__ == "__main__":
    newpost.build(POST)
