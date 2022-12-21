설치한 라이브러리들은 아래와 같다.

```python
import numpy as np
import pandas as pd

# data 폴더 csv 불러올때 파일명확인
from glob import glob 

# type 변환
from datetime import datetime, timedelta

# 시각화
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('seaborn-whitegrid')
import missingno as msno

# 데이터 시각화
import plotly
import random

line_color = ['#FFBF00', '#FF7F50', '#DE3163', 
             '#9FE2BF', '#40E0D0', '#6495ED', 
             '#117A65', '#2471A3', '#CCCCFF', 
             '#8E44AD', '#CD5C5C', '#F08080', 
             '#FA8072', '#E9967A', '#FFA07A', ]

# for문 진행상황 tracking
from tqdm import tqdm

# 전처리
from sklearn import model_selection
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder

#ML 알고리즘
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from lightgbm.sklearn import LGBMRegressor
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.ensemble import StackingRegressor

# 모델 튜닝 및 평가
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import KFold
from sklearn.multioutput import MultiOutputRegressor
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error

# Feature 중요도 _ LightGBM
from lightgbm import plot_importance

# 경고 무시
import sys
import warnings
warnings.filterwarnings('ignore')
pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)

import joblib 
import os

import random
import requests
import calendar
import time
```

데이터를 로드하는 과정은 아래와 같다. test set은 여러 csv파일이 분할되어 제공되었기 때문에 이를 합쳐주려 `read_csv_by_dir` 함수를 만들었다.

```python
def read_csv_by_dir(path):
    df_raw = pd.DataFrame()
    #os.listdir()은 해당 경로에 있는 파일들을 리스트로 만들어줌
    for files in tqdm(os.listdir(path)):
        if files.endswith('.csv'):
            df = pd.read_csv('/'.join([path, files]))
        df_raw = pd.concat((df_raw, df), axis=0)
    return df_raw
 
 
def load_files(): 
  # test 파일 불러오기
  path = 'Z:/team/과제2_dataset/dataset'
  test_raw = read_csv_by_dir('/'.join([path, 'test']))
  test_raw.to_csv('./test_raw.csv') # 병합된 test 파일을 아예 하나의 csv 파일로 저장해서 불러오기 용이하게 함
  test_raw = pd.read_csv('Z:/team/과제2_dataset/dataset/test_raw/test_raw.csv')
  test_raw.sort_values(by='TIME', inplace=True)
  test_raw = test_raw.reset_index(drop=True, inplace=True)

  #train 파일 불러오기
  train_raw = pd.read_csv('Z:/team/과제2_dataset/dataset/train/train.csv')

  #제출 파일 불러오기
  submission_sample_raw = pd.read_csv('Z:/team/과제2_dataset/dataset/submission_sample.csv')
```
 
불러온 파일들의 원본은 유지한다.
```python 
train = train_raw.copy()
test = test_raw.copy()
submission = submission_sample_raw.copy()
```

제공된 데이터들의 time변수는 모두 문자형이다. 이를 `to_datetime()` 함수로 날짜형으로 변경해준다. 그리고 time변수에 밀리초 단위가 5밀리초씩 늦은 데이터가 간혹 있는데, 이를 정각에 맞춰주기 위해 아래와 같은 처리를 해준다.
```python
def time_preprocessing():

    # time컬럼을 문자형에서 날짜 타입으로 변경
    train.TIME = pd.to_datetime(train['TIME'])
    test.TIME = pd.to_datetime(test['TIME'])
    train.reset_index(drop=True, inplace=True)
    test.reset_index(drop=True, inplace=True)

    #밀리초 단위가 5밀리초씩 늦은 row가 있어서 이를 정각으로 맞춰주기 위한 작업
    from datetime import datetime, timedelta
    train['MINUTE']=train['TIME'].dt.minute
    train['MOD']=train['MINUTE']%10
    train.loc[train['MOD'] == 9, 'TIME'] = train['TIME']+timedelta(milliseconds=5)
    train.drop(['MINUTE','MOD'], axis=1, inplace=True)

    test['MINUTE']=test['TIME'].dt.minute
    test['MOD']=test['MINUTE']%10
    test.loc[test['MOD'] == 9, 'TIME'] = test['TIME']+timedelta(milliseconds=5)
    test.drop(['MINUTE','MOD'], axis=1, inplace=True)
```

