# -*- coding: utf-8 -*-

# 외국인 연도별 국내 체류 인구추이
# 데이터 : 통계청 - 국적(지역) 및 체류자격별 체류외국인 현황
# 파일명 : 국적_지역__및_체류자격별_체류외국인_현황_20240507152130.xlsx
# 링크 : https://kosis.kr/statHtml/statHtml.do?orgId=101&tblId=DT_1B81A21

#%%

# 패키지
import pandas as pd                  # 데이터프레임 가공
import numpy as np                   # 데이터프레임 수학 연산
import matplotlib.pyplot as plt      # 도표 패키지
import matplotlib.font_manager as fm # 글씨체 지정 패키지
import add_font as af
#%%

# 데이터 불러오기

df = pd.read_excel('국적_지역_및_체류자격별_체류외국인_현황_20240507152130(수정).xlsx')
print(df.head())
print(df.columns)

#%%

# 첫 번째 행 삭제

df = df.drop(df.index[0])

df = df.reset_index(drop=True)
print(df)

#%%

# 열 이름 중복으로 채우기

df = df.fillna(method='ffill', inplace=False)

#%%

# 칼렴 확인

print(df.columns)

#%%

# 칼럼이름 수정하기

new_columns = {'국적(지역)별(1)':'대륙별', '성별(1)':'성별'}
df = df.rename(columns=new_columns)

#%%

# '성별'칼럼에서 '남자', '여자' 들어가 있는 행 삭제

df = df[(df['성별'] != '남자') & (df['성별'] != '여자')]

#%%

# '성별' 칼럼 삭제

df = df.drop(columns=['성별'])

#%%

# '열'과 '행' 전환
df = df.transpose()

df.to_excel('외국인_체류현황.xlsx', index=False)  # 인덱스 미포함하여 저장

#%%

df = pd.read_excel('외국인_체류현황.xlsx')

#%%

# 열 이름 바꾸기
df = df.rename(columns={'Unnamed: 0': '연도'})

print(df)

#%%

# 단위 : 1 = 1만명으로 변경

df['총계'] = df['총계'] / 10000
df['아시아주계'] = df['아시아주계'] / 10000
df['북아메리카주계'] = df['북아메리카주계'] / 10000
df['남아메리카주계'] = df['남아메리카주계'] / 10000
df['유럽주계'] = df['유럽주계'] / 10000
df['오세아니아주계'] = df['오세아니아주계'] / 10000
df['아프리카주계'] = df['아프리카주계'] / 10000
df['기타계'] = df['기타계'] / 10000

#%%
af.reg()
plt.rcParams["font.family"] = 'NanumGothic'

# 폰트 지정 - 맑은 고딕
# font_path = 'C:/Users/OSP/Desktop/malgun.ttf'  # 맑은 고딕 폰트 경로
# fontprop = fm.FontProperties(fname=font_path, size=18)

# 한글 폰트 설정
# plt.rcParams['font.family'] = 'malgun'

#%%
# 시각화-1 (총계 기준)
plt.figure(figsize=(8, 6))  # 그래프 크기 설정
plt.bar(df['연도'], df['총계'], color='skyblue', 'lightgreen')
plt.xlabel('연도', fontproperties=fontprop)
plt.ylabel('체류자 수', fontproperties=fontprop)
plt.title('연도별 체류외국인 현황(총계기준)', fontproperties=fontprop)
plt.show()

#%%

df = pd.read_excel('외국인_체류현황_1.xlsx')

#%%

df['총계'] = df['총계'] / 10000
df['아시아주계'] = df['아시아주계'] / 10000
df['북아메리카주계'] = df['북아메리카주계'] / 10000
df['유럽주계'] = df['유럽주계'] / 10000
df['기타지역'] = df['기타지역'] / 10000

#%%

# 히스토그램으로 시각화 진행
# '남아메리카주계', '오세아니아주계', '아프리카주계', '기타계'는 '그외지역'으로 합산

