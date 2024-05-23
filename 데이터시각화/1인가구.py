# -*- coding: utf-8 -*-

# 1인가구 통계자료

#%%
# 패키지
import pandas as pd                  # 데이터프레임 가공
import numpy as np                   # 데이터프레임 수학 연산
import matplotlib.pyplot as plt      # 도표 패키지
import matplotlib.font_manager as fm # 글씨체 지정 패키지
from add_font import *

#%%
# 데이터 로딩

df = pd.read_excel('1인가구_통계자료.xlsx')
print(df.head())
print(df.columns)
        
#%%
# 1인가구 단위 변경

df['남자'] = df['남자'] / 10000
df['여자'] = df['여자'] / 10000

#%%

reg()
plt.rcParams["font.family"] = 'NanumGothic'

# 폰트 지정 - 맑은 고딕
# font_path = 'C:/Users/OSP/Desktop/malgun.ttf'  # 맑은 고딕 폰트 경로
# fontprop = fm.FontProperties(fname=font_path, size=18)

# 한글 폰트 설정
# plt.rcParams['font.family'] = 'malgun'

#%%

# 1인가구_연도별_합계
df = pd.read_excel('1인가구_연도별_합계.xlsx')
df['1인가구'] = round(df['1인가구'] / 10000, 2)
df['2인가구'] = round(df['2인가구'] / 10000, 2)
df['3인가구'] = round(df['3인가구'] / 10000, 2)
df['4인가구'] = round(df['4인가구'] / 10000, 2)
df['4인가구_이상'] = round(df['4인가구_이상'] / 10000, 2)

#%%

# 1인가구_연도별_합계추이 (막대차트)
bar1 = plt.bar(df['연도'], df['합계'], color='skyblue')

for rect in bar1:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.1d' % height, ha='center', va='baseline', size = 12, color='black')
    
# 축 및 레이블 설정
plt.xlabel('연도')
plt.ylabel('1인 가구 수')
plt.title('연도별 1인 가구 증감추이')
plt.legend()

# 그래프 표시
plt.show()

#%%

# 1인가구~다가구_연도별_합계추이 (막대차트)
bar1 = plt.bar(df['연도'], df['1인가구'], color='skyblue')
bar2 = plt.bar(df['연도'], df['2인가구'], color='lightgreen')
bar3 = plt.bar(df['연도'], df['3인가구'], color='orange')
bar4 = plt.bar(df['연도'], df['4인가구'], color='purple')
bar5 = plt.bar(df['연도'], df['4인가구_이상'], color='yellow')

for rect in bar1:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.1d' % height, ha='center', va='baseline', size = 12, color='black')

for rect in bar2:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.1d' % height, ha='center', va='baseline', size = 12, color='black')

for rect in bar3:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.1d' % height, ha='center', va='baseline', size = 12, color='black')

for rect in bar4:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.1d' % height, ha='center', va='baseline', size = 12, color='black')

for rect in bar5:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.1d' % height, ha='center', va='baseline', size = 12, color='black')
    
# 축 및 레이블 설정
plt.xlabel('연도')
plt.ylabel('가구당 인구 수 증감추이')
plt.title('연도별 가구당 인구 수 증감추이')
plt.legend()

# 그래프 표시
plt.show()



#%%
df = pd.read_excel('1인가구_연도별_합계.xlsx')
df['1인가구'] = round(df['1인가구'] / 10000, 2)
df['2인가구'] = round(df['2인가구'] / 10000, 2)
df['3인가구'] = round(df['3인가구'] / 10000, 2)
df['4인가구'] = round(df['4인가구'] / 10000, 2)
df['4인가구_이상'] = round(df['4인가구_이상'] / 10000, 2)
#%%

# 전년 대비 증감률 계산
for col in df.columns[1:]:
    df[col + '_증감률'] = df[col].pct_change() * 100

plt.figure(figsize=(15, 10))  # 그래프 크기 설정

# 꺾은선그래프
plt.plot(df['연도'], df['1인가구'], marker='o', linestyle='-', color='skyblue', label='1인가구')
plt.plot(df['연도'], df['2인가구'], marker='o', linestyle='-', color='lightgreen', label='2인가구')
plt.plot(df['연도'], df['3인가구'], marker='o', linestyle='-', color='orange', label='3인가구')
plt.plot(df['연도'], df['4인가구'], marker='o', linestyle='-', color='purple', label='4인가구')
plt.plot(df['연도'], df['4인가구_이상'], marker='o', linestyle='-', color='yellow', label='4인가구_이상')

