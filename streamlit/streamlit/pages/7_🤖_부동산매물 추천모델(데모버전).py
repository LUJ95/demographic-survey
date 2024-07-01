# -*- coding: utf-8 -*-

# 패키지 모음

import streamlit as st
import geopandas as gpd
import plotly.express as px
import geopandas as gpd


#%%

# 페이지 기본 설정
st.set_page_config(page_title="서울특별시 부동산 매물 추천", page_icon=":robot_face:", layout="wide")
st.header(":robot_face: 부동산매물 추천모델(데모버전)")
st.subheader("👨‍💼👩‍💼개인 맞춤형 서울 아파트 매물🏘️을 추천해 드립니다.")
st.subheader("좌측 메뉴에서 🗺️지역 및 선호인프라🚉🏫🏥🏬🌳를 선택해주세요.")

#%%

# 메뉴 : 사이드바
st.sidebar.header("메뉴")
region = st.sidebar.selectbox("지역선택", ["선택해 주세요", '종로구', '중구', '용산구', '성동구', '광진구', '동대문구', '중랑구', '성북구', '강북구', '도봉구',
                                     '노원구', '은평구', '서대문구', '마포구', '양천구', '강서구', '구로구', '금천구', '영등포구', '동작구'
                                     '관악구', '서초구', '강남구', '송파구', '강동구'])
infra = st.sidebar.selectbox("선호인프라", ["선택해 주세요", '지하철', '초등학교', '중학교', '고등학교', '슈퍼마켓', '종합병원', '공원'])

#%%

# GeoJSON 파일 경로
geojson_path = '서울구별지도_SIG_5179.geojson'

# # GeoJSON 파일 읽기
gdf = gpd.read_file(geojson_path)

# # 좌표계를 EPSG:4326으로 변환
gdf = gdf.to_crs(epsg=4326)

# # 변환된 GeoJSON 데이터 저장
gdf.to_file('서울특별시_SIG_2022_wgs84.geojson', driver='GeoJSON')

# 변환된 GeoJSON 파일 경로
geojson_path = '서울특별시_SIG_2022_wgs84.geojson'

# GeoJSON 데이터 읽기
gdf = gpd.read_file(geojson_path)

# GeoDataFrame의 GeoJSON 형식 확인
geojson_data = gdf.__geo_interface__

# Plotly Express를 사용하여 대한민국 지도 그리기
fig = px.choropleth_mapbox(
    gdf,
    geojson=geojson_data,
    locations='SIG_KOR_NM',
    featureidkey='properties.SIG_KOR_NM',
    color='SIG_KOR_NM',
    hover_name='SIG_KOR_NM',
    mapbox_style="carto-positron",
    center={"lat": 37.5665, "lon": 126.9780},
    zoom=10,
    opacity=0.5,
    height= 600,  # 지도 높이 설정
    width= 800  # 지도 너비 설정
)

# 지도 레이아웃 설정
fig.update_layout(
    title="서울특별시 구별 지도",
    title_font_size=24,
    margin={"r":0,"t":0,"l":0,"b":0}
)

# Streamlit에 Plotly 지도 표시
st.plotly_chart(fig, use_container_width=True)
