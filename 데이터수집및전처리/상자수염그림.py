# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 16:30:34 2024

@author: bigdata
"""
#%%
# 머신러닝 변수 상자수염그림 그리기
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 한글 폰트 설정
font_path = "C:/Windows/Fonts/malgunbd.ttf"  # 자신이 사용하고 있는 한글 폰트의 경로로 변경해주세요.
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# Excel 파일에서 데이터 불러오기
file_path = '매매_실거래가격(비교)_수정_v11.xlsx'
sheet_name = 'Sheet1'  # 시트 이름에 따라 수정
df = pd.read_excel(file_path, sheet_name=sheet_name)

# 각 열 데이터에 대한 상자수염 그림 그리기
columns_to_plot = ['실거래가격지수', '지지율', 'PIR지수_전국', '매매수급동향', '소비자물가지수',
                   '종합부동산세_세율_개인', '아파트매매거래량', '주택담보대출']

plt.figure(figsize=(16, 12))

# 각 열 데이터에 대해 반복문으로 상자수염 그림 그리기
for i, column in enumerate(columns_to_plot, start=1):
    plt.subplot(4, 2, i)
    df[[column]].boxplot()
    plt.title(column)
    plt.ylabel('값')

plt.tight_layout()
plt.show()

#%%
# 머신러닝 변수 상자수염그림 그리기2
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 한글 폰트 설정
font_path = "C:/Windows/Fonts/malgunbd.ttf"  # 자신이 사용하고 있는 한글 폰트의 경로로 변경해주세요.
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# Excel 파일에서 데이터 불러오기
file_path = '매매_실거래가격(비교)_수정_v11.xlsx'
sheet_name = 'Sheet1'  # 시트 이름에 따라 수정
df = pd.read_excel(file_path, sheet_name=sheet_name)

# 각 열 데이터에 대한 상자수염 그림 그리기
columns_to_plot = ['실거래가격지수', '지지율', 'PIR지수_전국', '매매수급동향', '소비자물가지수',
                   '종합부동산세_세율_개인', '아파트매매거래량', '주택담보대출']

for column in columns_to_plot:
    plt.figure(figsize=(8, 6))  # 그래프 크기 설정
    df[[column]].boxplot()  # 상자수염 그림 그리기
    plt.title(f'상자수염 그림 - {column}')  # 그래프 제목 설정
    plt.ylabel('값')  # y축 레이블 설정
    plt.tight_layout()
    plt.show()  # 그래프 출력