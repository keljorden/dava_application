import pandas as pd

def clean(clean_strategie: str, col: pd.Series) -> pd.Series:

    if "dropna" in clean_strategie:
        return col.dropna()
    elif "fillna(0)" in clean_strategie:
        return col.fillna(0)
    elif "ffill" in clean_strategie:
        return col.ffill()
    elif "Interpolate" in clean_strategie:
        if pd.api.types.is_numeric_dtype(col):
            return col.interpolate(method='linear')
        else:
            return col.ffill()
    return col