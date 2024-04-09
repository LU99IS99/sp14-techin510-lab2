# import streamlit as st
# import pandas as pd
# import plotly.express as px

# st.set_page_config(
#     page_title="Penguins Explorer",
#     page_icon="🐧",
#     layout="centered",
# )

# st.title("🐧 Penguins Exploer")

# st.markdown("""
# ## observations""")
            
# df = pd.read_csv('https://raw.githubusercontent.com/mcnakhaee/palmerpenguins/master/palmerpenguins/data/penguins.csv')

# with st.sidebar:
#     # Input filter options
#     bill_length_slider = st.slider(
#         "Bill Length(mm)",
#         min(df["bill_length_mm"]),
#         max(df["bill_length_mm"])
#     )
#     species_filter = st.selectbox(
#         "Species",
#         df["species"].unique(),
#         index=None
#     )
#     islands_filter = st.multiselect("Island", df["island"].unique())


# df = df[df["bill_length_mm"] > bill_length_slider]


# with st.expander("RAW Data"):
#     st.write(df)

# #Filter data
# if islands_filter:
#    df = df[df["island"].isin(islands_filter)]
# if species_filter:
#    df = df[df["species"] == species_filter]
# df = df[df["bill_length_mm"] > bill_length_slider]

# with st.expander("RAW Data"):
#    st.write(df)

# fig = px.histogram(
#    df,
#    x="bill_length_mm"
# )

# fig2 = px.scatter(
#    df,
#    y="bill_length_mm"
# )

# st.write(df.head())
# Import libraries
import streamlit as st
import pandas as pd
import plotly.express as px

# Page configuration
st.set_page_config(page_title="Penguins Explorer", page_icon="🐧", layout="wide")

# Title and introduction
st.title("🐧 Penguins Explorer")
st.markdown("""
Explore the Palmer Penguins dataset. Use the sidebar to filter the data based on species, island, and bill length. 
Visualize the distribution and relationships within the data.
""")

# Load the dataset
df = pd.read_csv("https://raw.githubusercontent.com/mcnakhaee/palmerpenguins/master/palmerpenguins/data/penguins.csv")

# Sidebar for filters
with st.sidebar:
    st.header("Filter Options")
    species_filter = st.selectbox("Species", options=df["species"].unique(), index=0, key='species_filter')
    island_filter = st.multiselect("Island", options=df["island"].unique(), key='island_filter')
    bill_length_min, bill_length_max = st.slider("Bill Length (mm)", float(df["bill_length_mm"].min()), 
                                                 float(df["bill_length_mm"].max()), 
                                                 (float(df["bill_length_mm"].min()), 
                                                  float(df["bill_length_mm"].max())),
                                                 key='bill_length_slider')

# Filter the dataset based on the sidebar options
df_filtered = df[(df["species"] == species_filter) & 
                 (df["island"].isin(island_filter) if island_filter else df["island"]) &
                 (df["bill_length_mm"] >= bill_length_min) & 
                 (df["bill_length_mm"] <= bill_length_max)]

# Layout with columns for visualizations
col1, col2 = st.columns(2)

with col1:
    st.markdown("### Bill Length Distribution")
    fig = px.histogram(df_filtered, x="bill_length_mm")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.markdown("### Bill Length vs. Bill Depth")
    fig2 = px.scatter(df_filtered, x="bill_length_mm", y="bill_depth_mm", color="species")
    st.plotly_chart(fig2, use_container_width=True)

# Expander for raw data view
with st.expander("View Raw Data"):
    st.write(df_filtered)
