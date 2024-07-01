# -*- coding: utf-8 -*-

# 패키지 모음

import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings
import geopandas as gpd
import matplotlib.pyplot as plt
import json

#%%

# 제목
warnings.filterwarnings('ignore')
st.set_page_config(page_title="지역별 부동산 가격지수", page_icon=":house_buildings:", layout="wide")
st.title(":house_buildings:지역별 부동산 가격지수")
st.markdown('<style>div.block-container{padding-top:3rem;}</style>',unsafe_allow_html=True)

# 2013 ~ 2023년 시/도별 합산 순이동인구
data = {'region': ['서울특별시', '부산광역시', '대구광역시', '인천광역시', '광주광역시', '대전광역시', '울산광역시',
                   '세종특별자치시', '경기도', '강원도', '충청북도', '충청남도', '전라북도', '전라남도', '경상북도',
                   '경상남도', '제주특별자치도'],
    'value': [-961881, -204509, -156889, 99883, -69573, -112542, -80361, 253787, 1188218, 29813, 37895, 116883, -69603,
              -38422, -55470, -59603, 82374]}

# df으로 변환
df = pd.DataFrame(data)

# df 열 이름 수정(기존 'region', 'value')
df.columns = ['지역', '인구순이동']

# "지역 "데이터프레임을 리스트형으로 변경
region = df["지역"].tolist()

# 사이드바
st.sidebar.header("메뉴")
search_term = st.sidebar.text_input("검색")
region = st.sidebar.selectbox("지역", region)
page = st.sidebar.selectbox("주택 유형", ["선택", "아파트"])
internal_variable1 = st.sidebar.selectbox("인프라", ["선택", "교통", "건강", "안전", "교육", "여가"])
internal_variable2 = st.sidebar.selectbox("가구구성", ["선택", "1인가구", "2인가구", "3인가구", "4인가구", "4인가구 이상"])
dependent_variable = st.sidebar.selectbox("주택", ["선택", "추천매물1", "추천매물2", "추천매물3"])

# 시/도 지도 불러오기
geojson = 'SIDO_MAP_2022.json'
gdf = gpd.read_file(geojson)

# GeoDataFrame의 GeoJSON 형식 확인
geojson_data = gdf.__geo_interface__

# Plotly Express를 사용하여 대한민국 지도 그리기
fig = px.choropleth_mapbox(
    df,
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
if search_term in df['지역'].tolist():
    # 검색어에 해당하는 지역의 데이터를 가져와서 표시
    region_value = df.loc[df['지역'] == search_term, '인구순이동'].values[0]
    st.markdown(f"<div class='content'>{search_term}의 순이동자수: {region_value}</div>", unsafe_allow_html=True)

    # 해당 지역의 지도를 확대해서 표시
    fig.update_geos(fitbounds="locations", visible=True)

# Plotly 그래프를 Streamlit에 표시
st.plotly_chart(fig, use_container_width=True)

#%%

# 2013년 01월 ~ 2023년 12월 아파트 매매 실거래 지수
df2 = pd.read_excel("아파트_실거래가_지수.xlsx")

# 꺾은선 그래프 그리기
fig, ax = plt.subplots()
ax.plot(df2['일자'], df2['전국'], marker='o')

# 그래프 제목 및 라벨 설정
ax.set_title('전국 아파트 실거래가격지수')
ax.set_xlabel('연월')
ax.set_ylabel('실거래가격지수')

# Streamlit에 그래프 표시
st.pyplot(fig)

#%%


