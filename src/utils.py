import pandas as pd

def get_summary_stats(df: pd.DataFrame, group_col: str | None = None) -> pd.DataFrame:
    """
    Return summary statistics for numeric columns.
    If group_col is provided, compute per-group aggregates (mean, std, min, max, count).
    """
    num_df = df.select_dtypes(include="number")
    if group_col is None:
        return num_df.describe().T
    grouped = df.groupby(group_col)[num_df.columns]
    return grouped.agg(["mean", "std", "min", "max", "count"])

