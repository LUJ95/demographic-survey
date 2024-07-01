
import streamlit as st
import pandas as pd
import geopandas as gpd
import plotly.express as px
import plotly.graph_objs as go
import json
import os

# 페이지 기본 설정
st.set_page_config(page_title="📊종합", page_icon="📊종합", layout="wide")

st.subheader("📊종합")

# 2013 ~ 2023년 대전-세종 아파트 실거래 가격지수
# 데이터 읽기
df = pd.read_excel("아파트_실거래가_지수.xlsx")
wage_avg = pd.read_excel("월평균소득_종합.xlsx")
#%%

# 컬럼 분할

col1, col2 = st.columns((1, 1))


#%%

# 대전광역시 지도 및 꺾은선그래프

with col1:
    # 충청남도 및 충청북도 지도데이터
    data1 = {'region': ['대전광역시', '세종특별자치시', '충청남도', '충청북도'], 'value': [1, 2, 3, 4]}
    df1 = pd.DataFrame(data1)

    # 시/도 지도 불러오기
    geojson1 = '대전광역시_SIG_2022.geojson'
    geojson2 = '세종특별자치시_SIG_2022.geojson'
    geojson3 = '충청남도_SIG_2022.geojson'
    geojson4 = '충청북도_SIG_2022.geojson'

    gdf1 = gpd.read_file(geojson1)
    gdf2 = gpd.read_file(geojson2)
    gdf3 = gpd.read_file(geojson3)
    gdf4 = gpd.read_file(geojson4)
        
    # 두 GeoDataFrame 결합
    gdf_combined = gpd.GeoDataFrame(pd.concat([gdf1, gdf2, gdf3, gdf4], ignore_index=True))
        
    geojson_data = gdf_combined.__geo_interface__

    # Plotly Express를 사용하여 대한민국 지도 그리기
    fig = px.choropleth_mapbox(
        df1,
        geojson=geojson_data,
        locations='region',
        featureidkey='properties.CTP_KOR_NM',
        color='region',
        title="대전/세종/충남/충북 지도",
        mapbox_style="carto-positron",  # 지도 스타일 설정
        center={"lat": 36.5, "lon": 127},  # 지도 중심 위치 설정
        zoom=6.5,  # 지도 줌 레벨 설정
        opacity=0.7,  # 지도 투명도 설정
        height=600,  # 지도 높이 설정
        width=800  # 지도 너비 설정
        )

    fig.update_layout(
        title_font_size=30, # 그래프 제목 크기 조절
        legend={
            'font': {
                'size': 20 # 그래프 legend 크기 조절
            }
        }
        )
        # 지역 윤곽선 설정
    fig.update_geos(
        visible=True,  # 지역 윤곽선을 보이게 설정
        showcountries=False,  # 국가 경계선은 보이지 않게 설정
        showcoastlines=False,  # 해안선은 보이지 않게 설정
        projection_type='mercator'  # 투영 방식 설정
        )

    st.plotly_chart(fig)

#%%

with col2:
    # Plotly를 사용하여 라인 그래프 그리기
    line_fig = go.Figure()

    # 대전광역시 데이터 추가
    line_fig.add_trace(go.Scatter(
        x=df['일자'],
        y=df['대전광역시'],
        mode='lines+markers',
        name='대전'
        ))
    
    # 세종특별자치시 데이터 추가
    line_fig.add_trace(go.Scatter(
        x=df['일자'],
        y=df['세종특별자치시'],
        mode='lines+markers',
        name='세종'
        ))

    # 충청남도 데이터 추가
    line_fig.add_trace(go.Scatter(
        x=df['일자'],
        y=df['충청남도'],
        mode='lines+markers',
        name='충남'
        ))

    # 충청북도 데이터 추가
    line_fig.add_trace(go.Scatter(
        x=df['일자'],
        y=df['충청북도'],
        mode='lines+markers',
        name='충북'
        ))

    # 레이아웃 업데이트
    line_fig.update_layout(
        title={
            'text': '대전/세종/충남/충북 아파트 실거래가격지수 추이 비교(2013.01 ~ 2023.12)',
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {
                'size': 20  # 타이틀 폰트 크기 설정
            }
        },
        xaxis_title={
            'text': '연월',
            'font': {
                'size': 20  # x축 제목 폰트 크기 설정
            }
        },
        yaxis_title={
            'text': '가격지수',
            'font': {
                'size': 20  # y축 제목 폰트 크기 설정
            }
        },
        legend={
            'font': {
                'size': 20  # 레전드 폰트 크기 설정
            }
        },
        height=600,
        width=800
    )
    
    # x축과 y축의 수치 글씨 크기 설정
    fig.update_xaxes(tickfont=dict(size=20))
    fig.update_yaxes(tickfont=dict(size=20))
    
    st.plotly_chart(line_fig)
#%%
# 2023년도 지역별 월평균 임금 종합
# Plotly를 사용하여 막대 그래프 생성
fig = go.Figure()

# 첫 번째 데이터 추가
fig.add_trace(go.Bar(
    x= wage_avg['소득구간'],
    y= wage_avg['대전광역시'],
    name='대전',
    marker_color='skyblue',
    text=wage_avg['대전광역시'].round(0),
    textposition='outside',
    textfont=dict(size=20)
    ))

# 두 번째 데이터 추가
fig.add_trace(go.Bar(
    x= wage_avg['소득구간'],
    y= wage_avg['세종특별자치시'],
    name='세종',
    marker_color='dodgerblue',
    text=wage_avg['세종특별자치시'].round(0),
    textposition='outside',
    textfont=dict(size=20)
    ))

# 세 번째 데이터 추가
fig.add_trace(go.Bar(
    x= wage_avg['소득구간'],
    y= wage_avg['충청남도'],
    name='충남',
    marker_color='lightsalmon',
    text=wage_avg['충청남도'].round(0),
    textposition='outside',
    textfont=dict(size=20)
    ))
    
# 네 번째 데이터 추가
fig.add_trace(go.Bar(
        x= wage_avg['소득구간'],
        y= wage_avg['충청북도'],
        name='충북',
        marker_color='orangered',
        text=wage_avg['충청북도'].round(0),
        textposition='outside',
        textfont=dict(size=20)
        ))
    
# 레이아웃 업데이트
fig.update_layout(
title={
       'text': '대전/세종/충남/충북 월평균 소득구간 비율 비교',
       'y':0.9,
       'x':0.5,
       'xanchor': 'center',
       'yanchor': 'top',
       'font': {
           'size': 30  # 타이틀 폰트 크기 설정
       }
    },
    xaxis_title={
        'text': '소득구간',
        'font': {
            'size': 30  # x축 제목 폰트 크기 설정
        }
    },
    yaxis_title={
        'text': '비율(%)',
        'font': {
            'size': 30  # y축 제목 폰트 크기 설정
        }
    },
    legend={
        'font': {
            'size': 20  # 레전드 폰트 크기 설정
        }
    },
    barmode='group',  # 막대 그래프를 그룹으로 묶어서 비교
    height=600,
    width=1500
    )

# x축과 y축의 수치 글씨 크기 설정
fig.update_xaxes(tickfont=dict(size=20))
fig.update_yaxes(tickfont=dict(size=20))

# Streamlit에 그래프 표시
st.plotly_chart(fig)
