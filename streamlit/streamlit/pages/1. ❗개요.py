
import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="❗개요", page_icon="❗개요", layout="wide")

st.subheader("❗개요")

# HTML 태그를 사용하여 텍스트에 스타일 적용
st.markdown('<span style="font-size: 20px;">🔵 결론: 인프라의 중요성을 강조하며, 양극화 분석을 통해 좋은 도시를 선정하는 지표로 실거래 가격지수를 활용하였습니다.</span>', unsafe_allow_html=True)
st.markdown('<span style="font-size: 20px;"> 🔹 실거래 가격지수를 근거로 양극화 분석, 저번 프로젝트의 분석으로 시도 간 순이동 데이터를 확인하여 세종시의 우수성을 확인하였습니다.</span>', unsafe_allow_html=True)
st.markdown('<span style="font-size: 20px;"> 🔹 대전과 세종, 충남과 충북의 실거래 가격지수를 비교하여 도시 간 양극화 정도를 분석하였습니다.</span>', unsafe_allow_html=True)
st.markdown('<span style="font-size: 20px;">🔴 대전 편입이유 = 실거래 지수 높음 범죄율, 월소득평균, 생산가능 인구비율 등의 지표들을 근거로하여 실거래 가격지수를 선택하였습니다.</span>', unsafe_allow_html=True)
st.markdown('<span style="font-size: 20px;"> 🔸이는 도시의 생활 편의성과 경제적 활동성을 반영합니다.</span>', unsafe_allow_html=True)
#%%

