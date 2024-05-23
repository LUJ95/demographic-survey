# -*- coding: utf-8 -*-

import pandas as pd                  # 데이터프레임 가공
import numpy as np                   # 데이터프레임 수학 연산
import matplotlib.pyplot as plt      # 도표 패키지
import matplotlib.font_manager as fm # 글씨체 지정 패키지
from add_font import *
import add_font as af
import os

# 무주택 가구 통계

#%%
# def reg():
#     import matplotlib.font_manager as fm
#     import os

#     user_name = os.getlogin()

#     fontpath = [f'C:/Users/{user_name}/AppData/Local/Microsoft/Windows/Fonts']
#     font_files = fm.findSystemFonts(fontpaths=fontpath)
#     for fpath in font_files:
        
#         fm.fontManager.addfont(fpath)

reg()
plt.rcParams["font.family"] = 'NanumGothic'

#%%

# 연령별 (꺾은선 그래프)

df = pd.read_excel('무주택자_수(연령별)_수정.xlsx')
print(df.head())
print(df.columns)

#%%

import matplotlib.pyplot as plt

plt.figure(figsize=(20, 20))  # 그래프 크기 설정

df['30세미만'] = round(df['30세미만'] / 10000, 2)
df['30~39세'] = round(df['30~39세'] / 10000, 2)
df['40~49세'] = round(df['40~49세'] / 10000, 2)
df['50~59세'] = round(df['50~59세'] / 10000, 2)
df['60~69세'] = round(df['60~69세'] / 10000, 2)
df['70~79세'] = round(df['70~79세'] / 10000, 2)
df['80세이상'] = round(df['80세이상'] / 10000, 2)

#%%
# 증감률 계산 함수
def calculate_growth_rate(series):
    return series.pct_change() * 100

# 증감률 계산
df['30세미만_증감률'] = calculate_growth_rate(df['30세미만'])
df['30~39세_증감률'] = calculate_growth_rate(df['30~39세'])
df['40~49세_증감률'] = calculate_growth_rate(df['40~49세'])
df['50~59세_증감률'] = calculate_growth_rate(df['50~59세'])
df['60~69세_증감률'] = calculate_growth_rate(df['60~69세'])
df['70~79세_증감률'] = calculate_growth_rate(df['70~79세'])
df['80세이상_증감률'] = calculate_growth_rate(df['80세이상'])
#%%
plt.plot(df['연도'], df['30세미만'], marker='o', linestyle='-', color='yellow', label='30세미만')
plt.plot(df['연도'], df['30~39세'], marker='o', linestyle='-', color='orange', label='30~39세')
# plt.plot(df['연도'], df['40~49세'], marker='o', linestyle='-', color='pink', label='40~49세')
# # plt.plot(df['연도'], df['50~59세'], marker='o', linestyle='-', color='skyblue', label='50~59세')
# # plt.plot(df['연도'], df['60~69세'], marker='o', linestyle='-', color='red', label='60~69세')
# # plt.plot(df['연도'], df['70~79세'], marker='o', linestyle='-', color='cyan', label='70~79세')
# plt.plot(df['연도'], df['80세이상'], marker='o', linestyle='-', color='grey', label='80세이상')

