# project/src/utils.py
import re
import numpy as np
import pandas as pd

def to_snake(name: str) -> str:
    """Convert a label to snake_case."""
    s = re.sub(r"[^0-9a-zA-Z]+", "_", name.strip())
    s = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s)
    return re.sub(r"_+", "_", s).lower().strip("_")

def clean_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Return a copy with snake_case column names."""
    return df.rename(columns={c: to_snake(c) for c in df.columns})

def zscore(series: pd.Series, ddof: int = 0) -> pd.Series:
    """Standardize a numeric series to Z-scores."""
    mu = series.mean()
    sigma = series.std(ddof=ddof)
    if pd.isna(sigma) or sigma == 0:
        return pd.Series([pd.NA] * len(series), index=series.index, dtype="float")
    return (series - mu) / sigma
