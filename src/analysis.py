"""Reusable feature-building utilities for the robot predictive-maintenance project."""
import numpy as np
import pandas as pd

def add_features(df):
    df=df.copy()
    df["relative_time_s"]=df["time"]-df["time"].iloc[0]
    df["time_frac"]=np.arange(len(df))/max(len(df)-1,1)
    for col in ["temperature","voltage","position"]:
        df[f"{col}_roll_mean20"]=df[col].rolling(20,min_periods=1).mean()
        df[f"{col}_roll_std20"]=df[col].rolling(20,min_periods=2).std().fillna(0)
        df[f"{col}_delta20"]=df[col]-df[col].shift(20)
    return df
