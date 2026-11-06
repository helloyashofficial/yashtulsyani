#!/usr/bin/env python3
"""Essay 62 :: what-spinoza-meant-by-hope-and-fear  (Philosophy)

Sources fetched and read on 6 Nov 2026: Spinoza, Ethics Parts 3, 4 and 5 in
R. H. M. Elwes's translation (Project Gutenberg); Spinoza,
Theologico-Political Treatise, Author's Preface, Elwes translation (Project
Gutenberg); Stanford Encyclopedia of Philosophy, Spinoza (Nadler, 2004
archive) and Spinoza's Psychological Theory (LeBuffe, revised 2024);
Encyclopedia of Philosophy entry via Encyclopedia.com on the publication of
the Ethics; Lieberman and others (2007), Psychological Science, lab copy.
Not used: popular quotations attributed to Spinoza that could not be found
in the Elwes text.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import newpost, postkit as K

EXT = ' target="_blank" rel="noopener"'
def a(url, text):
    return '<a href="%s"%s>%s</a>' % (url, EXT, text)

E3 = "https://www.gutenberg.org/cache/epub/948/pg948.html"
E4 = "https://dev4.gutenberg.org/files/971/971.txt"
E5 = "https://www.gutenberg.org/files/975/975.txt"
TTP = "https://gutenberg.org/files/989/989-h/989-h.htm"
SEP = "https://plato.stanford.edu/archives/spr2004/entries/spinoza/"
SEPPSY = "https://plato.stanford.edu/ENTRiES/spinoza-psychological/"
ENC = "https://encyclopedia.com/humanities/encyclopedias-almanacs-transcripts-and-maps/spinoza-benedict-baruch-de-1632-1677"
LIEB = "https://sites.lifesci.ucla.edu/psych-sanlab/wp-content/uploads/sites/31/2016/03/Lieberman_2007_PsychScience.pdf"

ESSAY43 = '<a href="/writing/what-the-stoics-meant-by-what-is-up-to-us">what the Stoics meant by what is up to us</a>'
ESSAY52 = '<a href="/writing/what-epicurus-meant-by-pleasure">what Epicurus meant by pleasure</a>'
ESSAY61 = '<a href="/writing/what-learned-helplessness-actually-showed">what learned helplessness actually showed</a>'
ESSAY51 = '<a href="/writing/what-rumination-is">what rumination is</a>'

POST = dict(
    slug="what-spinoza-meant-by-hope-and-fear", num=62, cat="Philosophy", read="auto",
    date="2026-11-06",
    gen="rewrite/62-what-spinoza-meant-by-hope-and-fear.py",
    title="What Spinoza meant by hope and fear, and why he thought they come together",
    dek="Most people think of hope as the cure for fear. Spinoza, writing in the 1660s and 1670s, thought they were two sides of the same uncertainty, so that you never have one without the other. His answer was not more hope but more understanding.",
    takeaway="Baruch Spinoza (1632 to 1677) defined hope as an inconstant pleasure and fear as an inconstant pain, both arising from the idea of something past or future whose outcome we doubt. Because both rest on the same doubt, he argued, there is no hope unmingled with fear, and no fear unmingled with hope. He thought neither could be good in itself, since both show a lack of knowledge and power, and he warned that people kept swinging between them become credulous and superstitious. His remedy was understanding: an emotion stops being a passion once we form a clear idea of it, and grasping that things happen by necessity eases their hold. He did not think emotions could simply be switched off; an emotion can only be overcome by a stronger contrary one.",
    sections=[
        ("What Spinoza meant by hope and fear", [
            "Spinoza meant that hope and fear are the same state seen from two sides: a pleasure or a pain about something whose outcome we are unsure of. Because the doubt is shared, he wrote, there is no hope unmingled with fear, and no fear unmingled with hope. His cure for both was not reassurance but understanding.",
            "HTML:" + K.takeaways([
                "Hope is an inconstant pleasure, and fear an inconstant pain, about a past or future thing whose outcome we doubt.",
                "Since both rest on doubt, each always carries some of the other.",
                "When the doubt goes, hope becomes confidence and fear becomes despair.",
                "He held that hope and fear cannot be good in themselves, because they show a lack of knowledge.",
                "People who swing between them, he warned, become credulous and superstitious.",
                "His remedy was understanding the emotion and its causes, not suppressing it.",
            ]),
            "This essay reads Spinoza mostly in his own words, from the nineteenth-century translation by R. H. M. Elwes, which is free to read online, and sets out what scholars say about them. Where it draws a modern parallel, it says so.",
            "HTML:" + K.callout("definition", "A note on words",
                "<p>Translations differ. Where Elwes writes pleasure and pain, more recent translations use joy and sadness: the " + a(SEP, "Stanford Encyclopedia’s main entry") + ", for example, renders hope as an inconstant joy, where Elwes has an inconstant pleasure. As its " + a(SEPPSY, "entry on Spinoza’s psychology") + " notes, different translators give widely different translations for Spinoza’s particular affects. This essay quotes Elwes and keeps his words.</p>"),
        ]),
        ("Who Spinoza was", [
            "Baruch Spinoza was born in Amsterdam in 1632, into the city’s Portuguese-Jewish community, according to the " + a(SEP, "Stanford Encyclopedia of Philosophy") + ". In July 1656 the community issued against him what the entry calls the harshest writ of cherem, or excommunication, ever pronounced by the Sephardic community of Amsterdam. It was never rescinded.",
            "He published his Theological-Political Treatise anonymously in 1670, to great alarm, the same entry records. He tried to publish his main work, the Ethics, in 1675, but according to the " + a(ENC, "Encyclopedia of Philosophy") + ", theologians learned of his plans and complained to the civil authorities, and he gave up. He died in February 1677, and the Ethics appeared in his posthumous works later that year.",
            "The Ethics is laid out like a geometry book, in numbered definitions, propositions and proofs. Its third part is a catalogue of the emotions, and the definitions of hope and fear sit in that catalogue alongside love, hatred, envy and pity.",
        ]),
        ("Two passions made of doubt", [
            "Spinoza built every emotion from a few basic ones. In the " + a(E3, "third part of the Ethics") + ", pleasure is the transition of a man from a less to a greater perfection, and pain the transition from a greater to a less perfection. Many, such as love and hatred, are pleasure or pain accompanied by the idea of an external cause; others, like hope and fear, by the idea of something past or future.",
            "Hope and fear are pleasure and pain joined to uncertainty. In the definitions at the end of Part 3, hope is “an inconstant pleasure, arising from the idea of something past or future, whereof we to a certain extent doubt the issue.” Fear is defined in exactly parallel words: an inconstant pain arising from the idea of something past or future, whereof we to a certain extent doubt the issue. The word that carries the weight is inconstant. Both feelings flicker because the outcome they depend on has not settled.",
            "Take away the doubt and the feelings change their names. Confidence, in the next definition, is pleasure about something past or future wherefrom all cause of doubt has been removed; despair is the matching pain. Despair, on this account, is not the extreme of fear but fear that has lost its uncertainty: the bad outcome now looks certain. In his own phrase, confidence springs from hope, and despair from fear, once the causes of doubt are removed. He added that feeling no doubt is not the same as being completely certain; we can never be absolutely certain how any particular event will turn out, yet we can stop doubting it.",
            "Two more definitions finish the set. Joy, in Elwes’s wording (a narrower feeling than the joy of modern translations, which is his pleasure), is pleasure accompanied by the idea of something past, which has had an issue beyond our hope; disappointment is pain at something past which has had an issue contrary to our hope. Hope and fear, in other words, are the feelings of waiting, and these are the feelings of the result.",
            "HTML:" + K.table("Spinoza’s four emotions about the future",
                ["", "With doubt", "Doubt removed"],
                [["Pleasure", "Hope", "Confidence"],
                 ["Pain", "Fear", "Despair"]],
                source='Source: Spinoza, Ethics Part 3, Definitions of the Emotions XII to XV, <a href="' + E3 + '" target="_blank" rel="noopener">Elwes translation</a>.'),
        ]),
        ("Why you never get one without the other", [
            "From these definitions Spinoza drew his most striking claim. In the explanation that follows the definition of fear, he wrote: “From these definitions it follows, that there is no hope unmingled with fear, and no fear unmingled with hope.”",
            "His reasoning runs both ways. Someone who depends on hope and doubts how things will turn out is assumed to conceive something which excludes the existence of the hoped-for thing in the future, and to that extent feels pain; so, while dependent on hope, he fears for the issue. Equally, someone who fears an outcome he hates also conceives something that would rule it out, and to that extent feels pleasure, and so hopes that it will turn out as he desires. Every hope contains a picture of failure, and every fear a picture of escape.",
            "This is a claim about structure, not about mood. It does not say hopeful people are secretly gloomy. It says that hope and fear are built from the same doubt, so feeding one feeds the other. A person who keeps hope alive by keeping the question open also keeps fear alive, because the question is the same.",
            "That is why, in the " + a(E4, "fourth part of the Ethics") + ", he wrote that “Emotions of hope and fear cannot be in themselves good.” The note to that proposition gives the reason: such emotions show defective knowledge and an absence of power in the mind. The point is not that hope is a vice. It is that hope, like fear, is a sign that we do not yet understand our situation.",
            "Two details keep this from being as harsh as it sounds. First, the proof allows that hope and fear can be good, but only in so far as they can restrain excessive pleasure: they have a use as brakes, just not as a way to live. Second, he did not exempt the happy endings. The same note says that confidence, despair, joy, and disappointment are signs of a want of mental power, because even confidence and joy imply a preceding pain, namely hope and fear. The alternative he describes is the more we endeavour to be guided by reason, the less do we depend on hope, freeing ourselves from fear and, as far as we can, directing our actions by the sure counsels of wisdom.",
        ]),
        ("Fluctuating between hope and fear", [
            "Spinoza thought this swinging had consequences beyond the individual. He opened his " + a(TTP, "Theologico-Political Treatise") + " with it: “Men would never be superstitious, if they could govern all their circumstances by set rules, or if they were always favoured by fortune.” Instead, people are often kept fluctuating pitiably between hope and fear by the uncertainty of fortune’s greedily coveted favours, and so, he wrote, they are for the most part very prone to credulity.",
            "A few paragraphs later the preface puts it bluntly: “Superstition, then, is engendered, preserved, and fostered by fear.” In the " + a(E3, "Ethics") + " he traces the mechanism. Things which are accidentally the causes of hope or fear are called good or evil omens, and hence there have arisen superstitions, whereby men are everywhere assailed.",
            "The picture is of a mind that, unable to bear not knowing, grabs at any sign that seems to settle the question. The omen is a shortcut out of doubt. Spinoza’s complaint was that it is a false shortcut, and that people who live by such shortcuts are easy to lead.",
        ]),
        ("Fear makes a poor guide", [
            "In the " + a(E4, "fourth part") + " Spinoza turned the point on ethics itself. “He who is led by fear, and does good in order to escape evil, is not led by reason,” he wrote. Doing the right thing out of fear of punishment is, on his terms, a form of what he called bondage: human infirmity in moderating and checking the emotions.",
            "He applied the same test to life together. In the appendix to Part 4 he observed that harmony is often the result of fear: but such harmony is insecure. Peace kept only because each side fears the other lasts only as long as the fear does.",
            "His portrait of the person who has got free of this is a famous line: “A free man thinks of death least of all things; and his wisdom is a meditation not of death but of life.” The proof begins by defining the free man as one who lives under the guidance of reason, who is not led by fear.",
        ]),
        ("The remedy: understanding, not suppression", [
            "Spinoza did not think emotions could be switched off by deciding to. In Part 4 he wrote: “An emotion can only be controlled or destroyed by another emotion contrary thereto, and with more power for controlling emotion.” Telling yourself not to be afraid does nothing unless something stronger takes fear’s place.",
            "What he offered instead, in the " + a(E5, "fifth part of the Ethics") + ", was understanding. “An emotion, which is a passion, ceases to be a passion, as soon as we form a clear and distinct idea thereof.” A passion, for Spinoza, is an emotion we undergo because we are only a partial cause of it, in the " + a(SEPPSY, "Stanford Encyclopedia’s") + " phrase an inadequate or partial cause. Understanding its causes makes us more the author of what we feel.",
            "He added a second remedy. The mind has greater power over the emotions and is less subject thereto, in so far as it understands all things as necessary. His example is grief: the pain arising from the loss of any good is mitigated as soon as the person sees it could not have been kept. Applied to hope and fear, the thought is that seeing how events actually follow from their causes leaves less room for the flickering doubt both feed on.",
            "He also recommended preparation. In a note in Part 5 he advised framing fixed practical precepts and committing them to memory, so they are ready when needed, and wrote: “We should, in the same way, reflect on courage as a means of overcoming fear.” Read alongside his claim that only a stronger contrary emotion can overcome an emotion, courage works not as the absence of fear but as a stronger feeling that can displace it.",
            "HTML:" + K.compare("Two ways of handling fear", [
                ("Swapping fear for hope", ["Feels better at once"], ["Keeps the doubt open, so fear returns with it"], "The swing continues."),
                ("Spinoza’s route", ["Weakens the doubt both feed on"], ["Slow, and he admits it is difficult"], "Understanding the causes."),
            ], source='Based on Spinoza, Ethics Parts 3 to 5, <a href="' + E5 + '" target="_blank" rel="noopener">Elwes translation</a>.'),
        ]),
        ("A modern echo, not a proof", [
            "One line of modern research is sometimes set beside Spinoza’s claim that a clear idea of an emotion weakens it. In a " + a(LIEB, "2007 brain-imaging study") + ", Matthew Lieberman and colleagues showed 30 participants photographs of faces with emotional expressions. When people chose a word naming the emotion, rather than, for example, choosing a name that matched the face’s gender, activity in the amygdala was lower, and activity in a region of the right prefrontal cortex was higher.",
            "This is an echo, not a confirmation. The study does not mention Spinoza, measured brain activity rather than how people felt, and its authors wrote that it is unclear whether the linguistic component of affective labeling is critical. Naming an emotion in a laboratory task is also far from the full understanding of causes that Spinoza meant. The parallel is worth noticing, and no more than that.",
        ]),
        ("What this does and does not say", [
            "Read carefully, Spinoza does not say hope is foolish or that we should give up wanting things. He says that hope and fear are both reactions to doubt, that leaning on one keeps the other alive, and that the steadier ground lies in understanding what is actually happening and why. He ended the Ethics by admitting how hard that is: “But all things excellent are as difficult as they are rare.”",
            "Other essays here approach the same ground. " + ESSAY43.replace(">what the Stoics", ">What the Stoics") + " sets out an older school’s way of sorting what is in our power from what is not. " + ESSAY52.replace(">what Epicurus", ">What Epicurus") + " looks at another ancient attempt to remove the fear of death. And " + ESSAY61 + " describes how modern psychologists came to see the expectation of control as a protection against giving up, a finding that sits close to Spinoza’s idea that power and understanding grow together.",
        ]),
    ],
    note=[
        "Quotations from the Ethics and the Theologico-Political Treatise are from R. H. M. Elwes’s public-domain translation. Other translations word the same passages differently.",
    ],
    faqs=[
        ("How did Spinoza define hope and fear?",
         "Hope is an inconstant pleasure, and fear an inconstant pain, arising from the idea of something past or future whose outcome we to some extent doubt. The definitions are in Part 3 of the Ethics."),
        ("Why did Spinoza say there is no hope without fear?",
         "Because both depend on the same doubt. Anyone who hopes for something is unsure it will happen, so they also picture it not happening, which is painful. He wrote that there is no hope unmingled with fear, and no fear unmingled with hope."),
        ("Did Spinoza think hope was bad?",
         "He wrote that hope and fear cannot be good in themselves, because they show defective knowledge and an absence of power in the mind. He did not call hope a vice; he saw it as a sign that we do not yet understand our situation."),
        ("What did Spinoza recommend instead of hope?",
         "Understanding. He argued that an emotion stops being a passion once we form a clear and distinct idea of it, and that seeing things as following necessarily from their causes reduces the hold of emotions."),
        ("Where does the idea that fear breeds superstition come from?",
         "From the preface to Spinoza’s Theologico-Political Treatise, which says people kept fluctuating between hope and fear become credulous, and that superstition is engendered, preserved and fostered by fear."),
    ],
    related=[
        ("what-the-stoics-meant-by-what-is-up-to-us", "What the Stoics meant by what is up to us, and what it means for love", "Philosophy"),
        ("what-epicurus-meant-by-pleasure", "What Epicurus meant by pleasure, and why it was never about indulgence", "Philosophy"),
    ],
)

if __name__ == "__main__":
    newpost.build(POST)
