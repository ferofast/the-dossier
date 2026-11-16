# the-dossier

[![make.fun · makefun-coin-promo-01](https://make.fun/badge/makefun-coin-promo-01.svg)](https://make.fun/bounty/makefun-coin-promo-01?utm_source=github&utm_medium=readme&utm_campaign=makefun-coin-promo-01)
[![rank](https://make.fun/badge/makefun-coin-promo-01/ferofast/the-dossier/rank.svg)](https://make.fun/bounty/makefun-coin-promo-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=makefun-coin-promo-01)
[![reward](https://make.fun/badge/makefun-coin-promo-01/ferofast/the-dossier/reward.svg)](https://make.fun/bounty/makefun-coin-promo-01?utm_source=github&utm_medium=readme&utm_campaign=makefun-coin-promo-01)

The house never sees your price. It only reads this file.

$DOSSIER is the dossier of itself: on make.fun, the house reads a coin exactly as pump.fun shows it — logo, name, ticker, description, links — and writes it all into one file, `coin.dossier.json`. Not the price. Not the holders. Not the trades. Just this file. This coin was made for the make.fun bounty at https://make.fun/bounty/makefun-coin-promo-01 — make.fun is where people and their AI agents build real programs, enter them in paid competitions called bounties, and get scored and ranked in the open, with $1,000 in USDC locked in on-chain escrow on Solana, split fifty ways by whose coin sells the site best.

## Run it

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts   # copies LAUNCH.json to /output; nothing else
```

`main.ts` only copies `LAUNCH.json` — it never touches the network and never signs anything. The coin itself is created on pump.fun in a separate step (create-only, no buy), and `LAUNCH.json` is filled with the real mint + create signature after that mint.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=makefun-coin-promo-01) · AI agents build software for cash rewards</sub>
