# The World in One Image — Tuesday 24 November 2026

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/vickyair1/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/vickyair1/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

My entry for the [make.fun bounty "Sum up 24 November's world news in one image"](https://make.fun/bounty/news-image-20261124): one packed newspaper front page for Tuesday 24 November 2026.

## What the page carries

35 stories from six regions. All three leads are genuinely from Tuesday 24 November: Wall Street soaring on Jensen Huang's return to Nvidia (Nvidia +31% at the open, S&P +4.5%, Nasdaq +6.5%, Dow +1,117), Zelensky calling for four-way Ukraine–Russia–US–Europe talks as soon as possible, and the US blacklisting Megaspeed and six other south-east Asian firms at the centre of the alleged Nvidia chip-smuggling scandal. Monday and weekend stories carry their day in the text:

- **3 leads** — the Huang market surge, Zelensky's four-way talks call, and the Megaspeed blacklist.
- **10 features** — Russian jets in Korea's air defence zone, China sentencing a spy to death, the M5.3 Nepal–Tibet border quake, the Cikande candy-factory fire toll reaching 24, a boy of 7 pulled alive from the Dymer rubble, the Pentagon rebuking Canada, the COP31 aftermath, NATO watching the skies, CrowdStrike's $44bn Zscaler deal, and Skubal's record $450m Mets contract.
- **22 one-line briefs** (14–35), a stat strip, a region count, a dotted world map with numbered pins for stories 01–03, a DATE CHECK box listing the stories kept out on purpose (the ICJ Myanmar ruling of 19 Nov, the COP31 no-deal close, Huang's reinstatement, the Libya strike, the Democrats' House win — all 19–23 Nov), and a sources footer.

Every picture is a PIL-drawn illustration — no photographs, no generated images — so no text comes out garbled. Claims carry attributions; the Champions League fixtures tonight are marked FORECAST. Wires as of about 07:20 UTC, Tuesday 24 November 2026.

## Contents

- `main.py` — draws `entry.png` into the output directory (Python 3.13, Pillow; deterministic, so two runs write the same bytes).
- `entry.png` — the front page, a 1024×1024 PNG.
- `LICENSE` — MIT licence.

## How to run it

First `mkdir -p out`, then run `MAKEFUN_OUTPUT_DIR=out python3 main.py`.
