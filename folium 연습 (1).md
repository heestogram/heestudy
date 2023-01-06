```python
!pip3 install folium
```

    Collecting folium
      Downloading folium-0.14.0-py2.py3-none-any.whl (102 kB)
    Collecting branca>=0.6.0
      Downloading branca-0.6.0-py3-none-any.whl (24 kB)
    Requirement already satisfied: requests in c:\anaconda\lib\site-packages (from folium) (2.24.0)
    Requirement already satisfied: numpy in c:\anaconda\lib\site-packages (from folium) (1.20.3)
    Requirement already satisfied: jinja2>=2.9 in c:\anaconda\lib\site-packages (from folium) (2.11.2)
    Requirement already satisfied: idna<3,>=2.5 in c:\anaconda\lib\site-packages (from requests->folium) (2.10)
    Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in c:\anaconda\lib\site-packages (from requests->folium) (1.25.11)
    Requirement already satisfied: chardet<4,>=3.0.2 in c:\anaconda\lib\site-packages (from requests->folium) (3.0.4)
    Requirement already satisfied: certifi>=2017.4.17 in c:\anaconda\lib\site-packages (from requests->folium) (2022.9.24)
    Requirement already satisfied: MarkupSafe>=0.23 in c:\anaconda\lib\site-packages (from jinja2>=2.9->folium) (1.1.1)
    Installing collected packages: branca, folium
    Successfully installed branca-0.6.0 folium-0.14.0
    


```python
import random
import pandas as pd
import numpy as np

import folium
from folium.plugins import MarkerCluster, MiniMap
```

    C:\anaconda\lib\site-packages\pandas\core\computation\expressions.py:20: UserWarning: Pandas requires version '2.7.3' or newer of 'numexpr' (version '2.7.1' currently installed).
      from pandas.core.computation.check import NUMEXPR_INSTALLED
    


```python
df = pd.read_csv('Downloads/소상공인/소상공인시장진흥공단_상가(상권)정보_제주_202209.csv')
```
컬럼은 아래처럼 아주 많지만, 여기서 쓸 컬럼은 얼마 없다.

```python
df.columns
```




    Index(['상가업소번호', '상호명', '지점명', '상권업종대분류코드', '상권업종대분류명', '상권업종중분류코드',
           '상권업종중분류명', '상권업종소분류코드', '상권업종소분류명', '표준산업분류코드', '표준산업분류명', '시도코드',
           '시도명', '시군구코드', '시군구명', '행정동코드', '행정동명', '법정동코드', '법정동명', '지번코드',
           '대지구분코드', '대지구분명', '지번본번지', '지번부번지', '지번주소', '도로명코드', '도로명', '건물본번지',
           '건물부번지', '건물관리번호', '건물명', '도로명주소', '구우편번호', '신우편번호', '동정보', '층정보',
           '호정보', '경도', '위도'],
          dtype='object')




```python
def res_map(location):
    # 도로명주소에 내가 원하는 location이 포함되었는지 확인하고, 포함된 행만 반환
    df_ = df[df['도로명주소'].str.contains(location, na = False)]
    # 음식점을 알아볼 것이므로 상권업종대분류명이 '음식'인 행만 반환
    df_ = df_[df_["상권업종대분류명"]=="음식"]
    
    # 사용할 컬럼은 아래 4개뿐
    col = ['상호명','위도', '경도', '상권업종중분류명']
    df_ = df_.loc[:,col]
    
    # 작업을 편리하게 하기 위해 list 형식으로 반환
    data = df_.values.tolist()
    
    
    category = df_['상권업종중분류명'].unique()
    color_list = ['red', 'blue', 'green', 'purple', 'orange', 'darkred', 'lightred', 'beige', 'darkblue', 'darkgreen', 'white', 'pink', 'gray', 'black', 'lightgray']

    color_dict = {}
    for k in zip(category, color_list):
        color_dict[k[0]] = k[1]
    
    map_ = folium.Map((33.511504, 126.491179), zoom_start=13)
    for i in range(len(data)):
        folium.Marker([data[i][1],data[i][2]], 
                      popup = f'[{data[i][3]}]{data[i][0]}',
                     icon = folium.Icon(color=color_dict[data[i][3]])).add_to(map_)
    return map_
    
```