# 수치 및 증감률 추가 및 글씨 크기 설정
for i in range(1, len(df)):  # 첫 번째 행은 NaN 값이므로 1부터 시작
    plt.text(df['연도'][i], df['30세미만'][i], f"{df['30세미만'][i]}\n({df['30세미만_증감률'][i]:.1f}%)", color='black', ha='left', va='bottom', fontsize=8)
    plt.text(df['연도'][i], df['30~39세'][i], f"{df['30~39세'][i]}\n({df['30~39세_증감률'][i]:.1f}%)", color='black', ha='right', va='bottom', fontsize=8)
    # plt.text(df['연도'][i], df['40~49세'][i], f"{df['40~49세'][i]}\n({df['40~49세_증감률'][i]:.1f}%)", color='black', ha='right', va='bottom', fontsize=8)
    # # plt.text(df['연도'][i], df['50~59세'][i], f"{df['50~59세'][i]}\n({df['50~59세_증감률'][i]:.1f}%)", color='black', ha='right', va='bottom', fontsize=8)
    # # plt.text(df['연도'][i], df['60~69세'][i], f"{df['60~69세'][i]}\n({df['60~69세_증감률'][i]:.1f}%)", color='black', ha='right', va='bottom', fontsize=8)
    # # # plt.text(df['연도'][i], df['70~79세'][i], f"{df['70~79세'][i]}\n({df['70~79세_증감률'][i]:.1f}%)", color='black', ha='right', va='bottom', fontsize=8)
    # # plt.text(df['연도'][i], df['80세이상'][i], f"{df['80세이상'][i]}\n({df['80세이상_증감률'][i]:.1f}%)", color='black', ha='right', va='bottom', fontsize=8)

# for i in range(len(df)):
#     plt.text(df['연도'][i], df['30세미만'][i], str(df['30세미만'][i]), color='black', ha='left', va='bottom', fontsize=8)
#     plt.text(df['연도'][i], df['30~39세'][i], str(df['30~39세'][i]), color='black', ha='right', va='bottom', fontsize=8)
#     plt.text(df['연도'][i], df['40~49세'][i], str(df['40~49세'][i]), color='black', ha='right', va='bottom', fontsize=8)
#     plt.text(df['연도'][i], df['50~59세'][i], str(df['50~59세'][i]), color='black', ha='right', va='bottom', fontsize=8)
#     plt.text(df['연도'][i], df['60~69세'][i], str(df['60~69세'][i]), color='black', ha='right', va='bottom', fontsize=8)
#     plt.text(df['연도'][i], df['70~79세'][i], str(df['70~79세'][i]), color='black', ha='right', va='bottom', fontsize=8)
#     plt.text(df['연도'][i], df['80세이상'][i], str(df['80세이상'][i]), color='black', ha='right', va='bottom', fontsize=8)

plt.xticks(rotation=55)

plt.xlabel('연도')
plt.ylabel('무주택자 수')
plt.title('연령별 무주택자 증감추이(단위 : 만 명)')
plt.legend()
plt.show()
#%%

# 연령별 (누적 막대그래프)

plt.figure(figsize=(10, 10))  # 그래프 크기 설정

bar1 = plt.bar(df['연도'], df['30세미만'], color='yellow', label='30세미만')
bar2 = plt.bar(df['연도'], df['30~39세'], bottom=df['30세미만'], color='orange', label='30~39세')
bar3 = plt.bar(df['연도'], df['40~49세'], bottom=df['30세미만'] + df['30~39세'], color='pink', label='40~49세')
bar4 = plt.bar(df['연도'], df['50~59세'], bottom=df['30세미만'] + df['30~39세'] + df['40~49세'], color='skyblue', label='50~59세')
bar5 = plt.bar(df['연도'], df['60~69세'], bottom=df['30세미만'] + df['30~39세'] + df['40~49세'] + df['50~59세'], color='red', label='60~69세')
bar6 = plt.bar(df['연도'], df['70~79세'], bottom=df['30세미만'] + df['30~39세'] + df['40~49세'] + df['50~59세'] + df['60~69세'], color='cyan', label='70~79세')
bar7 = plt.bar(df['연도'], df['80세이상'], bottom=df['30세미만'] + df['30~39세'] + df['40~49세'] + df['50~59세'] + df['60~69세'] + df['70~79세'], color='grey', label='80세이상')

plt.xticks(rotation=55)

plt.xlabel('연도')
plt.ylabel('무주택자 수')
plt.title('연령별 무주택자 증감추이(단위 : 만 명)')
plt.legend()
# plt.grid(True)
plt.show()

#%%
# 성별 (꺾은선 그래프)

dfa = pd.read_excel('무주택자_수(성별)_수정.xlsx')

#%%

import matplotlib.pyplot as plt

plt.figure(figsize=(20, 20))  # 그래프 크기 설정

