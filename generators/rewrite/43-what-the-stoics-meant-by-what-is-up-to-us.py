#!/usr/bin/env python3
"""Essay 43 :: what-the-stoics-meant-by-what-is-up-to-us  (Philosophy, pillar)

Sources fetched and read on 2 Nov 2026. Handbook quotations are from
T. W. Higginson's translation (Project Gutenberg #45109). Epictetus' life
and thought: Margaret Graver, SEP "Epictetus" (Summer 2026 archive).
"Up to us": Tim O'Keefe, SEP "Ancient Theories of Freedom and Determinism".
Stoicism, the passions and CBT: Dirk Baltzly, SEP "Stoicism". Beck via
Donald Robertson's excerpt; Ellis via EBSCO Research Starters. Irvine via
the Bryn Mawr Classical Review of his 2009 book.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import newpost, postkit as K

EXT = ' target="_blank" rel="noopener"'
def a(url, text):
    return '<a href="%s"%s>%s</a>' % (url, EXT, text)

HANDBOOK = "https://gutenberg.org/cache/epub/45109/pg45109-images.html"
GRAVER = "https://plato.stanford.edu/archives/sum2026/entries/epictetus/"
OKEEFE = "https://plato.stanford.edu/archives/spr2021/entries/freedom-ancient/"
BALTZLY = "https://plato.stanford.edu/archives/win2021/entries/stoicism/"
ROBERTSON = "https://donaldrobertson.name/2010/09/10/excerpt-the-philosophy-of-cognitive-behavioural-therapy-cbt/"
EBSCO = "https://www.ebsco.com/research-starters/health-and-medicine/rational-emotive-therapy"
BMCR = "https://bmcr.brynmawr.edu/?p=26558"
CARTER = "https://classics.mit.edu/Epictetus/epicench.html"

ESSAY40 = '<a href="/writing/why-reassurance-is-never-enough">the essay on reassurance seeking</a>'
ESSAY42 = '<a href="/writing/what-attachment-styles-actually-measure">attachment anxiety</a>'

POST = dict(
    slug="what-the-stoics-meant-by-what-is-up-to-us", num=43, cat="Philosophy", read="auto",
    gen="rewrite/43-what-the-stoics-meant-by-what-is-up-to-us.py",
    title="What the Stoics meant by what is up to us, and what it means for love",
    dek="Epictetus opened his Handbook by dividing the world in two: what is up to us, and what is not. Other people, and how they feel about us, sit on the far side of that line. Read closely, that is less cold than it sounds.",
    takeaway="Epictetus taught that only our own judgements, aims, desires and aversions are fully up to us; bodies, property, reputation and, as the Stanford Encyclopedia puts it, our relationships with other people are not. The point is not to stop caring about people. It is to stop staking our peace on something that is not ours to decide, such as whether someone else loves us, and to put our effort where it can act: in how we judge, what we ask, and how we respond. The distinction is sharper than real relationships, where we have influence without control, and it is best used as a way of seeing where your effort belongs rather than as a rule for feeling less.",
    sections=[
        ("What up to us means", [
            "For Epictetus, what is up to us is our own judgements, aims, desires and aversions: in the words of his Handbook, whatever affairs are our own. What is not up to us is everything else, including our bodies, our property, our reputation and, by the same logic, what other people think, feel and do.",
            "HTML:" + K.takeaways([
                "The Handbook opens with a single division: things within our power and things beyond it.",
                "Within our power: opinion, aim, desire, aversion. Beyond it: body, property, reputation, office.",
                "A leading modern account lists our relationships with other people among the things outside our control.",
                "The Stoics were not asking people to stop loving. They were asking them not to stake their peace on what they cannot decide.",
                "Real relationships sit between the two categories: we have influence without control. Using the idea well means knowing which part is which.",
            ]),
            "This essay reads that opening closely, looks at what Epictetus said about other people in particular, takes the harshest passage seriously, and then asks what the distinction is good for in a relationship, and where it is too sharp to use as it stands.",
            "HTML:" + K.callout("definition", "Up to us",
                "<p>The usual English rendering of the Greek <em>eph’ hêmin</em>. As " + a(OKEEFE, "Tim O’Keefe’s entry in the Stanford Encyclopedia of Philosophy") + " notes, ancient writers spoke of what is up to us, or what depends on us, and none of their phrases should obviously be translated as free will.</p>"),
        ]),
        ("Who Epictetus was", [
            "The details of his life are brief and mostly secure. According to " + a(GRAVER, "Margaret Graver’s entry on Epictetus in the Stanford Encyclopedia of Philosophy") + ", he was born sometime in the 50s of the common era in Hierapolis, a Greek city in Asia Minor, and spent part of his life as the slave of Epaphroditus. He studied for a time under the Stoic philosopher Musonius Rufus, then set up his own school at Nicopolis, where he taught until his death around 135.",
            "He probably did not write the books that carry his name. According to the preface of the Discourses, his lectures were written down by the historian Arrian of Nicomedia, though a few scholars argue Epictetus composed them himself; the Handbook is a short abridgment of the Discourses. Graver is frank about its limits: she calls it a much attenuated account of his thought that at some points gives a misleading impression of his philosophical motivations.",
            "HTML:" + K.table("Epictetus at a glance",
                ["Detail", "What the sources say"],
                [["Born", "Sometime in the 50s CE, in Hierapolis, Asia Minor"],
                 ["Status", "Enslaved for part of his life, to Epaphroditus"],
                 ["Teacher", "The Stoic Musonius Rufus"],
                 ["School", "His own, at Nicopolis"],
                 ["Died", "Around 135 CE"],
                 ["The texts", "The Discourses, written down by Arrian of Nicomedia by their own account, and the Handbook as an abridgment"]],
                source='Source: <a href="' + GRAVER + '" target="_blank" rel="noopener">Graver, Stanford Encyclopedia of Philosophy, “Epictetus”</a>.'),
            "That caution matters for what follows. The Handbook is the version of Epictetus most people meet, and its compression is part of why the idea can sound colder than it is. Where the Handbook is stark, this essay checks it against the fuller account.",
        ]),
        ("The opening, read closely", [
            "The Handbook begins without preamble. In " + a(HANDBOOK, "Thomas Wentworth Higginson’s translation") + ": “There are things which are within our power, and there are things which are beyond our power.”",
            "Then it fills in both sides. Within our power are “opinion, aim, desire, aversion, and, in one word, whatever affairs are our own.” Beyond our power are “body, property, reputation, office, and, in one word, whatever are not properly our own affairs.”",
            "HTML:" + K.table("The division in the first chapter of the Handbook",
                ["Within our power", "Beyond our power"],
                [["Opinion", "Body"],
                 ["Aim", "Property"],
                 ["Desire", "Reputation"],
                 ["Aversion", "Office"],
                 ["In one word: whatever affairs are our own", "In one word: whatever are not properly our own affairs"]],
                source='Source: Epictetus, Handbook, chapter 1, <a href="' + HANDBOOK + '" target="_blank" rel="noopener">translated by T. W. Higginson</a>.'),
            "The list on the right is not a list of unimportant things. Health, money, standing and work are most of what people worry about. The claim is not that they do not matter. It is that they are not ours in the way our own judgements are: they can be taken away, interrupted or decided by someone else.",
            "The chapter then says what happens if you confuse the two. Treat what depends on others as if it were yours, and “you will be hindered, you will lament, you will be disturbed, you will find fault both with gods and men.” Keep to what is yours, and “no one will ever compel you, no one will restrict you”.",
            "It ends with a practical test. Faced with a troubling impression, ask whether it concerns something within your power or not, and if it does not, “be prepared to say that it is nothing to you.” That last phrase is where most readers flinch, and it is worth slowing down on.",
        ]),
        ("What sits inside the line", [
            "The fuller account of what is up to us turns on a word Epictetus uses often, <em>prohairesis</em>, which Graver renders as volition. Volition, she writes, is by nature unimpeded, and that is why freedom is for him an inalienable characteristic of the human being.",
            "What belongs to it is specific. In Graver’s summary, “our convictions, attitudes, intentions and actions are truly ours in a way that nothing else is”, because they depend on how we use the impressions that reach us. O’Keefe’s entry puts the same point in terms of assent: whether we accept an impression as true is up to us, and assent is the cause of our actions.",
            "And on the other side of the line, Graver lists the externals plainly: the appearance and comfort of one’s body, one’s possessions, one’s relationships with other people, the success or failure of one’s projects, and one’s power and reputation in the world.",
            "HTML:" + K.callout("note", "The sentence this essay is about",
                "<p>One’s relationships with other people are, for Epictetus, external to the sphere of volition. What another person feels, whether they stay, whether they love you, is not up to you. What you believe about it, what you ask for, and what you do are.</p>"),
            "That does not make externals worthless. Graver quotes a line from the Discourses that keeps the whole picture in balance: the materials of action are indifferent, but the use we make of them is not. A relationship is material. How you conduct yourself in it is entirely your concern.",
        ]),
        ("What Epictetus said about other people", [
            "Two short chapters near the end of the Handbook apply the idea directly to people who treat us badly.",
            "Chapter 42 is about being wronged or spoken ill of. In Higginson’s translation, the person who does so “acts or speaks from an impression that it is right for him to do so.” He cannot follow what seems right to you, only what seems right to him. The chapter ends with a phrase meant to be said on every such occasion: “It seemed so to him.”",
            "Chapter 43 offers an image. “Everything has two handles: one by which it may be borne, another by which it cannot.” If your brother acts unjustly, do not take hold of it by the handle of his injustice, but by the other one: that he is your brother, that he was brought up with you.",
            "HTML:" + K.stages("The two chapters as a sequence", [
                ("01", "Something hurtful happens", "Another person says or does something that wounds you. That is outside your control."),
                ("02", "Name how it seemed to them", "They acted on how things looked to them, not to you. Chapter 42: “It seemed so to him.”"),
                ("03", "Choose the handle", "Of everything true about the situation, choose what to take hold of. Chapter 43: he is your brother."),
                ("04", "Respond from there", "Your response is the part that is yours."),
            ], source='Source: Handbook, chapters 42 and 43, <a href="' + HANDBOOK + '" target="_blank" rel="noopener">Higginson translation</a>.'),
            "Neither chapter says the other person was right, or that the hurt is imaginary. They say something narrower: that the other person’s view is theirs, that you cannot make them see it your way by willing it, and that you still decide which true thing about them you build your response on.",
        ]),
        ("The hardest passage", [
            "Any honest reading has to include chapter 3, because it is the one people quote when they call Stoicism cold. In Higginson’s translation, it advises reminding yourself of the nature of whatever you love, beginning with trifles: if you have a favourite cup, that it is only a cup, so that if it breaks you can bear it; and, if you embrace your child or your wife, “that you embrace a mortal”, so that “if either of them dies, you can bear it.”",
            "Read alone, that sounds like advice to love less so as to lose less. The Stoics were accused of exactly that in their own time. As " + a(BALTZLY, "Dirk Baltzly’s entry on Stoicism in the Stanford Encyclopedia") + " notes, some critics called them the men of stone, while Aristotle’s followers argued that a happy life needs the passions moderated, not extinguished. Baltzly adds that the charge is not entirely fair, because the Stoics allowed that the wise person still has what they called good feelings.",
            "The fuller Epictetus pushes the other way too. Graver points out that he did not want people to be unfeeling like a statue, and that it is a misconception to think proper affection for friends and family must leave us open to debilitating emotions. For Epictetus, she writes, love of humanity is a willingness to exert oneself on others’ behalf, and the parent who stays at the bedside of a desperately sick child behaves more naturally, not less, than the one who runs away to weep.",
            "HTML:" + K.compare("Two readings of chapter 3", [
                ("Love less, lose less", [], ["Treats attachment itself as the mistake", "Matches the men of stone caricature", "Not supported by the fuller account of Epictetus"], "The reading critics attacked."),
                ("Love without owning", ["Keeps the affection", "Remembers the person is not yours to keep", "Puts effort into care rather than control"], [], "This essay’s reading, consistent with Graver’s account of the Discourses."),
            ], source='Sources: <a href="' + BALTZLY + '" target="_blank" rel="noopener">Baltzly, “Stoicism”</a>; <a href="' + GRAVER + '" target="_blank" rel="noopener">Graver, “Epictetus”</a>.'),
            "The second reading does not make the passage gentle. It is still asking something difficult: to love someone fully while knowing, at the same time, that they are mortal and not yours. But that is a different request from asking you to care less.",
        ]),
        ("Views, not things", [
            "Chapter 5 is the line from the Handbook most often quoted on its own. In Higginson’s version: “Men are disturbed not by things, but by the views which they take of things.” Death, the chapter goes on, is nothing terrible, or it would have seemed so to Socrates; the terror lies in our notion of death.",
            "Translations differ on the key word: Higginson writes views, and " + a(CARTER, "the translation by Elizabeth Carter in MIT’s Internet Classics Archive") + " has principles and notions. The idea is the same in each: the distress arrives through a judgement, and the judgement is the part that is up to us.",
            "That idea has a modern descendant. Baltzly notes strong affinities between the central role Stoicism gives to judgement and the techniques of cognitive behavioural therapy. The founders of two of those therapies said so themselves. " + a(ROBERTSON, "Donald Robertson quotes Aaron Beck and his co-authors") + ", writing in 1979, that the philosophical origins of cognitive therapy can be traced back to the Stoic philosophers, and " + a(EBSCO, "a reference summary of Albert Ellis’s rational emotive behaviour therapy") + " lists Epictetus and Marcus Aurelius among its philosophical origins.",
            "HTML:" + K.callout("warn", "A limit worth keeping",
                "<p>A family resemblance to a therapy is not evidence that reading Epictetus treats anything. The claim here is historical: the people who built these therapies named the Stoics as a source. Whether a particular idea helps a particular person is a separate question.</p>"),
        ]),
        ("What this means in a relationship", [
            "Put the pieces together and the distinction becomes practical. In any relationship there are things that are not up to you: whether the other person loves you, what they feel on a given day, whether they stay, what they think of you. And there are things that are: what you believe about the situation, what you ask for, how you ask, and what you do next.",
            "Most painful patterns in relationships involve putting effort on the wrong side of that line. (Coming back from an argument is a case in point, set out in <a href=\"/writing/what-repair-after-an-argument-actually-involves\">what repair after an argument actually involves</a>.) " + ESSAY40 + " describes one of them in detail: asking again and again for proof of something that is, in the end, another person’s to give. The asking is up to you. The feeling it is trying to secure is not, which is why no answer settles it.",
            "HTML:" + K.decision("Where does my effort belong here?",
                ("Is the thing I want settled something only the other person can decide?", [
                    ("Yes", ("Am I trying to secure it by pressure, testing or repeated asking?", [
                        ("Yes", "<p>That effort is aimed at what is not up to you. Move it to what is: say what you feel and what you would like, once, and let the answer be theirs.</p>"),
                        ("No", "<p>Then it may simply be uncertain. Uncertainty about another person is part of loving someone who is not you.</p>"),
                    ])),
                    ("No", "<p>Then it is yours: a judgement, a request, a response. That is where effort changes things.</p>"),
                ])),
            "The same lens helps with the fear itself. Someone high in " + ESSAY42 + " is, in the research’s terms, watchful for signs of rejection. Epictetus would not tell that person the fear is wrong. He would point out that the signs are about something outside their power, and that the part they can work on is the judgement they make about each sign: whether to accept it, as O’Keefe’s account of assent puts it, or to say, as the Handbook does, that it seemed so to them.",
        ]),
        ("Where the line is too sharp", [
            "The distinction is clean, and real relationships are not. You cannot decide whether someone loves you, but what you do affects how they feel, and pretending otherwise would be its own mistake.",
            "Modern writers have tried to account for this. " + a(BMCR, "A review of William Irvine’s 2009 book A Guide to the Good Life") + " describes his proposal of a three-way division: things we control completely, things we do not control at all, and things over which we have some control, such as whether we win a game of tennis. For the middle group, Irvine’s advice is to set internal goals: not to win, but to compete as hard as we can. The review is largely favourable, though the reviewer notes that Irvine’s shift from virtue towards tranquillity may seem to some a sleight of hand.",
            "Whatever its standing as an account of Stoicism, the middle category describes relationships well. You have influence without control. The useful version of the Stoic idea, for love, is to put your effort into the part that is yours (how honestly you speak, how well you listen, how you treat the other person) and to hold the result, their feelings and their choices, as theirs.",
            "Said that way, the distinction is not a rule for feeling less. It is a way of seeing where effort belongs, so that care goes into what care can actually change.",
        ]),
    ],
    note=[
        "Quotations from the Handbook are from Thomas Wentworth Higginson’s public-domain translation. Where the reading of Epictetus depends on scholarship rather than the text, the essay names the scholar and links the source.",
    ],
    faqs=[
        ("What did Epictetus mean by what is up to us?",
         "The things that are fully our own: our judgements, aims, desires and aversions. Everything else, including the body, property, reputation and our relationships with other people, is not up to us, because it can be taken away, interrupted or decided by someone else."),
        ("Is the dichotomy of control Epictetus' own phrase?",
         "The idea is his; it opens his Handbook. The phrase dichotomy of control is not in the Handbook. William Irvine uses it in his 2009 book A Guide to the Good Life, which also proposes a third category for things we partly control."),
        ("Does Stoicism mean not caring about people?",
         "No. Critics in antiquity called the Stoics men of stone, but the Stanford Encyclopedia notes that Epictetus did not want people to be unfeeling like a statue, and treated care for others as active effort on their behalf. The aim is not to love less but to stop staking one's peace on what one cannot control."),
        ("Is another person's love up to us?",
         "Not in Epictetus' sense. What another person feels and chooses is outside our control, although what we do can influence it. What is up to us is how we judge the situation, what we ask for, and how we act."),
        ("Is Stoicism the same as cognitive behavioural therapy?",
         "No, but they are related. Aaron Beck and his co-authors traced the philosophical origins of cognitive therapy to the Stoics, and Albert Ellis named Epictetus among the origins of rational emotive behaviour therapy. A historical link is not evidence that Stoic ideas work as treatment."),
    ],
    related=[
        ("why-reassurance-is-never-enough", "Why reassurance is never enough, and what to do instead", "Relationships"),
        ("what-attachment-styles-actually-measure", "What attachment styles actually measure, and what they cannot tell you", "Psychology"),
    ],
)

if __name__ == "__main__":
    newpost.build(POST)
