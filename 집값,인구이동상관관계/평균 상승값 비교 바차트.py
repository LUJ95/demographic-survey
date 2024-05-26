# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager

# 한글 폰트 설정
font_path = "C:/Windows/Fonts/malgunbd.ttf"
plt.rcParams['font.family'] = 'Malgun Gothic'

# 주어진 데이터
data = {
    "행정구역별(1)": ["전국", "서울", "부산", "대구", "인천", "광주", "대전", "울산", "세종", "경기", "강원", "충북", "충남", "전북", "전남", "경북", "경남", "제주"],
    "2023.12": [122.0, 157.0, 105.1, 102.1, 120.4, 126.4, 141.2, 99.0, 129.9, 135.2, 111.5, 109.1, 104.5, 108.6, 107.5, 100.2, 96.7, 108.1]
}

# 전국 평균 값
national_average = 122.0

# 색상 설정
colors = ["blue" if value < national_average else "red" for value in data["2023.12"]]

# 바 차트 그리기
plt.figure(figsize=(10, 6))
plt.bar(data["행정구역별(1)"], data["2023.12"], color=colors)
plt.axhline(y=national_average, color="gray", linestyle="--", label="전국 평균")
plt.xlabel("행정구역")
plt.ylabel("지수 (2017.11 = 100.0)")
plt.title("지역별 지수 (2023년 12월)")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()