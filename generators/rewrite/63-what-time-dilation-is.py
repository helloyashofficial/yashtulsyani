#!/usr/bin/env python3
"""Essay 63 :: what-time-dilation-is  (Physics and time)

Sources fetched and read on 6 Nov 2026: Einstein 1905, On the
Electrodynamics of Moving Bodies, Perrett and Jeffery translation (Pitt
reset copy); Harvey and Schucking, A Small Puzzle from 1905, Physics Today
(2005); Pound and Rebka, Apparent Weight of Photons, Physical Review
Letters (1960, course copy); Bailey and others, Nature 268 (1977); NIST news
release on the aluminium-ion clocks (2010) and Chou and others, Science
(2010) as cited there; Ashby, Relativity and the Global Positioning System,
Physics Today (2002).
Not used: Hafele and Keating 1971 to 1972 (original papers not readable);
per-day GPS breakdowns not stated in a fetched source.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import newpost, postkit as K

EXT = ' target="_blank" rel="noopener"'
def a(url, text):
    return '<a href="%s"%s>%s</a>' % (url, EXT, text)

EIN = "https://sites.pitt.edu/~jdnorton/teaching/Einstein_graduate/pdfs/Einstein_STR_1905_English_reset.pdf"
PUZZLE = "https://physicstoday.aip.org/features/a-small-puzzle-from-1905"
POUND = "https://faculty.cst.temple.edu/~tuf43817/PHYS4702/F15/PoundRebka.pdf"
MUON = "https://www.nature.com/articles/268301a0.pdf"
NIST = "https://www.nist.gov/news-events/news/2010/09/nist-pair-aluminum-atomic-clocks-reveal-einsteins-relativity-personal"
ASHBY = "https://physicstoday.aip.org/features/relativity-and-the-global-positioning-system"

ESSAY41 = '<a href="/writing/what-the-observer-effect-actually-says">what the observer effect actually says</a>'
ESSAY44 = '<a href="/writing/what-it-means-to-call-time-the-fourth-dimension">what it means to call time the fourth dimension</a>'
ESSAY48 = '<a href="/writing/why-time-has-a-direction">why time has a direction</a>'
ESSAY58 = '<a href="/writing/why-looking-at-the-sky-means-looking-into-the-past">why looking at the sky means looking into the past</a>'

POST = dict(
    slug="what-time-dilation-is", num=63, cat="Physics and time", read="auto",
    date="2026-11-06",
    gen="rewrite/63-what-time-dilation-is.py",
    title="What time dilation is, and why your head ages faster than your feet",
    dek="Time dilation sounds like science fiction, but it is one of the most thoroughly measured facts in physics. Clocks that move run slower, and clocks lower down in gravity run slower too. The effect has been measured across a 74-foot tower, in particles racing round a ring, between two clocks a foot apart, and in the satellites behind every map on your phone.",
    takeaway="Time dilation is the measured fact that clocks do not all tick at the same rate. A moving clock runs slow compared with one at rest, as Einstein showed in 1905, and a clock lower in a gravitational field runs slow compared with one higher up. Both effects have been confirmed many times: by light climbing a 74-foot tower at Harvard in 1960, by muons in a storage ring living about 29 times longer than at rest, and by aluminium-ion clocks at NIST that detected the difference across a height of 33 centimetres. GPS satellites must have their clocks adjusted before launch, or errors of more than 11 kilometres would build up in a day. The effects in everyday life are tiny: about 90 billionths of a second over a lifetime for a foot of height. Even Einstein got one prediction wrong, about clocks at the equator.",
    sections=[
        ("What time dilation is", [
            "Time dilation is the measured fact that clocks run at different rates depending on how they move and where they sit in gravity. A clock in motion runs slow compared with one at rest, and a clock lower in a gravitational field runs slow compared with one higher up. Both effects are small in daily life and have been measured precisely.",
            "HTML:" + K.takeaways([
                "Moving clocks run slow compared with clocks at rest. Einstein derived this in 1905.",
                "Clocks lower in gravity run slow compared with clocks higher up.",
                "In 1960, light sent up and down a 74-foot tower showed the gravitational effect.",
                "Fast-moving muons in a storage ring lived about 29 times longer than muons at rest.",
                "In 2010, NIST clocks detected the difference across a height of 33 centimetres.",
                "GPS would build up errors of more than 11 kilometres a day without correcting for both effects.",
            ]),
            "This essay is in the literal register, like " + ESSAY41 + ". It sets out what the theory says and what the measurements found, and keeps any borrowing for human life to one labelled paragraph near the end.",
            "HTML:" + K.callout("definition", "Time dilation",
                "<p>The difference in the rate at which two clocks tick because of their relative motion or their positions in a gravitational field. Each clock still ticks normally where it is; the difference shows up when the clocks are compared.</p>"),
        ]),
        ("Two causes: speed and gravity", [
            "Time dilation has two causes, which are easiest to keep apart. The first comes from speed. In his 1905 paper on what became special relativity, " + a(EIN, "Einstein") + " worked out that if one of two synchronised clocks is moved away and brought back, it will be found to be slow on its return compared with the clock that stayed put. In the 1923 English translation by Perrett and Jeffery, a clock moved from one point to another in a straight line lags behind the other which has remained there.",
            "The second comes from gravity, and belongs to Einstein’s later general theory of relativity. A clock lower down in a gravitational field ticks more slowly than one higher up. As " + a(NIST, "NIST put it in 2010") + ", scientists have known for decades that time passes faster at higher elevations, an effect that had earlier been measured by comparing clocks on the Earth’s surface and a high-flying rocket.",
            "The two effects can add together or pull against each other, depending on the situation. A satellite clock moves fast, which slows it, but it is also high above the Earth, which speeds it up. Which effect wins depends on the orbit, and for GPS satellites, as the section below shows, gravity wins.",
            "HTML:" + K.table("The two kinds of time dilation",
                ["Cause", "Which clock runs slow", "Theory"],
                [["Relative speed", "The moving one, compared with one at rest", "Special relativity, 1905"],
                 ["Gravity", "The lower one, compared with one higher up", "General relativity"]],
                source='Sources: <a href="' + EIN + '" target="_blank" rel="noopener">Einstein (1905)</a>; <a href="' + NIST + '" target="_blank" rel="noopener">NIST (2010)</a>.'),
        ]),
        ("The prediction Einstein got wrong", [
            "The 1905 paper also contains a prediction that turned out to be wrong, and the story of why is a good illustration of how the two effects interact. Einstein reasoned that because the Earth spins, a clock at the equator is moving faster than one at a pole, and concluded, in the " + a(EIN, "same translation") + ", that a balance-clock at the equator must go more slowly, by a very small amount, than a precisely similar clock situated at one of the poles.",
            "In a " + a(PUZZLE, "2005 article in Physics Today") + ", the physicists Alex Harvey and Engelbert Schucking explained why that is not what happens. Einstein’s argument used speed alone and ignored gravity. Because the Earth’s rotation makes sea level bulge at the equator, a clock there also sits at a different gravitational potential from one at a pole, and the authors show that these two effects exactly cancel each other if both clocks are at local sea level.",
            "So the equator clock’s extra speed slows it down, and its position in the Earth’s gravity speeds it up by precisely the same amount. Clocks at sea level, wherever they are on the globe, tick together, whatever their latitude. Einstein’s physics was right; the example was incomplete, because in 1905 he did not yet have a theory of gravity to include.",
        ]),
        ("Light climbing a tower", [
            "The gravitational effect was first measured on Earth in a laboratory at Harvard. In a paper titled " + a(POUND, "Apparent weight of photons") + ", published in Physical Review Letters in April 1960, Robert Pound and Glen Rebka sent gamma rays up and down the enclosed tower of the Jefferson Physical Laboratory, over a net operating baseline of 74 feet. They sent the light both upward and downward and compared the two, so the paper gives its prediction for a two-way height difference of 148 feet.",
            "Light that climbs out of gravity loses a tiny amount of energy, which shows up as a lower frequency, and light that falls gains it. This frequency shift is the same physics as clocks ticking at different rates: a clock at the bottom of the tower, seen from the top, appears to run slow. Pound and Rebka reported a ratio of measured to predicted shift of 1.05, plus or minus 0.10. In other words, the effect was there, at the size general relativity predicted, to within about ten per cent.",
        ]),
        ("Particles that live longer", [
            "The speed effect has been tested with unstable particles, which act as natural clocks because they decay at a known average rate. Muons are a favourite. In a " + a(MUON, "1977 paper in Nature") + ", J. Bailey and colleagues reported measurements of muons circling a storage ring at nearly the speed of light, with a Lorentz factor, the amount by which relativity predicts their clocks slow, of 29.33.",
            "The " + a(MUON, "measured lifetimes") + " of the circling muons were about 64.4 microseconds. For negative muons, the paper gives the lifetime at rest as 2.1948 microseconds. The fast muons lived about 29 times longer, as predicted. The authors report that the Einstein time dilation factor agrees with experiment with a fractional error of 2 × 10⁻³ at 95% confidence, about two parts in a thousand.",
            "Because the muons were travelling in a circle and coming back round, the experiment is close to Einstein’s 1905 picture of a clock that travels a closed path and returns slow. It is also the clearest answer to anyone who thinks time dilation is an illusion of measurement.",
        ]),
        ("A foot is enough", [
            "By 2010 clocks had become precise enough to detect both effects at human scale. Researchers at NIST built two clocks, each based on the ticking of a single aluminium ion, in different laboratories joined by a 75-metre optical fibre. According to " + a(NIST, "NIST’s release") + ", one of the clocks keeps time to within 1 second in about 3.7 billion years. The work was published by C. W. Chou, D. B. Hume, T. Rosenband and D. J. Wineland in Science in September 2010.",
            "They raised one clock by 33 centimetres, about a foot, and, in NIST’s words, sure enough, the higher clock ran at a slightly faster rate than the lower clock, exactly as predicted. They also made the ion in one clock move at speeds equivalent to several metres per second, and saw the moving clock run slow, at speeds comparable to a car travelling about 20 miles per hour.",
            "The release translated the height result into a human scale: you age faster when you stand a couple of steps higher on a staircase. The difference is much too small for humans to perceive directly, it added, adding up to approximately 90 billionths of a second over a 79-year lifetime. That is the sense in which your head ages faster than your feet: measurably, and by almost nothing.",
            "HTML:" + K.stages("Four tests of time dilation", [
                ("1960", "Harvard tower", "Light over 74 feet showed the gravitational shift, within about 10 per cent."),
                ("1977", "Storage ring", "Circling muons lived about 29 times longer, agreeing to about two parts in a thousand."),
                ("1977", "First GPS satellite", "Its clock’s shift matched the calculation to better than 1 per cent."),
                ("2010", "NIST clocks", "Clocks 33 centimetres apart in height ticked at measurably different rates."),
            ], source='Sources: <a href="' + POUND + '" target="_blank" rel="noopener">Pound and Rebka (1960)</a>; <a href="' + MUON + '" target="_blank" rel="noopener">Bailey and others (1977)</a>; <a href="' + ASHBY + '" target="_blank" rel="noopener">Ashby (2002)</a>; <a href="' + NIST + '" target="_blank" rel="noopener">NIST (2010)</a>.'),
        ]),
        ("Why your phone needs it", [
            "Time dilation is not only a laboratory curiosity. Satellite navigation depends on it. As " + a(ASHBY, "Neil Ashby explained in Physics Today in 2002") + ", the GPS satellites orbit about 20,000 km above Earth’s surface, with periods of 11 hours and 58 minutes. A receiver works out its position from the timing of signals from several satellites, so the clocks must agree to within about 4 nanoseconds if navigation errors of more than a metre are to be avoided.",
            "Both effects act on the satellite clocks. Their speed slows them; their height, which puts them higher in Earth’s gravity, speeds them up, and because the GPS orbits are high, Ashby writes, the gravitational blueshift is the largest contribution. The net correction is 4.4645 parts in ten billion. Multiplying that by the 86,400 seconds in a day gives about 38 microseconds a day, a calculation made here rather than quoted. The essay on the fourth dimension, linked below, gives the same figure from another source.",
            "" + a(ASHBY, "Ashby") + " is blunt about the stakes: if these relativistic effects were not corrected for, satellite clock errors building up in just one day would cause navigational errors of more than 11 km, quickly rendering the system useless. The fix is simple: nowadays the rate of every orbiting GPS clock is adjusted by this factory offset before launch. When the first GPS satellite was launched in 1977, the shift measured in its first weeks was 4.425 parts in ten billion, agreeing with the relativistic calculation to better than 1%.",
        ]),
        ("What it does not mean", [
            "Time dilation is often described in ways that go further than the physics. It does not mean that time feels slower to anyone. Each clock, and each person, experiences its own time normally; the difference appears only when two clocks that have had different histories are compared. It does not mean that time is an illusion, either. The muons and the NIST clocks measured real, repeatable differences.",
            "Nor do the everyday effects matter to a human life. The NIST figure, 90 billionths of a second over a lifetime for a foot of height, is far below anything a person could notice. The effects only become large at speeds close to that of light, or near very strong gravity, conditions far outside anything in ordinary life. The practical uses lie elsewhere: NIST’s Till Rosenband suggested that comparing such clocks could be useful in geodesy and geophysics, measuring differences in height through differences in time.",
            "HTML:" + K.callout("warn", "A metaphor, labelled as one",
                "<p>It is tempting to borrow time dilation for human life: to say that time runs differently for people in different situations, or that a hard week ‘dilated’ time. That is a metaphor, and only a metaphor. The physics is about clocks, speed and gravity. It says nothing about how long an hour feels, and it does not show that people live in different times in any sense beyond the measured nanoseconds.</p>"),
        ]),
        ("What this does and does not say", [
            "Read plainly, time dilation says that there is no single clock for the universe. How much time passes between two events depends on the path between them, through space and through gravity. The effects are tiny where we live and enormous near light speed, and they have been measured in towers, rings, laboratories and orbit.",
            "Other essays here take the physics in different directions. " + ESSAY44.replace(">what it means", ">What it means") + " explains how relativity joins space and time into one structure. " + ESSAY58.replace(">why looking", ">Why looking") + " shows how the finite speed of light turns the night sky into a view of the past. And " + ESSAY48 + " asks why, if the laws of physics run either way, time seems to move in only one direction.",
        ]),
    ],
    note=[
        "The 38 microseconds a day figure is calculated from Ashby’s net correction and is not quoted from his article. The Hafele and Keating flights of 1971 are not described here because their original papers could not be read.",
    ],
    faqs=[
        ("What is time dilation in simple terms?",
         "Clocks do not all tick at the same rate. A moving clock runs slow compared with one at rest, and a clock lower in gravity runs slow compared with one higher up. The differences show up when the clocks are compared."),
        ("Has time dilation actually been measured?",
         "Yes, many times. Examples include light sent up a 74-foot tower at Harvard in 1960, muons in a storage ring that lived about 29 times longer than at rest, and NIST clocks in 2010 that detected the effect across a height of 33 centimetres."),
        ("Does your head really age faster than your feet?",
         "Yes, by a tiny amount. NIST estimated the difference for a foot of height at approximately 90 billionths of a second over a 79-year lifetime, far too small to notice."),
        ("Why does GPS need relativity?",
         "Satellite clocks run at a different rate from ground clocks because of their speed and height. Without correcting for this, errors building up in one day would cause navigation errors of more than 11 km, according to Neil Ashby."),
        ("Did Einstein ever get time dilation wrong?",
         "In 1905 he predicted that a clock at the equator would run slower than one at a pole. Later analysis showed that, once gravity is included, the two effects cancel for clocks at sea level."),
    ],
    related=[
        ("what-it-means-to-call-time-the-fourth-dimension", "What it means to call time the fourth dimension, and what it does not", "Fourth dimension"),
        ("why-time-has-a-direction", "Why time has a direction, and what entropy does and does not explain", "Physics and time"),
    ],
)

if __name__ == "__main__":
    newpost.build(POST)
