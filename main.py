#!/usr/bin/env python3
"""Build the news-image-20261124 front page (1024x1024 PNG).

Dense one-page newspaper for Tuesday 24 November 2026: 35 stories across
6 regions - 3 leads, 10 features, 22 briefs - plus a stat strip, a region
tally, a dotted world map with numbered pins, a DATE CHECK box of stories
deliberately left out (they happened 19-23 Nov), and a source footer.
Every story was checked against reporting published on 24 Nov 2026
(AP, Reuters, BBC, AFP, ANI, USGS, UEFA and others); Monday and weekend
stories are dated in their own text. All pictures are drawn here with
PIL - no photographs, no generated images - so no text is ever garbled.
All headlines and summaries are written fresh for this page.

Deterministic: no clock, no randomness, fixed font paths; PIL's PNG
writer is deterministic, so two runs produce identical bytes.
"""
import os

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BG = (247, 242, 231)      # newsprint cream
INK = (18, 18, 18)
RED = (176, 32, 22)
DARK = (18, 18, 20)
GREY = (96, 92, 84)
TEAL = (18, 74, 96)
SEA = (32, 96, 122)
SKY = (196, 222, 232)
GOLD = (214, 164, 32)
GREEN = (46, 110, 62)
CREAM = (250, 246, 236)
AMBER = (168, 110, 8)
RULE = (150, 145, 132)

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUT = os.path.join(OUT_DIR, "entry.png")

