#!/usr/bin/env python3
"""Essay 67 :: what-montaigne-meant-by-because-it-was-he  (Philosophy)

Sources fetched and read on 7 Nov 2026: Montaigne, Of Friendship, Charles
Cotton's translation edited by W. C. Hazlitt (Project Gutenberg, Essays
volume 6); the same edition's biography and letters (volume 1); Stanford
Encyclopedia of Philosophy, Montaigne (revised 2026); Cambridge University
Library exhibition page on Of Friendship.
Not used: the story of the phrase being added in stages to the Bordeaux
copy, which no fetched source states; claims about La Boetie's office.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import newpost, postkit as K

EXT = ' target="_blank" rel="noopener"'
def a(url, text):
    return '<a href="%s"%s>%s</a>' % (url, EXT, text)

OF = "https://www.gutenberg.org/cache/epub/3586/pg3586.html"
V1 = "https://www.gutenberg.org/cache/epub/3581/pg3581.html"
SEP = "https://plato.stanford.edu/ENTRIES/montaigne/"
CUL = "https://wwwe.lib.cam.ac.uk/CUL/exhibitions/Montaigne/c3.html"

ESSAY43 = '<a href="/writing/what-the-stoics-meant-by-what-is-up-to-us">what the Stoics meant by what is up to us</a>'
ESSAY57 = '<a href="/writing/what-aristotle-meant-by-the-three-kinds-of-friendship">what Aristotle meant by the three kinds of friendship</a>'
ESSAY52 = '<a href="/writing/what-epicurus-meant-by-pleasure">what Epicurus meant by pleasure</a>'
ESSAY55 = '<a href="/writing/what-the-michelangelo-phenomenon-says">what the Michelangelo phenomenon says</a>'

POST = dict(
    slug="what-montaigne-meant-by-because-it-was-he", num=67, cat="Philosophy", read="auto",
    date="2026-11-07",
    gen="rewrite/67-what-montaigne-meant-by-because-it-was-he.py",
    title="What Montaigne meant by “because it was he, because it was I”",
    dek="Asked why he loved his friend Étienne de La Boétie, Montaigne said there was no reason he could give, except this: because it was he, because it was I. It is one of the most quoted lines about friendship, and it comes from a writer famous for doubting almost everything else.",
    takeaway="Michel de Montaigne (1533 to 1592) wrote his essay Of Friendship about Étienne de La Boétie, whom he met by chance and who died in August 1563, aged about thirty-two. Montaigne counted only four years of their friendship, and wrote that if pressed to explain why he loved him, it could only be expressed by answering: because it was he, because it was I. He separated this perfect friendship from common friendships: in it, the two souls mix so completely that there is no sign of the seam, it cannot be shared with a rival, and words like benefit and thanks have no place. He contrasted it with family ties, erotic love and marriage, and wrote dismissively of women’s capacity for it, a view of his time. The essay claims such friendship comes about perhaps once in three ages. It is less a theory of friendship than a portrait of one, and an admission that some attachments resist explanation.",
    sections=[
        ("What Montaigne meant", [
            "Montaigne meant that his friendship with La Boétie had no reason outside itself. It was not based on usefulness, pleasure or shared opinions, but on who the two of them were. Asked to explain it, he could only point to the two people: because it was he, because it was I.",
            "HTML:" + K.takeaways([
                "Montaigne wrote Of Friendship about Étienne de La Boétie, who died in 1563.",
                "He counted only four years of their friendship.",
                "Pressed for a reason he loved him, he said: because it was he, because it was I.",
                "He set this perfect friendship apart from common friendships, family ties and love.",
                "In it, he wrote, souls mix so fully that the seam disappears, and it allows no rival.",
                "He thought such friendship came perhaps once in three ages.",
            ]),
            "This essay reads Montaigne in Charles Cotton’s seventeenth-century English translation, as edited by W. C. Hazlitt, which is free to read online. Quotations keep Cotton’s wording, including where other translations differ.",
            "HTML:" + K.callout("definition", "The line itself",
                "<p>In " + a(OF, "Cotton’s translation") + ": “If a man should importune me to give a reason why I loved him, I find it could no otherwise be expressed, than by making answer: because it was he, because it was I.” An earlier English translation, by John Florio, renders the ending “because it was my selfe”, as quoted by " + a(CUL, "Cambridge University Library") + ".</p>"),
        ]),
        ("Montaigne and La Boétie", [
            "Montaigne lived from 1533 to 1592, according to the " + a(SEP, "Stanford Encyclopedia of Philosophy") + ", which records that he came from a rich bourgeois family, retired at the age of only 37 to his father’s castle, and published his Essays in three main editions, in 1580, 1588 and, after his death, 1595. Around 1576 he had a medal struck with the motto Que sais-je?, what do I know?",
            "A " + a(CUL, "Cambridge University Library exhibition") + " records that around 1559 Montaigne met La Boétie, who was also working for the Parlement, and that La Boétie fell ill and died at the age of thirty-two. A letter Montaigne wrote about the death, printed in the " + a(V1, "Hazlitt edition") + ", dates it to 18 August 1563. In it, Montaigne records his friend’s words to him: “I beg of you, as a mark of my affection to you, to accept my library.” In another letter he called La Boétie “the greatest man, in my judgment, of our age.”",
            "The Hazlitt biography says the two met by pure chance at some festive celebration in the town, and speaks of six years. Montaigne himself, in the essay, counts only “the four years I had the happiness to enjoy the sweet society of this excellent man.” The sources differ on dates; the essay is clear about what those years meant to him.",
        ]),
        ("The friendship he described", [
            "In " + a(OF, "Of Friendship") + ", Montaigne describes how the friendship began, before the two had met: “We sought one another long before we met, and by the characters we heard of one another.” When they did meet, by chance at what he calls a great city entertainment, they were “so mutually taken with one another” that from then on nothing was closer to either than the other.",
            "He sets this apart from everything else that goes by the name. In ordinary friendships, people are joined by some advantage or occasion. In the friendship he means, the souls mix and work themselves into one piece, with so universal a mixture that there is “no more sign of the seam by which they were first conjoined.” It is in this setting that he gives his famous answer. The reason he loved La Boétie could not be expressed otherwise than: because it was he, because it was I.",
            "The phrase is less evasive than it sounds. Montaigne is saying that the friendship did not rest on any quality that someone else could also have had, such as wit, learning or kindness. If it had, it could in principle have been transferred to another person with the same qualities. It rested on the two particular people. Explaining it by a reason would have made it smaller.",
            "The image of the seam supports this reading. A seam is where two pieces of cloth are joined, and it always shows; you can see where one ends and the other begins. Montaigne’s claim is that in this friendship the join had vanished. That is also why he cannot give a reason. A reason would point to some part of one person that attracted the other, and so would show the seam he says is not there.",
        ]),
        ("Common friendships and perfect ones", [
            "Montaigne distinguishes sharply between two kinds. For ordinary friendships he accepts a cautious maxim he attributes to Chilo: “Love him, so as if you were one day to hate him; and hate him so as you were one day to love him.” That advice, he says, suits common friendships, which call for prudence, but would be an insult to the kind he means.",
            "“Common friendships will admit of division,” he writes; “one may love the beauty of this person, the good-humour of that,” and so on through other qualities in other friends. The perfect friendship cannot. “The multitude of friends for the perfect friendship I speak of is indivisible,” in Cotton’s wording, and it cannot possibly admit of a rival. Each friend gives himself so wholly to the other that nothing is left to divide.",
            "It also abolishes the ordinary bookkeeping of favours. In such a friendship, he writes, words like benefits, obligation, acknowledgment, entreaty, thanks, and the like have no place, because everything is held in common and neither friend can give anything to the other or owe him anything. Montaigne calls these “words of division and distinction”.",
            "HTML:" + K.table("Montaigne’s two kinds of friendship",
                ["", "Common friendship", "Perfect friendship"],
                [["Basis", "Some advantage, occasion or quality", "The two people themselves"],
                 ["Can be shared?", "Yes, among several friends", "No; it admits no rival"],
                 ["Favours and thanks", "Normal and expected", "Have no place"],
                 ["Right attitude", "Caution", "Complete trust"],
                 ["How common?", "Ordinary", "Perhaps once in three ages"]],
                source='Source: Montaigne, Of Friendship, <a href="' + OF + '" target="_blank" rel="noopener">Cotton translation</a>.'),
        ]),
        ("What friendship is not", [
            "Much of the essay defines friendship by what it is not. Of parents and children, " + a(OF, "Montaigne writes") + " that “That of children to parents is rather respect,” and adds that “The father and the son may be of quite contrary humours.” Of brothers, he observes that when they pursue their fortune and advancement by the same path, it is hardly possible but they must of necessity often jostle and hinder one another.",
            "He compares friendship with erotic love, and finds love’s fire “more active, more eager, and more sharp: but withal, ’tis more precipitant, fickle, moving, and inconstant.” Friendship, by contrast, is “a general and universal fire, but temperate and equal, a constant established heat, all gentle and smooth, without poignancy or roughness.”",
            "Marriage, he writes, is a covenant the entrance into which only is free, but the continuance in it forced and compulsory, and it carries other dependencies besides the two people. And he doubts that women can take part in the friendship he describes, writing that they do not appear to be endued with constancy of mind. That view is of its time and is presented here as his, not defended. It sits oddly with his own account, in which the deciding fact about a friend is not a type but an individual.",
        ]),
        ("The book that was not printed", [
            "The essay was originally meant to introduce a work by La Boétie. Montaigne describes it as a discourse that he called Voluntary Servitude, written when its author was young; a note in the Hazlitt edition says he was not yet eighteen, and that some editions say sixteen. Montaigne had planned to make it the centrepiece of his book, in the place where a painter puts his finest picture.",
            "He changed his mind. In " + a(OF, "Cotton’s wording") + ", “Because I have found that that work has been since brought out, and with a mischievous design, I have refrained from inserting it here.” Others had published it for political purposes he did not share. In its place he offered, he writes, another piece of a more gay and frolic air: a set of La Boétie’s sonnets, which follow the essay as the next chapter, titled in the " + a(V1, "Hazlitt edition’s contents") + " Nine-and-twenty sonnets of Estienne de la Boetie. Montaigne, the " + a(CUL, "Cambridge exhibition") + " notes, also oversaw the publication of some of his friend’s works. Keeping his friend’s writing in print was one of the ways he kept faith with him.",
            "The numbering of the chapter varies between editions. The Hazlitt edition counts Of Friendship as chapter 27 of Book I, followed by the sonnets as chapter 28; the Cambridge exhibition cites it as Book I, chapter 28. The essay is the same.",
        ]),
        ("After the loss", [
            "The last part of the essay is grief. Montaigne compares the rest of his life with the time he had with his friend and finds it, in " + a(OF, "Cotton’s wording") + ", “nothing but smoke, an obscure and tedious night.” Since the loss, he writes, “I have only led a languishing life; the very pleasures that present themselves to me, instead of administering anything of consolation, double my affliction for his loss.”",
            "This is striking from the writer who had a medal struck asking what do I know, and whose Essays question custom, certainty and his own judgement at every turn. On this one subject he does not doubt. He claims such a friendship comes about perhaps once in three ages, saying it is much if fortune bring it but once to pass in three ages, and he is sure he had one.",
            "The essay also explains, in part, why the Essays exist at all. Montaigne opens Of Friendship by comparing his writing to the work of a painter in his house, who fills the empty spaces around a central picture with decorative figures. “What are these things I scribble,” he asks, “other than grotesques and monstrous bodies, made of various parts.” The central picture was to have been his friend’s work.",
        ]),
        ("Montaigne and Aristotle", [
            "Montaigne knew the classical tradition on friendship well, and quotes a saying he attributes to Aristotle: “O my friends, there is no friend.” He applies it to common friendships, which call for guardedness because the bond may not hold, not to the perfect kind he describes.",
            "Aristotle’s own account, set out in the essay on " + ESSAY57 + ", sorts friendships by what they rest on: usefulness, pleasure, or goodness. Montaigne’s perfect friendship goes further than Aristotle’s best kind in one respect. Aristotle explains the highest friendship by the goodness of the friends; Montaigne declines to explain his at all, beyond pointing to the two people. That refusal is the heart of the line.",
            "HTML:" + K.callout("warn", "Reading it today",
                "<p>Montaigne describes something he believed almost no one would experience. Reading the essay as a standard that every close friendship must meet would turn a portrait of grief into a source of disappointment. It is more useful as a description of what made one attachment irreplaceable.</p>"),
        ]),
        ("What this does and does not say", [
            "Read plainly, Of Friendship does not give a theory of how to make friends, or a test for which friendships are real. It describes one friendship, says why it could not be explained by any reason other than the two people in it, and records what its loss did to the man left behind. Its famous line is an admission that some attachments are to a person, not to anything the person has.",
            "Other essays here look at friendship and closeness from different directions. " + ESSAY43.replace(">what the Stoics", ">What the Stoics") + " sets out an older school’s view of what is and is not in our control, including other people. " + ESSAY52.replace(">what Epicurus", ">What Epicurus") + " describes a school that placed friendship near the top of a good life. And " + ESSAY55 + " looks at modern research on how close partners shape who each other becomes.",
        ]),
    ],
    note=[
        "Quotations are from Charles Cotton’s translation as edited by W. C. Hazlitt. Dates for the friendship differ between sources: Montaigne counts four years, the Hazlitt biography six, and the Cambridge exhibition dates the meeting to around 1559.",
    ],
    faqs=[
        ("What does “because it was he, because it was I” mean?",
         "Montaigne’s answer when asked why he loved his friend La Boétie. He meant the friendship rested on the two people themselves, not on any quality or advantage that could be named or found in someone else."),
        ("Who was Étienne de La Boétie?",
         "Montaigne’s closest friend, who also worked for the Parlement. He died in August 1563, aged about thirty-two, and left Montaigne his library. He wrote a discourse known as Voluntary Servitude."),
        ("How long were Montaigne and La Boétie friends?",
         "Montaigne himself speaks of four years. Other sources give different dates; the Cambridge University Library dates their meeting to around 1559, and La Boétie died in 1563."),
        ("How did Montaigne distinguish friendships?",
         "He separated common friendships, based on some advantage and calling for caution, from a perfect friendship in which two souls merge, which cannot be shared with a rival and has no place for favours or thanks."),
        ("Did Montaigne think women could be friends in this way?",
         "He doubted it, writing that women did not appear to have the constancy of mind for such friendship. The view reflects his time, and sits awkwardly with his own claim that friendship rests on the individual."),
    ],
    related=[
        ("what-aristotle-meant-by-the-three-kinds-of-friendship", "What Aristotle meant by the three kinds of friendship, and why only one lasts", "Philosophy"),
        ("what-epicurus-meant-by-pleasure", "What Epicurus meant by pleasure, and why it was never about indulgence", "Philosophy"),
    ],
)

if __name__ == "__main__":
    newpost.build(POST)
