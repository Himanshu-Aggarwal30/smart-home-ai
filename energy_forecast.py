import pandas as pd
from sklearn.linear_model import LinearRegression


def forecast_energy(data):

    # ensure dataframe exists
    if data is None or data.empty:
        return pd.DataFrame()

    # ensure Energy column exists
    if "Energy" not in data.columns:
        return pd.DataFrame()

    df = data.copy()

    # remove invalid rows
    df = df.dropna(subset=["Energy"])

    # need minimum rows for regression
    if len(df) < 3:
        return pd.DataFrame()

    # create time index
    df["Time"] = range(len(df))

    X = df[["Time"]]
    y = df["Energy"]

    model = LinearRegression()
    model.fit(X, y)

    # future timeline
    future_time = list(range(len(df), len(df) + 24))

    future_df = pd.DataFrame({
        "Time": future_time
    })

    predictions = model.predict(future_df)

    predictions = [max(0, round(float(p), 2)) for p in predictions]

    forecast_df = pd.DataFrame({
        "Time": future_time,
        "Energy": predictions
    })

    return forecast_df