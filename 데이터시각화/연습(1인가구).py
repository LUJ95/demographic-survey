# -*- coding: utf-8 -*-

#%%
# 데이터 불러오기
dfa = pd.read_excel('1인가구_주거형태_비중1.xlsx')

#%%

# 꺾은선 그래프로 2015 ~ 2022년 주거형태별 1인 가구 현황 나타내기

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 10))  # 그래프 크기 설정


dfa['기타'] = round(dfa['기타'] / 10000, 2)
dfa['다세대주택'] = round(dfa['다세대주택'] / 10000, 2)
dfa['단독주택'] = round(dfa['단독주택'] / 10000, 2)
dfa['비거주용건물내 주택'] = round(dfa['비거주용건물내 주택'] / 10000, 2)
dfa['아파트'] = round(dfa['아파트'] / 10000, 2)
dfa['연립주택'] = round(dfa['연립주택'] / 10000, 2)

# 꺾은선 그래프
plt.plot(dfa['연도'], dfa['단독주택'], marker='o', linestyle='-', color='grey', label='단독주택')
plt.plot(dfa['연도'], dfa['아파트'], marker='o', linestyle='-', color='yellow', label='아파트')
plt.plot(dfa['연도'], dfa['기타'], marker='o', linestyle='-', color='orange', label='기타')
plt.plot(dfa['연도'], dfa['다세대주택'], marker='o', linestyle='-', color='pink', label='다세대주택')
plt.plot(dfa['연도'], dfa['비거주용건물내 주택'], marker='o', linestyle='-', color='skyblue', label='비거주용건물내 주택')
plt.plot(dfa['연도'], dfa['연립주택'], marker='o', linestyle='-', color='red', label='연립주택')

# 각 데이터 포인트에 수치 표시
for col in dfa.columns[1:]:
    for i, txt in enumerate(dfa[col]):
        plt.annotate(txt, (dfa['연도'][i], dfa[col][i]), textcoords="offset points", xytext=(0,10), ha='right')

plt.xticks(rotation=55)

plt.xlabel('연도')
plt.ylabel('1인 가구')
plt.title('주거형태별 1인 가구 현황(단위 : 만 가구)')
plt.legend()
# plt.grid(True)
plt.show()
