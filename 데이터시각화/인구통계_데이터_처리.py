# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import pandas as pd
df = pd.read_excel('전출지_전입지_2013~2023_데이터가공버젼.xlsx')
df2 = pd.read_excel('인구이동률_월__분기__년__20240507135720.xlsx')
df3 = pd.read_excel('전출지_전입지_시도_별_이동자수_20240507135712.xlsx')
df4 = pd.read_excel('시군구별_이동자수_전처리.xlsx')

#%%

df_reset = df.reset_index(drop=True)


#%%

# 비어있는 열의 데이터를 가장 위에 있는 열로 채우기
df_fill = df.fillna(method='ffill', inplace=False)



#%%

# 연속된 행을 삭제해주는 함수

df_fill_drop = df_fill.drop(columns=[f'순이동자수 (명).{i}' for i in range(1, 11)], inplace=False)

columns_to_sum = [f'순이동자수 (명).{i}' for i in range(1, 11)]

#%%


# 1열과 2열의 값이 같은 경우를 찾아 삭제하기
df_new = df_fill_drop.rename(columns={'Unnamed: 0': 'first', 'Unnamed: 1': 'second'})


df_new = df_new[df_new['first'] != df_new['second']]

#%%


# 합산할 열의 범위 지정
columns_to_sum = [f'순이동자수 (명).{i}' for i in range(1, 11)]


# 지정한 열의 값을 더한 총합 계산하여 새로운 열 추가
df_new['Total'] = df_new[columns_to_sum].sum(axis=1)


# 데이터프레임을 엑셀 파일로 저장
excel_file_path = 'C:/Users/daptys/demographic_survey/인구이동자료/df_new_1.xlsx'  # 저장할 엑셀 파일 경로 및 파일명
df_new.to_excel(excel_file_path, index=True)  # index=False를 설정하여 인덱스를 저장하지 않음

#%%

# 데이터프레임에서 index 0을 제거
df.drop = df.drop('index' , axis=1)


#%%

# 내림차순 정렬
df2_sorted_down = df2.sort_values(by='2024.01.2')


# 오름차순 정렬
df2_sorted_up = df2.sort_values(by='2024.01.2', ascending=False)


#%%

# 데이터프레임에서 index 0을 제거
df = df.drop(0)






#%%
# 데이터프레임의 행과 열 확인
rows, cols = df2.shape
print("행의 개수:", rows)
print("열의 개수:", cols)

#%%
# 데이터프레임의 행의 이름 확인
row_names = df_new.index.tolist()
print("행의 이름:", row_names)

# 데이터프레임의 열의 이름 확인
col_names = df_new.columns.tolist()
print("열의 이름:", col_names)

#%%

import os
print(os.getcwd())
