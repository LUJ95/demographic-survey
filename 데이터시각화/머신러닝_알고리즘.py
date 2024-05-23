# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense

# 데이터 불러오기
data = pd.read_excel('매매_실거래가격(비교)_수정.xlsx')
data.set_index('연도_월', inplace=True)
real_price_index = data['실거래가격지수']

# 결측값 대체
real_price_index.fillna(method='bfill', inplace=True)  # 이전 값으로 대체

# 데이터 전처리
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(real_price_index.values.reshape(-1, 1))

# LSTM 입력 데이터 생성
def create_dataset(data, time_step):
    X, y = [], []
    for i in range(len(data) - time_step):
        X.append(data[i:(i + time_step), 0])
        y.append(data[i + time_step, 0])
    return np.array(X), np.array(y)

time_step = 3  # 시간 스텝 설정 (조정 가능)
X, y = create_dataset(scaled_data, time_step)

# LSTM 모델 구성
model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(time_step, 1)))
model.add(LSTM(units=50))
model.add(Dense(units=1))
model.compile(optimizer='adam', loss='mean_squared_error')

# 모델 학습
model.fit(X, y, epochs=100, batch_size=32, verbose=1)

# 결측값 대체할 데이터 선택 (2013년 1월부터 2014년 2월까지)
start_date = '2013-01-01'
end_date = '2014-02-01'
missing_data = real_price_index[start_date:end_date].copy()

# 데이터 전처리 및 예측
missing_scaled_data = scaler.transform(missing_data.values.reshape(-1, 1))
missing_X, _ = create_dataset(missing_scaled_data, time_step)
missing_predict = model.predict(missing_X)
missing_predict = scaler.inverse_transform(missing_predict)

# 대체된 값으로 실제 데이터 업데이트
real_price_index[start_date:end_date] = np.nan  # 결측값으로 초기화
real_price_index[start_date:end_date].iloc[time_step:time_step+len(missing_predict)] = missing_predict.flatten()

# 결과 출력
print("결측값 대체 완료.")