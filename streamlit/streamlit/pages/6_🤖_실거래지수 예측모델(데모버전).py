# -*- coding: utf-8 -*-

# 패키지 모음

import streamlit as st
import geopandas as gpd
import plotly.express as px
import geopandas as gpd
from datetime import datetime

#%%

# 페이지 기본 설정
st.set_page_config(page_title="부동산 실거래지수 예측", page_icon=":robot_face:", layout="wide")
st.header(":robot_face: 미래 부동산 실거래지수 예측모델(데모버전)")
st.subheader("미래의 🏘️아파트 📈실거래지수를 알려드립니다.")
st.subheader("좌측 메뉴에서 🗺️지역 및 📆연월을 선택해 주세요.")

#%%

# 년도와 월을 선택할 수 있는 범위 설정
years = list(range(2024, datetime.now().year + 50))
months = list(range(1, 13))

#%%

# 컬럼 분할

col1, col2, col3 = st.columns((1, 1, 1))

#%%
# 메뉴 : 사이드바
st.sidebar.header("메뉴")
region = st.sidebar.selectbox("지역", ["선택해 주세요", '서울특별시', '부산광역시', '대구광역시', '인천광역시', '광주광역시', '대전광역시', '울산광역시',
                                     '세종특별자치시', '경기도', '강원도', '충청북도', '충청남도', '전라북도', '전라남도', '경상북도',
                                     '경상남도', '제주특별자치도'])

start_year = st.sidebar.selectbox("시작연도", years)
start_month = st.sidebar.selectbox("시작 월", months)

end_year = st.sidebar.selectbox("종료연도", years)
end_month = st.sidebar.selectbox("종료 월", months)

# 선택된 년월을 날짜 형식으로 변환
start_date = datetime(start_year, start_month, 1)
end_date = datetime(end_year, end_month, 1)

# 선택된 지역, 시작 날짜와 종료 날짜 표시

with col1:
    st.markdown(f"<h4>지역: {region}</h3>", unsafe_allow_html=True)

with col2:
    st.markdown(f"<h4>시작 연월: {start_date.strftime('%Y-%m')}</h3>", unsafe_allow_html=True)

with col3:
    st.markdown(f"<h4>종료 연월: {end_date.strftime('%Y-%m')}</h3>", unsafe_allow_html=True)

