# -*- coding: utf-8 -*-
"""
Created on Sun May 26 06:50:22 2024

@author: Dan
"""

import pandas as pd
import numpy as np
from scipy.stats import pearsonr
import matplotlib.pyplot as plt

# 실거래 가격지수 데이터
real_estate_data = {
    "Region": ["서울", "부산", "대구", "인천", "광주", "대전", "울산", "세종", "경기", "강원", "충북", "충남", "전북", "전남", "경북", "경남", "제주"],
    "Price_Index": [157.0, 105.1, 102.1, 120.4, 126.4, 141.2, 99.0, 129.9, 135.2, 111.5, 109.1, 104.5, 108.6, 107.5, 100.2, 96.7, 108.1]
}

# 인구 유입/유출 데이터
population_movement_data = {
    "Region": ["경기", "세종", "충남", "인천", "제주", "충북", "강원", "전남", "경북", "경남", "광주", "전북", "울산", "대전", "대구", "부산", "서울"],
    "Population_Change": [1114087.0, 245091.0, 103508.0, 77848.0, 74551.0, 34782.0, 26827.0, -36116.0, -53605.0, -63397.0, -66981.0, -67406.0, -82668.0, -112853.0, -145538.0, 186799.0, -861331.0]
}


population_add_data = {
    "Region": ["경기", "세종", "충남", "인천", "제주", "충북", "강원"],
    "Population_Change": [1114087.0, 245091.0, 103508.0, 77848.0, 74551.0, 34782.0, 26827.0]
}


population_minus_data = {
    "Region": ["전남", "경북", "경남", "광주", "전북", "울산", "대전", "대구", "부산", "서울"],
    "Population_Change": [-36116.0, -53605.0, -63397.0, -66981.0, -67406.0, -82668.0, -112853.0, -145538.0, 186799.0, -861331.0]
}

# 데이터 프레임 생성
real_estate_df = pd.DataFrame(real_estate_data)
population_movement_df = pd.DataFrame(population_movement_data)
population_movement_add_df = pd.DataFrame(population_add_data)
population_movement_minus_df = pd.DataFrame(population_minus_data)


# 병합된 데이터 프레임
merged_df = pd.merge(real_estate_df, population_movement_df, on='Region')
merged_add_df = pd.merge(real_estate_df, population_movement_add_df, on='Region')
merged_minus_df = pd.merge(real_estate_df, population_movement_minus_df, on='Region')

# 상관계수 계산
correlation, p_value = pearsonr(merged_minus_df['Price_Index'], merged_minus_df['Population_Change'])

# 데이터 시각화
plt.figure(figsize=(12, 8))
plt.scatter(merged_minus_df['Price_Index'], merged_minus_df['Population_Change'], color='blue')

# 각 점에 데이터 레이블 추가
for i in range(len(merged_minus_df)):
    plt.text(merged_minus_df['Price_Index'][i], merged_minus_df['Population_Change'][i], merged_minus_df['Region'][i], fontsize=15)

plt.title('인구 유입유출과 집값의 상관관계')
plt.xlabel('집값')
plt.ylabel('인구이동')
plt.grid(True)
plt.show()

print(f"Correlation: {correlation}, P-value: {p_value}")