import streamlit as st
import pandas as pd
from firebase_config import get_database

import datetime

def save_energy(room, energy):

    db = get_database()

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    db.child("energy_logs").push({
        "Room": room,
        "Energy": energy,
        "Timestamp": timestamp
    })


@st.cache_data
def load_energy():

    db = get_database()

    data = db.child("energy_logs").get()

    if data is None:
        return pd.DataFrame(columns=["Room","Energy"])

    if isinstance(data, dict):
        records = list(data.values())

    elif hasattr(data, "each"):
        records = [item.val() for item in data.each()]

    else:
        return pd.DataFrame(columns=["Room","Energy"])

    df = pd.DataFrame(records)

    if df.empty:
        return pd.DataFrame(columns=["Room","Energy"])
    
    df = pd.DataFrame(records)

    if "Timestamp" in df.columns:
        df["Timestamp"] = pd.to_datetime(df["Timestamp"])

    # normalize column names
    df.columns = [c.capitalize() for c in df.columns]

    if "Room" not in df.columns or "Energy" not in df.columns:
        return pd.DataFrame(columns=["Room","Energy"])

    return df