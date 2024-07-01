# -*- coding: utf-8 -*-

# 패키지 모음

import streamlit as st
from tkinter.tix import COLUMN
from pyparsing import empty
from PIL import Image
import altair as alt
import plotly.express as px
import pandas as pd
import os
import warnings
import geopandas as gpd
import matplotlib.pyplot as plt
import json

#%%

# 페이지 기본 설정
st.set_page_config(page_title="서울특별시 부동산 가격지수", page_icon=":house_buildings:", layout="wide")

#- 페이지 컬럼 분할
cols = st.columns((1, 1, 2))
cols[0].metric("서울특별시")

# 페이지 헤더, 서브헤더 제목 설정
st.header("본인이 원하는 부동산 매물을 추천드립니다.:cityscape:")
st.subheader("")
warnings.filterwarnings('ignore')
st.title(":house_buildings:서울특별시 부동산 가격지수 (2013년 1월 ~ 2023년 12월)")
st.markdown('<style>div.block-container{padding-top:3rem;}</style>',unsafe_allow_html=True)

#%%

# 사이드바
st.sidebar.header("메뉴")
search_term = st.sidebar.text_input("검색")
# region = st.sidebar.selectbox("지역", region)
page = st.sidebar.selectbox("주택 유형", ["선택", "아파트"])
internal_variable1 = st.sidebar.selectbox("인프라", ["선택", "교통", "건강", "안전", "교육", "여가"])
internal_variable2 = st.sidebar.selectbox("가구구성", ["선택", "1인가구", "2인가구", "3인가구", "4인가구", "4인가구 이상"])
dependent_variable = st.sidebar.selectbox("주택", ["선택", "추천매물1", "추천매물2", "추천매물3"])

#%%

# 2013 ~ 2023년 서울특별시 아파트 실거래가 지수 추이

# 데이터 읽기
df = pd.read_excel("아파트_실거래가_지수.xlsx")

# '일자'와 '전국'열만 포함한 데이터프레임 생성

chart_data = df[['일자', '서울특별시']]
st.line_chart(chart_data.set_index('일자'))

#%%




#%%
# 서울특별시 25개 구
data = {'region': ['서울특별시'],'value': [1]}

# df으로 변환
df2 = pd.DataFrame(data)

# df 열 이름 수정(기존 'region', 'value')
df2.columns = ['지역', '인구순이동']

# "지역 "데이터프레임을 리스트형으로 변경
region = df2["지역"].tolist()

# 시/도 지도 불러오기
geojson = 'SEOUL_MAP_2022.json'
gdf = gpd.read_file(geojson)

# GeoDataFrame의 GeoJSON 형식 확인
geojson_data = gdf.__geo_interface__

# Plotly Express를 사용하여 대한민국 지도 그리기
fig = px.choropleth_mapbox(
    df2,
    geojson=geojson_data,
    locations='지역',
    featureidkey='properties.CTP_KOR_NM',
    color='인구순이동',
    hover_name='지역',
    title="대한민국 시/도별 인구순이동 지도",
    mapbox_style="carto-positron",  # 지도 스타일 설정
    center={"lat": 37.5, "lon": 127},  # 지도 중심 위치 설정
    zoom=6.5,  # 지도 줌 레벨 설정
    opacity=0.7,  # 지도 투명도 설정
    height=600,  # 지도 높이 설정
    width=800,  # 지도 너비 설정
)

fig.update_layout(
    title_font_size=32  # 그래프 제목의 글씨 크기 조정
)

# 지역 윤곽선 설정
fig.update_geos(
    visible=True,  # 지역 윤곽선을 보이게 설정
    showcountries=False,  # 국가 경계선은 보이지 않게 설정
    showcoastlines=False,  # 해안선은 보이지 않게 설정
    projection_type='mercator'  # 투영 방식 설정
)

# 검색어에 따라 지도를 확대하고 해당 지역의 값 표시
if search_term in df2['지역'].tolist():
    # 검색어에 해당하는 지역의 데이터를 가져와서 표시
    region_value = df2.loc[df['지역'] == search_term, '인구순이동'].values[0]
    st.markdown(f"<div class='content'>{search_term}의 순이동자수: {region_value}</div>", unsafe_allow_html=True)

    # 해당 지역의 지도를 확대해서 표시
    fig.update_geos(fitbounds="locations", visible=True)

# Plotly 그래프를 Streamlit에 표시
st.plotly_chart(fig, use_container_width=True)

