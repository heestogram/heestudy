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


 
 
 
 
