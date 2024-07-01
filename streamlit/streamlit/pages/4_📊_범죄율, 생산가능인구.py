
import streamlit as st
from PIL import Image

#%%
# 페이지 기본 설정

st.set_page_config(page_title="📊범죄율 - 생산가능인구 현황", page_icon="📊범죄율 - 생산가능인구 현황", layout="wide")

st.subheader("📊범죄율 - 생산가능인구 현황")

# 이미지 파일 경로 설정
image_path = 'E:\streamlit\image\crime.jpg'  # 이미지 파일 경로를 실제 파일 경로로 바꿔주세요
image_path1 = 'E:\streamlit\image\population.jpg' 
image_path2 = 'E:\streamlit\image\infra.png'

# 이미지를 스트림릿 앱에 표시

img = Image.open(image_path)
img1 = Image.open(image_path1)
img2 = Image.open(image_path2)

# 이미지 크기 조정
new_width = 700
new_height = 500
img_resized = img.resize((new_width, new_height))
img_resized1 = img1.resize((new_width, new_height))


new_width1 = 1500
new_height1 = 600

img_resized2 = img2.resize((new_width1, new_height1))

col1, col2 = st.columns(2)
with col1:
    st.image(img_resized, caption='범죄율')

with col2:
    st.image(img_resized1, caption='생산가능인구')
    
st.markdown(" ", unsafe_allow_html=True)
st.markdown(" ", unsafe_allow_html=True)
st.markdown(" ", unsafe_allow_html=True)    
    
center_style = "display: block; margin-left: auto; margin-right: auto;"



st.image(img_resized2, caption='아파트 가격에 따른 인프라 거리')