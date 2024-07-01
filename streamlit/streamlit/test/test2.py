# -*- coding: utf-8 -*-

# 패키지 모음
import streamlit as st
import geopandas as gpd
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import os

# 페이지 기본 설정
st.set_page_config(page_title="대전광역시 지도 및 라인 그래프", page_icon=":earth_asia:", layout="wide")
st.header("대전광역시 지도 및 라인 그래프")
st.subheader("대전광역시의 지도를 보여주고, 옆에 라인 그래프를 표시합니다.")

# 컬럼 분할
col1, col2 = st.columns((2, 1))
col3, col4 = st.columns((2, 1))

with col1:
    # 서울특별시 구별 행정단위
    data1 = {'region': ['대전광역시']}
    # df으로 변환
    df1 = pd.DataFrame(data1)

    # 시/도 지도 불러오기
    geojson = '대전광역시_SIG_2022.geojson'
    if not os.path.exists(geojson):
        st.error(f"GeoJSON 파일이 존재하지 않습니다: {geojson}")
    else:
        gdg = gpd.read_file(geojson)
        geojson_data = gdg.__geo_interface__

        # Plotly Express를 사용하여 대한민국 지도 그리기
        fig = px.choropleth_mapbox(
            df1,
            geojson=geojson_data,
            locations='region',
            featureidkey='properties.CTP_KOR_NM',
            title="대전광역시",
            mapbox_style="carto-positron",  # 지도 스타일 설정
            center={"lat": 36.35, "lon": 127.38},  # 지도 중심 위치 설정
            zoom=10,  # 지도 줌 레벨 설정
            opacity=0.7,  # 지도 투명도 설정
            height=600,  # 지도 높이 설정
            width=600,  # 지도 너비 설정
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
    # 라인 그래프 데이터
    line_data = {
        "년도": [2015, 2016, 2017, 2018, 2019, 2020, 2021],
        "인구수": [1500000, 1550000, 1600000, 1580000, 1570000, 1560000, 1550000]
    }

    df_line = pd.DataFrame(line_data)

    # Plotly를 사용하여 라인 그래프 그리기
    line_fig = go.Figure()

    line_fig.add_trace(go.Scatter(
        x=df_line['년도'],
        y=df_line['인구수'],
        mode='lines+markers',
        name='인구수'
    ))

    line_fig.update_layout(
        title='대전광역시 인구수 변화',
        xaxis_title='년도',
        yaxis_title='인구수',
        height=600,
        width=400
    )

    st.plotly_chart(line_fig)

