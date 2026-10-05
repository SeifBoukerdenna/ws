# AGENTS.md

Rules for every agent working in this repo (Claude Code, Codex, or anything else).

This repo is a personal research workbench for creating, evaluating, and backtesting
trading models on event contracts (prediction markets), stocks/ETFs, and options.
Trades are always placed by hand, outside this repo.

## Hard rules

1. This repo never places orders or calls broker trading endpoints. Market data and simulation only.
2. Secrets live only in `.env` (gitignored). API keys are read-only. Never print, log, or commit them.
3. Costs are first-class. Every simulated trade carries its full cost: commissions,
   exchange/regulatory fees, bid-ask spread, slippage, contract-specific fees, and
   CAD↔USD conversion. A result without costs is not a result.
4. No lookahead: anything used at time t must have been knowable at time t.
5. No new `.md` files besides the ones listed in "Where things go" and `research/` theses.
   Scratch thinking stays in the chat, not the repo.
6. No notebooks, ever. Experiments are scripts in `scripts/`.
7. Commit directly to `main` after each approved task. Never push unless the user asks.

Ask the user first before: adding a dependency, changing a data format, deleting files
or data, or touching anything near secrets.

`tests/test_repository_rules.py` enforces rules 5 and 6, so `just check` fails on a stray
`.md` file or a notebook.

## Language and naming

This is the most important section. Code is read far more often than it is written.

- Long, descriptive names: `fetch_daily_option_chain`, not `get_chain`.
  No abbreviations except: `id`, `url`, `api`, `utc`, `csv`, `usd`, `cad`, `bps`.
- Units in names: `price_usd`, `fee_bps`, `holding_period_days`, `timestamp_utc`.
  (`bps` means basis points: 1 bps = 0.01%.)
- One concept = one word. Use the vocabulary table below. Before introducing a new core
  term, add it to the table first. Max 20 rows.
- Comments explain WHY, never WHAT. If code needs a WHAT comment, rename things instead.
- Timestamps are always timezone-aware UTC. Money uses `Decimal` in any accounting code.

| Term | Meaning | Never |
|---|---|---|
| instrument | Anything that can be traded: a stock, ETF, option contract, or event contract. | asset, security, ticker |
| symbol | The string that identifies an instrument, such as `"SPY"`. | ticker |
| position | How much of one instrument is held at a point in time. | holding |
| order | A simulated instruction to buy or sell. Simulated only, never sent anywhere. | |
| fill | A simulated execution of an order: quantity, price, time, and cost. | execution |
| cost | The umbrella for everything a trade loses: fees + spread + slippage + currency conversion. | friction |
| thesis | A written, testable claim, one file in `research/`. | hypothesis |
| signal | A value, computed only from data knowable at time t, that suggests a trade. | indicator, alpha |
| strategy | Rules that turn signals into simulated orders. | system, algo |
| backtest | A simulation of a strategy over historical data, with full costs. | |
| run | One execution of a backtest with fixed inputs and a recorded result. | trial |

### Talking to the user

- Explain like they're smart but new to the domain. Their background is software engineering.
- Define every finance or statistics term the first time it appears in a message.
- No undefined acronyms. Short sentences.

## Where things go

| Path | Holds |
|---|---|
| `src/market_workbench/core/` | Shared types for the vocabulary above. |
| `src/market_workbench/data/` | Fetching and storing market data, through read-only APIs. |
| `src/market_workbench/costs/` | Everything that computes a cost. |
| `src/market_workbench/backtest/` | Simulating strategies over historical data. |
| `src/market_workbench/evaluation/` | Measuring results: returns, risk, statistical significance. |
| `scripts/` | One-off experiments, one script each. Run with `just run <name>`. |
| `tests/` | Pytest tests. |
| `research/` | Theses, one file each. |

The only allowed `.md` files: `AGENTS.md`, `CLAUDE.md`, `README.md`, `ROADMAP.md`,
`research/_template.md`, `research/YYYY-MM-DD-short-slug.md`, `.claude/agents/*.md`.

## Commands

- `just`: list every recipe.
- `just setup`: install Python and the dev tools into `.venv`.
- `just check`: lint, format check, strict type check, tests. Must pass before every commit.
- `just fmt`: format the code and apply safe lint fixes.
- `just test [arguments]`: run pytest; arguments pass through, e.g. `just test -k costs`.
- `just run <name> [arguments]`: execute `scripts/<name>.py`. Here "run" is the everyday
  verb, not a backtest run.

## Research theses

- One file per thesis: `research/YYYY-MM-DD-short-slug.md`, copied from
  `research/_template.md`. Max 40 lines.
- Status moves from `idea` to `testing`, then to `rejected` or `adopted`.
- Rejected theses stay in the repo. They record what didn't work and why.
- A Result only counts if it comes from a backtest with full costs.

## Dashboard (future, don't build yet)

- TypeScript. Dense and information-first, like a professional trading terminal.
- Neutral palette, one accent color, tabular numbers.
- No gradients, glassmorphism, emoji, hero sections, or generic card grids.
