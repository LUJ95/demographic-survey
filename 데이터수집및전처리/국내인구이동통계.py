# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 09:45:30 2024

@author: bigdata
"""
#%%
# 국내인구이동통계 크롤링 코드
import requests
import pandas as pd

# URL 정의
url = "https://kosis.kr/openapi/Param/statisticsParameterData.do?method=getList&apiKey=MGI2MWUxZGUxOTc1MzQ5NWNjNzgyYTI1NzIyNjZkMDE=&itmId=T10+T20+T25+T30+T31+T32+T40+T50+&objL1=00+11+26+27+28+29+30+31+36+41+51+43+44+52+46+47+48+50+&objL2=&objL3=&objL4=&objL5=&objL6=&objL7=&objL8=&format=json&jsonVD=Y&prdSe=M&startPrdDe=201301&endPrdDe=202312&orgId=101&tblId=DT_1B26001_A01"

# GET 요청 보내기
response = requests.get(url)
data = response.json()

# JSON 데이터를 DataFrame으로 변환
df = pd.DataFrame(data)

# DataFrame을 엑셀 파일로 저장
output_file = "국내인구이동통계.xlsx"
df.to_excel(output_file, index=False)

print(f"데이터가 {output_file} 파일로 저장되었습니다.")
#%%
import pandas as pd

# 파일 경로
file_path = './국내인구이동통계.xlsx'

# 엑셀 파일 읽기
data = pd.read_excel(file_path)

# 지역별 데이터프레임 생성 및 피벗
region_dfs = []

for region, group in data.groupby('C1_NM'):
    pivot_df = group.pivot(index='PRD_DE', columns='ITM_NM', values='DT')
    # 지역명을 열로 추가
    pivot_df['지역'] = region
    # 열 순서 변경: '지역' 열을 최상단으로 올리기
    pivot_df = pivot_df[['지역'] + [col for col in pivot_df.columns if col != '지역']]
    region_dfs.append(pivot_df.reset_index())

# 모든 지역별 데이터프레임을 하나로 합치기
combined_df = pd.concat(region_dfs, ignore_index=True)

# 전체 데이터를 CSV 파일로 저장
combined_df.to_csv('국내인구이동통계.csv', encoding='utf-8-sig', index=False)

print("전체 데이터가 포함된 CSV 파일 저장이 완료되었습니다.")
#%%
import pandas as pd

# 파일 경로
file_path = './국내인구이동통계.xlsx'

# 엑셀 파일 읽기
data = pd.read_excel(file_path)

# 지역별 데이터프레임 생성 및 피벗
region_dfs = []

for region, group in data.groupby('C1_NM'):
    pivot_df = group.pivot(index='PRD_DE', columns='ITM_NM', values='DT')
    # 지역명을 열로 추가
    pivot_df['지역'] = region
    # 열 순서 변경: '지역' 열을 최상단으로 올리기
    pivot_df = pivot_df[['지역'] + [col for col in pivot_df.columns if col != '지역']]
    region_dfs.append(pivot_df.reset_index())

# 각 지역별로 엑셀 파일로 저장
excel_writer = pd.ExcelWriter('국내인구이동통계_지역별.xlsx', engine='xlsxwriter')

for i, df in enumerate(region_dfs):
    sheet_name = f'지역_{i+1}'
    df.to_excel(excel_writer, sheet_name=sheet_name, index=False)

excel_writer.close()

print("각 지역별 엑셀 파일 저장이 완료되었습니다.")
