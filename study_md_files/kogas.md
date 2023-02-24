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
  
  return test_raw, train_raw, submission_sample_raw
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
    
    return test, train
```

분석을 위해 기상청 외부데이터를 수집하기로 했다. 이는 탱크의 압력이 기온이나 습도 등에 분명한 영향을 받을 것으로 사료되기 때문이다. 대회의 분석 대상은 삼척 LNG 기지인데, 이에 인접한 기상청 3군데를 선정했고 해당 기상청의 데이터를 기본 제공 데이터와 합쳐주는 함수를 만들었다. 3군데 중 최종적으로 택한 곳은 동해였다. 선택 이유는 발표자료 슬라이드로 설명을 갈음한다.

<img src="https://user-images.githubusercontent.com/115082062/208942571-3bb76bdb-4e14-4685-8e81-884932dc9d52.png">

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

<br>

아래와 같은 식으로 이상치를 판별하게 된다.
```python
outlier(test,'PRESSURE-S')
outlier(test,'PRESS')
outlier(test,'FY_SUM')
outlier(test,'TI_MEAN')
outlier(test, 'LP_TOTAL')
outlier(test, 'STN-MFR-S')
outlier(test, 'FI_SUM')
```
----PRESSURE-S----
이상치 범위는 103.800이상, 98.200이하
큰 이상치 값의 개수는 0개이고 전체 중 0.000%
작은 이상치 값의 개수는 5739개이고 전체 중 17.366%
----PRESS----
이상치 범위는 1032.383이상, 987.450이하
큰 이상치 값의 개수는 0개이고 전체 중 0.000%
작은 이상치 값의 개수는 0개이고 전체 중 0.000%
----FY_SUM----
이상치 범위는 46.748이상, 9.450이하
큰 이상치 값의 개수는 67개이고 전체 중 0.203%
작은 이상치 값의 개수는 2개이고 전체 중 0.006%
----TI_MEAN----
이상치 범위는 -133.341이상, -149.931이하
큰 이상치 값의 개수는 0개이고 전체 중 0.000%
작은 이상치 값의 개수는 1482개이고 전체 중 4.484%
----LP_TOTAL----
이상치 범위는 869.165이상, 66.477이하
큰 이상치 값의 개수는 383개이고 전체 중 1.159%
작은 이상치 값의 개수는 0개이고 전체 중 0.000%
----STN-MFR-S----
이상치 범위는 775.722이상, 19.494이하
큰 이상치 값의 개수는 62개이고 전체 중 0.188%
작은 이상치 값의 개수는 0개이고 전체 중 0.000%
----FI_SUM----
이상치 범위는 45.285이상, 4.789이하
큰 이상치 값의 개수는 552개이고 전체 중 1.670%
작은 이상치 값의 개수는 0개이고 전체 중 0.000%

이상치 보간이 필요한 경우엔 아래 함수를 이용해 보간을 해주었다. train set의 경우 data leakage를 신경 쓰지 않고 time 방식으로 `interpolate` 시켰다.  `interpolate` 함수의 method를 time으로 설정하면 결측치들을 시간의 흐름에 맞게 보간해준다.

```python
#이상치 보간이 필요한 columns list
remove_list = ["PRESS", "PRESSURE-S", "LP_TOTAL", "STN-MFR-S", "FI_SUM"] 

#이상치 보간해주는 함수
def remove_outlier(remove_list,method_):
    global train
    for var in remove_list:
        q1 = train[var].quantile(0.25)
        q3 = train[var].quantile(0.75)
        iqr = q3-q1
        train.loc[train[var]<=q1-1.5*iqr, var] = np.NaN
        train.loc[train[var]>=q3+1.5*iqr, var] = np.NaN
        train = train.set_index('TIME')
        train = train.interpolate(method=method_)
        train.reset_index(drop=False, inplace=True)
    return train

train = remove_outlier(remove_list,"time")
```

특히, `STN-MFR-S` 변수의 경우에는 Outlier 함수로는 잡히지 않았지만 그래프에서 극단적으로 낮은 부분을 발견하게 되었고, 이것들이 완전 무작위 결측(MCAR)일 것이란 판단 하에 보간해주었다.
```python
train.loc[train['STN-MFR-S'] < 2, 'STN-MFR-S'] = np.NaN
train = train.set_index('TIME')
train = train.interpolate(method='time')
train.reset_index(drop=False, inplace=True)
```

이제 test set의 이상치와 결측치를 처리해줘야 한다. train set과 다르게 data leakage를 주의해야 하기에 굉장히 조심스러운 부분이었다. 특히 `PRESSURE-S`변수는 이상치가 전체 중 17%에 육박하여 아예 변수에서 제외했다.

<img src="https://user-images.githubusercontent.com/115082062/208939044-f1ce3738-117a-45be-9401-a3cc5295b21b.png">
위 사진처럼 test set의 `PRESSURE-S`는 완전 무작위 결측값이 상당히 많았다. 이 변수는 생산기지의 현지기압을 의미하는 변수다. 즉, 이 변수를 DROP하는 대신, 기상청 외부 데이터에 있는 현지기압값을 끌고 온다면 나름 대체가 될 것으로 판단했다. 무리하게 이상치를 보간하는 방식보단 외부데이터의 힘을 빌리는 쪽을 택했다.

발표평가에서 심사위원 한 분이 "왜 이상치로 판단했고, 이를 drop함으로써 얻는 실익이 무엇이냐"라고 물었다. 이에 대한 답으로 기압 값이 상식적으로 100kPa 안팎을 도는 것이 정상적인데, 이 데이터의 경우 0으로 찍혀 있는 것이 전체의 17%에 육박하므로 기기의 결함이나 데이터 오기입, 즉 완전 무작위 결측이 확실하다고 답했다. 또한 모델 성능의 눈에 띄는 향상은 없었지만, 기존 데이터를 무리하게 보간하는 것은 기존 데이터를 왜곡시키는 고육지책이며 적절한 외부데이터가 있는데 drop하지 않을 이유가 없었다고 설명했다.


<img src="https://user-images.githubusercontent.com/115082062/208939047-e0fa0281-9e6c-4c8f-8c1b-8ddd060edba3.png">
위 사진은 test set의 `LP_TOTAL`이다. 눈에 띄게 커지는 부분이 있다. 하지만 앞선 `PRESSURE-S`처럼 변수 자체를 drop하기엔 `LP_TOTAL`이 LNG 공정도 상에서 타겟값과 공학적으로 밀접한 관련이 있는 변수라고 판단했다. 그리고 실제로 이상치가 그리 많은 편도 아니었다. 따라서 이 값들은 train set `LP_TOTAL`의 3분위수로 대체하였다. 

```python
LP_TOTAL_3qt = train['LP_TOTAL'].quantile(0.75)
test.loc[test['LP_TOTAL']>=869.165, 'LP_TOTAL'] = LP_TOTAL_3qt
```