dfa['남자'] = round(dfa['남자'] / 10000, 2)
dfa['여자'] = round(dfa['여자'] / 10000, 2)

#%%
# 증감률 계산 함수
def calculate_growth_rate(series):
    return series.pct_change() * 100

# 증감률 계산
dfa['남자_증감률'] = calculate_growth_rate(dfa['남자'])
dfa['여자_증감률'] = calculate_growth_rate(dfa['여자'])

#%%

plt.plot(dfa['연도'], dfa['남자'], marker='o', linestyle='-', color='yellow', label='남자')
plt.plot(dfa['연도'], dfa['여자'], marker='o', linestyle='-', color='orange', label='여자')
# 수치 및 증감률 추가 및 글씨 크기 설정
for i in range(0, len(dfa)):  # 첫 번째 행은 NaN 값이므로 1부터 시작
    plt.text(dfa['연도'][i], dfa['남자'][i], f"{dfa['남자'][i]}\n({dfa['남자_증감률'][i]:.1f}%)", color='black', ha='left', va='bottom', fontsize=8)
    plt.text(dfa['연도'][i], dfa['여자'][i], f"{dfa['여자'][i]}\n({dfa['여자_증감률'][i]:.1f}%)", color='black', ha='right', va='bottom', fontsize=8)

plt.xticks(rotation=55)

plt.xlabel('연도')
plt.ylabel('무주택자 수')
plt.title('연령별 무주택자 증감추이(단위 : 만 명)')
plt.legend()
plt.show()

#%%
# 성별 (누적 막대그래프)

bar1 = plt.bar(dfa['연도'], dfa['남자'], label='남자', color = 'skyblue')  # 첫 번째 그래프
bar2 = plt.bar(dfa['연도'], dfa['여자'], bottom=dfa['남자'], label='여자', color = 'orange')  # 두 번째 그래프 (누적)

for rect1, rect2 in zip(bar1, bar2):
    height1 = rect1.get_height()
    height2 = rect2.get_height()
    total_height = height1 + height2
    
    # 남자 수치 표시
    plt.text(rect1.get_x() + rect1.get_width() / 2.0, height1 / 2, '%.1d' % height1, ha='center', va='center', size=12, color='black')
    
    # 여자 수치 표시
    plt.text(rect2.get_x() + rect2.get_width() / 2.0, height1 + height2 / 2, '%.1d' % height2, ha='center', va='center', size=12, color='black')

# 축 및 레이블 설정
plt.xlabel('연도')
plt.ylabel('인구')
plt.title('성별 무주택자 증감추이(단위 : 만 명)')
plt.legend()
# 그래프 표시
plt.show()

#%%
# 전체 (전국 기준)

dfb = pd.read_excel('무주택자_수_(전체)_수정.xlsx')
dfb.head()

#%%

# 데이터 변환
dfb['소계'] = round(dfb['소계'] / 10000, 2)

# 증감률 계산 함수
def calculate_growth_rate(series):
    return series.pct_change() * 100

# 증감률 계산
dfb['소계_증감률'] = calculate_growth_rate(dfb['소계'])

# 그래프 크기 설정
plt.figure(figsize=(10, 8))

# 막대 그래프 그리기
bar1 = plt.plot(dfb['연도'], dfb['소계'], marker='o', linestyle='-', color='skyblue', label='무주택자 수')

# 수치 및 증감률 추가 및 글씨 크기 설정
for i in range(0, len(dfb)):  # 첫 번째 행은 NaN 값이므로 1부터 시작
    plt.text(dfb['연도'][i], dfb['소계'][i], f"{dfb['소계'][i]:.2f}\n({dfb['소계_증감률'][i]:.1f}%)", color='black', ha='center', va='bottom', fontsize=12)

plt.xticks(rotation=55)

# 축 및 레이블 설정
plt.xlabel('연도')
plt.ylabel('무주택자 수')
plt.title('무주택자 수(단위: 만 명)')
# plt.legend()

# 그래프 표시
plt.show()