plt.figure(figsize=(10, 10))  # 그래프 크기 설정
bar1 = plt.bar(df['연도'], df['총계'], color='skyblue', label='총계')
bar2 = plt.bar(df['연도'], df['아시아주계'], color='lightgreen', label='아시아주계')
bar3 = plt.bar(df['연도'], df['북아메리카주계'], color='orange', label='북아메리카주계')
bar4 = plt.bar(df['연도'], df['유럽주계'], color='purple', label='유럽주계')
bar5 = plt.bar(df['연도'], df['기타지역'], color='yellow', label='기타지역')

plt.xticks(rotation=55)

# 막대 위 값 표시
for rect in bar1:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.1d' % height, ha='center', va='bottom', size = 12, color='black')        

for rect in bar2:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.1d' % height, ha='center', va='bottom', size = 12, color='black')        

for rect in bar3:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.1d' % height, ha='center', va='bottom', size = 12, color='black')        

for rect in bar4:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.1d' % height, ha='center', va='bottom', size = 12, color='black') 

for rect in bar5:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.1d' % height, ha='center', va='top', size = 12, color='black')
    
plt.xlabel('연도')
plt.ylabel('체류자 수')
plt.title('연도별 체류외국인 현황(단위 : 만 명)')
# plt.legend(bbox_to_anchor=(1.05, 1))
plt.legend()
plt.show()

plt.rc('font', family='NaNumBarunGothic')
plt.rcParams['figure.dpi'] = 140
#%%

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 10))  # 그래프 크기 설정

# 각 열 데이터를 따로 처리하여 막대 그래프에 추가
bar1 = plt.bar(df['연도'], df['총계'], color='skyblue', label='총계')
bar2 = plt.bar(df['연도'], df['아시아주계'], color='lightgreen', label='아시아주계')
bar3 = plt.bar(df['연도'], df['북아메리카주계'], color='orange', label='북아메리카주계')
bar4 = plt.bar(df['연도'], df['남아메리카주계'], color='pink', label='남아메리카주계')
bar5 = plt.bar(df['연도'], df['유럽주계'], color='purple', label='유럽주계')
bar6 = plt.bar(df['연도'], df['오세아니아주계'], color='yellow', label='오세아니아주계')
bar7 = plt.bar(df['연도'], df['아프리카주계'], color='cyan', label='아프리카주계')
bar8 = plt.bar(df['연도'], df['기타계'], color='grey', label='기타계')

plt.xticks(rotation=55)

# 막대 위 값 표시
for rect in bar1:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.1d' % height, ha='center', va='bottom', size = 12, color='black')        

for rect in bar2:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.1d' % height, ha='center', va='bottom', size = 12, color='black')        

for rect in bar3:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.1d' % height, ha='center', va='bottom', size = 12, color='black')        

for rect in bar4:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.1d' % height, ha='center', va='bottom', size = 12, color='black')        

for rect in bar5:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.1d' % height, ha='center', va='bottom', size = 12, color='black')        

for rect in bar6:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.1d' % height, ha='center', va='bottom', size = 12, color='black')        

for rect in bar7:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.1d' % height, ha='center', va='bottom', size = 12, color='black')        

for rect in bar8:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.1d' % height, ha='center', va='bottom', size = 12, color='b')        
plt.xlabel('연도')
plt.ylabel('체류자 수')
plt.title('연도별 체류외국인 현황(총계기준)')
# plt.legend(bbox_to_anchor=(1.05, 1))
plt.legend()
plt.show()

plt.rc('font', family='NaNumBarunGothic')
plt.rcParams['figure.dpi'] = 140

#%%

dft = pd.read_excel('외국인_방문_목적_전처리(상위10).xlsx')

# 2013년 ~ 2022년 합산 기준 상위 10개 방문 목적
"""
재외동포(F-4)
비전문취업(E-9)
방문취업(H-2)
단기방문(C-3)
사증면제(B-1)
영주(F-5)
결혼이민(F-6)
관광통과(B-2)
방문동거(F-1)
유학(D-2)
"""

