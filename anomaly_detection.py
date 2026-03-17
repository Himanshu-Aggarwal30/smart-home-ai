import pandas as pd
from sklearn.ensemble import IsolationForest


def detect_anomalies(data):

    # correct dataframe check
    if data is None or data.empty:
        return pd.DataFrame()

    df = data.copy()

    # ensure Energy column exists
    if "Energy" not in df.columns:
        return pd.DataFrame()

    if "Timestamp" in df.columns:
        df = df[["Timestamp","Energy"]]
    else:
        df = df[["Energy"]]

    # not enough data → mark all normal
    if len(df) < 5:
        df["anomaly"] = "Normal"
        return df

    model = IsolationForest(
        contamination=0.15,
        random_state=42
    )

    predictions = model.fit_predict(df[["Energy"]])

    df["anomaly"] = pd.Series(predictions).map({
        1: "Normal",
        -1: "Anomaly"
    })

    return df