```python
def res_map(location):
    # 도로명주소에 내가 원하는 location이 포함되었는지 확인하고, 포함된 행만 반환
    df_ = df[df['도로명주소'].str.contains(location, na = False)]
    # 음식점을 알아볼 것이므로 상권업종대분류명이 '음식'인 행만 반환
    df_ = df_[df_["상권업종대분류명"]=="음식"]
    
    # 사용할 컬럼은 아래 4개뿐
    col = ['상호명','위도', '경도', '상권업종중분류명']
    df_ = df_.loc[:,col]
    
    # 작업을 편리하게 하기 위해 list 형식으로 반환
    data = df_.values.tolist()
```
folium에서는 Marker를 설정할 수 있다. Marker란 우리가 지도 앱에서 자주 보는 핀을 의미한다. 이 때 핀의 색깔을 지정할 수 있는데, 우리는 상권업종중분류명에 따라 color를 달리 할 것이다. 그래서 중분류명과 color를 한 쌍으로 하는 딕셔너리를 만들 것이다.

color_list는 folium의 내장된 icon의 color들을 리스트로 갖고온 것이다.

```python
    category = df_['상권업종중분류명'].unique()
    color_list = ['red', 'blue', 'green', 'purple', 'orange', 'darkred', 'lightred', 'beige', 'darkblue', 'darkgreen', 'white', 'pink', 'gray', 'black', 'lightgray']

    color_dict = {}
    for k in zip(category, color_list):
        color_dict[k[0]] = k[1]
```
이제 본격적으로 지도를 그려볼 것이다. 아래 부분은 지도의 초기 설정을 하는 부분이다. 초기 위도와 경도를 지정해주고, `zoom_start` 파라미터로 확대를 어느정도 할지 설정한다. 값이 클수록 지도는 더 확대된다. 필자는 초기 좌표를 제주공항으로 잡아주었다.

```python
    map_ = folium.Map((33.511504, 126.491179), zoom_start=13)
```
이제 앞서 만든 data 리스트를 가져다 쓴다. data의 저장된 값들을 초반 10개 식당만 뽑아보면 다음과 같다. 즉, `data[0][0]`을 입력하면 '제라진'이 나올 것이고, `data[0][1]`을 입력하면 33.2514383512425라는 위도값이 나올 것이다.

```python
data[:10]
```




    [['제라진', 33.2514383512425, 126.431964272011, '한식'],
     ['시골길', 33.2517005185431, 126.42275280511, '한식'],
     ['삼정식당', 33.2538946164217, 126.42443030442, '한식'],
     ['팡팡가요주점', 33.251828906594, 126.425057561329, '유흥주점'],
     ['예원회수산', 33.2533594787683, 126.427026012877, '일식/수산물'],
     ['무궁화한식당', 33.2484066169078, 126.410472378291, '한식'],
     ['케이팝', 33.2518402302897, 126.425239777172, '유흥주점'],
     ['사랑방조림식당', 33.2517005185431, 126.42275280511, '한식'],
     ['너바나', 33.2514702890931, 126.426641376889, '유흥주점'],
     ['모모야마일식당', 33.2484066169078, 126.410472378291, '일식/수산물']]


folium.Marker를 data에 저장된 식당 수만큼 반복하여 각 식당마다 marker를 만들어줄 것이다. 

처음에 오는 파라미터는 위도와 경도이다. 

`popup` 파라미터는 marker를 클릭했을 때 보여줄 제목을 의미한다. 필자는 f string을 사용하여 `[상권업종중분류명]상호명` 형식으로 만들었다.

`icon` 파라미터에서 아이콘에 대한 설정을 할 수 있다. 우리가 앞서 만들었던 `color_dict`를 활용하여 중분류에 따라 색깔을 달리 지정하도록 한다.

마지막으로 `add_to(map_)`을 해주면 marker를 지도에 추가한다는 의미이다.

```python
    for i in range(len(data)):
        folium.Marker([data[i][1],data[i][2]], 
                      popup = f'[{data[i][3]}]{data[i][0]}',
                     icon = folium.Icon(color=color_dict[data[i][3]])).add_to(map_)
    return map_
```


```python
res_map("중문")
```