# 해석
"""
재외동포(F-4): 대한민국 국적을 가지고 있으나 외국에 거주하는 한국인을 가리킵니다. F-4 비자는 재외동포를 위한 비자입니다.
비전문취업(E-9): 전문성이 필요하지 않은 일자리로 근로자들을 대상으로 하는 비자 유형입니다.
방문취업(H-2): 짧은 기간 동안의 일자리를 위해 방문하는 비자입니다.
단기방문(C-3): 단기 여행이나 비즈니스를 위해 방문하는 비자입니다.
사증면제(B-1): 일부 국가의 국민은 사증이나 비자 없이 한국을 방문할 수 있습니다.
영주(F-5): 외국인이 한국에서 영구적으로 거주하고 싶을 때 받는 비자 유형입니다.
결혼이민(F-6): 외국인과 대한민국 국민이 결혼하여 대한민국에 거주하고자 할 때 취득하는 비자입니다.
관광통과(B-2): 한국을 비롯한 일부 국가로 여행을 하다가 다른 국가로 이동하기 위해 한국을 경유하는 비자입니다.
방문동거(F-1): 외국인이 한국에 잠시 머물기 위해 가족, 친구 등과 동거하며 체류하는 비자입니다.
유학(D-2): 외국인이 대한민국에서 학업을 하기 위해 필요한 비자입니다.
"""
#%%

dft['총계'] = dft['총계'] / 10000
dft['재외동포(F-4)'] = dft['재외동포(F-4)'] / 10000
dft['비전문취업(E-9)'] = dft['비전문취업(E-9)'] / 10000
dft['방문취업(H-2)'] = dft['방문취업(H-2)'] / 10000
dft['단기방문(C-3)'] = dft['단기방문(C-3)'] / 10000
dft['사증면제(B-1)'] = dft['사증면제(B-1)'] / 10000
dft['영주(F-5)'] = dft['영주(F-5)'] / 10000
dft['결혼이민(F-6)'] = dft['결혼이민(F-6)'] / 10000
dft['관광통과(B-2)'] = dft['관광통과(B-2)'] / 10000
dft['방문동거(F-1)'] = dft['방문동거(F-1)'] / 10000
dft['유학(D-2)'] = dft['유학(D-2)'] / 10000
dft['기타(Others)'] = dft['기타(Others)'] / 10000

#%%

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 10))  # 그래프 크기 설정

# 각 열 데이터를 따로 처리하여 막대 그래프에 추가
bar1 = plt.bar(dft['연도'], dft['총계'], color='skyblue', label='총계')
bar2 = plt.bar(dft['연도'], dft['기타(Others)'], color='grey', label='기타')
bar3 = plt.bar(dft['연도'], dft['비전문취업(E-9)'], color='pink', label='비전문취업')
bar4 = plt.bar(dft['연도'], dft['방문취업(H-2)'], color='yellow', label='방문취업')
bar5 = plt.bar(dft['연도'], dft['영주(F-5)'], color='cyan', label='영주')
bar6 = plt.bar(dft['연도'], dft['결혼이민(F-6)'], color='grey', label='결혼이민')
bar7 = plt.bar(dft['연도'], dft['유학(D-2)'], color='red', label='유학')
bar9 = plt.bar(dft['연도'], dft['관광통과(B-2)'], color='black', label='관광통과')
bar10 = plt.bar(dft['연도'], dft['방문동거(F-1)'], color='brown', label='방문동거')

plt.xticks(rotation=55)

# 막대 위 값 표시
for rect in bar1:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.1d' % height, ha='center', va='bottom', size = 12, color='black')        

plt.xlabel('연도')
plt.ylabel('체류 목적')
plt.title('목적별 외국인 체류자 수(단위: 만 명)')
# plt.legend(bbox_to_anchor=(1.05, 1))
plt.legend()
plt.show()
#%%

dft = pd.read_excel('외국인_방문_목적_전처리(상위4).xlsx')