분석을 위해 기상청 외부데이터를 수집하기로 했다. 이는 탱크의 압력이 기온이나 습도 등에 분명한 영향을 받을 것으로 사료되기 때문이다. 대회의 분석 대상은 삼척 LNG 기지인데, 이에 인접한 기상청 3군데를 선정했고 해당 기상청의 데이터를 기본 제공 데이터와 합쳐주는 함수를 만들었다.

```python
def weather_generator(location):
    #동해, 원덕, 궁촌 3개 중 1개만 실행
    if location == "donghae":
        #동해 기상데이터 불러오기
        df_2019 = pd.read_csv('Z:/team/donghae_weather/donghae_weather_2019.csv', encoding='cp949')
        df_2020 = pd.read_csv('Z:/team/donghae_weather/donghae_weather_2020.csv', encoding='cp949')
        df_2021 = pd.read_csv('Z:/team/donghae_weather/donghae_weather_2021.csv', encoding='cp949')
        weather_test = pd.read_csv('Z:/team/donghae_weather/donghae_weather_test.csv', encoding='cp949')
        
    elif location == "wondeok":
        #원덕읍 기상데이터 불러오기
        df_2019 = pd.read_csv('Z:/team/1111_upload/wondeok_weather_2019.csv', encoding='cp949')
        df_2020 = pd.read_csv('Z:/team/1111_upload/wondeok_weather_2020.csv', encoding='cp949')
        df_2021 = pd.read_csv('Z:/team/1111_upload/wondeok_weather_2021.csv', encoding='cp949')
        weather_test = pd.read_csv('Z:/team/1111_upload/wondeok_weather_test.csv', encoding='cp949')

    elif location == "goongchon":
        #궁촌 기상데이터 불러오기
        df_2019 = pd.read_csv('Z:/team/1111_upload/goongchon_weather_2019.csv', encoding='cp949')
        df_2019 = df_2019[:8661]
        df_2020 = pd.read_csv('Z:/team/1111_upload/goongchon_weather_2020.csv', encoding='cp949')
        df_2020 = df_2020[:8784]
        df_2021 = pd.read_csv('Z:/team/1111_upload/goongchon_weather_2021.csv', encoding='cp949')
        df_2021 = df_2021[:744]
        weather_test = pd.read_csv('Z:/team/1111_upload/goongchon_weather_test.csv', encoding='cp949')
        weather_test = weather_test[:7343]

    #train set에 쓰이는 기상 데이터 3개년도를 합치고 가공
    donghae_result = pd.concat([df_2019, df_2020, df_2021], ignore_index=True)
    donghae_result.rename(columns={'일시':'TIME'}, inplace=True)
    donghae_result['TIME']=pd.to_datetime(donghae_result['TIME'])

    #test set에 쓰이는 기상 데이터 가공
    weather_test.rename(columns={'일시':'TIME'}, inplace=True)
    weather_test['TIME']=pd.to_datetime(weather_test['TIME'])

    #원하는 컬럼만 갖고오기
    donghae_temp_train = donghae_result.loc[:, ['TIME', '기온(°C)', '습도(%)', '증기압(hPa)', '현지기압(hPa)']]
    weather_test = weather_test.loc[:, ['TIME', '기온(°C)', '습도(%)', '증기압(hPa)', '현지기압(hPa)']]

    #결측치 보간
    donghae_temp_train = donghae_temp_train.set_index('TIME')
    donghae_temp_train = donghae_temp_train.interpolate(method = 'time')
    donghae_temp_train.reset_index(drop = False, inplace = True)

    #결측치 보간
    weather_test = weather_test.set_index('TIME')
    weather_test = weather_test.interpolate(method = 'time')
    weather_test.reset_index(drop = False, inplace = True)

    print("기상청 데이터를 10분단위로 생성합니다.")
    #날씨데이터는 정각의 데이터밖에 없다.
    #10분 단위로 데이터를 생성해주기 위한 작업이다.
    weather_test_ = weather_test
    new_row = pd.DataFrame({'TIME':[np.NaN,np.NaN,np.NaN,np.NaN,np.NaN]}
                          )
    j=0
    for i in tqdm(range(1, weather_test_.shape[0]+1)):
        weather_test_ = pd.concat([weather_test_.iloc[:i+j], new_row, weather_test_.iloc[i+j:]], ignore_index=True)
        j+=5

    weather_test__ = weather_test_

    for i in tqdm(range(weather_test__.shape[0])):
        weather_test__.iloc[i+1:i+2,[0]] = weather_test__.iloc[i:i+1,[0]]+timedelta(minutes=10)

    weather_test__ = weather_test__.set_index('TIME')
    weather_test__ = weather_test__.interpolate(method = 'time')
    weather_test__.reset_index(drop = False, inplace = True)

    weather_test = weather_test__
    print("기상청 데이터 생성이 완료됐습니다.")

    weather_test['TIME']=pd.to_datetime(weather_test['TIME'])
    
    global train
    global test
    
    train_temp_join = pd.merge(train, donghae_temp_train, left_on='TIME', right_on='TIME', how='left')
    test_temp_join = pd.merge(test, weather_test, left_on='TIME', right_on='TIME', how='left')

    train_temp_join.set_index('TIME', inplace=True)
    train_temp_join = train_temp_join.interpolate(method='time', inplace=True)
    train_temp_join.reset_index(drop = False, inplace = True)
    train_temp_join.rename(columns={'기온(°C)':'TEMP', '습도(%)':'HUMID', '증기압(hPa)':'VAPOR', '현지기압(hPa)':'PRESS'}, inplace=True)
    test_temp_join.rename(columns={'기온(°C)':'TEMP', '습도(%)':'HUMID', '증기압(hPa)':'VAPOR', '현지기압(hPa)':'PRESS'}, inplace=True)

    #날씨 정보가 추가된 버전으로 train 덮어쓰기
    train = train_temp_join
    #날씨 정보가 추가된 버전으로 test 덮어쓰기
    test = test_temp_join
    
    return train, test
    
train, test = weather_generator("donghae")
```
기상청 데이터를 10분단위로 생성합니다.
100%|█████████████████████████████████████████████████████████████████████████████| 7344/7344 [00:19<00:00, 367.78it/s]
100%|██████████████████████████████████████████████████████████████████████████| 44064/44064 [00:32<00:00, 1366.25it/s]
기상청 데이터 생성이 완료됐습니다.

