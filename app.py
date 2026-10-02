import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.set_page_config(layout="wide")

df = pd.read_csv("India_census.csv")
list_of_States = list(df["State"].unique())
list_of_States.insert(0, "Overall India")

st.sidebar.title("India Data Explorer")
Selected_state = st.sidebar.selectbox("Select a State", list_of_States)
primary = st.sidebar.selectbox("Select Primary Parameter", sorted(df))
secondary = st.sidebar.selectbox("Select Seconday Paramter", sorted(df))


plot = st.sidebar.button("Plot Graph")

if plot:

    st.text('Size Reprsents the Primary data')
    st.text("Color represents the secondary data")

    if Selected_state == "Overall India":
        fig = px.scatter_map(
            df,
            lat="Latitude",
            lon="Longitude",
            zoom=4,
            size=primary,
            color=secondary,
            size_max=35,
            color_continuous_scale="Plasma",
            map_style="carto-positron",
            width=1200,
            height=700,
            hover_name="District",
        )

        st.plotly_chart(fig,use_container_width=True)

    else:
        state_df = df[df['State'] == Selected_state]
        fig = px.scatter_map(
            state_df,
            lat="Latitude",
            lon="Longitude",
            zoom=6,
            size=primary,
            color=secondary,
            size_max=35,
            color_continuous_scale="Plasma",
            map_style="carto-positron",
            width=1200,
            height=700,
            hover_name="District",
        )

        st.plotly_chart(fig,use_container_width=True)
