# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 09:20:21 2024

@author: Shin
"""
# 사용자 분류

import pandas as pd

# columns_name : 나이 / 예산 / 가족 구성원 수 / 등급  
information = pd.DataFrame([[20, 15000, '1'], [30, 30000, '2'], [40, 50000, '4'],
                 [50, 100000, '3'], [60, 65000, '5'], [70, 45000, '2'],
                 [80, 30000, '1'], [90, 200000, '3']],
                 index = ['신정윤님', '박주찬님', '오승필님', '성우진님', '이의재님',
                          '파이썬님', '딥러닝님', '판다스님'],
                columns = ['age', 'budget', 'family_member'])


information[information['budget'] <= 50000]
'''  
                 age  budget family_member
      신정윤님   20   15000             1
      박주찬님   30   30000             2
      오승필님   40   50000             4
      파이썬님   70   45000             2
      딥러닝님   80   30000             1'''

rank3 = information[(information['budget'] > 50000) & (information['budget'] < 100000)]
print(rank3)
'''
'          age  budget family_member
이의재님   60   65000             5'''
information[information['budget'] >= 100000]
'''
          age  budget family_member
성우진님   50  100000             3
판다스님   90  200000             3'''



information.to_excel('D:/WORKSPACE/github/MYSELF24/Python/MiniProject-May/seoulcity/user.xlsx')