# 각 데이터 포인트에 수치 및 증감률 표시
for col in df.columns[1:6]:  # '연도'와 증감률 컬럼을 제외한 데이터 컬럼
    for i in range(0, len(df)):
        value = df[col][i]
        change = df[col + '_증감률'][i]
        plt.annotate(f'{value} ({change:.2f}%)', 
                     (df['연도'][i], df[col][i]), 
                     textcoords="offset points", 
                     xytext=(0,10), 
                     ha='center')

# 축 및 레이블 설정
plt.xticks(rotation=55)
plt.xlabel('연도')
plt.ylabel('가구당 인구 수')
plt.title('연도별 가구당 인구 수 증감률(단위: 만 가구)')
plt.legend()

# 그래프 표시
plt.show()
#%%

# 1인 가구 성별 비교 - 누적막대그래프

bar1 = plt.bar(df['연도'], df['남자'], label='남자', color = 'skyblue')  # 첫 번째 그래프
bar2 = plt.bar(df['연도'], df['여자'], bottom=df['남자'], label='여자', color = 'orange')  # 두 번째 그래프 (누적)

# 막대그래프에 수치 표시
for rect in bar1:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.1d' % height, ha='center', va='top', size = 12, color='black')        

for rect in bar2:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.1d' % height, ha='center', va='bottom', size = 12, color='black')        

# for bar1, bar2, bar3, year in zip(bars1, bars2, bars3, df['연도']):
#     total_height = bar1.get_height() + bar2.get_height()
#     plt.text(bar3.get_x() + bar3.get_width() / 2, bar3.get_height(), f'{int(bar3.get_height())}', ha='center', va='baseline')

# 축 및 레이블 설정
plt.xlabel('연도')
plt.ylabel('인구')
plt.title('1인가구')
plt.legend()

# 그래프 표시
plt.show()

#%%

# 1인가구 지역별 남녀 주거형태

dfa = pd.read_excel('성_및_거처의_종류별_1인가구__시군구_20240514102535_수정.xlsx')
print(dfa.head())
print(dfa.columns)


#%%

dfa = dfa.fillna(method='ffill', inplace=False) # 열 이름 중복으로 채우기

#%%

# 데이터 불러오기
dfa = pd.read_excel('1인가구_주거형태_비중1.xlsx')

#%%

dfa['기타'] = dfa['기타'] / 10000
dfa['다세대주택'] = dfa['다세대주택'] / 10000
dfa['단독주택'] = dfa['단독주택'] / 10000
dfa['비거주용건물내 주택'] = dfa['비거주용건물내 주택'] / 10000
dfa['아파트'] = dfa['아파트'] / 10000
dfa['연립주택'] = dfa['연립주택'] / 10000

#%%
af.reg()
plt.rcParams["font.family"] = 'NanumGothic'

# 폰트 지정 - 맑은 고딕
# font_path = 'C:/Users/OSP/Desktop/malgun.ttf'  # 맑은 고딕 폰트 경로
# fontprop = fm.FontProperties(fname=font_path, size=18)

# 한글 폰트 설정
# plt.rcParams['font.family'] = 'malgun'

#%%

# (순서) 단독주택 -> 아파트 -> 기타 -> 다세대주택 -> 비거주용건물내 주택 -> 연립주택

plt.figure(figsize=(10, 10))  # 그래프 크기 설정

bar1 = plt.bar(dfa['연도'], dfa['단독주택'], color='grey', label='단독주택')
bar2 = plt.bar(dfa['연도'], dfa['아파트'], bottom=dfa['단독주택'], color='yellow', label='아파트')
bar3 = plt.bar(dfa['연도'], dfa['기타'], bottom=dfa['단독주택'] + dfa['아파트'], color='orange', label='기타')
bar4 = plt.bar(dfa['연도'], dfa['다세대주택'], bottom=dfa['단독주택'] + dfa['아파트'] + dfa['기타'], color='pink', label='다세대주택')
bar5 = plt.bar(dfa['연도'], dfa['비거주용건물내 주택'], bottom=dfa['단독주택'] + dfa['아파트'] + dfa['기타'] + dfa['다세대주택'], color='skyblue', label='비거주용건물내 주택')
bar6 = plt.bar(dfa['연도'], dfa['연립주택'], bottom=dfa['단독주택'] + dfa['아파트'] + dfa['기타'] + dfa['다세대주택'] + dfa['비거주용건물내 주택'], color='red', label='연립주택')


