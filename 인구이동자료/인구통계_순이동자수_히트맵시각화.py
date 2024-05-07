# -*- coding: utf-8 -*-
"""
Created on Tue May  7 15:31:44 2024

@author: daptys
"""

import pandas as pd
from matplotlib import font_manager, rc
df = pd.read_excel('전출지_전입지_데이터가공_히트맵_시각화.xlsx')

# 한글 폰트 설정
font_path = "C:/Windows/Fonts/malgunbd.ttf"  # 자신이 사용하고 있는 한글 폰트의 경로로 변경해주세요.
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)


#%%



#%%

import seaborn as sns
import matplotlib.pyplot as plt

# 데이터프레임에서 순이동자수 열을 피벗하여 히트맵으로 그리기 위해 변환
pivot_df = df.pivot_table(values="Total", index="first", columns="second")

# 히트맵 시각화를 하기 전에 인덱스 열의 순서를 바꿈
desired_order = ["전국","강원특별자치도", "경기도", "경상남도", "경상북도", "광주광역시", "대구광역시", "대전광역시", "부산광역시", "서울특별시", "세종특별자치시", "울산광역시", "인천광역시", "전라남도", "전북특별자치도", "제주특별자치도", "충청남도", "충청북도"]
pivot_df = pivot_df.reindex(index = desired_order, columns = desired_order)

# 히트맵 시각화
plt.figure(figsize=(10, 8))
sns.heatmap(pivot_df, annot=False, cmap="coolwarm", fmt=".0f", linewidths=.5)
plt.title("전국지역 간 순이동자수 히트맵")
plt.xlabel("이동지")
plt.ylabel("출발지")
plt.show()

#%%
from sklearn.preprocessing import StandardScaler

df1 = df


scaler = StandardScaler()

# 데이터를 표준화
standardized_data = scaler.fit_transform(df1)

print("Standardized Data:")
print(standardized_data)

#%%



#%%

from sklearn.preprocessing import OneHotEncoder
import numpy as np

# 범주형 데이터 예시
categories = ['cat', 'dog', 'elephant', 'cat', 'dog']

print(categories)

# OneHotEncoder 객체 생성
encoder = OneHotEncoder()

print(encoder)

# 문자열을 숫자로 변환
encoded_data = encoder.fit_transform(np.array(categories).reshape(-1, 1))

print(encoded_data)

# 변환된 데이터를 배열로 변환
encoded_data_array = encoded_data.toarray()

print("Encoded Data:")
print(encoded_data_array)


#%%


