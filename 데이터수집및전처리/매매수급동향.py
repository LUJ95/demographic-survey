# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 09:49:17 2024

@author: bigdata
"""
#%%
# 매매수급동향 크롤링
import requests
import pandas as pd

# API URL 설정
api_url = "https://kosis.kr/openapi/Param/statisticsParameterData.do?method=getList&apiKey=MGI2MWUxZGUxOTc1MzQ5NWNjNzgyYTI1NzIyNjZkMDE=&itmId=index+&objL1=01+&objL2=a0+&objL3=&objL4=&objL5=&objL6=&objL7=&objL8=&format=json&jsonVD=Y&prdSe=M&startPrdDe=201301&endPrdDe=202312&orgId=408&tblId=DT_40803_N0007"

try:
    # API 요청
    response = requests.get(api_url)
    response.raise_for_status()  # HTTP 오류 발생 시 예외 처리

    # JSON 데이터 파싱
    data = response.json()

    # 응답 데이터가 바로 배열로 포함된 경우
    if isinstance(data, list):
        extracted_data = []
        for item in data:
            extracted_data.append({
                '시점': item.get('PRD_DE'),
                '항목': item.get('C1_NM'),
                '값': item.get('DT')
            })

        # 데이터프레임으로 변환
        df = pd.DataFrame(extracted_data)

        # 데이터 타입 변환 및 정리 (예: '값'을 숫자로 변환)
        df['값'] = pd.to_numeric(df['값'], errors='coerce')

        # 결과 출력
        print(df.head())

        # 데이터프레임 저장 (옵션)
        df.to_excel('매매수급동향.xlsx', index=False)

    else:
        raise ValueError("Unexpected JSON format")

except requests.exceptions.HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except ValueError as val_err:
    print(f'Value error: {val_err}')
except Exception as err:
    print(f'Other error occurred: {err}')