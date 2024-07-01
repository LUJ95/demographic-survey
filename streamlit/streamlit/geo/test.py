import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

st.set_page_config(
    page_title="Multipage App",
    page_icon="🏘️"
)

st.title("나")
st.sidebar.success("아래 페이지를 선택하세요.")
