# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 09:49:19 2024

@author: bigdata
"""
#%%
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, RobustScaler, StandardScaler
from sklearn.decomposition import PCA
from sklearn.impute import SimpleImputer

# 엑셀 파일 목록
file_names = [
    "지지율.xlsx",
    "PIR지수_전국.xlsx",
    "매매수급동향.xlsx",
    "소비자물가지수.xlsx",
    "종합부동산세_세율_개인.xlsx",
    "아파트매매거래량.xlsx",
    "주택담보대출.xlsx"
]

# 데이터프레임 병합
dfs = []
for file in file_names:
    df = pd.read_excel(file, engine='openpyxl', dtype={'시점': int})
    dfs.append(df)

# 첫 번째 데이터프레임 선택하여 병합 시작
merged_df = dfs[0]
for df in dfs[1:]:
    merged_df = pd.merge(merged_df, df, on='시점', how='outer')

# NaN 값 처리 (평균값으로 대체)
imputer = SimpleImputer(strategy='mean')
merged_df_filled = pd.DataFrame(imputer.fit_transform(merged_df.select_dtypes(include=['float64', 'int64'])), columns=merged_df.select_dtypes(include=['float64', 'int64']).columns)

# 병합된 데이터프레임에 시점 추가
merged_df_filled['시점'] = merged_df['시점']

# 스케일러 객체 생성
min_max_scaler = MinMaxScaler()
robust_scaler = RobustScaler()
standard_scaler = StandardScaler()

# 스케일링 적용
df_min_max_scaled = pd.DataFrame(min_max_scaler.fit_transform(merged_df_filled.drop(columns=['시점'])), columns=merged_df_filled.drop(columns=['시점']).columns)
df_robust_scaled = pd.DataFrame(robust_scaler.fit_transform(merged_df_filled.drop(columns=['시점'])), columns=merged_df_filled.drop(columns=['시점']).columns)
df_standard_scaled = pd.DataFrame(standard_scaler.fit_transform(merged_df_filled.drop(columns=['시점'])), columns=merged_df_filled.drop(columns=['시점']).columns)

# 차원축소 및 주성분분석 (PCA)
pca = PCA(n_components=4)  # 원하는 주성분 수 설정 

# PCA 적용 (원본, MinMax 스케일링, Robust 스케일링, Standard 스케일링 데이터프레임에 대해)
pca_original = pca.fit_transform(merged_df_filled.drop(columns=['시점']))
pca_min_max = pca.fit_transform(df_min_max_scaled)
pca_robust = pca.fit_transform(df_robust_scaled)
pca_standard = pca.fit_transform(df_standard_scaled)

# PCA 결과 데이터프레임 생성
pca_original_df = pd.DataFrame(pca_original, columns=['PC1', 'PC2', 'PC3', 'PC4'])
pca_min_max_df = pd.DataFrame(pca_min_max, columns=['PC1', 'PC2', 'PC3', 'PC4'])
pca_robust_df = pd.DataFrame(pca_robust, columns=['PC1', 'PC2', 'PC3', 'PC4'])
pca_standard_df = pd.DataFrame(pca_standard, columns=['PC1', 'PC2', 'PC3', 'PC4'])

# 결과 출력
print("PCA 결과 (원본 데이터프레임):")
print(pca_original_df.head())

print("PCA 결과 (MinMax 스케일링 데이터프레임):")
print(pca_min_max_df.head())

print("PCA 결과 (Robust 스케일링 데이터프레임):")
print(pca_robust_df.head())

print("PCA 결과 (Standard 스케일링 데이터프레임):")
print(pca_standard_df.head())

# 병합된 데이터프레임을 엑셀 파일로 저장 (시점 포함)
merged_df_filled.to_excel('머신러닝변수목록_전처리후.xlsx', index=False)