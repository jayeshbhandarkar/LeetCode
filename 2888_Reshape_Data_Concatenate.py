import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    concatenated_df = pd.concat([df1, df2], axis=0, ignore_index=True)
    return concatenated_df
