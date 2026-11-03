#!/usr/bin/env python3
"""Essay 47 :: why-we-blame-the-people-we-love  (Philosophy)

Sources fetched and read on 3 Nov 2026: P. F. Strawson, "Freedom and
Resentment" (scanned text on Ted Honderich's UCL site; quotations checked
against it, OCR slips silently corrected), the British Academy's record of
Proceedings vol. 48, and Stanford Encyclopedia of Philosophy entries:
Snowdon on Strawson (biography only; its 1960 date is not used), Talbert on
moral responsibility, the Compatibilism entry, Coates and Tognazzini on
blame, Caruso on scepticism about moral responsibility, Hoefer on causal
determinism, and the Forgiveness entry.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import newpost, postkit as K

EXT = ' target="_blank" rel="noopener"'
def a(url, text):
    return '<a href="%s"%s>%s</a>' % (url, EXT, text)

FR = "https://www.homepages.ucl.ac.uk/~uctytho/dfwstrawson1.htm"
BA = "https://www.thebritishacademy.ac.uk/publishing/proceedings-british-academy/proceedings-volumes-1-111/48/"
SNOWDON = "https://plato.stanford.edu/archives/sum2018/entries/strawson/"
TALBERT = "https://plato.stanford.edu/archives/spr2020/entries/moral-responsibility/"
COMPAT = "https://plato.stanford.edu/archives/sum2026/entries/compatibilism/"
BLAME = "https://plato.stanford.edu/archives/spr2026/entries/blame/"
CARUSO = "https://plato.stanford.edu/archives/sum2026/entries/skepticism-moral-responsibility/"
HOEFER = "https://plato.stanford.edu/archives/sum2014/entries/determinism-causal/"

ESSAY43 = '<a href="/writing/what-the-stoics-meant-by-what-is-up-to-us">what the Stoics meant by what is up to us</a>'
ESSAY45 = '<a href="/writing/what-repair-after-an-argument-actually-involves">the essay on repair</a>'
ESSAY44 = '<a href="/writing/what-it-means-to-call-time-the-fourth-dimension">what it means to call time the fourth dimension</a>'

POST = dict(
    slug="why-we-blame-the-people-we-love", num=47, cat="Philosophy", read="auto",
    date="2026-11-03",
    gen="rewrite/47-why-we-blame-the-people-we-love.py",
    title="Why we blame the people we love, and what determinism would change",
    dek="If every choice had causes that reached back before a person was born, could anyone still be blamed? In 1962 P. F. Strawson answered by looking not at physics but at resentment, gratitude and forgiveness, and at what they show about loving someone.",
    takeaway="Strawson argued that blame lives in our reactions to how other people treat us: resentment, gratitude, hurt feelings and forgiveness, which he called the reactive attitudes. Some excuses soften those reactions without ending them, such as he did not mean to; others take a person outside them, such as he is only a child. Seeing someone purely as something to be managed is a stance we can take at times, but not one we could hold towards everyone and still have relationships. So, for creatures like us, he thought it practically inconceivable that a general belief in determinism would end these attitudes. Critics reply that this does not answer the sceptic, and some argue that resentment and indignation could be given up while concern and the thankful side of gratitude remain.",
    sections=[
        ("What Strawson argued", [
            "Strawson argued that blaming someone is not, at bottom, a verdict about free will. It is part of reacting to how people treat us, with resentment, gratitude, hurt feelings and forgiveness. Because those reactions are part of having relationships at all, he thought a belief that everything is determined could not, for people as we are, make us give them up.",
            "HTML:" + K.takeaways([
                "Strawson’s 1962 lecture Freedom and Resentment looked at blame through our reactions to each other, not through metaphysics.",
                "He called those reactions the reactive attitudes: gratitude, resentment, forgiveness, love and hurt feelings among them.",
                "Some excuses soften resentment (he did not mean to); others take a person out of its reach (he is only a child).",
                "We can see a person purely as something to manage, but not everyone, all the time, and still have relationships.",
                "Critics say this does not answer the sceptic, and some argue resentment could go while concern and the thankful side of gratitude stay.",
            ]),
            "This essay sets out the argument in Strawson’s own words where possible, what it means for the people closest to us, and the strongest objections to it.",
            "HTML:" + K.callout("definition", "Reactive attitudes",
                "<p>Strawson’s term for the feelings we have in response to the attitudes and intentions other people show towards us, such as gratitude, resentment, forgiveness, love and hurt feelings. To feel them is to treat someone as a participant in a relationship, not as an object.</p>"),
        ]),
        ("The lecture", [
            "Peter Frederick Strawson was an Oxford philosopher, born in London in 1919 and died in Oxford in 2006, according to " + a(SNOWDON, "Paul Snowdon’s entry in the Stanford Encyclopedia of Philosophy") + ". He gave Freedom and Resentment as the British Academy’s philosophical lecture for 1962; " + a(BA, "the Academy’s record") + " lists it in volume 48 of its Proceedings, published in 1963. Snowdon calls it perhaps his most famous and widely discussed paper.",
            "The lecture begins with a joke at philosophy’s expense. In " + a(FR, "the text of the essay") + ", Strawson opens: “Some philosophers say they do not know what the thesis of determinism is.” He then divides those who think they do into two camps, which he calls the optimists and the pessimists: those who think determinism leaves our practices of blame and praise intact, and those who think it would undermine them.",
            "His move was to refuse the terms both sides were using. As " + a(COMPAT, "the Stanford Encyclopedia’s entry on compatibilism") + " puts it, Strawson broke ranks with the classical compatibilists, arguing that both camps had been debating a distorted simulacrum of the real thing.",
        ]),
        ("What matters to us", [
            "The real thing, for Strawson, starts with an observation about ordinary life: “the very great importance that we attach to the attitudes and intentions towards us of other human beings.” We do not only care what people do to us. We care whether they meant well, whether they noticed us, whether they were careless or cruel.",
            "Out of that care come the reactions he names: gratitude, resentment, forgiveness, love and hurt feelings. They are not judgements we reach after an inquiry into free will. As " + a(BLAME, "the Stanford Encyclopedia’s entry on blame") + " summarises it, regarding others as morally responsible is, for Strawson, not a matter of judgement but of emotional response.",
            "His account of forgiveness shows how much these feelings carry. To ask to be forgiven, he writes, “is in part to acknowledge that the attitude displayed in our actions was such as might properly be resented and in part to repudiate that attitude for the future (or at least for the immediate future); and to forgive is to accept the repudiation and to forswear the resentment.”",
            "HTML:" + K.callout("note", "A theory of blame, or not",
                "<p>The essay is often treated as the origin of emotional accounts of blame, but the Stanford Encyclopedia’s entry on blame notes that it contains little sustained discussion of blame as such. Its subject is the whole web of reactions between people, of which blame is one part.</p>"),
        ]),
        ("Two kinds of excuse", [
            "Strawson’s most useful observation is that excuses come in two kinds, and they work differently.",
            "The first kind leaves the person fully inside the relationship and changes what we think they did. “He didn’t mean to.” “He hadn’t realized.” “He didn’t know.” “He couldn’t help it.” Pleas like these do not ask us to stop seeing someone as a person who owes us goodwill. They tell us that, this time, the ill will we saw was not there.",
            "The second kind changes how we see the person. Strawson’s examples include “He wasn’t himself”, “He has been under very great strain recently” and “He’s only a child”. These do not say the act was innocent. In Strawson’s words, they invite us to suspend our ordinary reactive attitudes towards the agent, either at the time of his action or all the time. He splits them into two groups: the first, such as “He wasn’t himself”, which he treats as the less important, and the second, such as “He’s only a child”, which concerns people we do not treat as ordinary participants at all.",
            "HTML:" + K.table("Strawson’s two kinds of plea",
                ["Kind", "Examples from the essay", "What it changes"],
                [["Pleas that modify resentment", "He didn’t mean to. He hadn’t realized. He didn’t know. He couldn’t help it.", "What we think was done: there was no ill will in it"],
                 ["Pleas that suspend the participant attitude", "He wasn’t himself. He has been under very great strain recently. He’s only a child.", "How we see the person: our ordinary reactive attitudes are suspended, at the time of the act or altogether"]],
                source='Source: <a href="' + FR + '" target="_blank" rel="noopener">Strawson, Freedom and Resentment (1962), section 4</a>.'),
            "Later philosophers sharpened this into a distinction between excusing and exempting. In " + a(TALBERT, "Matthew Talbert’s entry on moral responsibility") + ", drawing on Gary Watson, an exempted agent is not excused from blame but exempted from it: the point is not that his behaviour turns out to have been harmless, but that he is seen as one of whom better behaviour cannot reasonably be demanded.",
        ]),
        ("The objective attitude", [
            "The second kind of plea moves us towards what Strawson calls the objective attitude. His description is exact: “To adopt the objective attitude to another human being is to see him, perhaps, as an object of social policy; as a subject for what, in a wide range of sense, might be called treatment; as something certainly to be taken account, perhaps precautionary account, of; to be managed or handled or cured or trained; perhaps simply to be avoided.”",
            "One line captures the cost. “If your attitude towards someone is wholly objective, then though you may fight him, you cannot quarrel with him.” A quarrel assumes the other person can be reasoned with, wronged and answerable. A fight does not.",
            "HTML:" + K.compare("The two stances", [
                ("Participant attitude", ["Resentment and gratitude make sense", "The other person can be argued with", "Forgiveness is possible"], ["Leaves us open to being hurt"], "The stance a relationship assumes."),
                ("Objective attitude", ["Can protect us from the strain of involvement", "Fitting where ordinary goodwill cannot be expected"], ["You may fight, but not quarrel", "The person becomes something to manage"], "A resource, not a way to live with everyone."),
            ], source='Source: <a href="' + FR + '" target="_blank" rel="noopener">Strawson, Freedom and Resentment, section 4</a>.'),
            "Strawson does not condemn the objective attitude. He notes it is available as a resource in other cases too, even with people we would normally treat as participants, “as a refuge, say, from the strains of involvement”. What he doubts is that anyone could take it towards everyone, all the time.",
        ]),
        ("What determinism would change", [
            "Now the question the lecture set out to address. Causal determinism is, in " + a(HOEFER, "Carl Hoefer’s definition") + ", roughly the idea that every event is necessitated by antecedent events and conditions together with the laws of nature. If that were true of every human choice, should resentment, gratitude and forgiveness go?",
            "Strawson’s answer is careful. He does not say giving up the reactive attitudes is impossible. He writes that it is “not absolutely inconceivable that it should happen”. “But I am strongly inclined to think that it is, for us as we are, practically inconceivable.”",
            "His reason is about relationships, not physics. The human commitment to participation in ordinary relationships, he writes, is “too thoroughgoing and deeply rooted” for a general theoretical conviction to remove it; and being involved in relationships as we know them simply is being exposed to the range of reactive attitudes. Seen that way, the framework of these attitudes “as a whole” “neither calls for, nor permits, an external ‘rational’ justification”. Inside the framework, particular reactions are still revised all the time, by exactly the kinds of plea above.",
            "HTML:" + K.stages("Strawson’s argument, in four steps", [
                ("01", "Start from what we care about", "Other people’s attitudes and intentions towards us matter to us enormously."),
                ("02", "Notice the reactions", "Gratitude, resentment, forgiveness and hurt feelings are how that care shows."),
                ("03", "Look at how excuses work", "Determinism does not imply that no one means what they do, or that everyone is abnormal, so it does not make the ordinary excuses true of everyone."),
                ("04", "Ask what is left", "And in any case a wholly objective stance towards everyone is, for us as we are, practically inconceivable."),
            ], source='A summary of sections 3 and 4 of <a href="' + FR + '" target="_blank" rel="noopener">Freedom and Resentment</a>.'),
            "In the terms philosophers use, this is a compatibilist conclusion; " + a(COMPAT, "compatibilism") + " is the thesis that free will is compatible with determinism. Talbert describes the essay as a touchstone for much of the work on moral responsibility that followed it, especially by compatibilists.",
        ]),
        ("The objections", [
            "The argument has been influential and much criticised. Three challenges are worth knowing.",
            "The first is that it may put our practices beyond criticism. As " + a(TALBERT, "Talbert sets out") + ", the approach would be particularly problematic if it meant that a group’s responsibility practices are beyond criticism simply because they are that group’s practices, a worry he attributes to Fischer and Ravizza.",
            "The second questions how committed we really are. Talbert lists several critics, Gary Watson among them, who doubt the assumption that we are too deeply and naturally committed to these practices to give them up, or that giving them up would distort our moral lives.",
            "Watson also discussed a hard case that shows how much these attitudes are asked to carry. As " + a(BLAME, "the entry on blame") + " describes it, Robert Harris was an unequivocally cruel murderer and also, in a real sense, a victim of his tragic formative circumstances. His history raises the question whether he is a fitting target of blame at all, and the thought there but for the grace of God go I can make indignation feel self-righteous. In this essay’s reading, the case shows reactive attitudes pulling in two directions at once.",
            "The third is the sceptic’s. Derk Pereboom, as " + a(CARUSO, "Gregg Caruso’s entry on scepticism about moral responsibility") + " explains, argues that whatever the nature of reality, deterministic or not, we lack basic-desert moral responsibility, the kind that would make blame deserved in itself, and that resentment and indignation would be undercut. But the sceptic need not reject all reactive attitudes. Pereboom proposes moral concern, disappointment, sorrow and resolve in place of resentment, and the entry notes that gratitude, in its thankful aspect, is in the clear.",
            "HTML:" + K.table("Three challenges to Strawson",
                ["Challenge", "The worry"],
                [["Practices beyond criticism", "That the way we happen to blame might be shielded from criticism just because it is how we live"],
                 ["How committed are we?", "That we may be less locked into these attitudes than Strawson assumed"],
                 ["Pereboom’s scepticism", "That resentment and indignation could give way to concern, disappointment, sorrow and resolve, while the thankful side of gratitude remains"]],
                source='Sources: <a href="' + TALBERT + '" target="_blank" rel="noopener">Talbert</a>; <a href="' + BLAME + '" target="_blank" rel="noopener">Coates and Tognazzini</a>; <a href="' + CARUSO + '" target="_blank" rel="noopener">Caruso</a>, Stanford Encyclopedia of Philosophy.'),
        ]),
        ("What this means between people", [
            "What follows is this essay’s reading rather than Strawson’s argument, and it is offered as one.",
            "Resentment is uncomfortable, but on Strawson’s account it is also a form of respect: it treats the other person as someone who can be answerable to you. The alternative is not serene detachment. It is the objective attitude, in which you may manage a partner but cannot quarrel with them. A relationship where one person has quietly stopped expecting anything of the other, and handles them instead, has moved from one stance to the other, whatever it looks like from outside.",
            "That is also why the two kinds of excuse matter at home. “She didn’t mean it” keeps someone inside the relationship while softening the reaction. “That’s just how he is” can start to move them outside it. The second is sometimes the kinder thought and sometimes the more dismissive one, and it is worth noticing which you are reaching for.",
            "Two other essays on this site meet this one. Epictetus’ line “It seemed so to him”, set out in " + ESSAY43 + ", is an older way of loosening resentment by understanding the other person’s view rather than by ceasing to treat them as a person. And Strawson’s definition of forgiveness, accepting someone’s repudiation of what they did and forswearing resentment, connects with " + ESSAY45 + ", and with its caution, from the research, that forgiving frequent or major offences is less advisable.",
            "And for anyone tempted by the physics, " + ESSAY44 + " explains why relativity does not settle whether the future is as real as the present. Strawson’s point is that even if it were fixed, the question of how to treat the person in front of you would look much the same.",
        ]),
    ],
    note=[
        "Quotations from Freedom and Resentment are from a scanned text of the essay; where the scan has obvious slips (such as sratitude for gratitude), the correct word is used. Where the essay’s reading departs from Strawson’s argument, it says so.",
    ],
    faqs=[
        ("What are reactive attitudes?",
         "P. F. Strawson's name for the feelings we have in response to how other people treat us, such as gratitude, resentment, forgiveness, love and hurt feelings. In his 1962 essay Freedom and Resentment he argued that these reactions, not theoretical judgements, are the basis of holding people responsible."),
        ("Does determinism mean no one is to blame?",
         "Strawson argued not, at least in practice. He thought it not absolutely inconceivable that a belief in determinism could end our reactive attitudes, but practically inconceivable for people as we are, because having relationships at all means being exposed to those attitudes. Sceptics such as Derk Pereboom argue that no one deserves blame in the most basic sense, determinism or not, and that resentment and indignation would be undercut, though concern, sorrow and the thankful side of gratitude would not."),
        ("What is the objective attitude?",
         "Strawson's term for seeing another person as something to be managed, handled, treated or avoided, rather than as a participant in a relationship. He thought it fitting in some cases and useful as a refuge from the strain of involvement, but not something anyone could take towards everyone."),
        ("Is it wrong to feel resentment towards a partner?",
         "On Strawson's account, resentment is part of treating someone as answerable to you, so it is not wrong in itself. Philosophers such as Pereboom argue it could be replaced by concern, disappointment, sorrow and resolve. Whether to act on it, and when to forgive, are separate questions."),
        ("What is the difference between excusing and exempting someone?",
         "An excuse says the act was not what it seemed, as in he did not mean to. An exemption says the person is not, at least for now, someone of whom better behaviour can reasonably be demanded, as in he is only a child. The distinction comes from Strawson and was sharpened by later philosophers, including Gary Watson."),
    ],
    related=[
        ("what-the-stoics-meant-by-what-is-up-to-us", "What the Stoics meant by what is up to us, and what it means for love", "Philosophy"),
        ("what-repair-after-an-argument-actually-involves", "What repair after an argument actually involves, and what the famous numbers miss", "Relationships"),
    ],
)

if __name__ == "__main__":
    newpost.build(POST)
