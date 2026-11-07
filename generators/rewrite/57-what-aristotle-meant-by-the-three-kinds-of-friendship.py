#!/usr/bin/env python3
"""Essay 57 :: what-aristotle-meant-by-the-three-kinds-of-friendship  (Philosophy)

Sources fetched and read on 5 Nov 2026: Nicomachean Ethics Books VIII and IX
in W. D. Ross's translation (Elpenor full text, with IntraText for Book IX
chapters); SEP "Friendship" (Helm), Fall 2005 and Spring 2006 archives, and
the Summer 2016 notes on Cooper; Britannica summary and topic page;
Diogenes Laertius 5.20 in Hicks's translation (Wikisource mirror);
Pakaluk 2005 chapter summary (Cambridge Core).
No Bekker numbers are given, because no fetched source showed them.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import newpost, postkit as K

EXT = ' target="_blank" rel="noopener"'
def a(url, text):
    return '<a href="%s"%s>%s</a>' % (url, EXT, text)

EL = "https://www.ellopos.net/Elpenor/greek-texts/ancient-greece/aristotle/nicomachean-ethics-b.asp?pg="
NE81, NE82, NE83, NE834, NE84, NE86, NE87, NE88, NE89, NE910 = (EL + "4", EL + "5", EL + "6", EL + "7", EL + "8", EL + "9", EL + "11", EL + "12", EL + "13", EL + "38")
NE94 = "https://www.intratext.com/IXT/ENG2244/_P2R.HTM"
NE98 = "https://www.intratext.com/IXT/ENG2244/_P2V.HTM"
NE99 = "https://www.intratext.com/IXT/ENG2244/_P2W.HTM"
SEP = "https://plato.stanford.edu/archives/spr2006/entries/friendship/"
SEPNOTES = "https://plato.stanford.edu/archives/sum2016/entries/friendship/notes.html"
BRIT = "https://www.britannica.com/summary/Aristotle"
BRITNE = "https://www.britannica.com/topic/Nicomachean-Ethics"
DL = "https://kwx.liehendr.com/content/wikisource_en_all_maxi_2022-09/A/Lives_of_the_Eminent_Philosophers/Book_V"
PAKALUK = "https://www.cambridge.org/core/product/FF4BF4BC53565712F75BFC3B7BD63410"

ESSAY43 = '<a href="/writing/what-the-stoics-meant-by-what-is-up-to-us">what the Stoics meant by what is up to us</a>'
ESSAY52 = '<a href="/writing/what-epicurus-meant-by-pleasure">what Epicurus meant by pleasure</a>'
ESSAY55 = '<a href="/writing/what-the-michelangelo-phenomenon-says">what the Michelangelo phenomenon says</a>'
ESSAY67 = '<a href="/writing/what-montaigne-meant-by-because-it-was-he">what Montaigne meant by because it was he, because it was I</a>'

POST = dict(
    slug="what-aristotle-meant-by-the-three-kinds-of-friendship", num=57, cat="Philosophy", read="auto",
    date="2026-11-05",
    gen="rewrite/57-what-aristotle-meant-by-the-three-kinds-of-friendship.py",
    title="What Aristotle meant by the three kinds of friendship, and why only one lasts",
    dek="Aristotle gave a fifth of his book on ethics to friendship. His central idea is simple: people love each other for what is useful, for what is pleasant, or for who the other person is. Only the last kind, he thought, survives change. The idea is easy to misread as a ranking of people.",
    takeaway="In Books VIII and IX of the Nicomachean Ethics, Aristotle distinguished three kinds of friendship by what is loved: the useful, the pleasant and the good. Friendships of utility and pleasure, he wrote, are incidental and easily dissolved when the use or pleasure ends. Perfect friendship is between people who are good and alike in virtue, who wish each other well for the other’s own sake; it is rare, needs time and familiarity, and lasts as long as they are good. He called a friend another self, argued that the good person should be a lover of self in the right sense, and doubted anyone could have many friends of the best kind. Scholars still disagree about whether the lesser two are real friendships at all.",
    sections=[
        ("What Aristotle meant", [
            "Aristotle meant that friendships differ by what each person loves in the other: their usefulness, the pleasure of their company, or their character. The first two, he argued, end when the use or pleasure ends. The third, between good people who wish each other well for the other’s own sake, is rare, takes time, and lasts.",
            "HTML:" + K.takeaways([
                "Aristotle discusses friendship in two of the ten books of the Nicomachean Ethics.",
                "The three things that make someone lovable are the good, the pleasant and the useful.",
                "Friendships of utility and pleasure are, in his word, incidental, and easily dissolved.",
                "Perfect friendship is between people who are good and alike in virtue, and wish each other well for the other’s sake.",
                "Such friendships are rare and need time: people cannot know each other until they have eaten salt together.",
                "Whether the lesser two count as real friendships is still debated.",
            ]),
            "This essay reads Aristotle in W. D. Ross’s translation and sets out what he argued and what scholars say about it. Like " + ESSAY43 + ", it treats an ancient idea as a practical one, while being clear about where the text ends and interpretation begins.",
            "HTML:" + K.callout("definition", "Philia",
                "<p>The Greek word translated as friendship is philia. As Bennett Helm notes in the " + a(SEP, "Stanford Encyclopedia of Philosophy") + ", philia is in some ways importantly different from what we ordinarily think of as friendship: it extends not just to friends but also to family members, business associates, and one’s country at large.</p>"),
        ]),
        ("Why friendship gets two books", [
            "Aristotle, according to " + a(BRIT, "Britannica") + ", was born in 384 BCE in Stagira and died in 322 BCE in Chalcis. His Nicomachean Ethics, which Britannica’s " + a(BRITNE, "entry on the work") + " describes as ten books, possibly brought together by his son, is mostly about how to live well. Michael Pakaluk, in a " + a(PAKALUK, "2005 introduction") + ", notes that Aristotle devotes one-fifth of his treatise to a topic that is usually neglected altogether by contemporary moral theory.",
            "The reason is that, for Aristotle, friendship is not an extra. Book VIII opens, in " + a(NE81, "Ross’s translation") + ": “For without friends no one would choose to live, though he had all other goods.” And it is not only useful: “But it is not only necessary but also noble.” He even sets it beside justice, and ahead of it in one respect: “when men are friends they have no need of justice, while when they are just they need friendship as well.”",
        ]),
        ("Three things worth loving", [
            "The core of the account is a claim about what people love in each other. In " + a(NE82, "Book VIII") + ": “For not everything seems to be loved but only the lovable, and this is good, pleasant, or useful.” So: “There are therefore three kinds of friendship, equal in number to the things that are lovable.”",
            "Friendship also needs both sides to know it. " + a(NE82, "Aristotle notes") + " that if someone wishes another person well but the wish is not returned, “we ascribe only goodwill, if the wish is not reciprocated.” A friendship is mutual and recognised by both.",
            "HTML:" + K.table("Aristotle’s three friendships",
                ["Kind", "What is loved", "How long it lasts", "Typical of"],
                [["Utility", "What the other is useful for", "Until the usefulness ends", "Older people, in his view"],
                 ["Pleasure", "The pleasure of the other’s company", "Until the pleasure fades", "Young people, in his view"],
                 ["The good", "The other person’s character, for their own sake", "As long as both remain good", "Good people, who are rare"]],
                source='Summarised from <a href="' + NE82 + '" target="_blank" rel="noopener">Nicomachean Ethics VIII.2</a> and <a href="' + NE83 + '" target="_blank" rel="noopener">VIII.3</a>, Ross’s translation.'),
        ]),
        ("Friendships of use and pleasure", [
            "Aristotle does not despise the first two kinds, but he is clear about their limits. In " + a(NE82, "his words") + ", they are friendships in which people love each other not for who they are but for what they get: “And thus these friendships are only incidental.” And so: “Such friendships, then, are easily dissolved, if the parties do not remain like themselves.” When one person stops being useful or pleasant, the reason for the friendship goes.",
            "He links each kind to a stage of life. Utility friendship, " + a(NE83, "he writes") + ", “seems to exist chiefly between old people.” “On the other hand the friendship of young people seems to aim at pleasure,” and so the young “fall in love and quickly fall out of love, changing often within a single day.”",
            "He also notes that these lesser friendships are open to anyone. " + a(NE834, "In his words") + ": “For the sake of pleasure or utility, then, even bad men may be friends of each other.” The best kind is not.",
        ]),
        ("Perfect friendship", [
            "The third kind is what Aristotle calls perfect, or complete. In " + a(NE83, "Ross’s translation") + ": “Perfect friendship is the friendship of men who are good, and alike in virtue.” What marks it is the direction of the wish: “Now those who wish well to their friends for their sake are most truly friends.” And so it lasts: “their friendship lasts as long as they are good”, since goodness is “an enduring thing.”",
            "It is also rare, for two reasons. The first is that good people are rare: “But it is natural that such friendships should be infrequent; for such men are rare,” he writes " + a(NE834, "a little later") + ". The second is time: “Further, such friendship requires time and familiarity,” and, quoting a proverb, “men cannot know each other till they have ‘eaten salt together’.” He adds a line that will be familiar to anyone who has made a new friend: “for a wish for friendship may arise quickly, but friendship does not.”",
            "The other two kinds are measured against this one. Perfect friends, " + a(NE84, "Aristotle writes") + ", are “friends without qualification; the others are friends incidentally and through a resemblance to these.” As " + a(NE83, "the previous chapter") + " makes clear, a perfect friendship is also useful and pleasant; the lesser kinds have only part of what it has.",
            "HTML:" + K.callout("note", "Good, in Aristotle’s sense",
                "<p>One reading worth avoiding: good here does not mean spotless. The friendship Aristotle has in mind is between people “alike in virtue”, that is, people loved for their character. The claim is that friendships built on character, rather than on use or pleasure, are the ones that survive change.</p>"),
        ]),
        ("Unequal friends, distance and justice", [
            "Not every friendship is between equals, and Aristotle discusses those too. In " + a(NE87, "VIII.7") + " he writes: “But there is another kind of friendship, viz. that which involves an inequality between the parties.” In these, he argues, the better should be more loved than he loves, and when the love is in proportion to the merit of the parties, then in a sense arises equality. In " + a(NE88, "VIII.8") + " he adds that loving seems to be the characteristic virtue of friends.",
            "He also thinks friendship needs to be lived. In " + a(NE84, "VIII.5") + " he observes that distance does not break off the friendship absolutely, but only the activity of it, and that there is nothing so characteristic of friends as living together. He adds a warning: “But if the absence is lasting, it seems actually to make men forget their friendship; hence the saying ‘out of sight, out of mind’.”",
            "And he connects friendship to fairness. Friendship and justice, " + a(NE89, "he writes") + ", seem to be concerned with the same objects, and he quotes a proverb with approval: “what friends have is common property” expresses the truth, “for friendship depends on community.” For Aristotle, friendship is not only a private feeling but part of what holds a shared life together.",
        ]),
        ("Another self", [
            "Book IX contains Aristotle’s most famous phrase about friendship. He argues that friendly feeling for others grows out of a person’s relation to themselves: in " + a(NE94, "his words") + ", “Friendly relations with one’s neighbours, and the marks by which friendships are defined, seem to have proceeded from a man’s relations to himself.” A good person, on this view, stands to a friend much as to himself, “for his friend is another self.”",
            "That raises an obvious worry: is friendship then a kind of selfishness? Aristotle takes the question head on in " + a(NE98, "IX.8") + ": “The question is also debated, whether a man should love himself most, or some one else.” His answer is that self-love is not always the selfish kind people criticise. The good person, he writes, is seen to assign to himself the greater share in what is noble, and so: “Therefore the good man should be a lover of self.” Such a person, he adds, does many acts for the sake of his friends and his country, if necessary dying for them.",
            "He also asks whether a happy person, who has everything, needs friends at all. In " + a(NE99, "IX.9") + " his answer is yes: “But it seems strange, when one assigns all good things to the happy man, not to assign friends,” because “man is a political creature and one whose nature is to live with others.” So: “The man who is to be happy will therefore need virtuous friends.”",
        ]),
        ("How many friends?", [
            "Aristotle doubted anyone could have many friends of the best kind. In " + a(NE910, "IX.10") + " he asks, “Should we, then, make as many friends as possible,” and answers that for friends too there is a fixed number: “perhaps the largest number with whom one can live together.” It would seem, he writes, actually impossible to be a great friend to many people.",
            "He points to experience, " + a(NE910, "in the same chapter") + ": the famous friendships of this sort are always between two people. And those who have many friends and mix intimately with them all, he writes, are thought to be no one’s friend, except in the way proper to fellow-citizens. He makes the same point in " + a(NE86, "VIII.6") + ": “One cannot be a friend to many people in the sense of having friendship of the perfect type with them.”",
            "HTML:" + K.callout("warn", "Lines Aristotle did not write",
                "<p>“A friend is a single soul dwelling in two bodies” is not in the Ethics. It is a saying that " + a(DL, "Diogenes Laertius") + " reports Aristotle gave when asked what a friend is. And “a friend to all is a friend to none” is a modern paraphrase; Ross’s Aristotle says that those who mix intimately with many friends are thought to be no one’s friend, except as fellow-citizens.</p>"),
        ]),
        ("Are the lesser kinds real friendships?", [
            "Scholars disagree about how to read the three kinds. One reading, which Helm describes in the " + a(SEP, "Stanford Encyclopedia") + ", takes pleasure and utility friendships to be at best deficient modes of friendship, with virtue friendships the only genuine, non-deficient kind.",
            "Another reading resists that. The " + a(SEPNOTES, "encyclopedia’s notes") + " record that Cooper, in a 1977 paper, tries to refute this understanding of Aristotle: on his reading, even friends of utility and pleasure can wish each other well for the other’s own sake, because the usefulness or pleasure is what causes the well-wishing, not what justifies it. Helm, in the " + a(SEP, "main entry") + ", acknowledges the pull of this: all three kinds of friendship seem to involve a concern for your friend for his sake, though he resolves the tension the other way.",
            "The disagreement matters for how the idea is used. Read strictly, Aristotle seems to rank most friendships as second-rate. Read Cooper’s way, he is describing what holds different friendships together, and allowing that real care can grow in all of them.",
        ]),
        ("What this offers, and what it does not", [
            "Read in his own words, Aristotle offers a clear test rather than a ranking of people: what, in this friendship, is actually loved? If it is mainly use or pleasure, the friendship may still be good, but it will probably not survive the end of the use or the pleasure. If it is the other person, for their own sake, it can.",
            "It also offers a realistic sense of scale. The best friendships take time, cannot be many, and depend on both people continuing to be who they are. That is not a counsel of despair; it is a reason to invest in the few.",
            "Other essays here meet the idea at different points. " + ESSAY52.replace(">what Epicurus", ">What Epicurus") + " describes another ancient school that put friendship near the top of what makes a life good. " + ESSAY67.replace(">what Montaigne", ">What Montaigne") + " follows a Renaissance writer who described a friendship that, in his view, needed no reason at all. And " + ESSAY55.replace(">what the Michelangelo", ">What the Michelangelo") + " looks at modern research on how close partners help each other become who they want to be, which echoes Aristotle’s idea of friends who want the good for each other.",
        ]),
    ],
    note=[
        "Aristotle is quoted from W. D. Ross’s translation of the Nicomachean Ethics. Chapter numbers follow the online texts linked; standard Bekker references are not given.",
    ],
    faqs=[
        ("What are Aristotle's three kinds of friendship?",
         "Friendships of utility, based on what each is useful for; of pleasure, based on enjoying each other's company; and of the good, based on each person's character and wishing each other well for the other's sake. He sets them out in Book VIII of the Nicomachean Ethics."),
        ("Which kind of friendship lasts, according to Aristotle?",
         "Perfect friendship between good people, which he says lasts as long as they are good. Friendships of utility and pleasure are easily dissolved when the use or pleasure ends."),
        ("What did Aristotle mean by a friend is another self?",
         "That a good person wishes for a friend what they wish for themselves, so that friendly feeling for others grows out of a person's right relation to themselves. The phrase is from Book IX of the Nicomachean Ethics."),
        ("Did Aristotle say a friend is a single soul in two bodies?",
         "Not in the Ethics. Diogenes Laertius reports it as Aristotle's reply when asked what a friend is."),
        ("How many true friends can you have, according to Aristotle?",
         "Only a few. He argues there is a limit set by how many people one can actually live alongside, and that it seems impossible to be a great friend to many people."),
    ],
    related=[
        ("what-the-stoics-meant-by-what-is-up-to-us", "What the Stoics meant by what is up to us, and what it means for love", "Philosophy"),
        ("what-epicurus-meant-by-pleasure", "What Epicurus meant by pleasure, and why it was never about indulgence", "Philosophy"),
    ],
)

if __name__ == "__main__":
    newpost.build(POST)
