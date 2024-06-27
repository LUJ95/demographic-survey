# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 11:21:05 2024

@author: bigdata
"""
#%%
# 아파트매매거래량 크롤링
import requests
import pandas as pd

# API URL 설정
api_url = "https://kosis.kr/openapi/Param/statisticsParameterData.do?method=getList&apiKey=MGI2MWUxZGUxOTc1MzQ5NWNjNzgyYTI1NzIyNjZkMDE=&itmId=13103114433T1+&objL1=13102114433A.0001+13102114433A.0002+13102114433A.0003+13102114433A.0004+13102114433A.0005+13102114433A.0006+13102114433A.0007+13102114433A.0008+13102114433A.0009+13102114433A.0010+13102114433A.0011+13102114433A.0012+13102114433A.0013+13102114433A.0014+13102114433A.0015+13102114433A.0016+13102114433A.0017+13102114433A.0018+13102114433A.0019+&objL2=&objL3=&objL4=&objL5=&objL6=&objL7=&objL8=&format=json&jsonVD=Y&prdSe=M&startPrdDe=201301&endPrdDe=202312&orgId=408&tblId=DT_408_2006_S0049"

# API 요청
response = requests.get(api_url)
response.raise_for_status()

# JSON 데이터 파싱
data = response.json()

# 필요한 데이터 추출
extracted_data = []
for item in data:
    extracted_data.append({
        '시점': item.get('PRD_DE'),
        '지역': item.get('C1_NM'),
        '값': item.get('DT')
    })

# 데이터프레임으로 변환
df = pd.DataFrame(extracted_data)

# 데이터 타입 변환 및 정리 (예: '값'을 숫자로 변환)
df['값'] = pd.to_numeric(df['값'], errors='coerce')

# 결과 출력
print(df.head())

# 데이터프레임 저장 (옵션)
df.to_excel('아파트매매거래량.xlsx', index=False)
