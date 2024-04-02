import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Penguins Explorer",
    page_icon="🐧",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None
)
df = pd.read_csv('https://raw.githubusercontent.com/mcnakhaee/palmerpenguins/master/palmerpenguins/data/penguins.csv')


bill_length_slider = st.slider(
    "Bill Length(mm)",
    min(df["bill_length_mm"]),
    max(df["bill_length_mm"])
)

df = df[df["bill_length_mm"] > bill_length_slider]

species_filter = st.selectbox("Species", df["species".unique()])
df = df[df["species"]] == species_filter

islands_filter = st.multiselect("Island", df["island"].unique())
df = df[df["island"]] == islands_filter

st.write(df.head())

