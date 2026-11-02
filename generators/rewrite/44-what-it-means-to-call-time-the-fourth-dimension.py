#!/usr/bin/env python3
"""Essay 44 :: what-it-means-to-call-time-the-fourth-dimension  (Fourth dimension, pillar)

Literal register, like essay 41. Sources fetched and read on 2 Nov 2026:
Minkowski 1908 (German text on de.wikisource; English translation by
Lewertoff and Petkov, 2012), Einstein's Relativity (Lawson translation,
ch. 17), Savitt's SEP entry "Being and Becoming in Modern Physics",
Einstein Online, a UCSD lecture outline, HyperPhysics on Hafele-Keating,
Pogge (Ohio State) on GPS, Weinstein (arXiv) on Einstein and Minkowski,
Rucker and the Public Domain Review on Hinton, Quote Investigator on the
Besso letter. Every human-life use of this vocabulary is labelled metaphor.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import newpost, postkit as K

EXT = ' target="_blank" rel="noopener"'
def a(url, text):
    return '<a href="%s"%s>%s</a>' % (url, EXT, text)

MINK_DE = "https://de.wikisource.org/wiki/Raum_und_Zeit_(Minkowski)"
MINK_EN = "https://hedberg.ccnysites.cuny.edu/PHYS351/FALL-2023/docs/Minkowski-space-and-time-original.pdf"
OLDTR = "https://arxiv.org/pdf/1110.0003"
EIN17 = "https://www.marxists.org/reference/archive/einstein/works/1910s/relative/ch17.htm"
SAVITT = "https://plato.stanford.edu/archives/sum2026/entries/spacetime-bebecome/"
EONLINE = "https://www.einstein-online.info/en/explandict/spacetime/"
UCSD = "https://kintriligator.physics.ucsd.edu/w15/lecWk5.pdf"
HK = "https://hyperphysics.gsu.edu/hbase/Relativ/airtim.html"
GPS = "https://www.astronomy.ohio-state.edu/pogge.1/Ast162/Unit5/gps"
WEIN = "https://arxiv.org/pdf/1210.6929"
RUCKER = "https://www.rudyrucker.com/pdf/rucker_charles_hinton_intro.pdf"
PDR = "https://publicdomainreview.org/essay/notes-on-the-fourth-dimension"
QI = "https://quoteinvestigator.com/2024/03/18/stubborn-illusion/"
PT1905 = "https://physicstoday.aip.org/news/einsteins-special-relativity-paper-arrives-at-annalen-der-physik"

ESSAY41 = '<a href="/writing/what-the-observer-effect-actually-says">the essay on the observer effect</a>'

POST = dict(
    slug="what-it-means-to-call-time-the-fourth-dimension", num=44, cat="Fourth dimension", read="auto",
    gen="rewrite/44-what-it-means-to-call-time-the-fourth-dimension.py",
    title="What it means to call time the fourth dimension, and what it does not",
    dek="In 1908 a mathematician told a room of scientists that space and time on their own would become mere shadows. What he meant is precise, it has been measured, and it is stranger and more modest than the version that travels.",
    takeaway="Calling time the fourth dimension means that every event is located by four numbers, three for place and one for time, and that relativity makes the split between space and time depend on the observer. It does not mean time is just another direction of space: it enters the geometry with the opposite sign, which is why all observers agree on the interval between two events but not on their distance or duration. The effect is measured every day in atomic clocks and satellite navigation. Whether this means the past and future exist as fully as the present is a live philosophical question that relativity does not settle on its own.",
    sections=[
        ("What calling time a dimension means", [
            "Calling time the fourth dimension means that every event can be located by four numbers: three for where it happens and one for when. Relativity adds the part that matters. How those four numbers split into space and time depends on the observer, so space and time are best treated as one structure, spacetime.",
            "HTML:" + K.takeaways([
                "The idea comes from Hermann Minkowski, who presented it in a lecture in Cologne on 21 September 1908.",
                "An event needs four numbers to locate it: three of place and one of time.",
                "Time is not just a fourth direction of space. It enters the geometry with the opposite sign.",
                "Observers in relative motion disagree about which distant events happen at the same time.",
                "The effects are measured: atomic clocks flown on aircraft, and the clocks on navigation satellites.",
                "Relativity does not by itself settle whether the past and future are as real as the present.",
            ]),
            "This essay sets out what the idea says in physics, how it has been tested, the philosophical question it leaves open, and the older, different fourth dimension it is often confused with. Like " + ESSAY41 + ", it is the literal half of a pair: it states the physics straight so that any metaphor built on it can be checked against something.",
            "HTML:" + K.callout("definition", "Spacetime",
                "<p>The totality of all events, each located by three coordinates of place and one of time. As " + a(EONLINE, "Einstein Online") + " puts it, this observer-independent totality of all events is called spacetime, and how it is split into space and time can differ from observer to observer.</p>"),
        ]),
        ("The 1908 lecture", [
            "The phrase belongs to Hermann Minkowski, a mathematician who, according to " + a(WEIN, "the historian of physics Galina Weinstein") + ", had been Einstein’s mathematics professor at the Zurich Polytechnic. Einstein had published special relativity three years earlier; " + a(PT1905, "Physics Today notes") + " that the paper reached the journal Annalen der Physik on 30 June 1905.",
            "Minkowski gave his lecture, Raum und Zeit, on 21 September 1908 at the 80th assembly of German natural scientists and physicians in Cologne, according to " + a(MINK_DE, "the German text and its publication record") + ". He opened with the sentence that made it famous. In " + a(MINK_EN, "the 2012 English translation by Fritz Lewertoff and Vesselin Petkov") + ": “From now onwards space by itself and time by itself will recede completely to become mere shadows and only a type of union of the two will still stand independently on its own.”",
            "The version usually quoted comes from an older translation, by W. Perrett and G. B. Jeffery, in which space by itself and time by itself are " + a(OLDTR, "doomed to fade away into mere shadows") + ". The German has them sinking down to shadows. The wording differs; the claim does not.",
            "He then named the pieces. A point in space at a given time, a set of values x, y, z and t, he called a worldpoint. The path of a particle through spacetime he called a worldline. And he thought the name his audience used for the new physics undersold it: he called the phrase relativity postulate very feeble, and proposed instead the postulate of the absolute world.",
            "HTML:" + K.table("Minkowski’s vocabulary",
                ["Term", "What it names"],
                [["Worldpoint", "A point in space at a given time: a set of values x, y, z, t"],
                 ["Worldline", "A curve in spacetime: the history of a particle, point by point"],
                 ["World postulate", "His preferred name for the principle, in place of relativity postulate"]],
                source='Source: <a href="' + MINK_EN + '" target="_blank" rel="noopener">Minkowski, Space and Time (1908), translated by Lewertoff and Petkov (2012)</a>.'),
            "Einstein did not take to it at once. Weinstein, citing the physicist and biographer Abraham Pais, reports that he first called the four-dimensional formulation superfluous learnedness. He changed his mind as he worked towards general relativity, and in his own popular book he wrote that without Minkowski’s idea, general relativity would perhaps have got no farther than its long clothes.",
        ]),
        ("Four numbers for every event", [
            "The core idea is easier than its reputation. In chapter 17 of " + a(EIN17, "Einstein’s book Relativity, in Robert Lawson’s translation") + ", every event is described by four numbers: three space coordinates, x, y and z, and a time coordinate, t. From this he concludes that the world in which we live is a four-dimensional space-time continuum.",
            "That much was true before relativity. A meeting needs a place and a time; a train timetable is a four-number description of events. What relativity changed is that the four numbers no longer split into space and time the same way for everyone. Einstein was aware of how the idea sounded. The same chapter observes that the non-mathematician is seized by a mysterious shuddering on hearing of four-dimensional things, by a feeling not unlike that awakened by thoughts of the occult.",
            "HTML:" + K.callout("note", "What is new, and what is not",
                "<p>Using a time coordinate alongside three of space is ordinary bookkeeping. What relativity adds is that different observers carve the same four-dimensional set of events into space and time differently, and that only the combined structure is the same for all of them.</p>"),
        ]),
        ("Why time is not just another direction", [
            "The most common misunderstanding is that time is simply a fourth direction, like up, along and across. It is not, and the difference is a sign.",
            "In ordinary space, the distance between two points is the same whatever direction you face. In spacetime, the quantity that every observer agrees on is not a distance but an interval, and time enters it with the opposite sign from space. " + a(UCSD, "A University of California, San Diego lecture outline") + " notes that it is the relative minus sign between space and time that matters, and that all inertial observers agree on the value of the space-time interval between two events.",
            "Einstein made the same point another way. Time behaves exactly like the three space coordinates, he wrote, only after the usual time coordinate is replaced by an imaginary quantity proportional to it. The mathematician and writer Rudy Rucker puts it plainly in " + a(RUCKER, "his introduction to Charles Hinton’s writings") + ": spacetime differs from four-dimensional Euclidean space most essentially in the fact that the invariant measure is interval rather than distance.",
            "HTML:" + K.table("Space and spacetime compared",
                ["Feature", "Ordinary three-dimensional space", "Spacetime"],
                [["Coordinates", "x, y, z", "x, y, z, t"],
                 ["What every observer agrees on", "Distance between two points", "Interval between two events"],
                 ["How time enters", "Not at all", "With the opposite sign from space"],
                 ["What observers can disagree on", "Nothing about distance", "Lengths, durations and which events are simultaneous"]],
                source='Sources: <a href="' + UCSD + '" target="_blank" rel="noopener">UCSD lecture outline</a>; <a href="' + RUCKER + '" target="_blank" rel="noopener">Rucker</a>; <a href="' + EIN17 + '" target="_blank" rel="noopener">Einstein, Relativity, ch. 17</a>.'),
            "That sign is why there are two kinds of separation in Minkowski’s lecture, timelike and spacelike. Events that could be linked by something travelling slower than light have a timelike separation, and every observer agrees which came first. Events too far apart for any signal to connect have a spacelike separation, and for those the order in time can differ between observers.",
        ]),
        ("When is now?", [
            "The most surprising consequence concerns the word now. In everyday life, a moment is the same moment everywhere. In relativity it is not.",
            "As " + a(SAVITT, "Steven Savitt’s entry in the Stanford Encyclopedia of Philosophy") + " explains it, observers in relative motion assign different times to the same distant events. This feature of special relativity is called the relativity of simultaneity. In the entry’s worked example, two observers passing each other disagree about a distant event so far that one assigns it roughly minus three days, in the past, and the other roughly plus three days, in the future.",
            "HTML:" + K.stages("The relativity of simultaneity, in four steps", [
                ("01", "Two observers meet", "They pass each other at high relative speed, at the same place and the same moment."),
                ("02", "A distant event", "Something happens very far away, too far for any signal from it to have reached them yet."),
                ("03", "Different answers", "Each assigns that event a time using their own frame. The answers can differ by days."),
                ("04", "Neither is wrong", "There is no single fact about which distant events are happening now, only facts relative to a frame."),
            ], source='Source: <a href="' + SAVITT + '" target="_blank" rel="noopener">Savitt, Being and Becoming in Modern Physics, Stanford Encyclopedia of Philosophy</a>.'),
            "Nothing contradictory follows, because the disagreement only arises for events that cannot affect each other in the time involved. For events that can, the order is the same for everyone. But it does mean there is no single universal present stretching across space.",
        ]),
        ("It has been measured", [
            "None of this is only on paper. In October 1971, as " + a(HK, "the HyperPhysics summary at Georgia State University") + " reports, Joseph Hafele and Richard Keating flew four caesium atomic clocks on regularly scheduled commercial jet flights around the world, eastward and then westward, and compared them with clocks on the ground.",
            "HTML:" + K.table("The 1971 airborne clock experiment, in nanoseconds",
                ["Direction", "Predicted", "Measured"],
                [["Eastward", "−40 ± 23", "−59 ± 10"],
                 ["Westward", "+275 ± 21", "+273 ± 7"]],
                source='Source: <a href="' + HK + '" target="_blank" rel="noopener">HyperPhysics, Georgia State University</a>, citing Hafele and Keating, Science 177 (1972).'),
            "The predictions combine two effects, one from speed and one from gravity, and the measurements matched them within the uncertainties. The same physics now runs inside every phone that finds its position by satellite. According to " + a(GPS, "Richard Pogge of Ohio State University") + ", the clocks on navigation satellites fall behind ground clocks by about 7 microseconds per day because of their speed, and get ahead by about 45 microseconds per day because they sit higher in Earth’s gravity, for a net difference of about 38 microseconds per day. Left uncorrected, he notes, the positioning errors would grow by about 10 kilometres each day.",
            "HTML:" + K.bars("Satellite clock drift relative to the ground, microseconds per day",
                [("Gravity effect (ahead)", 45, "+45"), ("Speed effect (behind)", 7, "-7"), ("Net", 38, "+38")],
                source="Source: Richard W. Pogge, Ohio State University, on relativity and GPS."),
        ]),
        ("Does the past still exist?", [
            "If there is no universal now, a philosophical question follows quickly. Is the present special? Or are past and future events as real as present ones, laid out in spacetime like places on a map? The second view is often called the block universe.",
            "Savitt’s entry sets out the positions. Presentism is the view that only the present exists. Eternalism holds that future and past events at a place are no more or less real than distant events at a time. Some philosophers have argued that relativity forces eternalism, because there is no frame-independent present to privilege.",
            "The entry’s conclusion is more careful. It says eternalism is not a straightforward consequence of adopting the spacetime viewpoint, that whether the block universe is refuted is controversial, and that one well-known argument against eternalism shows only that it is optional, not that it is false. It also notes that, for many, the deepest problems in the metaphysics of time concern passage, the sense that time flows.",
            "HTML:" + K.compare("Two views of time, and what relativity says", [
                ("Presentism", ["Matches how time feels", "The present is privileged"], ["Has to explain why physics finds no universal present"], "Under pressure from relativity, not refuted by it."),
                ("Eternalism, the block universe", ["Fits the spacetime picture naturally", "No privileged now is needed"], ["Has to explain the experience of passage"], "Compatible with relativity, not required by it."),
            ], source='Source: <a href="' + SAVITT + '" target="_blank" rel="noopener">Savitt, Stanford Encyclopedia of Philosophy</a>.'),
        ]),
        ("Einstein’s letter to the Besso family", [
            "The sentence most often used to settle this question comes from a letter, not a paper. In March 1955, after the death of his lifelong friend Michele Besso, Einstein wrote to Besso’s family. " + a(QI, "Quote Investigator’s research on the letter") + " gives the German: for us believing physicists, the separation between past, present and future has only the meaning of an illusion, albeit a stubborn one.",
            "The familiar English, a stubbornly persistent illusion, is one translation among several; Quote Investigator traces it to the physicist Freeman Dyson in 1979, and lists other renderings from 1972 onwards. A further version, that reality is merely an illusion, drops past, present and future altogether and is a misquotation.",
            "HTML:" + K.callout("warn", "Read it as what it was",
                "<p>This was a letter of condolence to a grieving family, written weeks before Einstein’s own death. It expresses how he, as a physicist, held the idea of time. It is not a result, and quoting it as proof that time is an illusion asks it to do something it was never written to do.</p>"),
        ]),
        ("The other fourth dimension", [
            "Before Minkowski, the fourth dimension already had a popular life, and it meant something else. In 1880, as " + a(RUCKER, "Rucker records") + ", the English mathematician Charles Howard Hinton published an essay called What Is the Fourth Dimension? Hinton was after a direct and intuitive knowledge of four-dimensional space: a fourth direction of space, at right angles to the other three.",
            "Hinton gave the language the tesseract, a four-dimensional cube; Rucker suggests he may have coined the word, and " + a(PDR, "Jon Crabb at the Public Domain Review") + " notes that he first used it in his 1888 book A New Era of Thought. Crabb also notes that Hinton was talking about an actual spatial dimension, and that by the late 1920s Einstein’s spacetime had more or less replaced the spatial fourth dimension in the popular imagination.",
            "HTML:" + K.table("Two fourth dimensions",
                ["Feature", "Hinton (from 1880)", "Minkowski (1908)"],
                [["What the fourth dimension is", "A fourth direction of space", "Time, joined with space"],
                 ["Basic measure", "Distance", "Interval"],
                 ["Status", "A mathematical and imaginative idea", "The structure of physical spacetime, tested by experiment"]],
                source='Sources: <a href="' + RUCKER + '" target="_blank" rel="noopener">Rucker</a>; <a href="' + PDR + '" target="_blank" rel="noopener">Crabb, Public Domain Review (2015)</a>.'),
            "Both ideas are interesting. They are not the same idea, and much of the mystique around the phrase fourth dimension comes from blending them.",
        ]),
        ("What the idea is good for, and what it is not", [
            "As physics, the idea is precise and modest. Events need four numbers; observers split them differently; the interval is shared; the effects show up in clocks. It says nothing about consciousness, nothing about destiny, and nothing about people.",
            "As a metaphor, and this paragraph is one, it offers something worth having. The relativity of simultaneity is a reminder that two honest observers can disagree about the order and timing of distant events without either being careless; in physics that is a fact about frames, and between people the resemblance is only a resemblance. The same tests apply here as in the observer-effect essay: say when you are borrowing, and do not let the borrowed word claim the authority of the experiment.",
            "Read straight, Minkowski’s lecture is not a doorway to the occult that Einstein said four-dimensional talk could suggest. It is a better map of where and when things happen, one that has been checked by flying clocks around the world, and one that still leaves open the oldest question about time: why it seems to pass.",
        ]),
    ],
    note=[
        "This essay is the literal half of the Fourth dimension subject on this site. Where it borrows the physics for anything human, it says so at that point.",
    ],
    faqs=[
        ("Is time the fourth dimension?",
         "In relativity, yes, in a specific sense: every event is located by three coordinates of place and one of time, and the four together form spacetime. But time is not just another direction of space. It enters the geometry with the opposite sign, which is why observers agree on the interval between events but can disagree about distances and durations."),
        ("Who first called time the fourth dimension?",
         "The idea of a four-dimensional spacetime was presented by the mathematician Hermann Minkowski in a lecture in Cologne on 21 September 1908, building on Einstein's special relativity of 1905. Others had speculated about time as a dimension earlier, but Minkowski's formulation is the one physics adopted."),
        ("Has time dilation been measured?",
         "Yes. In 1971 Hafele and Keating flew atomic clocks around the world on commercial flights, and the measured differences matched the predictions within their uncertainties. Satellite navigation clocks must also be corrected by about 38 microseconds per day for relativistic effects."),
        ("Does relativity prove the past and future exist?",
         "No. Relativity removes any universal present, which some argue supports the block universe view that past and future are as real as the present. The Stanford Encyclopedia of Philosophy notes that this is not a straightforward consequence of relativity and that the question remains debated."),
        ("Did Einstein say time is an illusion?",
         "In a 1955 letter of condolence to the family of his friend Michele Besso, he wrote that for believing physicists the separation between past, present and future is an illusion, albeit a stubborn one. It was a personal letter, not a scientific claim, and the popular English wording is a later translation."),
    ],
    related=[
        ("what-the-observer-effect-actually-says", "What the observer effect actually says, and what it does not", "Physics and time"),
    ],
)

if __name__ == "__main__":
    newpost.build(POST)
