from __future__ import annotations
from typing import Iterable, Optional, Literal
import numpy as np
import pandas as pd

NumCols = Optional[Iterable[str]]
ByAxis = Literal["row", "col"]
NormMethod = Literal["zscore", "minmax"]


def _num_cols(df: pd.DataFrame, cols: NumCols = None) -> list[str]:
    if cols is None:
        return df.select_dtypes(include="number").columns.tolist()
    return [c for c in cols if pd.api.types.is_numeric_dtype(df[c])]


def fill_missing_median(df: pd.DataFrame, cols: NumCols = None) -> pd.DataFrame:
    out = df.copy()
    use = _num_cols(out, cols)
    med = out[use].median(numeric_only=True)
    out[use] = out[use].fillna(med)
    return out


def drop_missing(
    df: pd.DataFrame,
    by: ByAxis = "row",
    how: Literal["any", "all"] = "any",
    thresh_frac: float | None = None,
    subset: Iterable[str] | None = None,
) -> pd.DataFrame:
    out = df.copy()
    if thresh_frac is not None:
        if not 0 <= thresh_frac <= 1:
            raise ValueError("thresh_frac must be in [0,1]")
        if by == "row":
            thresh = int(np.ceil(thresh_frac * out.shape[1]))
            return out.dropna(axis=0, thresh=thresh, subset=subset)
        else:
            thresh = int(np.ceil(thresh_frac * out.shape[0]))
            return out.dropna(axis=1, thresh=thresh)
    axis = 0 if by == "row" else 1
    return out.dropna(axis=axis, how=how, subset=subset if by == "row" else None)


def normalize_data(
    df: pd.DataFrame,
    cols: NumCols = None,
    method: NormMethod = "zscore",
    clip_minmax: tuple[float, float] | None = None,
) -> pd.DataFrame:
    out = df.copy()
    use = _num_cols(out, cols)
    if not use:
        return out

    if method == "zscore":
        m = out[use].mean(numeric_only=True)
        s = out[use].std(ddof=0, numeric_only=True).replace(0, np.nan)
        out[use] = (out[use] - m) / s
    elif method == "minmax":
        lo = out[use].min(numeric_only=True)
        hi = out[use].max(numeric_only=True)
        rng = (hi - lo).replace(0, np.nan)
        out[use] = (out[use] - lo) / rng
    else:
        raise ValueError("method must be 'zscore' or 'minmax'")

    if clip_minmax:
        lo, hi = clip_minmax
        out[use] = out[use].clip(lower=lo, upper=hi)

    return out
