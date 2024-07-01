
# -*- coding: utf-8 -*-

# 패키지 모음
import streamlit as st
import geopandas as gpd
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import os

# 페이지 기본 설정
st.set_page_config(page_title="대전광역시 및 서울특별시 지도 및 라인 그래프", page_icon=":earth_asia:", layout="wide")
st.header("대전광역시 및 서울특별시 지도 및 라인 그래프")
st.subheader("대전광역시와 서울특별시의 지도를 보여주고, 옆에 라인 그래프를 표시합니다.")

# 컬럼 분할
col1, col2 = st.columns((1, 1))

with col1:
    # 대전광역시 및 서울특별시 데이터
    data1 = {'region': ['대전광역시', '세종특별자치시'], 'value': [1, 2]}
    df1 = pd.DataFrame(data1)

    # 시/도 지도 불러오기
    geojson1 = '대전광역시_SIG_2022.geojson'
    geojson2 = '세종특별자치시_SIG_2022.geojson'

    gdf1 = gpd.read_file(geojson1)
    gdf2 = gpd.read_file(geojson2)
        
    # 두 GeoDataFrame 결합
    gdf_combined = gpd.GeoDataFrame(pd.concat([gdf1, gdf2], ignore_index=True))
        
    geojson_data = gdf_combined.__geo_interface__

    # Plotly Express를 사용하여 대한민국 지도 그리기
    fig = px.choropleth_mapbox(
        df1,
        geojson=geojson_data,
        locations='region',
        featureidkey='properties.CTP_KOR_NM',
        color='region',
        title="대전광역시 및 세종특별자치시",
        mapbox_style="carto-positron",  # 지도 스타일 설정
        center={"lat": 36.5, "lon": 127},  # 지도 중심 위치 설정
        zoom=6.5,  # 지도 줌 레벨 설정
        opacity=0.7,  # 지도 투명도 설정
        height=600,  # 지도 높이 설정
        width=800  # 지도 너비 설정
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

    st.plotly_chart(fig)

with col2:
    df = pd.read_excel("아파트_실거래가_지수.xlsx")
    # Plotly를 사용하여 라인 그래프 그리기
    line_fig = go.Figure()
        
    # 대전광역시 데이터 추가
    line_fig.add_trace(go.Scatter(
        x=df['일자'],
        y=df['대전광역시'],
        mode='lines+markers',
        name='대전'
        ))

    # 서울특별시 데이터 추가
    line_fig.add_trace(go.Scatter(
        x=df['일자'],
        y=df['세종특별자치시'],
        mode='lines+markers',
        name='세종'
        ))
    
    # 레이아웃 업데이트
    line_fig.update_layout(
        title={
            'text': '대전 및 세종 아파트 실거래가격지수 추이 (2013.01 ~ 2023.12)',
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {
                'size': 24  # 타이틀 폰트 크기 설정
            }
        },
        xaxis_title={
            'text': '연월',
            'font': {
                'size': 18  # x축 제목 폰트 크기 설정
            }
        },
        yaxis_title={
            'text': '가격지수',
            'font': {
                'size': 18  # y축 제목 폰트 크기 설정
            }
        },
        legend={
            'font': {
                'size': 16  # 레전드 폰트 크기 설정
            }
        },
        height=600,
        width=800
    )
    st.plotly_chart(line_fig)
