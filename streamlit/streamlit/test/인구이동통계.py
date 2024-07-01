# -*- coding: utf-8 -*-

# 패키지
import pandas as pd                  # 데이터프레임 가공
import numpy as np                   # 데이터프레임 수학 연산
import matplotlib.pyplot as plt      # 도표 패키지
import matplotlib.font_manager as fm # 글씨체 지정 패키지
import add_font as af

#%%

import matplotlib.pyplot as plt
from matplotlib import font_manager

font_path = './NanumGothic.ttf'  # NanumGothic 폰트의 경로로 수정
font_prop = font_manager.FontProperties(fname=font_path)
plt.rcParams['font.family'] = font_prop.get_name()

#%%

def reg():
    import matplotlib.font_manager as fm
    import os

    user_name = os.getlogin()

    fontpath = [f'C:/Users/{user_name}/AppData/Local/Microsoft/Windows/Fonts']
    font_files = fm.findSystemFonts(fontpaths=fontpath)
    for fpath in font_files:
        
        fm.fontManager.addfont(fpath)

reg()
# %%

def fontpath():
    
    import os

    user_name = os.getlogin()

    return f'C:/Users/{user_name}/AppData/Local/Microsoft/Windows/Fonts'

#%%


plt.rcParams["font.family"] = 'NanumGothic'

#%%

# 데이터 로딩

df = pd.read_excel('시도간이동자(전국).xlsx')

#%%

# 만 단위로 치환하기 (소수점 뒤 2자릿 수 반올림)

df['1~4세'] = round(df['1~4세'] / 10000, 2)
df['5~9세'] = round(df['5~9세'] / 10000, 2)
df['10~14세'] = round(df['10~14세'] / 10000, 2)
df['15~19세'] = round(df['15~19세'] / 10000, 2)
df['20~24세'] = round(df['20~24세'] / 10000, 2)
df['25~29세'] = round(df['25~29세'] / 10000, 2)
df['30~34세'] = round(df['30~34세'] / 10000, 2)
df['35~39세'] = round(df['35~39세'] / 10000, 2)
df['40~44세'] = round(df['40~44세'] / 10000, 2)
df['45~49세'] = round(df['45~49세'] / 10000, 2)
df['50~54세'] = round(df['50~54세'] / 10000, 2)
df['55~59세'] = round(df['55~59세'] / 10000, 2)
df['60~64세'] = round(df['60~64세'] / 10000, 2)
df['65~69세'] = round(df['65~69세'] / 10000, 2)
df['70~74세'] = round(df['70~74세'] / 10000, 2)
df['75세_이상'] = round(df['75세_이상'] / 10000, 2)

#%%

# 시도간이동자_전국기준 (2016~2022년)
# 누적막대그래프

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 10))  # 그래프 크기 설정

# 각 열 데이터를 따로 처리하여 막대 그래프에 추가
bar1 = plt.bar(df['연도'], df['1~4세'], color='skyblue', label='1~4세')
bar2 = plt.bar(df['연도'], df['10~14세'], color='lightgreen', label='10~14세')
bar3 = plt.bar(df['연도'], df['15~19세'], color='orange', label='15~19세')
bar4 = plt.bar(df['연도'], df['20~24세'], color='pink', label='20~24세')
bar5 = plt.bar(df['연도'], df['25~29세'], color='purple', label='25~29세')
bar6 = plt.bar(df['연도'], df['30~34세'], color='yellow', label='30~34세')
bar7 = plt.bar(df['연도'], df['35~39세'], color='cyan', label='35~39세')
bar8 = plt.bar(df['연도'], df['40~44세'], color='brown', label='40~44세')
bar9 = plt.bar(df['연도'], df['45~49세'], color='khaki', label='45~49세')
bar10 = plt.bar(df['연도'], df['50~54세'], color='darkslategray', label='50~54세')
bar11 = plt.bar(df['연도'], df['55~59세'], color='indigo', label='55~59세')
bar12 = plt.bar(df['연도'], df['60~64세'], color='coral', label='60~64세')
bar13 = plt.bar(df['연도'], df['65~69세'], color='deepskyblue', label='65~69세')
bar14 = plt.bar(df['연도'], df['70~74세'], color='hotpink', label='70~74세')
bar15 = plt.bar(df['연도'], df['75세_이상'], color='yellowgreen', label='75세_이상')

# for bars in [bar1, bar2, bar3, bar4, bar5, bar6, bar7, bar8, bar9, bar10, bar11, bar12, bar13, bar14, bar15]:
#     for rect in bars:
#         height = rect.get_height()
#         plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.1d' % height, ha='center', va='bottom', size=12, color='black')

# 축 및 레이블 설정
plt.xlabel('연도')
plt.ylabel('연령별 이동자 수')
plt.title('연령별 이동자 수 (단위: 만 명)')
plt.legend()

# 그래프 표시
plt.show()
#%%
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 10))  # 그래프 크기 설정

# 시도간이동자_전국기준 (2016~2022년)
# 꺾은선 그래프

plt.plot(df['연도'], df['1~4세'], marker='o', linestyle='-', color='skyblue', label='1~4세')
plt.plot(df['연도'], df['10~14세'], marker='o', linestyle='-', color='lightgreen', label='10~14세')
plt.plot(df['연도'], df['15~19세'], marker='o', linestyle='-', color='orange', label='15~19세')
plt.plot(df['연도'], df['20~24세'], marker='o', linestyle='-', color='pink', label='20~24세')
plt.plot(df['연도'], df['25~29세'], marker='o', linestyle='-', color='purple', label='25~29세')
plt.plot(df['연도'], df['30~34세'], marker='o', linestyle='-', color='yellow', label='30~34세')
plt.plot(df['연도'], df['35~39세'], marker='o', linestyle='-', color='cyan', label='35~39세')
plt.plot(df['연도'], df['40~44세'], marker='o', linestyle='-', color='brown', label='40~44세')
plt.plot(df['연도'], df['45~49세'], marker='o', linestyle='-', color='khaki', label='45~49세')
plt.plot(df['연도'], df['50~54세'], marker='o', linestyle='-', color='darkslategray', label='50~54세')
plt.plot(df['연도'], df['55~59세'], marker='o', linestyle='-', color='indigo', label='55~59세')
plt.plot(df['연도'], df['60~64세'], marker='o', linestyle='-', color='coral', label='60~64세')
plt.plot(df['연도'], df['65~69세'], marker='o', linestyle='-', color='deepskyblue', label='65~69세')
plt.plot(df['연도'], df['70~74세'], marker='o', linestyle='-', color='hotpink', label='70~74세')
plt.plot(df['연도'], df['75세_이상'], marker='o', linestyle='-', color='yellowgreen', label='75세_이상')

# 각 데이터 포인트에 수치 표시
for col in df.columns[2:]:
    for i, txt in enumerate(df[col]):
        plt.annotate(txt, (df['연도'][i], df[col][i]), textcoords="offset points", xytext=(0,10), ha='right')

plt.xticks(rotation=55)

# 축 및 레이블 설정
plt.xlabel('연도')
plt.ylabel('연령별 이동자 수')
plt.title('연령별 이동자 수_전국 기준(단위: 만 명)')
plt.legend()

# 그래프 표시
plt.show()