#!/usr/bin/env python3
"""Essay 66 :: what-the-impostor-phenomenon-is  (Psychology)

Sources fetched and read on 7 Nov 2026: ProQuest record for Clance and Imes
(1978) (citation only; the paper itself could not be read); Clance and
O'Toole (1988), author's site; Bravata and others (2020), Journal of
General Internal Medicine, abstract via Springer Medicine; APA Monitor
(Abramson, 2021); gradPSYCH (Weir, 2013); MIT News (Dizikes, 2022) on
Tewfik's Academy of Management Journal study; Feenstra and others (2020),
Frontiers in Psychology.
Not used: the widely repeated claim that 70 per cent of people have
impostor feelings, which no fetched source supports; details of the 1978
paper beyond what Clance and O'Toole report.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import newpost, postkit as K

EXT = ' target="_blank" rel="noopener"'
def a(url, text):
    return '<a href="%s"%s>%s</a>' % (url, EXT, text)

PQ = "https://www.proquest.com/docview/614350434"
CO88 = "https://www.paulineroseclance.com/pdf/ip_internal_barrier_to_empwrmnt_and_achv.pdf"
BRAV = "https://www.springermedicine.com/anxiety/prevalence-predictors-and-treatment-of-impostor-syndrome-a-syste/21827036"
MON = "https://www.apa.org/monitor/2021/06/cover-impostor-phenomenon"
GRAD = "https://www.apa.org/gradpsych/2013/11/fraud"
MIT = "https://news.mit.edu/2022/imposter-syndrome-upside-0415"
FEEN = "https://www.frontiersin.org/articles/10.3389/fpsyg.2020.575024/text"

ESSAY42 = '<a href="/writing/what-attachment-styles-actually-measure">what attachment styles actually measure</a>'
ESSAY56 = '<a href="/writing/what-the-spotlight-effect-is">what the spotlight effect is</a>'
ESSAY61 = '<a href="/writing/what-learned-helplessness-actually-showed">what learned helplessness actually showed</a>'
ESSAY62 = '<a href="/writing/what-spinoza-meant-by-hope-and-fear">what Spinoza meant by hope and fear</a>'
ESSAY71 = '<a href="/writing/what-cognitive-dissonance-is">what cognitive dissonance is</a>'

POST = dict(
    slug="what-the-impostor-phenomenon-is", num=66, cat="Psychology", read="auto",
    date="2026-11-07",
    gen="rewrite/66-what-the-impostor-phenomenon-is.py",
    title="What the impostor phenomenon is, and why it was never meant to be a syndrome",
    dek="Impostor syndrome has become a familiar phrase in working life: the sense that you are not as capable as others think, and will soon be found out. The psychologists who first described it in 1978 called it a phenomenon, not a syndrome, and the research since then is more mixed, and more interesting, than the label suggests.",
    takeaway="In 1978 the psychologists Pauline Rose Clance and Suzanne Imes described the impostor phenomenon, which Clance later defined as an internal experience of intellectual phoniness, among 150 highly successful women they saw in therapy, groups and college classes. People with these feelings credit success to hard work, luck, knowing the right people or charm rather than ability, and get caught in a cycle of anxious over-preparation or procrastination. Later research found that men experience it about as often as women. A 2020 systematic review of 62 studies found prevalence estimates ranging from 9 to 82 per cent, depending largely on how it was measured, frequent overlap with depression and anxiety, and no published studies of treatment. Clance has said it is not a clinical diagnosis. Researchers now also stress the role of the setting, and one 2022 study found that people with more workplace impostor thoughts were rated as more interpersonally effective.",
    sections=[
        ("What the impostor phenomenon is", [
            "The impostor phenomenon is a persistent feeling, in people with a real record of achievement, that they are not really as able as others believe and will eventually be exposed. They tend to credit their successes to luck or hard work rather than ability. It was first described in 1978, and it is an experience, not a medical diagnosis.",
            "HTML:" + K.takeaways([
                "Clance and Imes described it in 1978, among 150 highly successful women they saw in therapy, groups and college classes.",
                "People credit success to hard work, luck, connections or charm, not ability.",
                "Later research found men experience it about as often as women.",
                "Prevalence estimates range from 9 to 82 per cent, depending on how it is measured.",
                "It often overlaps with depression and anxiety, and no treatment trials had been published by 2020.",
                "One of its originators prefers phenomenon to syndrome; it is not a clinical diagnosis.",
            ]),
            "This essay sets out what the original authors described, what later studies measured, and where the popular idea goes further than the evidence.",
            "HTML:" + K.callout("definition", "Impostor phenomenon",
                "<p>In the words of " + a(CO88, "Clance and O’Toole") + ", “an internal experience of intellectual phoniness”. The popular name, impostor syndrome, is not the term its originators chose.</p>"),
        ]),
        ("Where the idea came from", [
            "The term comes from a 1978 paper by two psychologists, Pauline Rose Clance and Suzanne Imes, titled " + a(PQ, "The imposter phenomenon in high achieving women: Dynamics and therapeutic intervention") + ", published in the journal Psychotherapy. It came out of clinical work, not a survey.",
            "Writing ten years later, " + a(CO88, "Clance and Maureen O’Toole") + " described the original sample: 150 highly successful women, in fields such as law, nursing, medicine, social work and university teaching, together with graduate and undergraduate students. They were people with real achievements who still felt they did not deserve them.",
            "The first paper focused on women, and according to " + a(GRAD, "gradPSYCH") + ", Clance and Imes initially believed the phenomenon affected only women. That changed. Clance and O’Toole report that later research indicated that men do experience the phenomenon with as much frequency as women, though men may be less likely to admit it. They even cite one study of university faculty, by Topping in 1983, in which men scored higher than women. The authors still argue that the phenomenon may hold women back more, partly, they suggest, because women receive less of the encouragement offered to men and may carry unresolved dilemmas from childhood. The same 2013 article in the APA’s gradPSYCH notes that a later review found that men, too, can have the unenviable experience of feeling like frauds.",
        ]),
        ("The impostor cycle", [
            "Clance and O’Toole describe a pattern that keeps the feeling going, which they call the impostor cycle. Faced with a task, the person feels doubt and fear. They respond either by over-preparing or by procrastinating. They succeed and receive praise, yet the cycle is reinforced rather than broken, and the next task brings the same doubt. Elsewhere the authors note that such people credited their success to hard work or luck.",
            "The " + a(CO88, "1988 paper") + " lists other features its authors saw in clients. Among them are a dread of evaluation, a terror of failure and of looking foolish, guilt about success, difficulty taking in praise, and a habit of crediting success to hard work, luck, knowing the right people, being in the right place at the right time, or charm, rather than ability, while remembering negative feedback as proof of what is lacking. One item on Clance’s scale asks whether people feel discouraged if they are not “the best” or at least “very special”. The authors note that some held the belief that they must suffer in order to succeed. They also report, citing a 1984 study, that introverted people are much more likely to have high impostor phenomenon scores.",
            "HTML:" + K.stages("The impostor cycle", [
                ("1", "A task arrives", "Doubt and fear about whether one is good enough."),
                ("2", "Over-prepare or put it off", "Either far more work than needed, or putting the task off."),
                ("3", "Success", "The task goes well, often very well."),
                ("4", "Discount it", "Praise arrives, but the cycle is reinforced and the doubt returns."),
            ], source='Based on <a href="' + CO88 + '" target="_blank" rel="noopener">Clance and O’Toole (1988)</a>.'),
            "Clance and O’Toole also describe family patterns some clients reported, such as being told they were not the bright one in the family, or growing up with the message that a truly bright person finds things effortless. These are clinical observations from therapy, not findings from controlled studies.",
        ]),
        ("How common is it?", [
            "A figure often repeated online is that 70 per cent of people experience impostor feelings at some point. This essay could not find a primary source for that number. A widely cited overview of the evidence is a " + a(BRAV, "2020 systematic review") + " in the Journal of General Internal Medicine by Bravata and colleagues.",
            "The " + a(BRAV, "review") + " found that 62 studies of 14,161 participants met its criteria. Prevalence rates varied widely from 9 to 82 per cent, largely depending on the screening tool and cutoff used to assess symptoms. Put simply, how common impostor feelings are depends heavily on where the line is drawn. The review found it common in both men and women, often comorbid with depression and anxiety, and linked to weaker job performance, lower job satisfaction and burnout.",
            "Two limits stand out. The review notes that the studies were heterogeneous and that publication bias may be present. And, strikingly, no published studies evaluated treatments for this condition. Much of the advice offered about impostor feelings, in other words, has not been tested in trials.",
            "The most widely used measure is Clance’s own questionnaire. According to the " + a(CO88, "1988 paper") + ", it has 20 items rated from 1, not at all true, to 5, very true, and a cutoff score of 60 is recommended to identify people with the phenomenon. Choices like that cutoff are part of why prevalence estimates vary so much.",
            "HTML:" + K.table("What the 2020 review found",
                ["Question", "Finding"],
                [["How many studies?", "62 studies, 14,161 participants"],
                 ["How common?", "9 to 82 per cent, depending on tool and cutoff"],
                 ["Men or women?", "Common in both"],
                 ["Linked with?", "Depression, anxiety, burnout, lower job satisfaction"],
                 ["Treatments tested?", "No published studies"]],
                source='Source: <a href="' + BRAV + '" target="_blank" rel="noopener">Bravata and others (2020)</a>.'),
        ]),
        ("Phenomenon, not syndrome", [
            "The popular name gets one thing wrong in its originator’s eyes. According to the " + a(MON, "APA’s Monitor on Psychology") + " in 2021, Clance prefers the words phenomenon or experience to syndrome, and notes that impostor phenomenon isn’t a clinical diagnosis. “It’s a phenomenon experienced by many, and remembering that can help normalize it,” she said.",
            "The distinction matters. A syndrome sounds like a disorder that some people have and others do not, located inside the person. A phenomenon is something that happens to people, often in particular situations. That opens the question of what situations make it more likely, and it changes how people can talk about it: as something many share, rather than as a private defect.",
        ]),
        ("The role of the setting", [
            "Researchers have increasingly argued that impostor feelings are not only an individual trait. A " + a(FEEN, "2020 paper in Frontiers in Psychology") + " by Feenstra and colleagues, which puts syndrome in quotation marks in its title, argues that research has mostly treated the feelings as an individual problem, and calls for attention to the role of the environment in eliciting people’s impostor feelings, and for more structural and effective solutions.",
            "The APA Monitor article makes a similar point with specific examples. It reports that the psychologist Kevin Cokley, who has studied the phenomenon since 2013, says Black, Indigenous and other people of colour who work or study in predominantly White settings experience these feelings at higher rates, and that his research links impostor feelings to anxiety and depression among Black, Asian and Latino college students. Another psychologist quoted in the piece puts the general point plainly: “The problem isn’t necessarily the person; it can also be the setting or culture.”",
            "The same " + a(MON, "article") + " sets out what the feelings can cost. People caught up in them may be less willing to take career risks, may find it harder to negotiate pay, and may be more prone to burnout. It notes that a work culture with only White or male leadership can leave people from other groups feeling they do not deserve their place. A psychologist quoted in it recommends hiring and promoting people with under-represented identities, and the article adds that institutions should hold people accountable for microaggressions.",
            "This is not a claim that the feelings are imaginary or that individuals can do nothing. It is a reminder that feeling out of place in a room where few people resemble you may partly reflect the room itself, not only a distortion.",
        ]),
        ("An unexpected upside?", [
            "One recent study complicates the picture in a different way. In research described by " + a(MIT, "MIT News") + " in 2022 and published in the Academy of Management Journal, Basima Tewfik of MIT Sloan studied what she calls workplace impostor thoughts, in employees at an investment management firm, physicians in training, and participants in two experiments.",
            "People with more workplace impostor thoughts were rated as more interpersonally effective by supervisors, patients and hiring managers. Physicians in training who reported more of these thoughts were rated by patients as more empathetic and as listening better, and in video recordings they showed more eye contact, more open hand gestures and more nodding. The article reports no performance cost overall.",
            "Tewfik is careful not to turn this into advice. According to the article, she says the findings do not mean impostor thoughts should be encouraged, that they lower self-esteem, and that there are far better ways to become interpersonally effective. She also warns that people in solitary jobs, who cannot compensate through their dealings with others, may struggle more.",
            "Two details from the design are worth noting. At the investment firm, employees filled in surveys and their supervisors rated them two months later, so the ratings came from other people, not the employees themselves. And the data, the article reports, suggest that these thoughts can fade as people become more established in their roles. That is one reason Tewfik prefers not to call them a syndrome at all: the word implies something negative and permanent.",
        ]),
        ("What helps", [
            "Since no treatment trials existed as of the 2020 review, advice on impostor feelings rests on clinical experience and reasonable inference, not tested methods. Within those limits, the sources agree on several points. The " + a(MON, "APA Monitor") + " suggests examining the facts of your qualifications, sharing the feelings with trusted people, keeping a record of accomplishments and positive feedback, relaxing perfectionist standards, practising self-compassion, and expecting the feelings to return at career transitions.",
            "Clance’s own advice, quoted in " + a(GRAD, "gradPSYCH") + ", is concrete: do a task well enough, and develop and implement rewards for success, learn to celebrate. In therapy, the " + a(CO88, "1988 paper") + " recommends group work, so that people can see other capable people struggling in the same way, and keeping a journal of praise that has been discounted. It also stresses the relationship with the therapist: taking the person’s fears seriously, rather than repeating the dismissals they may have heard before, and accepting that change is slow. Its authors call for change in society as well as in the individual.",
            "HTML:" + K.callout("warn", "Not medical advice",
                "<p>This essay describes research. If feelings of fraudulence come with lasting low mood or anxiety, which the research suggests often go together, a doctor or qualified therapist is the right place to start.</p>"),
        ]),
        ("What this does and does not say", [
            "Read carefully, the research supports a modest picture. Many capable people feel like frauds, men and women alike; the feeling has a recognisable shape; it often travels with anxiety and low mood; and the setting matters as well as the person. It does not support treating impostor syndrome as a diagnosis, quoting a precise share of people who have it, or claiming that any particular technique has been shown to cure it.",
            "Other essays here meet the same ground from different directions. " + ESSAY56.replace(">what the spotlight", ">What the spotlight") + " looks at how much less others notice us than we fear. " + ESSAY61.replace(">what learned", ">What learned") + " describes how the way people explain their setbacks shapes what follows, the mirror image of discounting success. " + ESSAY62.replace(">what Spinoza", ">What Spinoza") + " traces an older argument that fear thrives on doubt. " + ESSAY71.replace(">what cognitive", ">What cognitive") + " looks at another classic idea about how people square what they do with what they believe. And " + ESSAY42 + " looks at another set of questionnaires whose numbers depend on how they are scored.",
        ]),
    ],
    note=[
        "The 1978 paper itself could not be read; its sample and findings are described as Clance and O’Toole (1988) report them. Clance holds the copyright on the scale described here.",
    ],
    faqs=[
        ("What is the impostor phenomenon?",
         "A persistent feeling, in people with a real record of achievement, that they are not as able as others think and will be found out. Clance and Imes described it in 1978."),
        ("Is impostor syndrome a real diagnosis?",
         "No. Pauline Rose Clance, who coined the term with Suzanne Imes, has said impostor phenomenon isn’t a clinical diagnosis, and she prefers phenomenon or experience to syndrome."),
        ("How common is impostor syndrome?",
         "Estimates vary from 9 to 82 per cent, according to a 2020 review of 62 studies, depending largely on the questionnaire and cutoff used. This essay could not trace the often-quoted figure of 70 per cent to a primary source."),
        ("Do men get impostor feelings?",
         "Yes. The first study focused on women, but later research found that men experience the phenomenon about as often as women, and the 2020 review found it common in both."),
        ("What helps with impostor feelings?",
         "No treatment trials had been published as of 2020. Suggestions from clinicians include checking the facts of your record, talking to trusted people, keeping a note of positive feedback, and relaxing perfectionist standards."),
    ],
    related=[
        ("what-the-spotlight-effect-is", "What the spotlight effect is, and why others notice us less than we think", "Psychology"),
        ("what-learned-helplessness-actually-showed", "What learned helplessness actually showed, and how its discoverers changed their minds", "Psychology"),
    ],
)

if __name__ == "__main__":
    newpost.build(POST)
