# Next-Day VaR Nowcasting for a Multi-Asset Portfolio
**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement
We aim to nowcast **next-day 1% Value-at-Risk (VaR)** for a five-asset liquid portfolio (SPY, TLT, GLD, HYG, DXY proxies). The goal is to provide a same-day risk number that the desk can use to set **position limits and overnight sizing**. Historical returns, realized volatility, and market regime features will be standardized into a defensible, reproducible VaR estimate with clear validation.

## Stakeholder & User
Primary users are the **risk team** and **PMs**. Risk needs coverage diagnostics for regulatory reporting; PMs need a number before the close to size exposure. Outputs must be drop-in compatible with the daily risk sheet and interpretable at a glance.

## Useful Answer & Decision
**Predictive**: a scalar VaR_{0.01}(t+1) in percent and dollars for today’s close, plus **explainability** (top feature attributions) and a table of **risk drivers by asset**. Deliverables include a CSV with the VaR timeline and a one-pager summary stored in `/docs/`.

## Assumptions & Constraints
- Assets are liquid; closing prices represent realizable marks.
- Features: rolling σ/β, term-structure spreads, simple regime flags; no latent factors beyond what can be justified.
- Data is end-of-day; no overnight news leakage modeling in Stage 01.
- Model must run < 1s on laptop-grade hardware; reproducible with pinned versions.

## Known Unknowns / Risks
- Regime breaks (e.g., macro events) degrade calibration.
- FX translation (DXY proxy) could mis-specify mixed-currency exposure.
- Serial correlation and heteroskedasticity require robust backtesting.

## Lifecycle Mapping
Goal → Stage → Deliverable  
- Decision-ready VaR → Problem Framing & Scoping (Stage 01) → stakeholder_memo.md  
- Clean feature set → Data Ingest & Engineering (Stage 02) → `src/features.py`, datasets in `/data/`  
- Calibrated model → Modeling & Validation (Stage 03) → VaR series + Kupiec LR test results  
- Communication → Handoff (Stage 04) → 1-pager and figures in `/docs/`

## Success Criteria
- **Unconditional coverage** within 0.8–1.2% on rolling 250-day window.
- **Kupiec LR test** p-value ≥ 0.05; violations clustered ratio not statistically excessive.
- Reproducible run: `python -m src.compute_var` regenerates the VaR CSV and figures.

## Repo Plan
`/data/` raw + processed • `/src/` reusable code • `/notebooks/` exploration and reports • `/docs/` memo/slide + figures. Weekly updates or upon material model/data change.
