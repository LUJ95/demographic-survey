# -*- coding: utf-8 -*-

# 패키지 모음

import streamlit as st
import pandas as pd

#%%

# 페이지 기본 설정
st.set_page_config(page_title="DAPT_도시양극화_프로젝트", page_icon=":cityscape:", layout="wide")
st.subheader("🙋‍♂️제3차 미니프로젝트🙋‍♀️")
st.markdown('<span style="font-size: 40px;">1. 대전/세종/충남/충북 도시양극화 분석 및 미래전망</span>', unsafe_allow_html=True)
st.markdown('<span style="font-size: 40px;">2. 개인 맞춤형 서울 아파트 매물 추천</span>', unsafe_allow_html=True)

#%%

# 메뉴 : 사이드바

st.sidebar.text_input("검색")