<br>

이제 데이터의 결측치와 이상치를 확인해야 한다. `info()`함수를 통해 확인해보니 결측치는 없는 것으로 확인되었다. 이상치를 확인하기 위해서는 iqr method를 기준으로 이상치 판독 함수를 만들고, 그래프를 그려 개형에서 튀는 부분이 있는지 확인해볼 것이다.
```python
#이상치 판독 함수
def outlier(sets, column):
    q1 = sets[column].quantile(0.25)
    q3 = sets[column].quantile(0.75)
    iqr = q3-q1
    top_fence = sets[sets[column] > q3+1.5*iqr].shape[0]
    bottom_fence = sets[sets[column] < q1-1.5*iqr].shape[0] 
    print("----{}----".format(column))
    print("이상치 범위는 {:.3f}이상, {:.3f}이하".format(q3+1.5*iqr,q1-1.5*iqr))
    print("큰 이상치 값의 개수는 {}개이고 전체 중 {:.3f}%".format(top_fence, (top_fence/sets.shape[0])*100))
    print("작은 이상치 값의 개수는 {}개이고 전체 중 {:.3f}%".format(bottom_fence, (bottom_fence/sets.shape[0])*100))
```

```python
#전체 변수들의 그래프를 그려보고 추이를 확인
#이상치가 의심되는 그래프들은 해당 그래프 하나만 크게 다시 그려보자
plot_list = list(train.columns)
plot_list.remove('TIME')

plt.figure(figsize=(30,10))

idx=1
for var in plot_list:
    plt.subplot(4,4,idx)
    plt.plot(train['TIME'], train[var])
    plt.title(var)
    idx+=1
```
<img src="https://user-images.githubusercontent.com/115082062/208907879-8cdf3d2c-2962-4eb7-b39c-5e614faf5482.png">