# bar1 = plt.bar(dfa['연도'], dfa['기타'], color='skyblue', label='기타')
# bar2 = plt.bar(dfa['연도'], dfa['다세대주택'], color='lightgreen', label='다세대주택')
# bar3 = plt.bar(dfa['연도'], dfa['단독주택'], color='orange', label='단독주택')
# bar4 = plt.bar(dfa['연도'], dfa['비거주용건물내 주택'], color='purple', label='비거주용건물내 주택')
# bar5 = plt.bar(dfa['연도'], dfa['아파트'], color='yellow', label='아파트')
# bar6 = plt.bar(dfa['연도'], dfa['연립주택'], color='red', label='연립주택')

plt.xticks(rotation=55)

# 막대 위 값 표시
# for rect in bar1:
#     height = rect.get_height()
#     plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.1d' % height, ha='center', va='bottom', size = 12, color='black')        

# for rect in bar2:
#     height = rect.get_height()
#     plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.1d' % height, ha='center', va='bottom', size = 12, color='black')        

# for rect in bar3:
#     height = rect.get_height()
#     plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.1d' % height, ha='center', va='bottom', size = 12, color='black')        

# for rect in bar4:
#     height = rect.get_height()
#     plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.1d' % height, ha='center', va='bottom', size = 12, color='black') 

# for rect in bar5:
#     height = rect.get_height()
#     plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.1d' % height, ha='center', va='bottom', size = 12, color='black')

# for rect in bar6:
#     height = rect.get_height()
#     plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.1d' % height, ha='center', va='top', size = 12, color='black')
        
    
plt.xlabel('연도')
plt.ylabel('1인 가구 수')
plt.title('주거형태별 1인 가구 현황(단위 : 만 가구)')
# plt.legend(bbox_to_anchor=(1.05, 1))
plt.legend()
plt.grid(True, axis='y')
plt.show()

plt.rc('font', family='NaNumBarunGothic')
plt.rcParams['figure.dpi'] = 140

#%%
# 데이터 불러오기

dfa = pd.read_excel('1인가구_주거형태_전처리_1.xlsx')

# 단위: 10000으로 변경

dfa['남자'] = dfa['남자'] / 10000
dfa['여자'] = dfa['여자'] / 10000

#%%

# 주거형태별로 데이터 분류 : 아파트

dfa = dfa[dfa['주거형태'] == '아파트']
bar1 = plt.bar(dfa['연도'], dfa['여자'], bottom=dfa['남자'], label='여자', color = 'orange')  # 두 번째 그래프 (누적)
bar2 = plt.bar(dfa['연도'], dfa['남자'], label='남자', color = 'skyblue')  # 첫 번째 그래프
# 막대그래프에 수치 표시
for rect in bar1:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.1d' % height, ha='center', va='top', size = 12, color='black')        

for rect in bar2:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.1d' % height, ha='center', va='top', size = 12, color='black')        

# for bar1, bar2, bar3, year in zip(bars1, bars2, bars3, df['연도']):
#     total_height = bar1.get_height() + bar2.get_height()
#     plt.text(bar3.get_x() + bar3.get_width() / 2, bar3.get_height(), f'{int(bar3.get_height())}', ha='center', va='baseline')

# 축 및 레이블 설정
plt.xlabel('연도')
plt.ylabel('인구')
plt.title('1인가구_주거형태_아파트')
plt.legend()

# 그래프 표시
plt.show()

#%%

# 데이터 읽기

dfa = pd.read_excel('1인가구_주거형태_전처리_1.xlsx')

#%%
# 단위: 10000으로 변경

dfa['남자'] = dfa['남자'] / 10000
dfa['여자'] = dfa['여자'] / 10000

#%%
# 주거형태별로 데이터 분류 : 단독주택

dfa = dfa[dfa['주거형태'] == '단독주택']
bar1 = plt.bar(dfa['연도'], dfa['여자'], bottom=dfa['남자'], label='여자', color = 'orange')  # 두 번째 그래프 (누적)
bar2 = plt.bar(dfa['연도'], dfa['남자'], label='남자', color = 'skyblue')  # 첫 번째 그래프


# 막대그래프에 수치 표시
for rect in bar1:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.1d' % height, ha='center', va='top', size = 12, color='black')        

for rect in bar2:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.1d' % height, ha='center', va='bottom', size = 12, color='black')        

# for bar1, bar2, bar3, year in zip(bars1, bars2, bars3, df['연도']):
#     total_height = bar1.get_height() + bar2.get_height()
#     plt.text(bar3.get_x() + bar3.get_width() / 2, bar3.get_height(), f'{int(bar3.get_height())}', ha='center', va='baseline')

# 축 및 레이블 설정
plt.xlabel('연도')
plt.ylabel('인구')
plt.title('1인가구_주거형태_단독주택')
plt.legend()

# 그래프 표시
plt.show()

#%%

dfb = pd.read_excel('성_및_연령별_1인가구__시군구_20240514141842(수정).xlsx')

