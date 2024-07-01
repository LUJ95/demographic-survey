
import streamlit as st
from PIL import Image

#%%

# 페이지 기본 설정
st.set_page_config(page_title="📊실거래 가격지수 - 실업률 현황", page_icon="📊실거래 가격지수 - 실업률 현황", layout="wide")

st.subheader("📊실거래 가격지수 - 실업률 현황")

# 이미지 파일 경로 설정
image_path = 'E:\streamlit\image\sil.jpg'  # 이미지 파일 경로를 실제 파일 경로로 바꿔주세요
image_path1 = 'E:\streamlit\image\work.jpg' 

# 이미지를 스트림릿 앱에 표시

img = Image.open(image_path)
img1 = Image.open(image_path1)

# 이미지 크기 조정
new_width = 700
new_height = 500
img_resized = img.resize((new_width, new_height))
img_resized1 = img1.resize((new_width, new_height))



col1, col2 = st.columns(2)
with col1:
    st.image(img_resized, caption='실거래 가격지수')

with col2:
    st.image(img_resized1, caption='실업률')
    
# 캡션 폰트 사이즈 조정

