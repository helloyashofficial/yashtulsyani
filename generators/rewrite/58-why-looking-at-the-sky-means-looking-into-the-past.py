#!/usr/bin/env python3
"""Essay 58 :: why-looking-at-the-sky-means-looking-into-the-past  (Physics and time)

Literal register. Sources fetched and read on 5 Nov 2026: NIST CODATA value
of c; BIPM definition of the metre; IAU archive page on units; NASA Glenn on
the light-year; NASA Space Place on the Moon's distance; Smithsonian NASM on
sunlight; NASA APOD on Proxima Centauri; NASA and ANU on Betelgeuse; NASA
Hubble Messier catalogue on M31; NASA and ESA on Planck; NASA 2024 on
JADES-GS-z14-0 and STScI 2026 on MoM-z14; Las Cumbres Observatory and
Swinburne on lookback time; NRAO on the observable universe; AMNH on Roemer;
BBC Sky at Night and Ingenium on whether visible stars are dead.
Light times for the Moon and the Sun's exact figure are derived from the
linked distances and c, and labelled as such.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import newpost, postkit as K

EXT = ' target="_blank" rel="noopener"'
def a(url, text):
    return '<a href="%s"%s>%s</a>' % (url, EXT, text)

NIST = "https://physics.nist.gov/cuu/Constants/Value/c.html"
BIPM = "https://www.bipm.org/en/si-base-units/metre"
IAU = "https://iauarchive.eso.org/public/themes/measuring/"
GLENN = "https://www.grc.nasa.gov/www/K-12/Numbers/Math/Mathematical_Thinking/how_long_is_a_light_year.htm"
MOON = "https://spaceplace.nasa.gov/s/moon-distance"
SUN = "https://howthingsfly.si.edu/ask-an-explainer/how-long-does-it-take-light-sun-get-earth"
PROXIMA = "https://science.nasa.gov/?p=1236897"
BETEL = "https://science.nasa.gov/universe/what-is-betelgeuse-inside-the-strange-volatile-star"
BETELANU = "https://science.anu.edu.au/news-events/news/supergiant-star-betelgeuse-smaller-closer-first-thought"
M31 = "https://science.nasa.gov/mission/hubble/science/explore-the-night-sky/hubble-messier-catalog/messier-31/"
PLANCK = "https://science.nasa.gov/resource/planck/"
ESA = "https://www.esa.int/Science_Exploration/Space_Science/Planck/Planck_science_highlights"
JADES = "https://science.nasa.gov/?p=485552"
MOM = "https://www.stsci.edu/contents/news-releases/2026/news-2026-107"
LCO = "https://lco.global/spacebook/distance-and-lookback-time/"
SWIN = "https://astronomy.swinburne.edu.au/cosmos/L/Lookback+Time"
NRAO = "https://public.nrao.edu/ask/inconsistency-between-the-age-and-diameter-of-the-universe/"
ROEMER = "https://www.amnh.org/learn-teach/curriculum-collections/cosmic-horizons-book/ole-roemer-speed-of-light"
SKYNIGHT = "https://www.skyatnightmagazine.com/space-science/are-most-stars-we-see-already-dead"
INGENIUM = "https://ingeniumcanada.org/channel/articles/the-death-of-stars"

ESSAY41 = '<a href="/writing/what-the-observer-effect-actually-says">what the observer effect actually says</a>'
ESSAY48 = '<a href="/writing/why-time-has-a-direction">why time has a direction</a>'
ESSAY44 = '<a href="/writing/what-it-means-to-call-time-the-fourth-dimension">what it means to call time the fourth dimension</a>'
ESSAY63 = '<a href="/writing/what-time-dilation-is">what time dilation is</a>'

POST = dict(
    slug="why-looking-at-the-sky-means-looking-into-the-past", num=58, cat="Physics and time", read="auto",
    date="2026-11-05",
    gen="rewrite/58-why-looking-at-the-sky-means-looking-into-the-past.py",
    title="Why looking at the sky means looking into the past",
    dek="Light is fast but not instant. Everything you see in the night sky is a report that left its source some time ago: a second for the Moon, eight minutes for the Sun, centuries for some stars, millions of years for the nearest large galaxy. The further you look, the older the news.",
    takeaway="Light travels at exactly 299,792,458 metres per second, a value fixed by definition. Because that speed is finite, we see every object as it was when its light left it: the Moon about 1.3 seconds ago, the Sun about 8 minutes 20 seconds ago, the nearest star about 4.2 years ago, the Andromeda galaxy about 2.5 million years ago. A light-year is a distance, not a time. The oldest light we can see, the cosmic microwave background, left about 380,000 years after the Big Bang, 13.8 billion years ago, and the James Webb Space Telescope has seen galaxies as they were less than 300 million years after it. For the most distant objects, the light’s travel time is not the same as their distance today, because the universe has expanded while the light was on its way. Despite a popular claim, the stars visible to the naked eye are very unlikely to be dead.",
    sections=[
        ("Why the sky is the past", [
            "Looking at the sky means looking into the past because light takes time to travel. We see each object as it was when its light set out: the Sun as it was about eight minutes ago, stars as they were years or centuries ago, galaxies as they were millions or billions of years ago. The further away something is, the older the view.",
            "HTML:" + K.takeaways([
                "The speed of light is exactly 299,792,458 metres per second, by definition.",
                "A light-year is the distance light travels in a year, about 9.46 trillion km. It measures distance, not time.",
                "We see the Sun as it was about 8 minutes 20 seconds ago, and the nearest star about 4.2 years ago.",
                "The oldest light we can see left about 380,000 years after the Big Bang.",
                "For very distant galaxies, travel time and present distance are different numbers, because space has expanded.",
                "The stars you see with the naked eye are very unlikely to be dead.",
            ]),
            "This essay is in the literal register, like " + ESSAY41 + ". It sets out what the physics and the measurements say, and keeps any borrowing for human life to one labelled paragraph at the end.",
            "HTML:" + K.callout("definition", "Lookback time",
                "<p>In the words of " + a(SWIN, "Swinburne University’s astronomy encyclopedia") + ", the time elapsed between when we detect the light here on Earth and when it was originally emitted by the source. It is how far into the past we are looking.</p>"),
        ]),
        ("A fixed speed", [
            "Light’s speed in a vacuum is not just measured very precisely; it is fixed. The US National Institute of Standards and Technology lists it as " + a(NIST, "299 792 458 metres per second, exact") + ". The reason, as the " + a(BIPM, "International Bureau of Weights and Measures") + " explains, is that the metre itself is defined by taking that value as fixed, with the second defined in terms of the frequency of caesium atoms.",
            "That speed is enormous by everyday standards and small by cosmic ones. It is what makes the sky a record of the past rather than a live picture.",
            "The first person to measure the speed of light was the Danish astronomer Ole Rømer. According to the " + a(ROEMER, "American Museum of Natural History") + ", which gives his dates as 1644 to 1710, in 1676 he became the first person to measure the speed of light, by timing eclipses of Jupiter’s moon Io, and realising that differences in their timing must be due to the finite speed of light. He estimated that light needed twenty-two minutes to cross the diameter of Earth’s orbit. The correct value, the museum notes, is 16.7 minutes; what mattered was that it was not zero.",
        ]),
        ("A light-year is a distance", [
            "The unit used for these distances is easy to misread. As " + a(GLENN, "NASA’s Glenn Research Center") + " puts it: “The light-year is a measure of distance, not time.” It is the total distance that a beam of light, moving in a straight line, travels in one year: almost 6 trillion miles, or, by the figure below, about 9.46 trillion kilometres.",
            "The International Astronomical Union defines it precisely. According to its " + a(IAU, "archived public page on units") + ", the light-year is the distance travelled by light in one Julian year of 365.25 days in a vacuum, which comes to 9,460,730,472,580.8 km. The same page notes that the light-year is only sometimes used in scientific papers as a distance unit, its use being mostly confined to popular publications.",
            "The useful property of the unit is that it converts directly into lookback. Something 100 light-years away is seen as it was 100 years ago, as long as the distances involved are small enough for the expansion of the universe not to matter.",
        ]),
        ("Seconds, minutes, years", [
            "Close to home, the delays are short. The Moon, according to " + a(MOON, "NASA") + ", is an average of 384,400 km away, so its light, or rather the sunlight it reflects, takes about 1.3 seconds to reach us. That figure is worked out here from the distance and the speed of light, not quoted from NASA.",
            "Sunlight takes longer. The " + a(SUN, "Smithsonian’s National Air and Space Museum") + " says that on average the Sun is 150 million kilometres away, and it takes a photon of light about 8 minutes and 20 seconds to travel from the Sun to Earth. If the Sun went dark, we would go on seeing it for over eight minutes.",
            "The figure can be made exact. The " + a(IAU, "International Astronomical Union") + " defines the astronomical unit, a conventional unit of length approximating the distance between the Sun and Earth, as 149,597,870,700 metres exactly. Dividing by the speed of light gives about 499 seconds, a little over 8 minutes 19 seconds, which is consistent with the Smithsonian’s average figure.",
            "The nearest star beyond the Sun is much further. In " + a(PROXIMA, "NASA’s words") + ": “Light takes only 4.24 years to reach us from Proxima Centauri.” The view of it tonight is more than four years old.",
            "HTML:" + K.table("How old is the view?",
                ["Object", "Distance", "We see it as it was"],
                [["The Moon", "384,400 km on average", "About 1.3 seconds ago (worked out from distance)"],
                 ["The Sun", "About 150 million km", "About 8 minutes 20 seconds ago"],
                 ["Proxima Centauri", "4.24 light-years", "About 4.24 years ago"],
                 ["Betelgeuse", "About 530 to 700 light-years; estimates differ", "About 530 to 700 years ago"],
                 ["Andromeda galaxy", "About 2.5 million light-years", "About 2.5 million years ago"]],
                source='Sources: <a href="' + MOON + '" target="_blank" rel="noopener">NASA</a>; <a href="' + SUN + '" target="_blank" rel="noopener">Smithsonian</a>; <a href="' + PROXIMA + '" target="_blank" rel="noopener">NASA APOD</a>; <a href="' + BETEL + '" target="_blank" rel="noopener">NASA</a> and <a href="' + BETELANU + '" target="_blank" rel="noopener">ANU</a>; <a href="' + M31 + '" target="_blank" rel="noopener">NASA Hubble</a>.'),
        ]),
        ("Centuries and millions of years", [
            "Bright stars are further still. Betelgeuse is around 700 light-years away according to " + a(BETEL, "NASA") + ", which adds that if you see Betelgeuse in the night sky, you’re seeing the star from about 700 years ago. A 2020 study reported by the " + a(BETELANU, "Australian National University") + " put it closer, at about 530 light-years, 25 per cent closer than previous thought. Distances to individual stars are hard to measure, and the honest answer is a range.",
            "Galaxies take the delay into the millions of years. The Andromeda galaxy, which " + a(M31, "NASA notes") + " can be seen with the naked eye, even in areas with moderate light pollution, is about 2.5 million light-years away. The faint smudge visible on a dark night is light that left Andromeda about 2.5 million years ago.",
        ]),
        ("The oldest light", [
            "Look far enough and the view reaches back towards the beginning. The universe’s age, as measured by the European Space Agency’s " + a(ESA, "Planck mission") + ", is 13.8 billion years. The oldest light that can be seen is the cosmic microwave background, which " + a(PLANCK, "NASA describes") + " as the oldest light in the universe, emitted just 380,000 years after the big bang. It is not light from the Big Bang itself, but from a few hundred thousand years after it.",
            "Between that light and today’s galaxies, the James Webb Space Telescope has been pushing back the record for the earliest galaxies seen. In May 2024, " + a(JADES, "NASA reported") + " a galaxy called JADES-GS-z14-0, seen as it was less than 300 million years after the big bang. That record has since been broken: in January 2026 the " + a(MOM, "Space Telescope Science Institute") + " described a galaxy called MoM-z14 that existed only 280 million years after the universe began, which it called Webb’s current most distant galaxy.",
            "HTML:" + K.table("Looking back towards the beginning",
                ["What we see", "How long ago the light set out"],
                [["Cosmic microwave background", "About 13.8 billion years ago, about 380,000 years after the Big Bang"],
                 ["MoM-z14, Webb’s most distant galaxy as of January 2026", "From about 280 million years after the Big Bang"],
                 ["JADES-GS-z14-0, the record holder in 2024", "From less than 300 million years after the Big Bang"]],
                source='Sources: <a href="' + PLANCK + '" target="_blank" rel="noopener">NASA</a> and <a href="' + ESA + '" target="_blank" rel="noopener">ESA</a> on Planck; <a href="' + JADES + '" target="_blank" rel="noopener">NASA (2024)</a>; <a href="' + MOM + '" target="_blank" rel="noopener">STScI (2026)</a>.'),
        ]),
        ("Reading the distance from the light", [
            "For galaxies too distant to measure any other way, astronomers read the lookback from the light itself. The " + a(LCO, "Las Cumbres Observatory") + " explains that the more distant an object, the more its light is redshifted, its wavelength shifted towards the red; the amount, written z, corresponds to the number of years the light from an object has travelled to reach us.",
            "That is how the JWST records are stated. NASA’s " + a(JADES, "2024 announcement") + " gave JADES-GS-z14-0 a redshift of 14.32, with an uncertainty of plus 0.08 or minus 0.20, which corresponds to a time less than 300 million years after the big bang. It described the galaxy as over 1,600 light-years across. The announcement also carried a note that the result was science in progress, not yet peer reviewed at the time.",
            "Swinburne’s " + a(SWIN, "encyclopedia") + " adds a detail that matters at these distances: for very distant objects, the lookback time is increased by the Hubble expansion of the universe.",
        ]),
        ("Travel time is not distance", [
            "For the most distant objects, one simplification breaks down. The " + a(LCO, "Las Cumbres Observatory") + " explains that the number of years the light from a very distant object has travelled is not the distance to the object in light years, because the universe has been expanding as the light travelled and the object is now much farther away.",
            "That is why the size of the observable universe is much larger than its age might suggest. As the National Radio Astronomy Observatory’s " + a(NRAO, "Ask an Astronomer page") + " explains, the structures seen in the cosmic microwave background would be 46.5 billion light-years from us now, and the often-quoted 93 billion light-year diameter refers to the observable universe, at best a theoretical estimate. The universe is 13.8 billion years old; it is not 13.8 billion light-years across.",
            "HTML:" + K.callout("warn", "Two numbers, often confused",
                "<p>Lookback time is how long ago the light left. Present distance is how far away the source is now. For nearby objects they are the same in light-years. For the most distant ones, " + a(LCO, "expansion") + " makes the present distance much larger.</p>"),
        ]),
        ("Are the stars we see already dead?", [
            "A popular claim says that many of the stars in the night sky no longer exist. Astronomers disagree. Writing in " + a(SKYNIGHT, "BBC Sky at Night Magazine") + ", Dr Alastair Gunn of the Jodrell Bank Centre for Astrophysics says it is unlikely, though not impossible, that any of them are already dead. His reasons are that all the stars visible to the naked eye lie within about 4,000 light-years of Earth, and that at that range a visible star dies only about once every 10,000 years.",
            "The reason is the timescales. Jesse Rogerson, writing for " + a(INGENIUM, "Ingenium") + ", notes that stars live a few hundred million years on the short side and multiple billions of years on the longer side, while, as he puts it, we are seeing the stars as they were up to thousands of years ago. His conclusion is blunter than Gunn’s: “it is extremely unlikely that any of them are dead.” A star’s light arriving late does not mean the star is gone. Even Betelgeuse, which is expected to explode, is not likely to do so, " + a(BETEL, "NASA says") + ", for about another 100,000 years.",
        ]),
        ("What this does and does not say", [
            "Read literally, the claim is simple and well established. Light has a finite, fixed speed, so every view of the sky is a view of the past, by an amount that grows with distance. For nearby objects the delay is seconds to centuries; for distant galaxies, billions of years, with expansion complicating the arithmetic. The sky is not a live picture, and most of it is not news of anything recent.",
            "Here is the one borrowing in this essay, labelled as such. As a metaphor only, the delay is a reminder that what we see of anything distant, a person far away included, arrives as it was, not as it is. In physics that is a fact about the speed of light; in a life it is only a resemblance, and nothing here suggests the physics governs it.",
            "Other essays here carry the physics further. " + ESSAY44.replace(">what it means", ">What it means") + " explains how relativity joins space and time into one structure. " + ESSAY63.replace(">what time", ">What time") + " looks at the measured fact that clocks run at different rates with speed and height. And " + ESSAY48 + " asks why records, including the light from the sky, point only to the past.",
        ]),
    ],
    note=[
        "The Moon’s light time and the 499-second figure for sunlight are worked out from the linked values and the speed of light. Distances to individual stars are uncertain, and ranges are given where sources differ.",
    ],
    faqs=[
        ("Is a light-year a unit of time?",
         "No. A light-year is a distance: how far light travels in a year, about 9.46 trillion km. It is useful for lookback because something 100 light-years away is seen as it was 100 years ago."),
        ("How long does sunlight take to reach Earth?",
         "About 8 minutes and 20 seconds on average, according to the Smithsonian's National Air and Space Museum.."),
        ("What is the oldest light we can see?",
         "The cosmic microwave background, emitted about 380,000 years after the Big Bang, which took place 13.8 billion years ago, according to NASA and ESA's Planck mission."),
        ("Are the stars we see in the night sky dead?",
         "Almost certainly not. The stars visible to the naked eye lie within about 4,000 light-years of Earth, so we see them as they were up to thousands of years ago, while stars live for hundreds of millions to billions of years."),
        ("Is the universe 13.8 billion light-years across?",
         "No. 13.8 billion years is its age. Because space has expanded while light travelled, the observable universe is much larger; one estimate puts the most distant structures we see about 46.5 billion light-years away now."),
    ],
    related=[
        ("why-time-has-a-direction", "Why time has a direction, and what entropy does and does not explain", "Physics and time"),
        ("what-entanglement-is", "What quantum entanglement actually is, and what it is not", "Physics and time"),
    ],
)

if __name__ == "__main__":
    newpost.build(POST)