#%%
# 연령별 1인 가구 증감 추이

dfb = pd.read_excel('성별_및_연령별_1인가구.xlsx')

#%%

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 10))  # 그래프 크기 설정

dfb['20세_미만'] = round(dfb['20세_미만'] / 10000)
dfb['20~24'] = round(dfb['20~24'] / 10000)
dfb['25~29'] = round(dfb['25~29'] / 10000)
dfb['30~34'] = round(dfb['30~34'] / 10000)
dfb['35~39'] = round(dfb['35~39'] / 10000)
dfb['40~44'] = round(dfb['40~44'] / 10000)
dfb['50~54'] = round(dfb['50~54'] / 10000)
dfb['55~59'] = round(dfb['55~59'] / 10000)
dfb['60~64'] = round(dfb['60~64'] / 10000)
dfb['65~69'] = round(dfb['65~69'] / 10000)
dfb['70~74'] = round(dfb['70~74'] / 10000)
dfb['75~79'] = round(dfb['75~79'] / 10000)
dfb['80~84'] = round(dfb['80~84'] / 10000)
dfb['85세_이상'] = round(dfb['85세_이상'] / 10000, 2)

#%%

# 연령별 1인 가구 - 꺾은선 그래프

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 10))  # 그래프 크기 설정

plt.plot(dfb['연도'], dfb['20세_미만'], marker='o', linestyle='-', color='grey', label='20세_미만')
plt.plot(dfb['연도'], dfb['20~24'], marker='o', linestyle='-', color='yellow', label='20~24')
plt.plot(dfb['연도'], dfb['25~29'], marker='o', linestyle='-', color='orange', label='25~29')
plt.plot(dfb['연도'], dfb['30~34'], marker='o', linestyle='-', color='pink', label='30~34')
plt.plot(dfb['연도'], dfb['35~39'], marker='o', linestyle='-', color='skyblue', label='35~39')
plt.plot(dfb['연도'], dfb['40~44'], marker='o', linestyle='-', color='red', label='40~44')
plt.plot(dfb['연도'], dfb['50~54'], marker='o', linestyle='-', color='darkgoldenrod', label='50~54')
# plt.plot(dfb['연도'], dfb['55~59'], marker='o', linestyle='-', color='gold', label='55~59')
# plt.plot(dfb['연도'], dfb['60~64'], marker='o', linestyle='-', color='grey', label='60~64')
# plt.plot(dfb['연도'], dfb['70~74'], marker='o', linestyle='-', color='darkkhaki', label='70~74')
# plt.plot(dfb['연도'], dfb['75~79'], marker='o', linestyle='-', color='olive', label='75~79')
# plt.plot(dfb['연도'], dfb['80~84'], marker='o', linestyle='-', color='yellowgreen', label='80~84')
# plt.plot(dfb['연도'], dfb['85세_이상'], marker='o', linestyle='-', color='dodgerblue', label='85세_이상')

# 각 데이터 포인트에 수치 표시
for col in dfb.columns[0:10]:
    for i, txt in enumerate(dfb[col]):
        plt.annotate(txt, (dfb['연도'][i], dfb[col][i]), textcoords="offset points", xytext=(0,10), ha='right')

plt.xticks(rotation=55)

plt.xlabel('연도')
plt.ylabel('1인 가구')
plt.title('연령별 1인 가구 증감추이_20세미만~54세(단위 : 만 가구)')
plt.legend()
# plt.grid(True)
plt.show()

#%%

# 연령별 1인 가구 - 누적 막대 차트 그리기

plt.figure(figsize=(10, 10))  # 그래프 크기 설정

bar1 = plt.bar(dfb['연도'], dfb['20~24'], color='grey', label='20~24')
bar2 = plt.bar(dfb['연도'], dfb['25~29'], bottom=dfb['20~24'], color='yellow', label='25~29')
bar3 = plt.bar(dfb['연도'], dfb['30~34'], bottom=dfb['20~24'] + dfb['25~29'], color='orange', label='30~34')
bar4 = plt.bar(dfb['연도'], dfb['35~39'], bottom=dfb['20~24'] + dfb['25~29'] + dfb['30~34'], color='pink', label='35~39')
bar5 = plt.bar(dfb['연도'], dfb['40~44'], bottom=dfb['20~24'] + dfb['25~29'] + dfb['30~34'] + dfb['35~39'], color='skyblue', label='40~44')

plt.xticks(rotation=55)

plt.xlabel('연도')
plt.ylabel('1인 가구')
plt.title('연령별 1인 가구 증감추이_20~44세(단위 : 만 가구)')
plt.legend()
# plt.grid(True)
plt.show()