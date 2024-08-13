import altair as alt
import streamlit as st
import pandas as pd

df=pd.read_csv('user_data_final.csv',encoding='utf-8')


st.header("Static site generators popularity  :thermometer: :star:")

"""
Static site generators (SSG) are open source tools to create blogs,
landing pages and documentation.
"""

st.header("Github stars")
"""
Number of stars in a Github repository is a proxy for SSG popularity,
at least among software developers.
"""

all_langs = df.columns


#st.altair_chart(chart, use_container_width=True)
