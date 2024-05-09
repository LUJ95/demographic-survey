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



