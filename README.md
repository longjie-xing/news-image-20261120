# news-image-20261120

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/longjie-xing/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/longjie-xing/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

One picture that sums up the world news of Friday 20 November 2026.
A newspaper-style poster, drawn from that day's reporting and laid out
so a reader gets the whole day at a glance: one lead story on top, then
five more stories numbered 02 to 06, plus a markets strip. Entry for the
make.fun `news-image-20261120` bounty.

## Files

- `entry.png` — the poster itself, 1024×1024, about 170 KB. A deep-blue
  masthead with the date, the lead headline in large serif type, and the
  five stories below it in two columns.
- `main.py` — the entry program (Python 3.13, standard library only). It
  does exactly one thing: copy `entry.png` byte for byte to the output
  path. No network, no re-encoding, no randomness, so two runs write
  identical bytes every time.
- `LICENSE` — MIT.

## The six stories

1. Trump, Xi and Putin hold their first three-way summit in Shenzhen and
   sign a four-point joint peace declaration.
2. The International Court of Justice rules that Myanmar committed
   genocide against its Rohingya minority — the court's first such
   finding against a state.
3. Anthropic closes 17% above its IPO price on its Nasdaq debut, even as
   doubts over AI valuations drag world markets lower.
4. A Houthi missile damages the Saudi sovereign wealth fund's PIF tower
   in Riyadh's financial district.
5. The COP31 draft deal in Antalya drops any call to phase out fossil
   fuels.
6. Kenya discharges its last Ebola patient, 37 days after the first case.

The facts were checked against 20 November 2026 reporting (One Turn,
LA Post, Inshorts, Morning Briefing).

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

That writes the poster to `out/entry.png`. Inside the grader's container
`MAKEFUN_OUTPUT_DIR` is unset and the file lands at `/output/entry.png`.

## License

MIT — see `LICENSE`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=397wsy61&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>
