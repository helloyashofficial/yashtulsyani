#!/usr/bin/env python3
"""Essay 40 :: why-reassurance-is-never-enough  (Relationships, pillar)

Every outside claim is linked to a source that was fetched and read on
24 Oct 2026. The loop's seven steps are taken from The Thing You Were
Afraid Of (the validation loop on its book page); the handbook tools are
named, not reproduced.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import newpost, postkit as K

EXT = ' target="_blank" rel="noopener"'
DOWNEY = '<a href="https://researchconnect.stonybrook.edu/en/publications/the-self-fulfilling-prophecy-in-close-relationships-rejection-sen/"%s>Downey, Freitas, Michaelis and Khouri (1998)</a>' % EXT
STARR = '<a href="https://researchconnect.stonybrook.edu/en/publications/excessive-reassurance-seeking-depression-and-interpersonal-reject/"%s>a 2008 meta-analysis by Lisa Starr and Joanne Davila</a>' % EXT
OSBORNE = '<a href="https://www.cambridge.org/core/journals/advances-in-psychiatric-treatment/article/excessive-reassuranceseeking/9B5208DB11EA7907CB95D93727DC86DF"%s>a short clinical review in Advances in Psychiatric Treatment</a>' % EXT
MERTON = '<a href="https://sociologica.unibo.it/article/download/13653/15729?inline=1"%s>named it in 1948</a>' % EXT
MURRAY = '<a href="https://pubmed.ncbi.nlm.nih.gov/15841862/"%s>a set of experiments by Sandra Murray and colleagues</a>' % EXT
BOOK1 = '<a href="/books/the-thing-you-were-afraid-of">The thing you were afraid of</a>'
PHYS = '<a href="/writing/what-the-observer-effect-actually-says">what the observer effect actually says</a>'

POST = dict(
    slug="why-reassurance-is-never-enough", num=40, cat="Relationships", read="auto",
    date="2026-10-24",
    gen="rewrite/40-why-reassurance-is-never-enough.py",
    title="Why reassurance is never enough, and what to do instead",
    dek="Asking someone to promise they still love you works for about an hour. The relief is real, which is exactly why the question comes back, and why it slowly changes the relationship it was meant to protect.",
    takeaway="Reassurance seeking calms anxiety quickly and briefly, and the relief teaches you to ask again. Repeated often enough, the asking becomes pressure, the pressure changes how the other person behaves, and the change looks like proof of the original fear. The research links excessive reassurance seeking to depression and, more weakly, to rejection. What helps is slower: tell a question from a request for proof, tolerate a little uncertainty before asking, and build a sense of worth that does not have to be borrowed from someone else every day.",
    sections=[
        ("What reassurance seeking is", [
            "Reassurance seeking is asking someone, again and again, to confirm something you are afraid is not true: that they still love you, that they are not angry, that you did nothing wrong. Asked once, it is ordinary. Asked repeatedly about the same fear, it stops answering anything and starts maintaining the fear it was meant to settle.",
            "HTML:" + K.takeaways([
                "Reassurance brings fast relief, and the relief is what keeps the asking going.",
                "Repeated about the same fear, the question becomes pressure, and pressure changes the other person's behaviour.",
                "That change can then look like proof of the fear, which is how a worry turns into a pattern.",
                "Research links excessive reassurance seeking to depression moderately, and to rejection more weakly. It does not show that asking causes either.",
                "What helps is to tell a question apart from a request for proof, and to build worth that is not borrowed daily.",
            ]),
            "The distinction that matters is not between asking and not asking. People in close relationships check in with each other all the time, and they should. The distinction is between a question that wants information and a question that wants a feeling. The first is answered once. The second is answered, felt, and then needed again, sometimes within the hour.",
            "HTML:" + K.callout("definition", "Excessive reassurance seeking",
                "<p>The research term for the pattern: persistently asking others whether you are worthy or whether they care, even after they have said so. The word that does the work is excessive. It describes a repetition, not a single conversation.</p>"),
            "This essay is about the second kind of question. It follows the argument of " + BOOK1 + ", which calls the pattern the validation loop, and it sets that argument against what the research actually supports. It is about a behaviour, not an attachment category; the research on those is set out in <a href=\"/writing/what-attachment-styles-actually-measure\">what attachment styles actually measure</a>.",
        ]),
        ("Why it works, for about an hour", [
            "The first thing to say about reassurance is that it works. That is not a weakness in the argument; it is the whole problem. If asking did nothing, nobody would keep asking.",
            "In " + OSBORNE + ", Osborne and Williams describe reassurance as something that quickly reduces anxiety and brings immediate relief, and then wears off, after which the seeking returns. The relief is genuine. It is also short, and the shortness is not a defect in the reassurance. The person who gave it said what they meant. The relief fades because the fear was never about the words.",
            "The same review names the mechanism that keeps the cycle going. Each time reassurance is sought and the anxiety falls, the act of asking gets the credit. The person learns that the asking is what made them feel safe, and so never learns what would have happened if they had waited. The feared outcome is never tested. It is only postponed. In the review's words, reassurance seeking is self-perpetuating.",
            "Put plainly: every answered question makes the next one more likely. Not because the partner answered badly, but because the answer arrived, and the relief that followed taught the wrong lesson about where safety comes from.",
        ]),
        ("The loop, step by step", [
            "The first book describes this as a loop with seven steps. Each step is reasonable on its own, which is why the loop is hard to see from inside it.",
            "HTML:" + K.stages("The validation loop, from The thing you were afraid of", [
                ("01", "Insecurity", "A doubt arrives: about being loved, about being enough, about the other person staying."),
                ("02", "Reassurance", "You ask for proof, directly or indirectly. Are we okay. Do you still want this."),
                ("03", "Relief", "The answer comes and the doubt quietens. This step is real, and it is the hook."),
                ("04", "Dependency", "Calm now depends on the next answer. Safety has moved outside you."),
                ("05", "Pressure", "The questions come more often. The other person begins to feel examined rather than loved."),
                ("06", "Distance", "They pull back a little, or answer with less warmth, because being tested is tiring."),
                ("07", "Confirmation", "The distance looks like the thing you feared. The doubt returns, stronger, with evidence."),
            ], source="Step names from the book. The one-line glosses are this essay's."),
            "The step that does the damage is not the first one. Insecurity is common and survivable. The damage happens between steps four and six, where the solution to the fear starts to produce the evidence for it. By step seven the original doubt has data, and the data was generated by the attempt to make the doubt go away.",
            "This is why the loop feels so convincing from inside. The person in it is not imagining the distance. The distance is real. What they cannot see is how much of it the loop itself produced.",
        ]),
        ("When the fear produces the thing it fears", [
            "There is a name for an expectation that brings about its own confirmation. The sociologist Robert K. Merton " + MERTON + ": a self-fulfilling prophecy is, in his words, &ldquo;a false definition of the situation evoking a new behavior which makes the originally false conception come true&rdquo;. The definition is precise about the order: the belief comes first, then the behaviour, then the result that seems to justify the belief.",
            "The clearest study of this in relationships is " + DOWNEY + ", published in the Journal of Personality and Social Psychology. They studied people who anxiously expect rejection, a trait they call rejection sensitivity, in dating couples, using daily diaries in one study and observed conflict discussions in another.",
            "Their findings are specific and worth stating carefully. Relationships of people high in rejection sensitivity were more likely to break up. In the daily diaries, the partners of women high in rejection sensitivity were more rejecting after conflicts at home. In the laboratory, those women behaved more negatively during a conflict discussion, and that behaviour helped explain their partners' more rejecting responses. The paper's own framing is that people who expect rejection behave in ways that elicit it.",
            "HTML:" + K.callout("warn", "Read this finding carefully",
                "<p>The study does not show that anxious people deserve to be left, or that their partners were blameless. It shows a mechanism: expectation shapes behaviour, and behaviour shapes the response. In these samples the pattern was found for women high in rejection sensitivity but not for men, and the women's behaviour explained part of the partners' reaction, not all of it.</p>"),
            "Notice what is and is not in that sentence. The fear was not supernatural and did not reach out and change anyone. It changed the person who held it, how they spoke and what they did in a hard conversation, and the other person responded to that. Nothing more mysterious is needed, and nothing more mysterious is claimed.",
        ]),
        ("What the research does and does not show", [
            "The broadest evidence on reassurance seeking itself comes from " + STARR + " in the Journal of Abnormal Psychology. It pooled the studies available at the time on excessive reassurance seeking, depression and interpersonal rejection.",
            "HTML:" + K.table("Excessive reassurance seeking: the meta-analytic picture",
                ["Association", "Studies pooled", "Effect size (r)", "How to read it"],
                [["With concurrent depression", "38", ".32", "Moderate. Stronger in self-report measures and in samples with more women"],
                 ["With concurrent rejection", "16", ".14", "Small. Stronger when the person reports the rejection themselves, and slightly stronger in romantic relationships"],
                 ["Over time (prospective)", "Reviewed, not pooled", "n/a", "Reviewed qualitatively rather than combined statistically"]],
                source='Source: Starr and Davila (2008), Journal of Abnormal Psychology 117(4). <a href="https://researchconnect.stonybrook.edu/en/publications/excessive-reassurance-seeking-depression-and-interpersonal-reject/" target="_blank" rel="noopener">Abstract</a>.',
                num_cols=(1, 2)),
            "Three things follow from that table, and they pull in different directions.",
            "First, the link to depression is real and not small. People who seek reassurance excessively tend to be more depressed at the same point in time. Second, the link to rejection is weaker, and stronger when the rejection is reported by the person themselves than by someone else reporting on it. Some of what feels like rejection may be the lens rather than the event. Third, and most important, these are mostly associations measured at one moment. They do not establish that asking causes depression or rejection. Low mood could drive the asking as easily as the other way round, and almost certainly both happen.",
            "The authors say their results support the model, with several important caveats, and call for more methodologically diverse research. That is the honest position, and it is the one this essay takes. The loop is a useful description of something many people recognise. It is supported by evidence, not proven by it.",
        ]),
        ("Is it a question or a request for proof?", [
            "The most practical skill in all of this is telling the two kinds of question apart before asking. They can use exactly the same words. What differs is what would satisfy them.",
            "HTML:" + K.decision("Before you ask: what is this question for?",
                ("Would one clear answer settle it for good?", [
                    ("Yes", ("Is it about a fact you do not know, such as a plan, a decision or what happened?", [
                        ("Yes", "<p>That is a question. Ask it once, plainly, and accept the answer.</p>"),
                        ("No", "<p>Check again. If the answer would need repeating tomorrow, it is a request for proof.</p>"),
                    ])),
                    ("No", ("Have you asked this, in some form, in the last few days?", [
                        ("Yes", "<p>That is the loop. The answer will help for a while and then you will need it again. Try the pause below first.</p>"),
                        ("No", "<p>It may still be a request for proof. Say what you are feeling rather than asking them to fix it.</p>"),
                    ])),
                ])),
            "The last branch is the one most people skip. There is a third option between asking for proof and staying silent, which is to name the feeling without handing someone a test. \"I am feeling insecure tonight\" is information. \"Do you still love me?\", asked for the fourth time this week, is an exam the other person cannot pass, because a pass only lasts until the next one.",
        ]),
        ("What helps instead", [
            "If the loop runs on borrowed calm, the way out is to need less of it, which is slower and less satisfying than asking. Nothing below works in an evening. All of it works better over a few months than another round of asking does. The idea underneath is old: Epictetus opened his Handbook by separating what is up to us from what is not, and another person’s feelings fall on the far side of that line, as the essay on <a href=\"/writing/what-the-stoics-meant-by-what-is-up-to-us\">what the Stoics meant by what is up to us</a> sets out.",
            "HTML:" + K.compare("Asking for proof, and what to do instead", [
                ("Asking for proof", ["Fast relief", "Feels like closeness in the moment"], ["Relief fades", "Teaches that safety lives in the other person", "Turns the partner into an examiner"], "Works tonight, costs later"),
                ("Naming the feeling", ["Honest", "Gives the other person something they can respond to"], ["Less immediate relief", "Feels exposed at first"], "Slower, and builds trust"),
                ("Tolerating the doubt", ["Tests the fear instead of postponing it", "Calm becomes yours"], ["Uncomfortable for a while", "Needs practice"], "The only option that shortens the loop"),
            ]),
            "There is one more lever, and it is the one the research points to most interestingly. In " + MURRAY + ", people low in self-esteem tended to see themselves as inferior to their partners, and that sense of inferiority undermined their confidence in being valued. When the gap was narrowed, by pointing them either to strengths in themselves or to flaws in their partner, their felt security in the partner's regard went up. People high in self-esteem did not show the same effect.",
            "Read carefully, that is a striking result. The security the low self-esteem participants were looking for in their partner's regard moved when the distance they felt between themselves and their partner moved, without the partner saying anything new. Some of what reassurance is asked to provide depends on how you see yourself in relation to the other person. That is close to the centre of the second book, " + '<a href="/books/nobody-has-to-shrink">Nobody has to shrink</a>' + ": do not make yourself small so someone else can feel big, and do not make someone else small so you can feel big.",
        ]),
        ("A pause before you ask", [
            "The handbook in the first book includes a thirty-second pause and a section on what to do before you seek reassurance. What follows is not taken from it; it is a minimal version you can use tonight.",
            "HTML:" + K.flow("The pause, in four moves", [
                ("Notice", "Catch the urge before the words. It often arrives as restlessness or a draft message you keep editing."),
                ("Name", "Say to yourself what you are actually afraid of, in one sentence. Not the question, the fear under it."),
                ("Wait", "Let the urge sit for a short while without acting on it. The aim is not to win, only to see that the feeling moves on its own."),
                ("Choose", "Then decide. Ask once, name the feeling instead, or let it go for tonight. Any of the three is fine if it is chosen."),
            ]),
            "HTML:" + K.checklist("reassurance-pause", "Before you ask, check:", [
                ("The question", ["I can say what fact I am missing", "One answer would settle it", "I have not asked this, in some form, this week"]),
                ("The feeling", ["I have named the fear underneath in one sentence", "I waited before acting on the urge"]),
            ], bands=[[0, "Probably a request for proof. Try naming the feeling instead."], [60, "Mixed. Ask once, plainly, and accept the answer."], [100, "That is a genuine question. Ask it."]]),
            "The waiting step is the one that changes things over time. Every time the urge passes without being fed, the learning that Osborne and Williams describe runs the other way: the feared outcome is tested, and does not happen.",
        ]),
        ("Where the physics comes in, and where it does not", [
            "Nothing in this essay needs quantum mechanics, and it would be dishonest to suggest otherwise. The loop is psychology: expectation, behaviour and response, studied with diaries and observed conversations.",
            "The books use a quantum vocabulary for one specific reason. It gives precise words for something the loop makes visible: that looking at a relationship anxiously is not a neutral act, because the person looking is part of what they are looking at. That is a metaphor, and it is labelled as one. The physics it borrows from says something narrower and more interesting, which is set out in " + PHYS + ".",
            "The short version is this. In physics, an observation is an interaction, usually with an instrument, and no mind is required. In a relationship, the observer is a person, the interaction is behaviour, and the effect is psychological. The structure rhymes. The mechanism does not, and the claim made here is only about the second one.",
        ]),
    ],
    note=[
        "If you recognised yourself in the loop, that is not a diagnosis, and it is not a verdict on you or your relationship. Most people run some version of it. If the doubt is constant, or the asking has started to take over your days, that is worth taking to a therapist rather than to an essay.",
    ],
    faqs=[
        ("Is it wrong to ask a partner for reassurance?",
         "No. Asking occasionally, about something new, is an ordinary part of closeness. It becomes a problem when the same fear is asked about repeatedly, because each answer helps briefly and teaches you to need the next one."),
        ("Why does reassurance stop working?",
         "Because it reduces anxiety quickly, which teaches you that asking is what keeps you safe. The fear is never tested against what would have happened without asking, so it survives every answer and returns when the relief fades."),
        ("Can insecurity really cause a breakup?",
         "Research on rejection sensitivity found that people who anxiously expect rejection were more likely to see their relationships end, and that women high in rejection sensitivity behaved in ways that made partners more rejecting after conflict; the same pattern was not found for men. That is one contributing mechanism, not the only cause, and it does not mean the anxious person is to blame."),
        ("What should I do instead of asking for reassurance?",
         "Tell a question apart from a request for proof, name the feeling rather than handing your partner a test, and practise waiting before acting on the urge. Over time, building a sense of worth that does not depend on daily answers does more than any single reply."),
        ("Is this the same as anxious attachment?",
         "They overlap but are not the same thing. Reassurance seeking is a behaviour that people with many different attachment patterns can show. This essay is about the behaviour and its loop rather than about attachment categories."),
    ],
    related=[
        ("what-the-observer-effect-actually-says", "What the observer effect actually says, and what it does not", "Physics and time"),
        ("what-attachment-styles-actually-measure", "What attachment styles actually measure, and what they cannot tell you", "Psychology"),
    ],
)

if __name__ == "__main__":
    newpost.build(POST)
