import streamlit as st
from PIL import Image
import pandas as pd
import geopandas as gpd
import plotly.express as px
import plotly.graph_objects as go
import os

#%%

# 페이지 기본 설정
st.set_page_config(page_title="인구순이동", page_icon="🚶‍♂️인구순이동", layout="wide")
st.subheader("🚶‍♂️2013 ~ 2023년 시/도별 합산 순이동인구")

#%%

# 데이터 생성
data = {
    '지역': ['서울특별시', '부산광역시', '대구광역시', '인천광역시', '광주광역시', '대전광역시', '울산광역시',
          '세종특별자치시', '경기도', '강원도', '충청북도', '충청남도', '전라북도', '전라남도', '경상북도'],
    '인구순이동': [-961881, -204509, -156889, 99883, -69573, -112542, -80361,
               253787, 1188218, 29813, 37895, 116883, -69603, -38422, -55470]
}

df = pd.DataFrame(data)

# Plotly 그래프 생성
fig = go.Figure()

# 막대 그래프 추가
fig.add_trace(go.Bar(
    x=df['지역'],
    y=df['인구순이동'],
    marker_color=['red' if val < 0 else 'blue' for val in df['인구순이동']],  # 인구순이동이 음수일 때는 빨간색, 양수일 때는 파란색
    text=(df['인구순이동'] / 10000).round(0),  # 막대에 텍스트로 값을 표시
    textposition='outside',  # 텍스트 위치 자동 설정
    textfont=dict(size=20),
    orientation='v',  # 세로 방향 막대 그래프 설정
    name='인구순이동',  # 범례에 표시될 이름 설정
))
# 레이아웃 업데이트
fig.update_layout(
    title={
        'text': '전국순이동(2013 ~ 2023년 합산)',
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': {
            'size': 30  # 타이틀 폰트 크기 설정
        }
    },
    xaxis_title={
        'text': '시도',
        'font': {
            'size': 25  # x축 제목 폰트 크기 설정
        }
    },
    yaxis_title={
        'text': '이동인구(단위: 만명)',
        'font': {
            'size': 25  # y축 제목 폰트 크기 설정
        }
    },
    legend={
        'font': {
            'size': 20  # 범례 폰트 크기 설정
        }
    },
    height=800,
    width=1400
)

# x축과 y축의 수치 글씨 크기 설정
fig.update_xaxes(tickfont=dict(size=25))
fig.update_yaxes(tickfont=dict(size=25))

# Streamlit에 그래프 표시
st.plotly_chart(fig)

#%%

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

# 시/도 지도 불러오기
geojson = 'SIDO_MAP_2022.json'
gdf = gpd.read_file(geojson)

# GeoDataFrame의 GeoJSON 형식 확인
geojson_data = gdf.__geo_interface__

# 양수와 음수에 따라 색상 설정하기
colors = {'양수': 'blue', '음수': 'red'}

# 색상 설정 함수
def get_color(value):
    if value >= 0:
        return '양수'
    else:
        return '음수'
    
# 'color' 열 추가
df['color'] = df['인구순이동'].apply(get_color)

# Plotly Express를 사용하여 대한민국 지도 그리기
fig = px.choropleth_mapbox(
    df,
    geojson=geojson_data,
    locations='지역',
    featureidkey='properties.CTP_KOR_NM',
    color='인구순이동',  # 색상은 '인구순이동' 컬럼으로 지정
    color_continuous_scale=[(0.0, "red"), (0.5, "white"), (1.0, "blue")],  # 색상 스케일 설정
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

print("Current working directory:", os.getcwd())
