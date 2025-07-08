import os
import pandas as pd
import streamlit as st

st.title("📊 Daily Betting Predictions (70%+ Confidence)")

if not os.path.exists("predictions.csv"):
    st.warning("predictions.csv not found. Running aggregator...")
    import aggregate  # Run the aggregator script

try:
    df = pd.read_csv("predictions.csv")
    if df.empty:
        st.warning("No predictions meet the 70% threshold today.")
    else:
        st.dataframe(df)
except Exception as e:
    st.error(f"Something went wrong: {e}")