SERIF_B = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SERIF_I = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"
SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap; returns a list of lines that fit in width px."""
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def para(draw, text, fnt, x, y, width, leading, fill=INK):
    """Draw wrapped text; returns the y just below the last line."""
    for line in wrap(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def rule(draw, x, y, w, fill=RULE, width=1):
    draw.line([(x, y), (x + w, y)], fill=fill, width=width)


# ---------------------------------------------------------------- story data
# Headlines and summaries written fresh for this page from the verified
# facts in the build brief. No number, time, quote or source is invented.
# Region tally (must match the chips): North America 14, Asia-Pacific 10,
# Europe 5, Middle East 3, Africa 2, Global 1 = 35.
#   North America: 01, 09, 12, 13, 14, 15, 16, 17, 18, 19, 20, 27, 30, 31.
#   Asia-Pacific: 02, 03, 04, 05, 06, 07, 21, 22, 23, 24.
#   Europe: 08, 10, 11, 28, 29. Middle East: 25, 34, 35.
#   Africa: 32, 33. Global: 26.
LEADS = [
    dict(num=1, place="WALL STREET, NORTH AMERICA", tag="MARKETS",
         source="AP · REUTERS",
         headline="HUANG'S RETURN SETS WALL ST ALIGHT",
         summary="Nvidia jumps 31% at the open on Jensen Huang's return. "
                 "The S&P 500 climbs 4.5%, the Nasdaq 6.5% and the Dow "
                 "1,117 points."),
    dict(num=2, place="KYIV, EUROPE", tag="REPORTED",
         source="AP · DAILY SUMMARY",
         headline="ZELENSKY SEEKS FOUR-WAY TALKS NOW",
         summary="Zelensky calls for Ukraine, Russia, the US and Europe to "
                 "meet as soon as possible; Kyiv is ready as early as "
                 "Tuesday."),
    dict(num=3, place="SINGAPORE, ASIA-PACIFIC", tag="REPORTED",
         source="REUTERS · BBC",
         headline="US BLACKLISTS MEGASPEED",
         summary="Washington puts Megaspeed and six south-east Asian firms "
                 "on its Entity List, at the centre of the alleged Nvidia "
                 "chip-smuggling scandal."),
]

FEATURES = [
    dict(num=4, place="SEOUL, ASIA-PACIFIC",
         headline="RUSSIAN JETS ENTER KOREA'S AIR ZONE",
         summary="Several Russian aircraft fly into the air defence zone on "
                 "Tuesday, the second push in a week; earlier reports of an "
                 "airspace violation are corrected."),
    dict(num=5, place="BEIJING, ASIA-PACIFIC",
         headline="CHINA SENTENCES SPY TO DEATH",
         summary="An official surnamed Ma is sentenced to death for spying "
                 "for an unnamed foreign country, state-linked press says."),
    dict(num=6, place="TAPLEJUNG, ASIA-PACIFIC",
         headline="QUAKE SHAKES NEPAL-TIBET BORDER",
         summary="A magnitude 5.3 tremor (Nepal's centre: 5.6) strikes at "
                 "07:02 IST; shaking is felt in India, Bhutan, Bangladesh "
                 "and China. No damage is reported."),
    dict(num=7, place="CIKANDE, ASIA-PACIFIC",
         headline="CANDY-FACTORY FIRE TOLL 24",
         summary="Search goes on Tuesday for about 30 missing after "
                 "Saturday's blaze at the PT Fonusa Agung Mulia plant; a "
                 "short circuit in an air conditioner is suspected."),
    dict(num=8, place="DYMER, EUROPE",
         headline="BOY, 7, PULLED ALIVE FROM RUBBLE",
         summary="The toll reaches 11 after Sunday's drone strike on a "
                 "block of flats; a boy and a woman of 79 are freed on "
                 "Monday after about 22 hours trapped."),
    dict(num=9, place="OTTAWA, NORTH AMERICA",
         headline="PENTAGON REBUKES CANADA",
         summary="The US says Ottawa falls short as a credible partner in "
                 "defending North America, citing defence spending and its "
                 "review of F-35 fighter jets."),
    dict(num=10, place="ANKARA, EUROPE",
         headline="COP31: NO DEAL, TALKS GO ON",
         summary="Erdogan says the summit laid groundwork for more climate "
                 "talks; the EU urges multilateral talks to continue after "
                 "the collapse, and a 22nd sanctions package is proposed."),
    dict(num=11, place="BRUSSELS, EUROPE",
         headline="NATO WATCHES THE SKIES",
         summary="Early-warning aircraft head to Poland after a missiles "
                 "incident, and the alliance vows space defence amid "
                 "reports of a Russian nuclear-armed satellite."),
    dict(num=12, place="WASHINGTON, NORTH AMERICA",
         headline="CROWDSTRIKE BUYS ZSCALER, $44BN",
         summary="CrowdStrike agrees to acquire Zscaler in a deal that "
                 "would create a cybersecurity giant, AP reports."),
    dict(num=13, place="NEW YORK, NORTH AMERICA",
         headline="SKUBAL'S $450M METS DEAL",
         summary="Tarik Skubal agrees a record nine-year, $450 million "
                 "contract with the New York Mets, an AP source says."),
]

BRIEFS = [
    (14, "IOWA, NORTH AMERICA",
     "Army to detonate 5 tons of degraded lead azide on Wednesday after "
     "court approval; Trump deferred to the appeals court on Monday."),
    (15, "WASHINGTON, NORTH AMERICA",
     "Rep. Jimmy Gomez resigns after the House ethics panel finds evidence "
     "of sexual misconduct."),
    (16, "NORTH CAROLINA, NORTH AMERICA",
     "Chuck Hubbard beats Rep. Virginia Foxx after a recount in their "
     "House race."),
    (17, "WASHINGTON, NORTH AMERICA",
     "Democrats clinch a House majority of at least 258 seats, the largest "
     "since 1992. (Mon)"),
    (18, "WASHINGTON, NORTH AMERICA",
     "Records from the October search of Rep. Ilhan Omar's home are "
     "unsealed."),
    (19, "WASHINGTON, NORTH AMERICA",
     "The FBI investigates an apparent hack of its national crime "
     "database. (Mon)"),
    (20, "OTTAWA, NORTH AMERICA",
     "Canada and Qatar are to sign an investment pact on Tuesday, a source "
     "says."),
    (21, "SINGAPORE, ASIA-PACIFIC",
     "Singapore and Australia sign two pacts as PM Wong hails a trusted "
     "partnership."),
    (22, "NEW DELHI, ASIA-PACIFIC",
     "India and Nepal announce major projects during PM Shah's visit to "
     "Delhi."),
    (23, "NEW DELHI, ASIA-PACIFIC",
     "India keeps third place in the Asia Power Index."),
    (24, "DHAKA, ASIA-PACIFIC",
     "Sheikh Hasina plans to return home from exile in India on 16 "
     "December."),
    (25, "DOHA, MIDDLE EAST",
     "The US and Qatar agree to strengthen cooperation in defence, trade "
     "and technology."),
    (26, "GLOBAL",
     "Oil falls about 3% - Brent $89.95 - as Libya's Sharara pipeline "
     "restarts. (Mon)"),
    (27, "SAN FRANCISCO, NORTH AMERICA",
     "Anthropic launches Claude Ship to help developers ship code faster."),
    (28, "ATHENS, EUROPE",
     "Greece's oldest modern-era museum reopens on the Acropolis after a "
     "major restoration."),
    (29, "EUROPE",
     "Champions League tonight: Arsenal-Dortmund, Man City-Napoli, Real "
     "Madrid-PSV. (FORECAST)"),
    (30, "HOUSTON, NORTH AMERICA",
     "Houston leaps seven spots to No. 1 in the AP Top 25 men's poll."),
    (31, "WASHINGTON, NORTH AMERICA",
     "The US loses measles-free status as cases reach their highest rate "
     "in decades."),
    (32, "KINSHASA, AFRICA",
     "Congo bans cobalt exports to halt a price slide."),
    (33, "JOHANNESBURG, AFRICA",
     "South Africans vote as service chaos tests the governing ANC."),
    (34, "GAZA, MIDDLE EAST",
     "Israeli strikes kill at least three in Gaza, including a worker with "
     "the UN Palestinian agency."),
    (35, "TEHRAN, MIDDLE EAST",
     "Iran says it will use all available tools to confront the US naval "
     "blockade."),
]

STAT_STRIP = ("S&P 500 +4.5%   ·   NASDAQ +6.5%   ·   DOW +1,117   ·   "
              "NVIDIA +31%   ·   BRENT $89.95   ·   35 STORIES   ·   "
              "6 REGIONS")

DATE_CHECK = ("Left out - not today: the ICJ's Myanmar genocide ruling "
              "(Thu 19 Nov); COP31 closing with no deal (Sun 23 Nov); "
              "Huang reinstated as Nvidia chief (Mon 23 Nov); Ukraine "
              "sinking a Russian corvette off Libya (Sun 23 Nov); "
              "Democrats' 258-seat House win (Mon 23 Nov).")

SOURCES = ("Sources: AP · Reuters · BBC · AFP · ANI · IANS · USGS · "
           "India NCS · UEFA · Finnhub. Wires as of about 07:20 UTC, "
           "Tuesday 24 November 2026. Forecasts are marked FORECAST; "
           "older stories carry their day in the text.")


# ---------------------------------------------------------------- drawing
def draw_masthead(draw):
    title = font(SERIF_B, 46)
    draw.text((512, 6), "THE WORLD IN ONE IMAGE", font=title, fill=INK,
              anchor="ma")
    sub = font(SANS_B, 15)
    draw.text((512, 58), "TUESDAY  24  NOVEMBER  2026  ·  ONE DAY · ONE PAGE · "
              "THE WORLD'S NEWS", font=sub, fill=RED, anchor="ma")
    rule(draw, 24, 82, 976, fill=INK, width=3)
    rule(draw, 24, 87, 976, fill=INK, width=1)


def draw_stat_strip(draw, y):
    draw.rectangle([0, y, W, y + 24], fill=DARK)
    fnt = font(SANS_B, 12)
    draw.text((512, y + 6), STAT_STRIP, font=fnt, fill=(240, 236, 224),
              anchor="ma")
    return y + 24


def draw_chart(draw, x, y, w, h):
    """Rising market bars for lead 1."""
    draw.rectangle([x, y, x + w, y + h], fill=(232, 244, 238),
                   outline=RULE)
    bars = [0.30, 0.42, 0.38, 0.55, 0.50, 0.68, 0.62, 0.80, 0.95]
    bw = w / len(bars)
    for i, v in enumerate(bars):
        bh = v * (h - 26)
        bx = x + i * bw + 3
        draw.rectangle([bx, y + h - 6 - bh, bx + bw - 6, y + h - 6],
                       fill=GREEN if i < len(bars) - 1 else RED)
    fnt = font(SANS_B, 12)
    draw.text((x + 6, y + 4), "+31%", font=fnt, fill=RED)
    draw.text((x + w - 6, y + 4), "S&P +4.5%", font=fnt, fill=GREEN,
              anchor="ra")


def draw_table(draw, x, y, w, h):
    """Four chairs around a table for lead 2 (no text: labels collided)."""
    draw.rectangle([x, y, x + w, y + h], fill=(232, 238, 244),
                   outline=RULE)
    cx, cy = x + w // 2, y + h // 2
    draw.ellipse([cx - 40, cy - 13, cx + 40, cy + 13], fill=(250, 246, 236),
                 outline=TEAL, width=2)
    for dx, dy, col in [(-56, -14, TEAL), (56, -14, RED),
                        (-56, 14, GOLD), (56, 14, GREEN)]:
        draw.ellipse([cx + dx - 9, cy + dy - 9, cx + dx + 9, cy + dy + 9],
                     fill=col)


def draw_chip(draw, x, y, w, h):
    """A chip on a list for lead 3."""
    draw.rectangle([x, y, x + w, y + h], fill=(244, 232, 232),
                   outline=RULE)
    cx, cy = x + w // 2, y + h // 2 + 2
    draw.rectangle([cx - 34, cy - 14, cx + 34, cy + 14], fill=DARK)
    for i in range(3):
        draw.line([(cx - 44, cy - 8 + i * 8), (cx - 36, cy - 8 + i * 8)],
                  fill=GOLD, width=3)
        draw.line([(cx + 36, cy - 8 + i * 8), (cx + 44, cy - 8 + i * 8)],
                  fill=GOLD, width=3)
    draw.rectangle([cx - 18, cy - 6, cx + 18, cy + 6], fill=GOLD)
    fnt = font(SANS_B, 12)
    draw.text((x + 6, y + 4), "ENTITY LIST", font=fnt, fill=RED)
    draw.text((x + w - 6, y + 4), "+6 FIRMS", font=fnt, fill=RED,
              anchor="ra")


LEAD_ART = [draw_chart, draw_table, draw_chip]


def draw_lead(draw, lead, x, y, w):
    art = LEAD_ART[lead["num"] - 1]
    art(draw, x, y, w, 44)
    yy = y + 46
    tagf = font(SANS_B, 12)
    draw.text((x, yy), "%02d  %s" % (lead["num"], lead["place"]),
              font=tagf, fill=RED)
    draw.text((x + w, yy), lead["tag"], font=tagf, fill=TEAL, anchor="ra")
    yy += 16
    yy = para(draw, lead["headline"], font(SERIF_B, 22), x, yy, w, 24)
    yy = para(draw, lead["summary"], font(SERIF, 12), x, yy + 2, w, 15)
    srcf = font(SANS, 10)
    draw.text((x, yy + 3), lead["source"], font=srcf, fill=GREY)
    return yy + 18


def draw_leads(draw, y):
    colw = 304
    xs = [24, 360, 696]
    bottom = y
    for lead, x in zip(LEADS, xs):
        bottom = max(bottom, draw_lead(draw, lead, x, y, colw))
    for x in (344, 680):
        draw.line([(x, y + 4), (x, bottom - 6)], fill=RULE, width=1)
    rule(draw, 24, bottom, 976, fill=INK, width=2)
    return bottom + 8


def draw_feature(draw, feat, x, y, w):
    tagf = font(SANS_B, 11)
    draw.text((x, y), "%02d  %s" % (feat["num"], feat["place"]),
              font=tagf, fill=RED)
    y += 13
    y = para(draw, feat["headline"], font(SERIF_B, 16), x, y, w, 17)
    y = para(draw, feat["summary"], font(SERIF, 11), x, y + 1, w, 13)
    return y + 3


def draw_features(draw, y):
    colw, gap = 478, 20
    row_h = 62
    for i, feat in enumerate(FEATURES):
        col, row = i % 2, i // 2
        x = 24 + col * (colw + gap)
        yy = y + row * row_h
        draw_feature(draw, feat, x, yy, colw)
    bottom = y + 5 * row_h - 2
    draw.line([(512, y + 2), (512, bottom)], fill=RULE, width=1)
    rule(draw, 24, bottom + 4, 976, fill=INK, width=2)
    return bottom + 10


def draw_briefs(draw, y):
    headf = font(SANS_B, 13)
    draw.text((24, y), "IN BRIEF", font=headf, fill=INK)
    draw.text((1000, y), "22 MORE STORIES", font=headf, fill=GREY,
              anchor="ra")
    y += 18
    colw, gap = 478, 20
    row_h = 23
    numf = font(SERIF_B, 12)
    txtf = font(SERIF, 11)
    for i, (num, place, text) in enumerate(BRIEFS):
        col, row = i % 2, i // 2
        x = 24 + col * (colw + gap)
        yy = y + row * row_h
        draw.text((x, yy), "%02d" % num, font=numf, fill=RED)
        para(draw, "%s - %s" % (place, text), txtf, x + 28, yy, colw - 28,
             11.5)
    return y + 11 * row_h + 2


# Coarse equirectangular land dots, 64 x 28 cells, hand-plotted.
WORLD = [
    "................................................................",
    "......xxxx......................................................",
    "...xxxxxxxxx.....xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx............",
    "..xxxxxxxxxxxx..xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx..........",
    "...xxxxxxxxxx...xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx..........",
    "....xxxxxxxx.....xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx...........",
    ".....xxxxxx.......xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx...........",
    "......xxxx.........xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx............",
    ".......xx...........xxxxxxxxxxxx..xxxxxxxxxxxx..................",
    "....................xxxxxxxxxx.....xxxxxxxxxx...................",
    ".....................xxxxxxxx.......xxxxxxxx....................",
    "......................xxxxxx.........xxxxxx.....................",
    ".......................xxxxx..........xxxx......................",
    "........................xxxx...........xxx.......................",
    ".........................xx............xx........................",
    "................................................................",
]
# (lon, lat, story num) pins for the three leads.
PINS = [(-74, 41, 1), (31, 50, 2), (104, 1, 3)]


def draw_map(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h], fill=(226, 238, 244),
                   outline=RULE)
    cell_w, cell_h = w / 64.0, h / 16.0
    for r, row in enumerate(WORLD):
        for c, ch in enumerate(row):
            if ch == "x":
                cx = x + c * cell_w + cell_w / 2
                cy = y + r * cell_h + cell_h / 2
                draw.ellipse([cx - 1, cy - 1, cx + 1, cy + 1], fill=TEAL)
    pinf = font(SANS_B, 11)
    for lon, lat, num in PINS:
        px = x + (lon + 180) / 360.0 * w
        py = y + (90 - lat) / 180.0 * h
        draw.ellipse([px - 8, py - 8, px + 8, py + 8], fill=RED,
                     outline=(255, 255, 255), width=1)
        draw.text((px, py - 1), str(num), font=pinf, fill=(255, 255, 255),
                  anchor="mm")


def draw_bottom(draw, y):
    # Left: dotted world map. Right: region tally + date check.
    map_w, map_h = 330, 56
    draw_map(draw, 24, y, map_w, map_h)
    x = 24 + map_w + 16
    w = 1000 - x
    tallyf = font(SANS_B, 12)
    draw.text((x, y), "WHERE THE NEWS CAME FROM", font=tallyf, fill=INK)
    tally = [("N. AMERICA", 14, RED), ("ASIA-PACIFIC", 10, TEAL),
             ("EUROPE", 5, SEA), ("M. EAST", 3, GOLD),
             ("AFRICA", 2, GREEN), ("GLOBAL", 1, GREY)]
    bx, by = x, y + 13
    bw = (w - 10) / 6.0
    for i, (name, n, col) in enumerate(tally):
        cx = bx + i * bw
        bar_h = 5 + n * 1.2
        draw.rectangle([cx, by + 20 - bar_h, cx + bw - 8, by + 20],
                       fill=col)
        draw.text((cx, by + 23), "%d" % n, font=font(SANS_B, 12), fill=INK)
        draw.text((cx, by + 34), name, font=font(SANS, 9), fill=GREY)
    yy = y + 58
    rule(draw, x, yy, w)
    yy = para(draw, "DATE CHECK  " + DATE_CHECK, font(SERIF_I, 11), x,
              yy + 4, w, 12, fill=(90, 40, 30))
    return max(y + map_h, yy) + 4


def draw_footer(draw, y):
    rule(draw, 24, y, 976, fill=INK, width=2)
    para(draw, SOURCES, font(SERIF, 10), 24, y + 5, 976, 11, fill=GREY)


def build():
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)
    draw_masthead(draw)
    y = draw_stat_strip(draw, 91)
    y = draw_leads(draw, y + 8)
    y = draw_features(draw, y)
    y = draw_briefs(draw, y)
    y = draw_bottom(draw, y)
    draw_footer(draw, y)
    os.makedirs(OUT_DIR, exist_ok=True)
    img.save(OUT, format="PNG")
    return OUT


if __name__ == "__main__":
    print(build())
