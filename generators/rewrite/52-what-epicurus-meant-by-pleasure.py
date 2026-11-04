#!/usr/bin/env python3
"""Essay 52 :: what-epicurus-meant-by-pleasure  (Philosophy)

Sources fetched and read on 4 Nov 2026: Diogenes Laertius Book X.121-140 in
R. D. Hicks's 1925 Loeb translation (Perseids), containing the Letter to
Menoeceus, Principal Doctrines I-V and the report at X.136; Vatican Sayings
translated by Peter Saint-Andre (CC0, monadnock.net); Konstan, SEP
"Epicurus", Summer 2006 archive; O'Keefe, IEP "Epicurus"; Britannica
"Epicurus"; Merriam-Webster "epicure"; Seneca Letter 21 in Gummere's Loeb
translation (ToposText); Gilleland on the tetrapharmakos, with the BMCR
2020.08.06 review; Archaeology magazine 2015 on Diogenes of Oinoanda;
Lactantius De Ira Dei 13 (Fletcher, EWTN).
Principal Doctrines beyond V are not quoted, because no copy of the Hicks
text beyond X.140 could be fetched.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import newpost, postkit as K

EXT = ' target="_blank" rel="noopener"'
def a(url, text):
    return '<a href="%s"%s>%s</a>' % (url, EXT, text)

DL = "https://cts.perseids.org/read/greekLit/tlg0004/tlg001/perseus-eng2/10.1.121-10.1.140"
VS = "https://monadnock.net/epicurus/vatican-sayings.html"
SEP = "https://plato.stanford.edu/archives/sum2006/entries/epicurus/"
IEP = "https://iep.utm.edu/epicur/"
BRIT = "https://www.britannica.com/biography/Epicurus"
MW = "https://www.merriam-webster.com/dictionary/epicure"
SENECA = "https://topostext.org/work/736"
TETRA = "https://laudatortemporisacti.blogspot.com/2013/03/the-epicurean-tetrapharmakos.html"
BMCR = "https://bmcr.brynmawr.edu/?p=49101"
OINO = "https://archaeology.org/issues/180-1507/features/3344-turkey-oinoanda-epicurean-inscription"
LACT = "https://www.ewtn.com/catholicism/library/treatise-on-the-anger-of-god-de-ira-dei-11482"

ARIST = '<a href="/writing/what-aristotle-meant-by-the-three-kinds-of-friendship">what Aristotle meant by the three kinds of friendship</a>'
ESSAY43 = '<a href="/writing/what-the-stoics-meant-by-what-is-up-to-us">what the Stoics meant by what is up to us</a>'
ESSAY47 = '<a href="/writing/why-we-blame-the-people-we-love">why we blame the people we love</a>'
ESSAY51 = '<a href="/writing/what-rumination-is">what rumination is</a>'
ESSAY50 = '<a href="/writing/what-your-partner-does-with-your-good-news">what your partner does with your good news</a>'

POST = dict(
    slug="what-epicurus-meant-by-pleasure", num=52, cat="Philosophy", read="auto",
    date="2026-11-04",
    gen="rewrite/52-what-epicurus-meant-by-pleasure.py",
    title="What Epicurus meant by pleasure, and why it was never about indulgence",
    dek="His name now stands for fine food and good wine. In his school the usual drink was water and the food barley bread, and he argued that the best life is one free of pain and fear, spent with friends. What he meant by pleasure is close to the opposite of what the word suggests.",
    takeaway="Epicurus (341 to 270 BCE, though some sources give 271) taught that pleasure is the goal of life, but by pleasure he meant the absence of pain in the body and of trouble in the soul, not luxury. He distinguished the pleasures of satisfying a want from the settled pleasure of being without want, and valued the second more. He sorted desires into natural and necessary, natural only, and empty, and advised satisfying the first, being careful with the second and dropping the third. He argued that death and the gods are nothing to fear, and placed friendship near the top of what wisdom provides. The modern sense of epicure as a lover of fine food comes from his critics, not from him.",
    sections=[
        ("What Epicurus meant by pleasure", [
            "Epicurus meant by pleasure the absence of pain in the body and of trouble in the mind. He did not mean feasting or luxury, and said so directly. The best life, on his view, is a calm one: simple needs met, groundless fears removed, and time spent with friends.",
            "HTML:" + K.takeaways([
                "Epicurus called pleasure the goal of life, and defined it as the absence of pain in the body and of trouble in the soul.",
                "He rejected the pleasures of the prodigal and of sensuality by name.",
                "He valued the settled pleasure of being without want above the pleasure of satisfying a want.",
                "He sorted desires into natural and necessary, natural only, and empty, and advised dropping the empty ones.",
                "He argued that death is nothing to us, and that friendship is among the greatest goods.",
                "The modern meaning of epicure, a lover of fine food, came from his critics.",
            ]),
            "This essay reads Epicurus mostly in his own words, from the few writings that survive, and sets out what scholars say about them. Like " + ESSAY43 + ", it treats an ancient philosophy as a practical one, while being clear about where the ancient view ends and modern interpretation begins.",
            "HTML:" + K.callout("definition", "Pleasure, in Epicurus",
                "<p>In his " + a(DL, "Letter to Menoeceus") + ", in R. D. Hicks’s translation: “By pleasure we mean the absence of pain in the body and of trouble in the soul.” The second half is what the " + a(IEP, "Internet Encyclopedia of Philosophy") + " calls tranquillity, ataraxia in Greek.</p>"),
        ]),
        ("A philosopher with the wrong reputation", [
            "Epicurus was born on Samos in 341 BCE and died in Athens in 270, according to " + a(BRIT, "Britannica") + ", which notes that he and his followers came to Athens in 306 and established a school that came to be known as the Garden. Unlike both of the city’s famous schools, Britannica records, it admitted women, and even one of Epicurus’s slaves, named Mouse. The " + a(IEP, "Internet Encyclopedia of Philosophy") + " gives his death as around 271 or 270.",
            "Life in the Garden was plain. Britannica describes water as the usual drink, with a small daily ration of wine allowed, and barley bread as the food, and observes that, quite different from the usual connotations of the word epicurean today, life in the house and garden was simple. It also cautions against one common romantic picture: there was no communal property, as there was in the Pythagorean schools.",
            "The reputation came from his opponents. " + a(MW, "Merriam-Webster’s note on the word epicure") + " explains that detractors in his own time and later reduced his notions of pleasure to material and sensual gratification. When the word entered English in the 16th century, it meant something like hedonist; the sense of a refined palate came later. Britannica adds that only the attacks of Stoic opponents support any idea of sexual irregularity.",
            "Epicurus was, in the words of the " + a(IEP, "Internet Encyclopedia of Philosophy") + ", a voluminous writer, but almost none of his own work survives. His surviving letters and main teachings are read today in the tenth book of the " + a(DL, "Lives of the Eminent Philosophers") + " by the later writer Diogenes Laertius, alongside a collection known as the " + a(VS, "Vatican Sayings") + " and the reports of later followers and critics.",
        ]),
        ("The absence of pain and trouble", [
            "The central passage is in the Letter to Menoeceus. In " + a(DL, "Hicks’s 1925 translation") + ": “When we say, then, that pleasure is the end and aim, we do not mean the pleasures of the prodigal or the pleasures of sensuality, as we are understood to do by some through ignorance, prejudice, or wilful misrepresentation. By pleasure we mean the absence of pain in the body and of trouble in the soul.”",
            "He goes on to name what does not produce a pleasant life: “It is not an unbroken succession of drinking-bouts and of revelry, not sexual love, not the enjoyment of the fish and other delicacies of a luxurious table, which produce a pleasant life; it is sober reasoning, searching out the grounds of every choice and avoidance.”",
            "This does not make Epicurus an ascetic. The same letter calls pleasure “our first and kindred good” and says that all pleasure is good because it is naturally akin to us. But he immediately adds that not all pleasure is choiceworthy: “we do not choose every pleasure whatsoever, but ofttimes pass over many pleasures” when a greater annoyance ensues from them. The skill that does the choosing he calls prudence: “Of all this the beginning and the greatest good is prudence,” and “prudence is a more precious thing even than philosophy.”",
            "HTML:" + K.callout("note", "Hedonist, or something else",
                "<p>Tim O’Keefe, writing in the " + a(IEP, "Internet Encyclopedia of Philosophy") + ", suggests that it might be less misleading to call Epicurus a “tranquillist” instead of a “hedonist”. The label is a scholar’s, not his, but it captures where his idea of pleasure points.</p>"),
        ]),
        ("Pleasures of motion and of rest", [
            "Epicurus distinguished two kinds of pleasure. " + a(DL, "Diogenes Laertius") + " quotes him: “Peace of mind and freedom from pain are pleasures which imply a state of rest; joy and delight are seen to consist in motion and activity.”",
            "Scholars call these kinetic and katastematic, or moving and static, pleasures. David Konstan, in the " + a(SEP, "Stanford Encyclopedia of Philosophy") + ", explains that kinetic pleasures involve the return to a stable or healthy state, such as the pleasurable elimination of hunger or thirst, while katastematic pleasure is a state rather than a process: the pleasure that accompanies well-being as such. O’Keefe, in the " + a(IEP, "Internet Encyclopedia of Philosophy") + ", notes that Epicurus says these static pleasures are the best pleasures.",
            "HTML:" + K.table("Two kinds of pleasure",
                ["", "Moving (kinetic)", "Resting (katastematic)"],
                [["What it is", "The process of satisfying a want", "The state of being without want or fear"],
                 ["Example", "Drinking when thirsty", "Being healthy and untroubled"],
                 ["Epicurus’s ranking", "Good, but not the goal", "The best pleasure"]],
                source='Sources: <a href="' + SEP + '" target="_blank" rel="noopener">Konstan, Stanford Encyclopedia of Philosophy</a>; <a href="' + IEP + '" target="_blank" rel="noopener">O’Keefe, Internet Encyclopedia of Philosophy</a>.'),
            "This is why the third of his main teachings sets a limit. In " + a(DL, "Hicks’s translation") + ": “The magnitude of pleasure reaches its limit in the removal of all pain.” Once nothing hurts and nothing troubles you, on this account, pleasure is complete, and chasing ever more intense experiences does not add to it.",
        ]),
        ("Three kinds of desire", [
            "The practical core of the philosophy is a sorting of desires. The " + a(DL, "Letter to Menoeceus") + " says: “We must also reflect that of desires some are natural, others are groundless; and that of the natural some are necessary as well as natural, and some natural only.” Konstan, in the " + a(SEP, "Stanford Encyclopedia") + ", describes the empty desires as those that have as their objects things designated by empty sounds, such as immortality.",
            "HTML:" + K.table("Epicurus’s three kinds of desire",
                ["Kind", "Examples", "What to do"],
                [["Natural and necessary", "Food, drink, shelter", "Satisfy them, simply"],
                 ["Natural only", "Rich food, luxury", "Enjoy them when they come, without depending on them"],
                 ["Empty", "Fame, wealth without limit, immortality", "Drop them; they can never be satisfied"]],
                source='The three kinds from the <a href="' + DL + '" target="_blank" rel="noopener">Letter to Menoeceus</a> and <a href="' + SEP + '" target="_blank" rel="noopener">Konstan</a>; the examples and advice are a summary in plain terms, not Epicurus’s list.'),
            "The reason simple living matters is that it makes pleasure secure. In the " + a(DL, "letter") + ", he writes that bread and water “confer the highest possible pleasure when they are brought to hungry lips.” Just before this, he says that independence of outward things is a great good, not so as in all cases to use little, but so as to be contented with little if we have not much.",
            "Seneca quotes one of Epicurus’s sharpest lines with approval in " + a(SENECA, "his twenty-first letter") + ", in Richard Gummere’s translation: “If you wish to make Pythocles rich, do not add to his store of money, but subtract from his desires.” One of the " + a(VS, "Vatican Sayings") + ", translated by Peter Saint-Andre, makes the same point about need: anyone free of hunger, thirst and cold, and confident of staying so, can rival the gods for happiness.",
        ]),
        ("Nothing to fear", [
            "Two fears get particular attention in his surviving writings: of the gods and of death. The first of his main teachings, in " + a(DL, "Hicks’s translation") + ", begins: “A blessed and eternal being has no trouble himself and brings no trouble upon any other being.” On this view, the gods have no interest in troubling anyone.",
            "On death, the " + a(DL, "Letter to Menoeceus") + " gives his most famous argument: “Death, therefore, the most awful of evils, is nothing to us, seeing that, when we are, death is not come, and, when death is come, we are not.” The second main teaching puts it in terms of feeling: the body, once resolved into its elements, has no feeling, and that which has no feeling is nothing to us.",
            "A later Epicurean, Philodemus, compressed the teaching into four lines, known as the four-part cure or tetrapharmakos. In " + a(TETRA, "Michael Gilleland’s translation") + ", paraphrased here: god is not to be feared, death is not to be viewed with apprehension, the good is easily acquired, and the terrible is easily endured. The wording is the school’s, not Epicurus’s; a " + a(BMCR, "2020 review in the Bryn Mawr Classical Review") + " notes there is no evidence for the term in Epicurus’s own writings, though it also reports an argument that the four-part remedy itself goes back to him, since his Principal Doctrines open with the same four ideas.",
            "His followers took the medical image seriously. Probably early in the second century CE, according to " + a(OINO, "Archaeology magazine") + ", an Epicurean named Diogenes paid for a wall inscription in the town of Oinoanda, in what is now Turkey, that may have contained some 25,000 words, to advertise publicly what he called the medicines that bring salvation.",
        ]),
        ("Friends", [
            "For a philosophy often caricatured as selfish, Epicureanism made remarkable room for other people. Konstan, in the " + a(SEP, "Stanford Encyclopedia") + ", writes that Epicurus placed an extremely high value on friendship, or love: the Greek is philia.",
            "Two of the " + a(VS, "Vatican Sayings") + ", in Saint-Andre’s translation, show the range of what he said. One is cautious: “Every friendship is an excellence in itself, even though it begins in mutual advantage.” The Greek of that saying is disputed, and other readings give a different sense. The other is unguarded: “Friendship dances around the world, announcing to each of us that we must awaken to happiness.”",
            "A generation before Epicurus, Aristotle had built a whole theory of friendship around the question: what, in a friendship, is actually loved? That account is set out in " + ARIST + ".",
            "The Garden itself was meant to be welcoming. Seneca, in " + a(SENECA, "the same letter") + ", records the motto carved in the Garden: “Stranger, here you will do well to tarry; here our highest good is pleasure.” The keeper of the house, he goes on, will welcome you with barley-meal and serve you water in abundance.",
        ]),
        ("What is not quite Epicurus", [
            "Two famous lines are often attached to Epicurus too confidently. The first is the argument about evil: if God wishes to take away evils and cannot, he is feeble; if he can and will not, he is envious. It is known from the Christian writer Lactantius, who in " + a(LACT, "On the Anger of God") + " introduces it as an argument of Epicurus. The " + a(IEP, "Internet Encyclopedia of Philosophy") + " counts Epicurus among the earliest philosophers known to have raised the problem of evil, but the famous wording should be quoted as reported by Lactantius, not as Epicurus’s own words.",
            "The second is eat, drink and be merry. The " + a(IEP, "Internet Encyclopedia of Philosophy") + " observes that another ancient school, the Cyrenaics, better fit the stereotype of hedonists recommending a policy of eat, drink and be merry. Epicurus’s own advice ran nearly the other way.",
            "Many other sayings circulate online under his name without a source or translator. A good test is whether a line can be traced to the tenth book of Diogenes Laertius, the Vatican Sayings, or a named later author quoting him. Most of the lines in this essay can; that is why they are here.",
        ]),
        ("What this offers, and what it does not", [
            "Read in his own words, Epicurus offers a demanding idea dressed in an inviting one. Pleasure is the goal, but the pleasure in question is calm: needs met simply, fears examined and dropped, and life shared with friends. That asks for restraint as much as enjoyment, and for prudence above everything.",
            "It does not offer a full account of a good life for everyone. " + a(MW, "Merriam-Webster’s note") + " describes his ideal as a secluded life, which many people neither want nor can have, and the promise of the four-part cure, that the terrible is easily endured, will sound too hopeful to anyone in serious pain. Any borrowing here is a borrowing of an attitude, not an endorsement of the whole system.",
            "Other essays here meet Epicurus at different points. The essay on the Stoics, linked above, sets out the rival school’s answer to the same question of how to live calmly. " + ESSAY51.replace(">what rumination", ">What rumination") + " describes, in modern psychological terms, one of the mental disturbances Epicurus wanted to remove. And " + ESSAY50 + " looks at what modern research says about sharing good things with others, which he would have recognised.",
        ]),
    ],
    note=[
        "Quotations from the Letter to Menoeceus, the Principal Doctrines (which Hicks calls the Sovran Maxims) and Diogenes Laertius are from R. D. Hicks’s 1925 Loeb translation; the Vatican Sayings are in Peter Saint-Andre’s translation; Seneca is in Richard Gummere’s.",
    ],
    faqs=[
        ("What did Epicurus mean by pleasure?",
         "The absence of pain in the body and of trouble in the soul. In his Letter to Menoeceus he says explicitly that he does not mean the pleasures of the prodigal or of sensuality, and that sober reasoning, not feasting, produces a pleasant life."),
        ("What are Epicurus's three kinds of desire?",
         "Natural and necessary, such as food and shelter; natural but not necessary, such as luxury; and empty, which aim at things like immortality and can never be satisfied. He advised satisfying the first simply and dropping the last."),
        ("What is ataraxia?",
         "Tranquillity, or freedom from mental disturbance. Epicurus counted peace of mind and freedom from pain as pleasures of rest, and ranked them above the pleasures of satisfying a want."),
        ("Did Epicurus say eat, drink and be merry?",
         "There is no evidence he did. The Internet Encyclopedia of Philosophy notes that another ancient school, the Cyrenaics, better fits that stereotype. In Epicurus's school the usual drink was water and the food barley bread, and he argued that simple living makes pleasure secure."),
        ("Is the Epicurean paradox about evil really by Epicurus?",
         "The famous wording is known from the Christian writer Lactantius, who presents it as an argument of Epicurus. It should be quoted as reported by Lactantius rather than as Epicurus's own words."),
    ],
    related=[
        ("what-the-stoics-meant-by-what-is-up-to-us", "What the Stoics meant by what is up to us, and what it means for love", "Philosophy"),
        ("why-we-blame-the-people-we-love", "Why we blame the people we love, and what determinism would change", "Philosophy"),
    ],
)

if __name__ == "__main__":
    newpost.build(POST)
