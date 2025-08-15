# Stakeholder Context Memo — Next-Day VaR Nowcasting
**Audience:** Risk Team & PMs  
**Author:** Carolina Zhu  
**Date:** August 14, 2025

## Problem
Provide a **next-day 1% VaR** for a five-asset portfolio to inform **overnight position limits** and daily sizing. The number must be defensible, reproducible, and quick to compute before the close.

## Users & Decisions
- **Risk:** coverage diagnostics, breach alerts, reporting artifacts
- **PMs:** limit setting and exposure sizing for the next session

## Required Output
- VaR\_{0.01}(t+1) in % and $, timeline CSV, and top feature attributions
- Figures: violations plot, rolling coverage, and Pareto of risk drivers by asset

## Data & Constraints
- Inputs: EOD prices (SPY, TLT, GLD, HYG, DXY), corporate actions adjusted
- Features: 5–60d vol, correlations, rate/credit spreads, simple regime flags
- Assumptions: liquidity at close; stable mapping from features to risk on short horizons

## Validation & Success
- Target coverage 1.0% ± 0.2% over 250 trading days
- Kupiec LR test p ≥ 0.05; violation clustering monitored with Christoffersen conditional test (report only)

## Risks
- Regime shifts, stale proxies, structural breaks; will monitor and re-calibrate thresholds.
