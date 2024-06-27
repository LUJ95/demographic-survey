# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 17:18:49 2024

@author: bigdata
"""
#%%
# 소비자물가지수 크롤링
import requests
import pandas as pd

# API URL 설정
api_url = "https://kosis.kr/openapi/Param/statisticsParameterData.do?method=getList&apiKey=MGI2MWUxZGUxOTc1MzQ5NWNjNzgyYTI1NzIyNjZkMDE=&itmId=T+&objL1=T10&objL2=&objL3=&objL4=&objL5=&objL6=&objL7=&objL8=&format=json&jsonVD=Y&prdSe=M&startPrdDe=201301&endPrdDe=202312&orgId=101&tblId=DT_1J22003"

# API 요청
response = requests.get(api_url)
response.raise_for_status()  # 요청 실패 시 예외 발생

# JSON 데이터 파싱
data = response.json()

# 필요한 데이터 추출
extracted_data = []
for item in data:  # 리스트에서 데이터 추출
    extracted_data.append({
        '시점': item.get('PRD_DE'),
        '항목명': item.get('ITM_NM'),
        '값': item.get('DT')
    })

# 데이터프레임으로 변환
df = pd.DataFrame(extracted_data)

# 데이터 타입 변환 및 정리 (예: '값'을 숫자로 변환)
df['값'] = pd.to_numeric(df['값'], errors='coerce')

# 결과 출력
print(df.head())

# 데이터프레임 저장 (옵션)
df.to_excel('소비자물가지수.xlsx', index=False)