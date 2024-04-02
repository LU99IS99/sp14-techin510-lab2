import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Penguins Explorer",
    page_icon="🐧",
    layout="centered",
)

st.title("🐧 Penguins Exploer")

st.markdown("""
## observations""")
            
df = pd.read_csv('https://raw.githubusercontent.com/mcnakhaee/palmerpenguins/master/palmerpenguins/data/penguins.csv')

with st.sidebar:
    # Input filter options
    bill_length_slider = st.slider(
        "Bill Length(mm)",
        min(df["bill_length_mm"]),
        max(df["bill_length_mm"])
    )
    species_filter = st.selectbox(
        "Species",
        df["species"].unique(),
        index=None
    )
    islands_filter = st.multiselect("Island", df["island"].unique())


df = df[df["bill_length_mm"] > bill_length_slider]


with st.expander("RAW Data"):
    st.write(df)

#Filter data
if islands_filter:
   df = df[df["island"].isin(islands_filter)]
if species_filter:
   df = df[df["species"] == species_filter]
df = df[df["bill_length_mm"] > bill_length_slider]

with st.expander("RAW Data"):
   st.write(df)

fig = px.histogram(
   df,
   x="bill_length_mm"
)

fig2 = px.scatter(
   df,
   y="bill_length_mm"
)

st.write(df.head())