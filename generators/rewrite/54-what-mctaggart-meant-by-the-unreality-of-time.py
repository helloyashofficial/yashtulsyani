#!/usr/bin/env python3
"""Essay 54 :: what-mctaggart-meant-by-the-unreality-of-time  (Fourth dimension)

Philosophy, literal register. Sources fetched and read on 4 Nov 2026:
McTaggart 1908, "The Unreality of Time", Mind 17 (JSTOR scan on PhilArchive
for pagination; Logic Museum transcription for wording); SEP "John M. E.
McTaggart" (McDaniel); IEP "John McTaggart Ellis McTaggart" (Thomas);
Trinity College page; SEP "Time" (Emery, Markosian and Sullivan); IEP
"Time"; SEP "Being and Becoming in Modern Physics" (Savitt); SEP "Charlie
Dunbar Broad" (Gustavsson), for Broad's 1923 words; Garrett 2017 on
Dummett; Cambridge Core abstracts (Dyke, Percival) and Routledge on Mellor.
Not used: Russell's own definition of change (could not be read).
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import newpost, postkit as K

EXT = ' target="_blank" rel="noopener"'
def a(url, text):
    return '<a href="%s"%s>%s</a>' % (url, EXT, text)

TEXT = "https://www.logicmuseum.com/time/mctaggartunreality.htm"
SCAN = "https://philarchive.org/archive/MCTTUO"
SEPM = "https://plato.stanford.edu/ENTRIES/mctaggart/"
IEPM = "https://iep.utm.edu/mctaggar/"
TRIN = "https://explore.trin.cam.ac.uk/assets/mctaggart/"
SEPT = "https://plato.stanford.edu/entries/time/"
IEPT = "https://iep.utm.edu/time/"
SAVITT = "https://plato.stanford.edu/entries/spacetime-bebecome/"
BROAD = "https://plato.stanford.edu/entries/broad/"
GARRETT = "https://openresearch-repository.anu.edu.au/bitstream/1885/250514/1/01_Garrett_Time%20Space%20Dummett%20and%20McTaggart.pdf"
CUP = "https://www.cambridge.org/core/product/7E08BAA5B3509FECC9BA899EE6C2BC29"
REALTIME = "https://www.cambridge.org/core/journals/philosophy-of-science/article/d-h-mellor-real-time-new-york-cambridge-university-press-1981-xi-203-pp/69CEAFF452E81ABFF6D8E5A2220E398B"
MELLOR = "https://www.routledge.com/Real-Time-II/Mellor/p/book/9780415097802"

ESSAY44 = '<a href="/writing/what-it-means-to-call-time-the-fourth-dimension">what it means to call time the fourth dimension</a>'
ESSAY49 = '<a href="/writing/what-flatland-teaches-about-the-fourth-dimension">what Flatland teaches about the fourth dimension</a>'
ESSAY48 = '<a href="/writing/why-time-has-a-direction">why time has a direction</a>'

POST = dict(
    slug="what-mctaggart-meant-by-the-unreality-of-time", num=54, cat="Fourth dimension", read="auto",
    date="2026-11-04",
    gen="rewrite/54-what-mctaggart-meant-by-the-unreality-of-time.py",
    title="What McTaggart meant by the unreality of time, and why the argument still matters",
    dek="In 1908 a Cambridge philosopher argued that time is not real. Almost nobody now accepts his conclusion. But the distinction he drew to reach it, between two ways of ordering events, still organises the whole debate about whether the past and future exist.",
    takeaway="J. M. E. McTaggart, in a 1908 paper in the journal Mind, distinguished two ways of ordering events: as past, present and future, which he called the A series, and as earlier and later, the B series. He argued that real time needs change, that change needs the A series, and that the A series is contradictory, because every event must be past, present and future, which are incompatible, and every attempt to remove the contradiction recreates it. He concluded that time is unreal. Few philosophers accept that conclusion, but his two series became the A-theory and B-theory of time, and the debate between presentism, the growing block and eternalism, now complicated by relativity, still runs along the lines he drew.",
    sections=[
        ("What McTaggart argued", [
            "McTaggart argued that time is unreal. Events can be ordered as past, present and future, or as earlier and later. He claimed time needs the first ordering, because only it allows change, and that the first ordering contradicts itself. Few accept his conclusion, but his two orderings still define the debate about time.",
            "HTML:" + K.takeaways([
                "The paper is The Unreality of Time, published in the journal Mind in 1908.",
                "The A series orders events as past, present and future. The B series orders them as earlier and later.",
                "McTaggart argued that time needs change, and change needs the A series.",
                "He then argued that the A series is contradictory, and that every attempt to fix it recreates the contradiction.",
                "Almost no one accepts his conclusion, but the A-theory and B-theory of time are named after his series.",
                "The modern debate about whether the past and future exist runs along the lines he drew.",
            ]),
            "This essay is about philosophy, not physics. It sets out the argument as McTaggart wrote it, quoting his paper, and then the main replies. It follows " + ESSAY44 + ", which covers the physics of spacetime and where the philosophical question begins.",
            "HTML:" + K.callout("definition", "The two series",
                "<p>In McTaggart’s " + a(TEXT, "paper") + ", the A series is the series of positions running from the far past through the near past to the present, and then from the present to the near future and the far future. The B series is the series of positions which runs from earlier to later.</p>"),
        ]),
        ("The man and the paper", [
            "John McTaggart Ellis McTaggart was born in London on 3 September 1866, according to the " + a(IEPM, "Internet Encyclopedia of Philosophy") + ", which notes that he spent almost his entire career at Trinity College, Cambridge, where he taught Bertrand Russell, G. E. Moore and C. D. Broad. He died on 18 January 1925. The " + a(TRIN, "college’s own page") + " describes him as a Fellow and Lecturer in Philosophy at Trinity for most of his life.",
            "He was an idealist: the " + a(SEPM, "Stanford Encyclopedia’s entry on him") + ", by Kris McDaniel, notes that throughout his life he defended the claim that ultimate reality consists of loving spirits, and calls him one of the most important systematic metaphysicians of the early twentieth century. Denying that time is real was, for him, part of a larger picture of what reality is like, not a denial that anything exists.",
            "The paper appeared in October 1908 in the journal Mind, " + a(SCAN, "volume 17, pages 457 to 474") + ". It opens frankly: “It doubtless seems highly paradoxical to assert that Time is unreal, and that all statements which involve its reality are erroneous.” He notes that he is not alone: in philosophy, he writes, time is treated as unreal by Spinoza, by Kant, by Hegel, and by Schopenhauer.",
        ]),
        ("Two ways of ordering events", [
            "The argument starts with an observation about how time appears. In the " + a(TEXT, "paper’s words") + ": “Positions in time, as time appears to us prima facie, are distinguished in two ways. Each position is Earlier than some, and Later than some, of the other positions. And each position is either Past, Present, or Future.”",
            "The difference matters. The B series is permanent: if one event is earlier than another, it is always earlier. The A series is not: an event is future, then present, then past. The B series is like a row of houses on a street; the A series is like a spotlight moving along them.",
            "HTML:" + K.table("McTaggart’s two series",
                ["", "A series", "B series"],
                [["Orders events as", "Past, present, future", "Earlier, later"],
                 ["Does an event’s position change?", "Yes: future, then present, then past", "No: earlier than is always earlier than"],
                 ["Needed for change, on McTaggart’s view?", "Yes", "Not by itself"]],
                source='Source: <a href="' + TEXT + '" target="_blank" rel="noopener">McTaggart, The Unreality of Time (1908)</a>. The street and spotlight images are an illustration, not his.'),
        ]),
        ("Step one: time needs the A series", [
            "McTaggart’s first claim is that time requires change, and that the B series alone has no change in it. Every earlier-later relation holds forever; nothing about it ever alters. What changes is only that events stop being future and become present, then past. In the " + a(TEXT, "paper") + ": “Without the A series then, there would be no change, and consequently the B series by itself is not sufficient for time, since time involves change.”",
            "He considers the opposite view, that the real nature of time only contains the distinction of the B series, and rejects it: “I believe it to be untenable.” So, on his account, the A series is essential to the nature of time. If it is not real, time is not real.",
            "The " + a(SEPM, "Stanford Encyclopedia") + " sets out the structure in three steps: time is real only if real change occurs; real change occurs only if the A series exists; the A series does not exist; therefore time is not real. The first two steps are this section. The third is where the argument becomes famous.",
        ]),
        ("Step two: the A series contradicts itself", [
            "The second claim is that the A series is contradictory. The " + a(TEXT, "paper") + " puts it in three short sentences: “Past, present, and future are incompatible determinations. Every event must be one or the other, but no event can be more than one.” And yet: “But every event has them all.” Every event is future at some point, present at another and past at another.",
            "The obvious reply is that an event is not past, present and future at once, but at different times: it is present, was future and will be past. McTaggart anticipated this. He considers the reply that the determinations are only incompatible when they are simultaneous, and answers: “But this explanation involves a vicious circle.”",
            "The circle is this. To say an event was future is to say it is future at some moment in the past. But that moment in the past itself has all three determinations, and so the contradiction returns one level up. Explaining that too needs another layer of tenses, which brings the contradiction back again. In McTaggart’s words: “You can never get rid of the contradiction, for, by the act of removing it from what is to be explained, you produce it over again in the explanation.”",
            "HTML:" + K.stages("The argument in four moves", [
                ("01", "Time needs change", "If nothing ever changed, there would be no time."),
                ("02", "Change needs the A series", "Earlier and later never change; only past, present and future do."),
                ("03", "The A series is contradictory", "Every event must have all three determinations, which exclude each other."),
                ("04", "So time is unreal", "Fixing the contradiction with more tenses only moves it up a level."),
            ], source='A summary of <a href="' + TEXT + '" target="_blank" rel="noopener">McTaggart (1908)</a>, following the structure given in the <a href="' + SEPM + '" target="_blank" rel="noopener">Stanford Encyclopedia</a>.'),
        ]),
        ("What is left: the C series", [
            "McTaggart concludes that neither time as a whole, nor the A series and B series, really exist. In the " + a(TEXT, "paper’s words") + ": “Our conclusion, then, is that neither time as a whole, nor the A series and B series, really exist.” The B series falls with the A series, because on his account it only counts as temporal because of it.",
            "That does not leave nothing. He describes a further ordering, which he calls the C series, that is not temporal, for it involves no change, but only an order. It is, he writes, a series of the permanent relations to one another of those realities which in time are events, and it is possible that the C series does really exist.",
            "The " + a(SEPM, "Stanford Encyclopedia") + " explains how the pieces fit: were there to be an A series, the conjunction of it with the C series would yield a B series. And it notes that, on his view, although time is unreal, our perception of temporal order is not wholly delusory. Something real is ordered; it is only the passing of time that is not.",
        ]),
        ("The replies", [
            "Almost no one accepts the conclusion. The philosopher Dyke, in an abstract on " + a(CUP, "Cambridge Core") + ", writes: “Today, almost no one agrees with his conclusion.” She adds that the argument remains the locus classicus for both the A-theory and the B-theory of time. The " + a(SEPT, "Stanford Encyclopedia’s entry on time") + " notes that the A/B distinction has stuck around as a way of classifying theories of change.",
            "B-theorists reject step one. They hold, in the entry’s words, that all change can be described in before-after terms: a thing being one way at an earlier time and another way at a later time is all that change is. On this view the B series is enough for time, and the A series is a feature of how things look from inside time, not of time itself. The philosopher D. H. Mellor developed this response at length in " + a(REALTIME, "Real Time, published in 1981") + ". " + a(MELLOR, "Routledge") + ", publisher of the sequel Real Time II, says that his Real Time dominated the philosophy of time for fifteen years, and the sequel includes a chapter titled McTaggart’s proof.",
            "A-theorists reject step two or three. They hold, as the " + a(SEPT, "same entry") + " puts it, that at least some important forms of change require classifying events as past, present or future, and look for ways the A series can be coherent.",
            "Not every reply has been critical. The philosopher Dummett published a defence of McTaggart’s proof in 1960. As " + a(GARRETT, "Garrett quotes him") + ", Dummett held that reality must be something of which there exists in principle a complete description, and that the description of what is really there, as it really is, must be independent of any particular point of view.",
            "HTML:" + K.compare("Three views of what exists", [
                ("Presentism", ["Matches the sense that only now is real"], ["Struggles with relativity’s lack of a universal now"], "Only present objects exist."),
                ("Growing block", ["Keeps the past fixed and the future open"], ["Must say what is special about the edge"], "The past and present exist; the future does not."),
                ("Eternalism", ["Fits the spacetime picture"], ["Must explain why time seems to pass"], "Past, present and future all exist."),
            ], source='Definitions from the <a href="' + SEPT + '" target="_blank" rel="noopener">Stanford Encyclopedia, Time</a>; the strengths and weaknesses are a summary of the debate in that entry and in <a href="' + SAVITT + '" target="_blank" rel="noopener">Savitt</a>.'),
        ]),
        ("The growing block, and relativity", [
            "One of McTaggart’s own students offered a middle view. C. D. Broad, in his 1923 book Scientific Thought, described a picture that, as the " + a(BROAD, "Stanford Encyclopedia’s entry on Broad") + " quotes it, accepts the reality of the present and the past, but holds that the future is simply nothing at all. In Broad’s words: “Nothing has happened to the present by becoming past except that fresh slices of existence have been added.” And: “The sum total of existence is always increasing, and it is this which gives the time-series a sense.” This is now called the growing block.",
            "Physics complicates every A-theory. The " + a(SEPT, "Stanford Encyclopedia’s entry on time") + " notes that, according to special relativity, it follows from the relativity of simultaneity that there is no fact of the matter as to what is present, and that this creates serious difficulty for the A-theory in general and for presentism in particular. It also notes that presentists and other A-theorists have a way of avoiding the worry.",
            "Steven Savitt, in the " + a(SAVITT, "Stanford Encyclopedia’s entry on being and becoming in modern physics") + ", surveys the arguments on both sides, including attempts to locate becoming in the structure of light cones, and concludes that it seems unlikely that a simple argument will decide between the views. Relativity changes the shape of the debate McTaggart began; it does not end it.",
        ]),
        ("What this does and does not say", [
            "Read carefully, McTaggart’s paper does not show that time is unreal, and almost no one thinks it does. What it shows is that the two ways we speak about time come apart: one in terms of past, present and future, which changes, and one in terms of earlier and later, which does not. Any account of time has to say which is fundamental, and how the other relates to it.",
            "That question connects to other essays here. " + ESSAY49.replace(">what Flatland", ">What Flatland") + " is about an older fourth dimension, a direction of space, which is easier to think about precisely because it does not pass. The essay on time as the fourth dimension, linked above, shows how relativity puts time and space into one structure, which some read as support for eternalism. And " + ESSAY48 + " asks why, whatever the metaphysics, time seems to run only one way.",
        ]),
    ],
    note=[
        "McTaggart is quoted from a transcription of the 1908 paper, checked against the original pagination in Mind. Broad is quoted through the Stanford Encyclopedia of Philosophy, and Dummett through Garrett, because their original texts could not be read in full.",
    ],
    faqs=[
        ("What is McTaggart's argument for the unreality of time?",
         "Time requires change; change requires the A series, which orders events as past, present and future; the A series is contradictory, because every event must have all three incompatible determinations; so time is unreal. He published it in Mind in 1908."),
        ("What is the difference between the A series and the B series?",
         "The A series orders events as past, present or future, and an event's position in it changes. The B series orders events as earlier or later, and those relations never change."),
        ("Did McTaggart think nothing exists?",
         "No. He was an idealist who held that ultimate reality consists of loving spirits, and he thought a non-temporal ordering, the C series, might really exist. What he denied was that time itself is real."),
        ("Does anyone accept McTaggart's conclusion?",
         "Very few. The philosopher Dyke writes that almost no one agrees with it today, but the argument remains the classic starting point for both the A-theory and the B-theory of time."),
        ("What is the growing block theory of time?",
         "The view that the past and present exist but the future does not, so that existence grows as time passes. C. D. Broad, one of McTaggart's students, set out a version of it in 1923."),
    ],
    related=[
        ("what-it-means-to-call-time-the-fourth-dimension", "What it means to call time the fourth dimension, and what it does not", "Fourth dimension"),
        ("what-flatland-teaches-about-the-fourth-dimension", "What Flatland teaches about the fourth dimension, and what it does not", "Fourth dimension"),
    ],
)

if __name__ == "__main__":
    newpost.build(POST)