# Top 4만 시각화
dft['총계'] = dft['총계'] / 10000
dft['기타(Others)'] = dft['기타(Others)'] / 10000
dft['비전문취업(E-9)'] = dft['비전문취업(E-9)'] / 10000
dft['방문취업(H-2)'] = dft['방문취업(H-2)'] / 10000
dft['영주(F-5)'] = dft['영주(F-5)'] / 10000
dft['결혼이민(F-6)'] = dft['결혼이민(F-6)'] / 10000

bar4 = plt.bar(dft['연도'], dft['영주(F-5)'], bottom=dft['방문취업(H-2)'], label='영주', color='cyan')
bar5 = plt.bar(dft['연도'], dft['결혼이민(F-6)'], bottom=dft['영주(F-5)'], label='결혼이민', color='brown')

plt.xticks(rotation=55)

# 막대 위 값 표시
for rect in bar1:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.1d' % height, ha='center', va='bottom', size = 12, color='black')

for rect in bar2:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.1d' % height, ha='center', va='bottom', size = 12, color='black')        
    
for rect in bar3:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.1d' % height, ha='center', va='bottom', size = 12, color='black')        
    
for rect in bar4:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.1d' % height, ha='center', va='bottom', size = 12, color='black')        
    
for rect in bar5:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.1d' % height, ha='center', va='bottom', size = 12, color='black')        
    
plt.xlabel('연도')
plt.ylabel('체류 목적')
plt.title('목적별 외국인 체류자 수(단위: 만 명)')
# plt.legend(bbox_to_anchor=(1.05, 1))
plt.legend()
plt.show()

#%%

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 10))  # 그래프 크기 설정

bar1 = plt.bar(dft['연도'], dft['기타(Others)'], color='grey', label='기타')
bar2 = plt.bar(dft['연도'], dft['비전문취업(E-9)'], bottom=dft['기타(Others)'], color='yellow', label='비전문취업')
bar3 = plt.bar(dft['연도'], dft['방문취업(H-2)'], bottom=dft['기타(Others)'] + dft['비전문취업(E-9)'], color='pink', label='방문취업')
bar4 = plt.bar(dft['연도'], dft['영주(F-5)'], bottom=dft['기타(Others)'] + dft['비전문취업(E-9)'] + dft['방문취업(H-2)'], color='orange', label='영주')
bar5 = plt.bar(dft['연도'], dft['결혼이민(F-6)'], bottom=dft['기타(Others)'] + dft['비전문취업(E-9)'] + dft['방문취업(H-2)'] + dft['영주(F-5)'], color='skyblue', label='결혼이민')

# 레이블 순서를 변경하여 legend에 전달합니다.
plt.legend(handles=[bar5, bar4, bar3, bar2, bar1])

# 막대 위 값 표시
# for rect in bar1:
#     height = rect.get_height()
#     plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.1d' % height, ha='center', va='top', size = 12, color='black')        

# for rect in bar2:
#     height = rect.get_height()
#     plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.1d' % height, ha='center', va='top', size = 12, color='black')        

# for rect in bar3:
#     height = rect.get_height()
#     plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.1d' % height, ha='center', va='top', size = 12, color='black')        

# for rect in bar4:
#     height = rect.get_height()
#     plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.1d' % height, ha='center', va='top', size = 12, color='black')        

plt.xticks(rotation=55)
plt.xlabel('연도')
plt.ylabel('체류 목적')
plt.title('목적별 외국인 체류자 수(단위: 만 명)')
plt.show()
               

#%%

# 테이블 피벗하기
pivot_dft = dft.pivot(index='연도', columns='방문목적', values='Value')
pivot_dft = pivot_dft[['기타(Others)','비전문취업(E-9)','방문취업(H-2)','영주(F-5)','결혼이민(F-6)']].copy()
pivot_dft

import matplotlib.pyplot as plt
%matplotlib inline

# Stacked Bar Chart
pivot_df.plot.bar(stacked=True, figsize=(10,7))