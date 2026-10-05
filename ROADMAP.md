# Roadmap

## Current state
- Infrastructure only: tooling, rules, 7 subagent definitions, and an empty Python package.
- The package `market_workbench` has empty subpackages: core, data, costs, backtest, evaluation.
- A smoke test and a repo-rules test (no notebooks, no stray `.md` files) run.
- `just check` passes on the empty skeleton.
- No market data, cost, backtest, or strategy code exists yet.

## Now
Infrastructure done. Nothing in progress: pick a first milestone from Next.

## Next
1. Cost model. One place that computes the full cost of a simulated trade for each
   instrument type. Parts: commission (the broker's fee), exchange and regulatory fees,
   bid-ask spread (the gap between the best buy price and the best sell price, which you
   pay to cross), slippage (the price moving against you between decision and fill),
   contract-specific fees, and conversion between Canadian dollars (CAD) and US dollars (USD).
   All in `Decimal`, Python's exact decimal number type, so money has no rounding drift.
2. Kalshi market data. A read-only fetcher for event-contract prices and history. An event
   contract is a bet that pays out if a stated event happens. Step zero: confirm which
   prediction markets you can legally trade from Québec, since trades are placed by hand.
3. Equities and options data vendor comparison. A thesis-researcher report comparing vendors
   on price, history depth, options coverage, and request limits of their programming
   interfaces. An option is a contract giving the right to buy or sell a stock at a set
   price. No code.
4. Core types. Instrument, position, order, and fill as typed classes, with timestamps in
   UTC (the universal time standard, no local time zones) and `Decimal` money.

## Later
- Backtest engine: simulated orders become fills with full costs.
- Evaluation: returns, risk, and whether a result is statistically real or just luck.
- TypeScript dashboard.

## Parked
Nothing yet.
