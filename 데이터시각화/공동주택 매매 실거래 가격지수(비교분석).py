# -*- coding: utf-8 -*-

import pandas as pd                  # 데이터프레임 가공
import numpy as np                   # 데이터프레임 수학 연산
import matplotlib.pyplot as plt      # 도표 패키지
import matplotlib.font_manager as fm # 글씨체 지정 패키지
import seaborn as sns
from add_font import *
import add_font as af
import os

#%%
def reg():
    import matplotlib.font_manager as fm
    import os

    user_name = os.getlogin()

    fontpath = [f'C:/Users/{user_name}/AppData/Local/Microsoft/Windows/Fonts']
    font_files = fm.findSystemFonts(fontpaths=fontpath)
    for fpath in font_files:
        
        fm.fontManager.addfont(fpath)

def fontpath():
    
    import os

    user_name = os.getlogin()

    return f'C:/Users/{user_name}/AppData/Local/Microsoft/Windows/Fonts'

reg()
plt.rcParams["font.family"] = 'NanumGothic'
#%%
plt.figure(figsize=(20, 20))  # 그래프 크기 설정

dfa = pd.read_excel('매매_실거래가격(비교)_수정_v8.xlsx')

#%%
# 상관 관계 확인

dfa.corr()

#%%
# 히트맵으로 상관 관계 시각화
# 1) 공동주택 매매 실거래 가격지수
# 2) 1인가구 수
# 3) 외국인(장기체류) 인원
# 4) 무주택가구 수
# 5) 대통령지지율

plt.figure(figsize=(15,20))  # 그림의 크기를 크게 설정
sns.heatmap(data=dfa.corr(), annot=True, 
fmt='.2f', linewidths=.5, cmap='Blues', 
annot_kws={"size": 8})  # 상관 계수 글꼴 크기 확대

# x축, y축 레이블 크기 조정
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()

#%%
# 레벨 맞추기

dfa['1인가구'] = round(dfa['1인가구'] / 100000, 2)
dfa['외국인(장기체류)'] = round(dfa['외국인(장기체류)'] / 100000, 2)
dfa['무주택가구수'] = round(dfa['무주택가구수'] / 100000, 2)

#%%
plt.plot(dfa['연도'], dfa['매매_실거래_가격지수'], marker='o', linestyle='-', color='yellow', label='가격지수')
plt.plot(dfa['연도'], dfa['1인가구'], marker='o', linestyle='-', color='orange', label='1인가구')
plt.plot(dfa['연도'], dfa['외국인(장기체류)'], marker='o', linestyle='-', color='pink', label='외국인(장기체류)')
plt.plot(dfa['연도'], dfa['무주택가구수'], marker='o', linestyle='-', color='skyblue', label='무주택가구수')

# 수치 및 증감률 추가 및 글씨 크기 설정
for i in range(0, len(dfa)):
    plt.text(dfa['연도'][i], dfa['매매_실거래_가격지수'][i], f"{dfa['매매_실거래_가격지수'][i]}\n({dfa['가격지수_증감률'][i]:.1f}%)", color='black', ha='left', va='bottom', fontsize=8)
    plt.text(dfa['연도'][i], dfa['1인가구'][i], f"{dfa['1인가구'][i]}\n({dfa['1인가구_증감률'][i]:.1f}%)", color='black', ha='left', va='bottom', fontsize=8)
    plt.text(dfa['연도'][i], dfa['외국인(장기체류)'][i], f"{dfa['외국인(장기체류)'][i]}\n({dfa['외국인_증감률'][i]:.1f}%)", color='black', ha='left', va='bottom', fontsize=8)
    plt.text(dfa['연도'][i], dfa['무주택가구수'][i], f"{dfa['무주택가구수'][i]}\n({dfa['무주택가구수_증감률'][i]:.1f}%)", color='black', ha='left', va='bottom', fontsize=8)


plt.xticks(rotation=55)

plt.xlabel('연도')
plt.ylabel('비교 분석')
plt.title('매매_실거래_가격지수 추이 상관관계')
plt.legend()
plt.show()

