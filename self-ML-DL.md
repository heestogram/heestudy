# 혼자 공부하는 머신러닝 딥러닝(박해선 저)

---

<aside>
💡 ‘혼자 공부하는 머신러닝 딥러닝’ 책을 읽고 공부한 내용을 요약한 페이지입니다. 
책에 나오는 코드를 그대로 쓰지 않고, 코드와 파라미터를 변형하고 조정해가며 다른 결과를 출력하며 공부했습니다.

</aside>

> **목차**
> 

## 01 나의 첫 머신러닝

---

### 01-3 마켓과 머신러닝

생선 중에 무엇이 도미이고 무엇이 빙어인지 알려주는 프로그램을 작성해보자.

```python
# 도미 데이터 준비하기
bream_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0, 
                31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0, 
                35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0]
bream_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0, 
                500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0, 
                700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0]
# 빙어 데이터 준비하기
smelt_length = [9.8, 10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
smelt_weight = [6.7, 7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]

import matplotlib.pyplot as plt #과학계산용 그래프 그리는 패키지 '맷플롯립'

plt.scatter(bream_length, bream_weight)
plt.xlabel('length') #x축 설정
plt.ylabel('weight') #y축 설정
plt.show()
```

> **k-최근접 이웃(k-Nearest Neighbors) 알고리즘:** 어떤 데이터에 대해 답을 구할 때 주위의 다른 데이터를 보고 다수를 차지하는 것을 정답으로 사용하는 알고리즘.
> 

```python
length = bream_length + smelt_length
weight = bream_weight + smelt_weight
fish_data = [[l,w] for l, w in zip(length, weight)] #리스트 내포 구문
#이러면 2차원 리스트가 만들어짐!

fish_target = [1]*35 + [0]*14 #도미는 1로, 빙어는 0으로 놓는다.
print(fish_target)

#k최근접 이웃 알고리즘을 구현한 클래스
from sklearn.neighbors import KNeighborsClassifier 

kn = KNeighborsClassifier() #클래스의 객체 만들어주기
kn.fit(fish_data, fish_target) #fit메서드는 training을 시켜준다.
kn.score(fish_data, fish_target) #score메서드는 모델을 평가하는 점수(정확도,accuracy)를 알려준다.

kn.predict([[30,600]]) #predict메서드는 새로운 데이터의 정답을 예측한다.

#가까운 몇 개의 데이터를 사용할지는 n_neighbors 매개변수로 정함!
kn49 = KNeighborsClassifier(n_neighbors=49) #주변의 49개의 데이터를 사용한다는 의미
kn49.fit(fish_data, fish_target)
kn49.score(fish_data, fish_target)
```

**01-3 핵심 키워드**

- 특성(feature): 데이터를 표현하는 하나의 성질
- k-최근접 이웃 알고리즘: 어떤 데이터에 대해 답을 구할 때 주위의 다른 데이터를 보고 다수를 차지하는 것을 정답으로 사용하는 알고리즘. 가장 간단한 머신러닝 알고리즘 중 하나
- 정확도(accuracy) = 정확히 맞힌 개수 /  전체 데이터 개수

**01-3 핵심 패키지와 함수**

- **matplotlib**
    - scatter(): 산점도를 그리는 맷플롯립 함수
- **scikit-learn**
    - `KNeighborsClassifier()`: k-최근접 이웃 분류 모델을 만드는 사이킷런 클래스
    - `fit()`은 사이킷런 모델을 훈련할 때 사용하는 메서드
    - `predict()`는 사이킷런 모델을 훈련하고 예측할 때 사용하는 메서드
    - `score()`은 훈련된 사이킷런 모델의 성능을 측정하는 메서드

---

## 02 데이터 다루기

---

### 02-1 훈련 세트와 테스트 세트

도미와 빙어 데이터/타깃을 주고 훈련한 다음 같은 데이터로 테스트한다면 모두 맞힐 것이 당연하다. 연습 문제와 시험 문제가 달라야 올바르게 모델의 성능을 평가할 수 있다. 따라서 평가에 사용할 **test set**와 훈련에 사용할 **train set**를 나눌 수 있어야 한다.

```python
#데이터 준비하기
fish_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0, 
                31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0, 
                35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0, 9.8, 
                10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
fish_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0, 
                500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0, 
                700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0, 6.7, 
                7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]

fish_data = [[l,w] for l,w in zip(fish_length, fish_weight)]
fish_target = [1]*35 + [0]*14

#총 49개의 샘플 가운데 처음 35개를 훈련세트로, 나머지 14개를 테스트세트로 쓴다. 
```

```python
from sklearn.neighbors import KNeighborsClassifier
kn = KNeighborsClassifier()
```

```python
#총 49개의 샘플 가운데 처음 35개를 훈련세트로, 나머지 14개를 테스트세트로 쓴다.
train_input = fish_data[:35] #슬라이싱으로 0부터 34번째 인덱스까지
train_target = fish_target[:35]
test_input = fish_data[35:]
test_target = fish_target[35:]
```

```python
kn = kn.fit(train_input, train_target)
kn.score(test_input, test_target)
#score를 확인해보니 0.0으로 나왔다. 왜일까?
#샘플링이 편향된 것! 나머지 14개를 테스트 세트로 떼어놓으면 훈련 세트에는 빙어가 하나도 없다!
#따라서 훈련 세트와 테스트 세트를 적절히 분류하는 것이 매우 중요.
```

**넘파이**는 파이썬의 대표적인 배열(array) 라이브러리로, 고차원의 배열을 손쉽게 만들 수 있다.

```python
import numpy as np
input_arr = np.array(fish_data)
target_arr = np.array(fish_target)
```

```python
#훈련 세트와 테스트 세트를 적절히 섞기 위한 대책
np.random.seed(42)
index = np.arange(49) #0부터 48까지 정수 배열
np.random.shuffle(index) #index를 무작위로 섞음
print(index)

train_input = input_arr[index[:35]]
train_target = target_arr[index[:35]]
test_input = input_arr[index[35:]]
test_target = target_arr[index[35:]]

#그래프를 그려서 도미, 빙어 데이터가 잘 섞였는지 확인
import matplotlib.pyplot as plt
plt.scatter(train_input[:,0], train_input[:,1])
plt.scatter(test_input[:,0], test_input[:,1])
plt.show()
```

![파란색이 훈련세트, 주황색이 테스트세트이다. 골고루 잘 섞인 것을 볼 수 있다.](%E1%84%92%E1%85%A9%E1%86%AB%E1%84%8C%E1%85%A1%20%E1%84%80%E1%85%A9%E1%86%BC%E1%84%87%E1%85%AE%E1%84%92%E1%85%A1%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC%20%E1%84%83%E1%85%B5%E1%86%B8%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC(%E1%84%87%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A2%E1%84%89%E1%85%A5%E1%86%AB%20%E1%84%8C%E1%85%A5)%205fee2e5b433a463bbeca29c95c3cd0ee/%EB%8F%84%EB%AF%B8_%EB%B9%99%EC%96%B4_%EB%9E%9C%EB%8D%A4_%EC%84%9E%EA%B8%B0.png)

파란색이 훈련세트, 주황색이 테스트세트이다. 골고루 잘 섞인 것을 볼 수 있다.

```python
kn = kn.fit(train_input, train_target)
kn.score(test_input, test_target)
kn.predict(test_input)
```

**02-1 핵심 키워드**

- **지도학습**: 입력과 타깃을 전달하여 모델을 훈련한 다음 새로운 데이터를 예측하는 데 사용
- **비지도학습**: 타깃 데이터가 없는 학습
- **훈련세트**: 모델을 훈련할 때 사용하는 데이터. 보통 훈련 세트가 클수록 좋음
- **테스트세트**: 모델을 평가할 때 사용하는 데이터. 보통 전체 데이터의 20~30%.

**02-1 핵심 패키지와 함수**

- **numpy**
    - `seed()`: 넘파이에서 난수를 생성하기 위한 정수 초기값을 지정
    - `arange()`: 일정한 간격의 정수 또는 실수 배열을 만듦. 기본 간격은 1
    - `shuffle`: 주어진 배열을 랜덤하게 섞음.

---

### 02-2 데이터 전처리

```python
fish_data = np.column_stack((fish_length, fish_weight)) 
# cloumn_stack은 전달받은 리스트를 일렬로 세운 다음 차례대로 연결
fish_target = np.concatenate((np.ones(35), np.zeros(14)))
# ones은 1을 n개만큼 배열로 만들고 zeros는 0을 n개만큼 배열로 만듦
```

사이킷런(**`train_test_split` 함수**)으로 훈련 세트와 테스트 데이터 나누기

```python
from sklearn.model_selection import train_test_split
train_input, test_input, train_target, test_target = train_test_split(fish_data, fish_target, stratify=fish_target, random_state=42)
#straify매개변수에 타깃데이터를 전달하면 클래스 비율에 맞게 데이터를 나눔
print(test_target)
```

```python
print(kn.predict([[25,150]])) #길이가 25이고 무게가 150인 생선을 예측
#원래대로라면 도미로 예측해야 하는데 빙어로 예측해버림. 왜일까?

distance, indexes = kn.kneighbors([[25,150]])
print(distance, indexes)
plt.scatter(train_input[:,0], train_input[:,1])
plt.scatter(train_input[indexes,0], train_input[indexes,1], marker ='D')
plt.scatter(25,150, marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()
```

![삼각형이 예측대상이고, 주황색이 인접한 5개의 샘플이다. 가깝기론 우측상단의 도미들이 더 가까워보이는데, 훨씬 멀어보이는 빙어가 인접한 샘플로 분류되었다.](%E1%84%92%E1%85%A9%E1%86%AB%E1%84%8C%E1%85%A1%20%E1%84%80%E1%85%A9%E1%86%BC%E1%84%87%E1%85%AE%E1%84%92%E1%85%A1%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC%20%E1%84%83%E1%85%B5%E1%86%B8%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC(%E1%84%87%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A2%E1%84%89%E1%85%A5%E1%86%AB%20%E1%84%8C%E1%85%A5)%205fee2e5b433a463bbeca29c95c3cd0ee/%EC%88%98%EC%83%81%ED%95%9C_%EB%8F%84%EB%AF%B8.png)

삼각형이 예측대상이고, 주황색이 인접한 5개의 샘플이다. 가깝기론 우측상단의 도미들이 더 가까워보이는데, 훨씬 멀어보이는 빙어가 인접한 샘플로 분류되었다.

위같은 착시가 일어나는 것은 y축의 범위가 x축에 비해 훨씬 넓기 때문이다. 두 축의 범위를 같게 해보자.

```python
plt.scatter(train_input[:,0], train_input[:,1])
plt.scatter(train_input[indexes,0], train_input[indexes,1], marker ='D')
plt.scatter(25,150, marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.xlim((0,1000)) #x축의 범위를 1000으로 넓혀 y축과 같은 스케일로 만들어보자
plt.show()
```

![이제야 납득이 가는 실제 거리](%E1%84%92%E1%85%A9%E1%86%AB%E1%84%8C%E1%85%A1%20%E1%84%80%E1%85%A9%E1%86%BC%E1%84%87%E1%85%AE%E1%84%92%E1%85%A1%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC%20%E1%84%83%E1%85%B5%E1%86%B8%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC(%E1%84%87%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A2%E1%84%89%E1%85%A5%E1%86%AB%20%E1%84%8C%E1%85%A5)%205fee2e5b433a463bbeca29c95c3cd0ee/%EB%8F%84%EB%AF%B8%EB%B9%99%EC%96%B4.png)

이제야 납득이 가는 실제 거리

두 특성의 scale이 다르기 때문에 생긴 일이다. 스케일이 상이하다면 k-최근접 알고리즘은 올바른 예측을 할 수 없다. 때문에 특성값을 **전처리(preprocessing)**해줘야 한다. 가장 널리 사용하는 전처리 방법 중 하나는 **표준점수(standard score)**이다.

```python
mean = np.mean(train_input, axis=0) #평균
std = np.std(train_input, axis=0) #표준편차
train_scaled = (train_input-mean)/std #표준점수
```

```python
new = ([25, 150] - mean)/std
plt.scatter(train_scaled[:,0], train_scaled[:,1])
plt.scatter(new[0],new[1], marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

kn.fit(train_scaled, train_target)
kn.score(test_scaled, test_target)
print(kn.predict([new]))

distance, indexes = kn.kneighbors([new])
new = ([25, 150] - mean)/std
plt.scatter(train_scaled[:,0], train_scaled[:,1])
plt.scatter(train_scaled[indexes,0], train_scaled[indexes,1], marker='D')
plt.scatter(new[0],new[1], marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()
```

![표준점수로 전처리해준 후엔 알고리즘이 제대로 작동하게 된다.](%E1%84%92%E1%85%A9%E1%86%AB%E1%84%8C%E1%85%A1%20%E1%84%80%E1%85%A9%E1%86%BC%E1%84%87%E1%85%AE%E1%84%92%E1%85%A1%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC%20%E1%84%83%E1%85%B5%E1%86%B8%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC(%E1%84%87%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A2%E1%84%89%E1%85%A5%E1%86%AB%20%E1%84%8C%E1%85%A5)%205fee2e5b433a463bbeca29c95c3cd0ee/%EB%8F%84%EB%AF%B8%EB%B9%99%EC%96%B4%201.png)

표준점수로 전처리해준 후엔 알고리즘이 제대로 작동하게 된다.

**02-2 핵심 키워드**

- **데이터 전처리(data-preprocessing)**: 훈련데이터를 주입하기 전 가공하는 단계
- 표준점수: 특성에 평균을 빼고 표준편차로 나눔. 반드시 훈련세트의 평균과 표준편차로 테스트 세트를 바꿔야 함
- 브로드캐스팅: 크기가 다른 넘파이 배열에서 자동으로 사칙 연산을 모든 행이나 열로 확장하여 수행하는 기능

**02-2 핵심 패키지와 함수**

- scikit-learn
    - **`train_test_split()`**: 훈련세트, 테스트세트를 나누는 함수. test_size 매개변수로 테스트세트의 비율 지정 가능.
    - `kneighbors()`: 입력한 데이터의 가장 가까운 이웃을 찾아 거리와 이웃 샘플의 인덱스를 반환.

---

## 03 회귀 알고리즘과 모델 규제

---

### 03-1 k-최근접 이웃 회귀

> **k-최근접 이웃 회귀**: 예측하려는 샘플에 가장 가까운 샘플 k개를 선택하고 이 수치들의 평균값을 예측 타깃값으로 추정한다.
> 

농어의 길이, 무게 데이터가 준비되어있을 때, 예측하려는 농어의 길이가 주어지면 무게가 얼마나 나갈지 예측하는 프로그램을 만들고자 한다.

```python
#데이터 준비
import numpy as np
perch_length = np.array([8.4, 13.7, 15.0, 16.2, 17.4, 18.0, 18.7, 19.0, 19.6, 20.0, 21.0,
       21.0, 21.0, 21.3, 22.0, 22.0, 22.0, 22.0, 22.0, 22.5, 22.5, 22.7,
       23.0, 23.5, 24.0, 24.0, 24.6, 25.0, 25.6, 26.5, 27.3, 27.5, 27.5,
       27.5, 28.0, 28.7, 30.0, 32.8, 34.5, 35.0, 36.5, 36.0, 37.0, 37.0,
       39.0, 39.0, 39.0, 40.0, 40.0, 40.0, 40.0, 42.0, 43.0, 43.0, 43.5,
       44.0])
perch_weight = np.array([5.9, 32.0, 40.0, 51.5, 70.0, 100.0, 78.0, 80.0, 85.0, 85.0, 110.0,
       115.0, 125.0, 130.0, 120.0, 120.0, 130.0, 135.0, 110.0, 130.0,
       150.0, 145.0, 150.0, 170.0, 225.0, 145.0, 188.0, 180.0, 197.0,
       218.0, 300.0, 260.0, 265.0, 250.0, 250.0, 300.0, 320.0, 514.0,
       556.0, 840.0, 685.0, 700.0, 700.0, 690.0, 900.0, 650.0, 820.0,
       850.0, 900.0, 1015.0, 820.0, 1100.0, 1000.0, 1100.0, 1000.0,
       1000.0])
```

```python
#훈련세트와 테스트세트로 나누기
from sklearn.model_selection import train_test_split
train_input, test_input, train_target, test_target = train_test_split(perch_length, perch_weight, random_state=42)

#현재 1차원 배열인 데이터들을 2차원 배열로 만드는 작업
train_input = train_input.reshape(-1,1) #reshape()메서드는 배열 크기를 바꿔줌.
test_input = test_input.reshape(-1,1) #-1을 지정하면 나머지 원소 개수로 모두 채우라는 의미

from sklearn.neighbors import KNeighborsRegressor #k-최근접 이웃 회귀 알고리즘을 구현한 클래스
knr = KNeighborsRegressor()
knr.fit(train_input, train_target)
print(knr.score(test_input, test_target)) #이 때 출력되는 점수가 바로 결정계수(R^2)
```

![Untitled](%E1%84%92%E1%85%A9%E1%86%AB%E1%84%8C%E1%85%A1%20%E1%84%80%E1%85%A9%E1%86%BC%E1%84%87%E1%85%AE%E1%84%92%E1%85%A1%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC%20%E1%84%83%E1%85%B5%E1%86%B8%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC(%E1%84%87%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A2%E1%84%89%E1%85%A5%E1%86%AB%20%E1%84%8C%E1%85%A5)%205fee2e5b433a463bbeca29c95c3cd0ee/Untitled.png)

```python
#결정계수가 아닌 타깃과 예측의 절댓값 오차를 평균하는 방식
from sklearn.metrics import mean_absolute_error
test_prediction = knr.predict(test_input)
mae = mean_absolute_error(test_target, test_prediction)
print(mae)
```

> **과대적합(overfitting)**: 훈련세트에서 점수가 아주 좋았는데 테스트 세트에서는 점수가 굉장히 나쁜 경우
**과소적합(underfitting)**: 훈련세트보다 테스트세트의 점수가 높거나 둘 다 너무 낮은 경우
> 

```python
knr.n_neighbors = 3 #기본값 5보다 이웃의 개수를 줄이면 국지적인 패턴에 민감해짐
#즉 overfitting의 여지가 커짐
knr.fit(train_input, train_target)
print(knr.score(train_input, train_target)) #0.9804899950518966
print(knr.score(test_input, test_target)) #0.974645996398761
#테스트세트의 점수가 더 낮고 둘 간의 차이도 크지 않으니 과소적합도 과대적합도 아님!
```

![n_neighbors 매개변수를 늘릴수록 데이터 전반의 경향을 따라가고, 줄일수록 훈련세트 샘플에 철저하게 먖춰지는 모습을 볼 수 있다.](%E1%84%92%E1%85%A9%E1%86%AB%E1%84%8C%E1%85%A1%20%E1%84%80%E1%85%A9%E1%86%BC%E1%84%87%E1%85%AE%E1%84%92%E1%85%A1%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC%20%E1%84%83%E1%85%B5%E1%86%B8%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC(%E1%84%87%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A2%E1%84%89%E1%85%A5%E1%86%AB%20%E1%84%8C%E1%85%A5)%205fee2e5b433a463bbeca29c95c3cd0ee/n_neighbors.png)

n_neighbors 매개변수를 늘릴수록 데이터 전반의 경향을 따라가고, 줄일수록 훈련세트 샘플에 철저하게 먖춰지는 모습을 볼 수 있다.

**03-1 핵심 키워드**

- **k-최근접 이웃 회귀**: 예측하려는 샘플에 가장 가까운 샘플 k개를 선택하고 이 수치들의 평균값을 예측 타깃값으로 추정
- **결정계수**: 대표적인 회귀 문제의 성능 측정 도구. 1에 가까울수록 좋다.
- 과대적합: 훈련세트에서 점수가 아주 좋았는데 테스트 세트에서는 점수가 굉장히 나쁜 경우
- 과소적합: 훈련세트보다 테스트세트의 점수가 높거나 둘 다 너무 낮은 경우

**03-1 핵심 패키지와 함수**

- scikit-learn
    - `KNeighborsRegressor`: k-최근접 이웃 회귀를 구현하는 사이킷런 클래스. n_neighbors 매개변수로 이웃의 개수를 지정한다. 기본값은 5
    - `mean_absolute_error()`: 회귀모델의 평균 절댓값 오차를 계산한다.
- numpy
    - **`reshape()`**: 배열의 크기를 바꾸는 메서드.

---

### 03-2 선형 회귀

k-최근접 이웃 알고리즘의 한계

```python
print(knr.predict([[50]])) 
#실제로 저울에 재보니 1500g인데, 최근접회귀모델에선 1033.33g으로 예측함

import matplotlib.pyplot as plt
distnces, indexes = knr.kneighbors([[50]])
plt.scatter(train_input, train_target)
plt.scatter(train_input[indexes], train_target[indexes], marker='D')
plt.scatter(50,1033,marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()
#길이가 길어질수록 무게가 늘어나는 것은 당연한데, 길이가 더 길어져도 최근접하는 것들의 무게는 일정하기에, 예측값이 커지지 않는다. 
#예를 들어 길이가 100cm라도 무게는 여전히 1033g일 것이라는 말이다.
```

![산점도로 보면 확연한 k-최근접 이웃 회귀의 한계점. 이런 식이면 농어가 아무리 커도 무게가 더 늘어나지 않는다.](%E1%84%92%E1%85%A9%E1%86%AB%E1%84%8C%E1%85%A1%20%E1%84%80%E1%85%A9%E1%86%BC%E1%84%87%E1%85%AE%E1%84%92%E1%85%A1%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC%20%E1%84%83%E1%85%B5%E1%86%B8%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC(%E1%84%87%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A2%E1%84%89%E1%85%A5%E1%86%AB%20%E1%84%8C%E1%85%A5)%205fee2e5b433a463bbeca29c95c3cd0ee/%EC%B5%9C%EA%B7%BC%EC%A0%91%ED%9A%8C%EA%B7%80%ED%95%9C%EA%B3%84.png)

산점도로 보면 확연한 k-최근접 이웃 회귀의 한계점. 이런 식이면 농어가 아무리 커도 무게가 더 늘어나지 않는다.

> **선형회귀(linear regression)**: 특성이 하나인 경우 그 특성을 가장 잘 나타내는 직선을 학습하는 알고리즘
> 

```python
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(train_input, train_target)
print(lr.predict([[50]])) #1241.83 출력
print(lr.coef_,lr.intercept_) #coef에는 기울기 계수가, intercept에는 절편이 저장되어 있다.

plt.scatter(train_input, train_target)
plt.plot([15,50],[15*lr.coef_ + lr.intercept_, 50*lr.coef_ + lr.intercept_])
plt.scatter(50, 1241.8, marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()
```

![앞서 지적된 최근접 이웃 회귀의 문제점은 해소가 되었다. 그러나 뭔가 이상한 부분이 있다.](%E1%84%92%E1%85%A9%E1%86%AB%E1%84%8C%E1%85%A1%20%E1%84%80%E1%85%A9%E1%86%BC%E1%84%87%E1%85%AE%E1%84%92%E1%85%A1%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC%20%E1%84%83%E1%85%B5%E1%86%B8%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC(%E1%84%87%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A2%E1%84%89%E1%85%A5%E1%86%AB%20%E1%84%8C%E1%85%A5)%205fee2e5b433a463bbeca29c95c3cd0ee/%EC%84%A0%ED%98%95%ED%9A%8C%EA%B7%80.png)

앞서 지적된 최근접 이웃 회귀의 문제점은 해소가 되었다. 그러나 뭔가 이상한 부분이 있다.

```python
print(lr.score(train_input, train_target))
print(lr.score(test_input, test_target))
#두 결정계수(R_squared) 모두 높은 편이 아니라 과소적합 된 듯하다.
#또한, 그래프 좌측하단을 보면 weight가 0아래로 내려가는 경우가 있는데, 무게가 음수일 수는 없으니 말이 안된다.
```

상기한 두 가지 문제점을 해소하기 위해 선형 회귀가 아니라 **다항회귀(polynomial regression)** 모델을 적용해야 한다. 다시말해, 최적의 직선을 찾는 것이 아니라 최적의 곡선을 찾는 것이다.

```python
#2차 방정식 그래프를 만드려면 길이를 제곱한 항이 train_input에 추가되어야 한다!
train_poly = np.column_stack((train_input**2, train_input))
test_poly = np.column_stack((test_input**2, test_input))
lr.fit(train_poly,train_target)
print(lr.predict([[50**2,50]]))
print(lr.coef_, lr.intercept_) #[  1.01433211 -21.55792498] 116.05021078278276
# 즉, 무게 = 1.01*길이^2 - 21.6*길이 +116.05라는 회귀식을 만든 것.
```

```python
point = np.arange(15,50) #구간별 직선을 그리기 위해 15에서 49까지 정수 배열을 만듦.
plt.scatter(train_input, train_target)
plt.plot(point, point**2*1.01 - point*21.6 + 116.05) #구간별로 직선 여러개를 합쳐 곡선처럼 만든 것.
plt.scatter(50, 1574, marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

print(lr.score(train_poly, train_target))
print(lr.score(test_poly, test_target))
```

![선형회귀보다 더 적합한 그래프가 그려졌다.](%E1%84%92%E1%85%A9%E1%86%AB%E1%84%8C%E1%85%A1%20%E1%84%80%E1%85%A9%E1%86%BC%E1%84%87%E1%85%AE%E1%84%92%E1%85%A1%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC%20%E1%84%83%E1%85%B5%E1%86%B8%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC(%E1%84%87%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A2%E1%84%89%E1%85%A5%E1%86%AB%20%E1%84%8C%E1%85%A5)%205fee2e5b433a463bbeca29c95c3cd0ee/%EB%8B%A4%ED%95%AD_%ED%9A%8C%EA%B7%80.png)

선형회귀보다 더 적합한 그래프가 그려졌다.

**03-2 핵심 키워드**

- 선형 회귀: 특성과 타깃 사이 관계를 가장 잘 나타내는 선형 방정식을 찾는 모델
- 모델 파라미터: 선형 회귀가 찾은 가중치처럼 모델이 특성에서 학습한 파라미터를 의미
- 다항 회귀: 다항식을 사용하여 특성과 타깃 사이의 관계를 나타냄

**03-2 핵심 패키지와 함수**

- scikit-learn
    - **`LinearRegression`**은 사이킷런의 선형 회귀 클래스이다. `coef_` 속성은 계수의 배열이고, `intercept_` 속성은 절편이다.

---

### 03-3 특성 공학

지금까지는 하나의 특성을 사용하여 선형회귀모델을 훈련시켰다. 이번에는 여러 개의 특성을 사용한 **다중회귀(multiple regression)**를 실행해본다. 특성이 2개면 선형 회귀는 평면을 학습한다.

> **특성 공학(feature engineering)**: 기존의 특성을 가공하여 새로운 특성을 뽑아내는 작업을 의미한다. 예를 들어 ‘농어길이 * 농어높이’로 새로운 특성을 만드는 방식
> 

**판다스(pandas)**는 인터넷에서 데이터를 바로 다운로드하여 사용할 수 있는 데이터 분석 라이브러리이다. 데이터프레임은 판다스의 핵심 데이터 구조로, 넘파이 배열과 비슷하게 다차원 배열을 다룰 수 있고 훨씬 많은 기능을 제공한다.

```python
import pandas as pd
df = pd.read_csv('https://bit.ly/perch_csv_data')
perch_full = df.to_numpy()
```

```python

perch_weight = np.array([5.9, 32.0, 40.0, 51.5, 70.0, 100.0, 78.0, 80.0, 85.0, 85.0, 110.0,
       115.0, 125.0, 130.0, 120.0, 120.0, 130.0, 135.0, 110.0, 130.0,
       150.0, 145.0, 150.0, 170.0, 225.0, 145.0, 188.0, 180.0, 197.0,
       218.0, 300.0, 260.0, 265.0, 250.0, 250.0, 300.0, 320.0, 514.0,
       556.0, 840.0, 685.0, 700.0, 700.0, 690.0, 900.0, 650.0, 820.0,
       850.0, 900.0, 1015.0, 820.0, 1100.0, 1000.0, 1100.0, 1000.0,
       1000.0])

from sklearn.model_selection import train_test_split
train_input, test_input, train_target, test_target = train_test_split(perch_full, perch_weight, random_state=42)
```

사이킷런은 특성을 만들거나 전처리하기 위한 다양한 클래스를 제공하는데, 이러한 클래스를 **변환기(transformer)**라고 한다.

```python
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(include_bias = False) #절편은 제외한다는 의미
poly.fit(train_input) #훈련세트의 샘플들을 서로 곱한 값과 제곱한 값으로 특성들을 훈련
train_poly = poly.transform(train_input) #훈련한 값을 토대로 변환
poly.get_feature_names() # 각각의 특성들이 어떤 조합으로 만들어졌는지 이름을 표시
test_poly = poly.transform(test_input)
poly.get_feature_names()
```

```python
lr.fit(train_poly, train_target)
print(lr.score(train_poly, train_target)) #0.990318. 매우 높은 점수
print(lr.score(test_poly, test_target)) #0.971455
```

```python
#5제곱까지 늘려보면 어떨까?
poly = PolynomialFeatures(degree=5, include_bias = False) 
#degree매개변수로 고차항의 최대 차수를 지정
poly.fit(train_input)
train_poly = poly.transform(train_input)
test_poly = poly.transform(test_input)

lr.fit(train_poly, train_target)
print(lr.score(train_poly, train_target)) #0.999999
print(lr.score(test_poly, test_target)) #-144.405
#즉, 특성의 개수를 늘릴수록 형편없는 overfitting이 된다.
```

**03-3 핵심 키워드**

- 다중 회귀(mutiple regression): 여러 개의 특성을 사용하는 회귀 모델
- 특성 공학: 주어진 특성을 조합하여 새로운 특성을 만드는 일련의 작업

**03-3 핵심 패키지와 함수**

- **pandas**
    - `read_csv()`는 csv파일을 판다스 데이터프레임으로 변환하는 함수이다.
- scikit-learn
    - **`PolynomialFeatures`**는 주어진 특성을 조합하여 새로운 특성을 만드는 변환기 클래스이다. `include_bias`가 False이면 절편을 위한 특성을 추가하지 않는다. `degree`는 최고 차수를 지정하고 기본값은 2이다.

---

### 03-4 규제

> **규제(Regularization)**: 모델이 과대적합되지 않도록 만드는 작업이다. 선형 회귀 모델의 경우 특성에 곱해지는 계수의 크기를 작게 만드는 과정이다.
> 

특성의 스케일이 정규화되지 않으면 곱해지는 계수 값에도 차이가 난다. 만약 선형 회귀 모델에 규제를 적용할 때 계수 값의 크기가 서로 많이 다르면 공정하게 규제되지 않을 테니, 먼저 정규화를 해줘야 한다.

```python
from sklearn.preprocessing import StandardScaler #표준점수로 바꿔주는 변환기 클래스
ss = StandardScaler()
ss.fit(train_poly)
train_scaled = ss.transform(train_poly)
test_scaled = ss.transform(test_poly)
```

> **릿지(ridge)**: 계수를 제곱한 값을 기준으로 규제하는 것
> 

```python
from sklearn.linear_model import Ridge
ridge = Ridge()
ridge.fit(train_scaled, train_target)
print(ridge.score(train_scaled, train_target)) #0.9896. 완벽에 가까운 점수에서 살짝 하락
print(ridge.score(test_scaled, test_target)) #0.9790. 다시 정상으로 돌아옴. 규제가 잘 됐다는 의미.
```

규제를 할 때에 규제의 양을 조절하는 **alpha** 매개변수가 있다. 모델이 학습하는 파라미터는 모델 파라미터였다면, 이렇게 사람이 직접 지정하는 파라미터는 **하이퍼 파라미터**라고 한다.

```python
#적절한 alpha 값을 찾기 위한 비교 그래프 그리기
import matplotlib.pyplot as plt
train_score=[]
test_score=[]
alpha_list = [0.001, 0.01, 0.1, 1, 10, 100]
for alpha in alpha_list:
  ridge = Ridge(alpha=alpha)
  ridge.fit(train_scaled, train_target)
  train_score.append(ridge.score(train_scaled, train_target))
  test_score.append(ridge.score(test_scaled, test_target))

plt.plot(np.log10(alpha_list), train_score)
plt.plot(np.log10(alpha_list), test_score)
plt.xlabel('alpha')
plt.ylabel('R_squared')
plt.show()
```

![파란색이 훈련세트, 주황색이 테스트 세트이다.](%E1%84%92%E1%85%A9%E1%86%AB%E1%84%8C%E1%85%A1%20%E1%84%80%E1%85%A9%E1%86%BC%E1%84%87%E1%85%AE%E1%84%92%E1%85%A1%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC%20%E1%84%83%E1%85%B5%E1%86%B8%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC(%E1%84%87%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A2%E1%84%89%E1%85%A5%E1%86%AB%20%E1%84%8C%E1%85%A5)%205fee2e5b433a463bbeca29c95c3cd0ee/alpha.png)

파란색이 훈련세트, 주황색이 테스트 세트이다.

적절한 alpha값은 두 그래프가 제일 가깝고 테스트 세트의 점수가 가장 높은 -1, 즉 10^-1=0.1로 보인다.

```python
ridge=Ridge(alpha=0.1)
ridge.fit(train_scaled, train_target)
print(ridge.score(train_scaled, train_target)) #0.9903
print(ridge.score(test_scaled, test_target)) #0.9827
#alpha를 0.1로 설정하니 과대적합과 과소적합 사이의 균형을 잘 찾음
```

> **라쏘(lasso)**: 계수의 절댓값을 기준으로 규제하는 것
> 

```python
#Ridge클래스를 Lasso클래스로 바꾸기만 하면 됨.
from sklearn.linear_model import Lasso
lasso = Lasso()
lasso.fit(train_scaled, train_target)
print(lasso.score(train_scaled, train_target))
print(lasso.score(test_scaled, test_target))
```

**03-4 핵심 키워드**

- **릿지**: 계수를 제곱한 값을 기준으로 규제하는 것. 효과가 좋아 널리 사용됨
- **라쏘**: 계수의 절댓값을 기준으로 규제하는 것. 릿지와 달리 계수를 아예 0으로 만들 수도 있음
- 하이퍼파라미터: 알고리즘이 학습하는 파라미터가 아니라 사람이 사전에 지정하는 파라미터

**03-4  핵심 패키지와 함수**

- scikit-learn
    - **`Ridge`**는 릿지 회귀모델을 훈련하는 알고리즘. alpha매개변수로 규제 강도를 조정하고, 기본값은 1이다.
    - **`Lasso`**는 라쏘 회귀모델을 훈련하는 알고리즘. 이 클래스는 최적의 모델을 찾기 위해 좌표축을 따라 최적을 수행해가는 좌표 하강법(coordinate descent)을 사용한다.

---

## 04 다양한 분류 알고리즘

---

### 04-1 로지스틱 회귀

> **k-최근접 이웃 분류기**: k-최근접 이웃을 이용하여 인접 샘플의 클래스 비율을 확률로 나타내는 방식
> 

```python
#데이터 준비
import pandas as pd
fish = pd.read_csv('https://bit.ly/fish_csv_data')
fish.head() #처음 5개 행 출력
print(pd.unique(fish['Species']))
fish_input = fish[['Weight','Length','Diagonal','Height','Width']].to_numpy()
fish_target= fish['Species'].to_numpy()

#훈련세트와 테스트세트 구분
from sklearn.model_selection import train_test_split
train_input, test_input, train_target, test_target = train_test_split(fish_input, fish_target, random_state=42)

#표준화 전처리
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
ss.fit(train_input)
train_scaled = ss.transform(train_input)
test_scaled = ss.transform(test_input)

from sklearn.neighbors import KNeighborsClassifier
kn = KNeighborsClassifier(n_neighbors=3)
kn.fit(train_scaled, train_target)
print(kn.score(train_scaled, train_target))
print(kn.score(test_scaled, test_target))

import numpy as np
proba = kn.predict_proba(test_scaled[:5]) #테스트세트 첫 5개 샘플의 확률
print(np.round(proba, decimals=4)) #소수점 네번째 자리까지 표기, 다섯번째 자리에서 반올림

distances, indexes = kn.kneighbors(test_scaled[3:4])
print(train_target[indexes])
```

그러나 k-최근접 이웃 방식은 3개의 최근접 이웃만을 활용하기에 가능한 확률은 0/3, 1/3, 2/3, 3/3이 전부이다. 더 디테일한 확률이 필요하다. 로지스틱 회귀는 이것을 가능하게 해준다.

> **로지스틱 회귀(logistic regression)**: 선형 방정식을 활용한 분류 모델로서, **시그모이드 함수**나 **소프트맥스 함수**를 활용하여 클래스의 확률을 출력한다. z값이 아주 큰 음수이면 확률이 0이 되고, 아주 큰 양수이면 1이 되도록 한다.
> 

![왼쪽은 시그모이드 그래프, 오른쪽은 시그모이드 함수. x값이 로지스틱 방정식이다.](%E1%84%92%E1%85%A9%E1%86%AB%E1%84%8C%E1%85%A1%20%E1%84%80%E1%85%A9%E1%86%BC%E1%84%87%E1%85%AE%E1%84%92%E1%85%A1%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC%20%E1%84%83%E1%85%B5%E1%86%B8%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC(%E1%84%87%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A2%E1%84%89%E1%85%A5%E1%86%AB%20%E1%84%8C%E1%85%A5)%205fee2e5b433a463bbeca29c95c3cd0ee/Untitled%201.png)

왼쪽은 시그모이드 그래프, 오른쪽은 시그모이드 함수. x값이 로지스틱 방정식이다.

```python
#시그모이드 함수 그리기
import numpy as np
import matplotlib.pyplot as plt
z = np.arange(-5,5,0.1)
phi = 1/(1+np.exp(-z))
plt.plot(z, phi)
plt.xlabel('z')
plt.ylabel('phi')
plt.show()
```

로지스틱 회귀로 간단한 이진 분류를 수행해보자. 이진분류의 경우 시그모이드의 출력이 0.5보다 크면 양성, 작으면 음성으로 판단한다.

```python
#불리언 인덱싱을 활용하여 도미(Bream)와 빙어(Smelt)만 뽑아냄
bream_smelt_indexes = (train_target == 'Bream') | (train_target == 'Smelt')

train_bream_smelt = train_scaled[bream_smelt_indexes]
target_bream_smelt = train_target[bream_smelt_indexes]

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
lr.fit(train_bream_smelt, target_bream_smelt)

print(lr.predict(train_bream_smelt[:5])) #처음 5개 샘플 예측
print(lr.predict_proba(train_bream_smelt[:5])) #처음 5개 샘플의 확률 출력
#결과값
['Bream' 'Smelt' 'Bream' 'Bream' 'Bream']
[[0.99759855 0.00240145]
 [0.02735183 0.97264817]
 [0.99486072 0.00513928]
 [0.98584202 0.01415798]
 [0.99767269 0.00232731]]

#decision_function(): z값을 계산하는 메서드
decisions = lr.decision_function(train_bream_smelt[:5])
print(decisions)
#결과값
[-6.02927744  3.57123907 -5.26568906 -4.24321775 -6.0607117 ]
#이 z값을 시그모이드 함수에 넣으면 확률을 얻을 수 있음

from scipy.special import expit
print(expit(decisions))
#결과값
[0.00240145 0.97264817 0.00513928 0.01415798 0.00232731]
#predict_proba()메서드 출력의 두번째 열과 동일!
```

이제 로지스틱 회귀로 다중 분류를 수행해보자.

```python
lr = LogisticRegression(C=20, max_iter=1000)
#max_iter매개변수는 반복 횟수를 지정
#C는 릿지의 alpha처럼 규제의 정도를 위한 매개변수. 작을수록 규제가 커짐.
lr.fit(train_scaled, train_target)
print(lr.score(train_scaled, train_target)) #0.9327
print(lr.score(test_scaled, test_target)) #0.925
print(lr.predict(test_scaled[:5]))
proba = lr.predict_proba(test_scaled[:5])
print(np.round(proba, decimals=3))
```

다중분류는 클래스마다 z값을 하나씩 계산한다. 이중 분류의 경우 z값을 시그모이드 함수를 사용하여 확률로 변환했지만, 다중 분류의 경우 **소프트맥스 함수**를 사용하여 z값을 확률로 변환한다.

```python
decision = lr.decision_function(test_scaled[:5])
print(np.round(decision, decimals=2)) #z값 출력.

from scipy.special import softmax
proba = softmax(decision, axis=1) #axis매개변수는 계산할 축을 지정
print(np.round(proba, decimals=3))
#결과값
[[0.    0.014 0.841 0.    0.136 0.007 0.003]
 [0.    0.003 0.044 0.    0.007 0.946 0.   ]
 [0.    0.    0.034 0.935 0.015 0.016 0.   ]
 [0.011 0.034 0.306 0.007 0.567 0.    0.076]
 [0.    0.    0.904 0.002 0.089 0.002 0.001]]
#앞서 구한 proba 배열과 결과가 일치함!
```

**04-1 핵심 키워드**

- **로지스틱 회귀**: 선형 방정식을 사용한 분류 알고리즘
- 다중 분류: 타깃 클래스가 2개 이상인 분류 문제
- **시그모이드 함수**: 이중 분류에서 쓰이며, 선형 방정식의 출력(z)을 0과 1 사이의 확률값으로 출력
- **소프트맥스 함수**: 다중 분류에서 쓰이며, 여러 선형 방정식의 출력 결과를 정규화하여 합이 1이 되도록 만듦.

**04-1 핵심 패키지와 함수**

- scikit-learn
    - `LogisticRegression`: 로지스틱 회귀를 위한 클래스. C매개변수에서 규제의 강도를 제어한다. 작을수록 규제가 강해진다.
    - `predict_proba()`: 예측 확률을 반환하는 메서드
    - `decision_function()`: 모델이 학습한 선형 방정식의 값(z)을 반환하는 메서드.

---

### 04-2 확률적 경사 하강법

앞서 훈련한 모델을 버리지 않고 새로운 데이터에 대해서만 조금씩 훈련할 수 없을까? ⇒이러한 방식이 점진적 학습이다. 대표적인 점진적 학습 알고리즘은 **확률적 경사 하강법(Stochastic Gradient Descent)**이다.

훈련세트에서 랜덤하게 하나의 샘플을 선택하여 가파른 경사를 조금 내려간다. 그 다음 훈련 세트에서 랜덤하게 또 다른 샘플을 하나 선택하여 경사를 조금 내려간다. 이런 식으로 전체 샘플을 모두 사용할 때까지 계속한다. 만약 모든 샘플을 사용했다면, 훈련세트에 모든 샘플을 다시 채워넣고 앞선 과정을 반복한다. 이 때 훈련세트를 한 번 모두 사용하는 텀을 **에포크(epoch)**라고 부른다.

샘플을 1개씩 꺼내는 것이 **확률적 경사 하강법**, 샘플을 여러개씩 꺼내는 것이 **미니배치 경사 하강법**, 샘플을 전부 꺼내는 것이 **배치 경사 하강법**이다.

> **손실함수(loss function)**: 머신러닝 알고리즘이 얼마나 엉터리인지 측정하는 함수. 로지스틱 손실 함수, 크로스엔트로피 손실 함수 등이 있다.
> 

```python
#데이터 준비 및 전처리
import pandas as pd
fish = pd.read_csv('http://bit.ly/fish_csv_data')

fish_input = fish[['Weight', 'Length', 'Diagonal', 'Height', 'Width']].to_numpy()
fish_target = fish[['Species']].to_numpy()
from sklearn.model_selection import train_test_split
train_input, test_input, train_target, test_target = train_test_split(fish_input, fish_target, random_state=42)

from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
ss.fit(train_input)
train_scaled = ss.transform(train_input)
test_scaled = ss.transform(test_input)
```

```python
# 확률적 경사 하강법을 제공하는 분류용 클래스 SGDClassifier
from sklearn.linear_model import SGDClassifier
sc = SGDClassifier(loss='log', max_iter=10, random_state=42)
#loss는 손실함수를 지정하는 매개변수. log는 로지스틱 손실 함수
#max_iter는 수행할 에포트 횟수
sc.fit(train_scaled, train_target)
print(sc.score(train_scaled, train_target)) #0.7731
print(sc.score(test_scaled, test_target)) #0.775
#출력된 훈련세트와 테스트세트의 정확도가 낮은 걸 보아하니 반복 횟수 10번이 부족한 것으로 보임.

sc.partial_fit(train_scaled, train_target)
#partial_fit메서드는 호출할 때마다 1 에포크씩 이어서 훈련한다.
print(sc.score(train_scaled, train_target)) #0.8151
print(sc.score(test_scaled, test_target)) #0.825
#아직 점수가 낮지만 그래도 나아졌다.
```

그렇다면 에포크를 어느 정도로 두어야 가장 뛰어난 점수가 나올까.

```python
import numpy as np
sc = SGDClassifier(loss='log', random_state=42)
train_score = []
test_score = []
classes = np.unique(train_target)

for _ in range(300): #300번의 에포크를 반복
  sc.partial_fit(train_scaled, train_target, classes = classes)
  train_score.append(sc.score(train_scaled, train_target))
  test_score.append(sc.score(test_scaled, test_target))

import matplotlib.pyplot as plt
plt.plot(train_score)
plt.plot(test_score)
plt.xlabel('epoch')
plt.ylabel('accuracy')
plt.show()
```

![주황색은 테스트 세트, 파란색은 훈련 세트이다.](%E1%84%92%E1%85%A9%E1%86%AB%E1%84%8C%E1%85%A1%20%E1%84%80%E1%85%A9%E1%86%BC%E1%84%87%E1%85%AE%E1%84%92%E1%85%A1%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC%20%E1%84%83%E1%85%B5%E1%86%B8%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC(%E1%84%87%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A2%E1%84%89%E1%85%A5%E1%86%AB%20%E1%84%8C%E1%85%A5)%205fee2e5b433a463bbeca29c95c3cd0ee/%EC%97%90%ED%8F%AC%ED%81%AC.jpg)

주황색은 테스트 세트, 파란색은 훈련 세트이다.

50번째 에포크부터는 점수가 거의 향상하지 않고, 100번째 에포크부터는 두 세트 간의 격차가 벌어지고 있다. 따라서 백 번째 에포크가 적절한 반복 횟수로 보인다.

```python
sc = SGDClassifier(loss='log', max_iter=100, tol=None, random_state=42)
#SGDClassifier는 일정 에포크동안 성능이 향상되지 않으면 자동으로 멈춘다
#그러나 tol매개변수를 None으로 지정하면 자동으로 멈추지 않고 끝까지 간다.
sc.fit(train_scaled, train_target)
print(sc.score(train_scaled, train_target)) #0.9579
print(sc.score(test_scaled, test_target)) #0.925
#최종 결과가 좋게 나옴!
```

**04-2 핵심 키워드**

- **확률적 경사 하강법(stochastic gradient descent)**: 훈련 세트에서 샘플 하나씩 꺼내 손실 함수의 경사를 따라 최적의 모델을 찾는 알고리즘.
- 손실함수: 확률적 경사 하강법이 최적화할 대상으로, 이중 분류에는 **로지스틱 회귀 손실함수**를 사용하고, 다중 분류에는 크**로스엔트로피 손실함수**를 사용한다.
- **에포크(epoch)**: 확률적 경사 하강법에서 전체 샘플을 모두 사용하는 한 번 반복을 의미한다.

**04-2 핵심 패키지와 함수**

- scikit-learn
    - **`SGDClassifier`**: 확률적 경사 하강법을 사용한 분류 모델을 만드는 클래스.
        - `loss` 매개변수는 최적화할 손실 함수를 택한다.
        - `penalty` 매개변수는 규제의 종류를 지정한다.
        - `max_iter` 매개변수는 에포크 횟수를 지정한다.
        - `tol` 매개변수는 반복을 멈출 조건이다.
    - `SGDRegressor`: 확률적 경사 하강법을 사용한 회귀 모델을 만드는 클래스

---

## 05 트리 알고리즘

---

### 05-1 결정 트리

와인 겉면에 적힌 알코올 도수, 당도, pH로 와인 종류를 구별하는 프로그램을 만들려 한다. 이것을 로지스틱 회귀로 분류해보자.

```python
#데이터 준비
import pandas as pd
wine = pd.read_csv('https://bit.ly/wine_csv_data')
wine.info() 
#info 메서드는 데이터프라임의 각 열의 데이터 타입과 누락된 데이터를 확인하는 데 쓰인다.
wine.describe()
#describe 메서드는 열에 대한 간략한 통계를 출력해준다.

data = wine[['alcohol','sugar','pH']].to_numpy() #넘파이 배열로 전환
target = wine[['class']].to_numpy()

#훈련 세트와 테스트 세트 나누기
from sklearn.model_selection import train_test_split
train_input, test_input, train_target, test_target = train_test_split(data, target, test_size=0.2, random_state=42)

#훈련세트 전처리
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
ss.fit(train_input)
train_scaled = ss.transform(train_input)
test_scaled = ss.transform(test_input)

#로지스틱 회귀모델 훈련
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
lr.fit(train_scaled, train_target)
print(lr.score(train_scaled, train_target))
print(lr.score(test_scaled, test_target))
#결과값
0.7808350971714451
0.7776923076923077
#다소 낮게 나옴.

print(lr.coef_, lr.intercept_)
#결과값
[[ 0.51270274  1.6733911  -0.68767781]] [1.81777902]
```

이 모델을 머신러닝을 잘 모르는 이에게 설명한다고 가정해보자.

> 이 모델은 알코올 도수 값에 0.51270274를 곱하고 당도에 1.6733911을 곱하고 ... 이 값이 0보다 크면 화이트 와인, 작으면 레드 와인인데, 현재 약 77% 정도를 정확히 화이트 화인으로 분류했습니다.
> 

영 어지러운 소리가 아닐 수 없다. 하지만 순서도처럼 잘 도식화되어 머신러닝 문외한이더라도 쉽게 이해할 수 있는 프로그램이 있으니, 바로 **결정 트리(Decision Tree)**이다.

```python
from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier(random_state=42)
dt.fit(train_scaled, train_target)
print(dt.score(train_scaled, train_target)) #0.9969
print(dt.score(test_scaled, test_target)) #0.8592
#과대적합된 모델.
```

```python
#사이킷런은 plot_tree()함수를 통해 결정 트리를 그림으로 보여준다.
#맨 위 노드를 루트노드, 맨 아래 노드를 리프 노드라 부른다
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
plt.figure(figsize=(10,7))
plot_tree(dt, max_depth=1,filled=True,feature_names=['alcohol','sugar', 'pH'])
#max_depth매개변수를 1로 설정하면 루트노드를 제외하고 하나의 노드를 확장해서 그린다.
plt.show()
```

![결정트리.jpg](%E1%84%92%E1%85%A9%E1%86%AB%E1%84%8C%E1%85%A1%20%E1%84%80%E1%85%A9%E1%86%BC%E1%84%87%E1%85%AE%E1%84%92%E1%85%A1%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC%20%E1%84%83%E1%85%B5%E1%86%B8%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC(%E1%84%87%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A2%E1%84%89%E1%85%A5%E1%86%AB%20%E1%84%8C%E1%85%A5)%205fee2e5b433a463bbeca29c95c3cd0ee/%EA%B2%B0%EC%A0%95%ED%8A%B8%EB%A6%AC.jpg)

루트 노드를 보자. 당도가 -0.239이하인지 질문을 한다. 만약 이하라면 왼쪽 가지로, 초과라면 오른쪽 가지로 이동한다. 총 샘플 수는 5197개이며, 그 중 음성 클래스(레드 와인)는 1,258개, 양성 클래스(화이트 와인)는 3,939개임을 알 수 있다.

그 밑 노드를 보면 오른쪽 노드가 더 색깔이 짙음을 알 수 있다. `plot_tree()`함수에서 `filled=True`로 지정하면 클래스마다 색깔을 부여하고, 특정 클래스의 비율이 높아지면 점점 진한색으로 표시한다.

결정 트리에서는 리프 노드에서 가장 많은 클래스가 예측 클래스가 된다. 두번째 노드가 리프 노드라면, 두 노드 모두 양성 클래스가 과반수이므로 양성으로 예측할 것이다.

> **불순도(impurity)**: 결정 트리 모델이 트리를 성장시키는 기준. 결정 트리 모델은 부모 노드와 자식 노드의 불순도 차이가 가능한 크도록 트리를 성장시킨다. 대표적으로 **지니 불순도(Gini impurity)**가 쓰인다.
> 

지니 불순도 = 1 -(음성 클래스 비율^2 + 양성 클래스 비율^2)

루트 노드를 예로 들면 1,528개가 음성이고 3,939개가 양성이었으므로 지니 불순도는 1- ((1259/5197)^2 + (3937/5197)^2) = 0.367이다. 만약 클래스의 비율이 정확히 반반이라면 **지니 불순도는 0.5**가 되어 최악이 된다.

만약 노드에 하나의 클래스만 있다면 지니 불순도는 0이 되고, 이런 노드를 순수 노드라고 부른다.

부모 노드와 자식 노드 간의 불순도 차이를 **정보 이득(information gain)**이라고 부르고, 결정 트리는 정보 이득을 최대화하는 방식으로 학습한다.

무한정 자라나는 트리는 과대적합을 만들기 마련이다. 따라서 해줄 필요가 있다.

```python
dt = DecisionTreeClassifier(max_depth=3, random_state=42)
dt.fit(train_scaled, train_target)
print(dt.score(train_scaled, train_target))
print(dt.score(test_scaled, test_target))

plt.figure(figsize=(20,15))
plot_tree(dt, filled=True, feature_names=['alcohol','sugar','pH'])
plt.show()
```

![결정트리2.jpg](%E1%84%92%E1%85%A9%E1%86%AB%E1%84%8C%E1%85%A1%20%E1%84%80%E1%85%A9%E1%86%BC%E1%84%87%E1%85%AE%E1%84%92%E1%85%A1%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC%20%E1%84%83%E1%85%B5%E1%86%B8%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC(%E1%84%87%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A2%E1%84%89%E1%85%A5%E1%86%AB%20%E1%84%8C%E1%85%A5)%205fee2e5b433a463bbeca29c95c3cd0ee/%EA%B2%B0%EC%A0%95%ED%8A%B8%EB%A6%AC2.jpg)

결정 트리의 또다른 장점은 클래스별 비율을 가지고 불순도를 계산하기에, 특성값의 스케일을 전처리할 필요가 없다는 것이다.

```python
#어떤 특성이 가장 유용한지 나타내는 특성 중요도
print(dt.feature_importances_)
```

**05-1 핵심 키워드**

- **결정 트리**: 예/아니오에 대한 질문을 이어나가면서 정답을 찾아 학습하는 알고리즘
- **불순도(impurity)**: 결정 트리가 최적의 질문을 찾기 위한 기준. 지니 불순도와 엔트로피 불순도가 있다.
- **정보 이득**: 부모노드와 자식노드의 불순도 차이

**05-2 핵심 패키지와 함수**

- pandas
    - `info()`: 데이터프레임의 요약된 정보 출력
    - `describe()`: 데이터프레임 열의 통계값을 요약
- scikit-learn
    - **`DesicionTreeClassifier`**: 결정 트리 분류 클래스
        - `criterion`매개변수는 불순도를 지정하며 기본값은 **gini(지니불순도)**이다.
        - **`max_depth`**매개변수는 트리가 성장할 최대 깊이를 지정한다.
    - plot_tree()는 결정 트리 모델을 시각화하는 함수이다.
        - `max_depth`매개변수로 나타낼 트리의 깊이를 지정한다
        - `feature_names`매개변수로 특성의 이름을 지정한다
        - `filled`매개변수를 True로 하면 타깃값에 따라 노드의 색을 채운다.

---

### 05-2 교차 검증과 그리드 서치

테스트 세트를 사용해 자꾸 성능을 확인하다보면 점점 테스트 세트에 모델을 맞추게 된다. 일반화 성능을 정확히 예측하려면 가능한 한 테스트 세트를 사용하지 말아야 한다. 모델을 만들고 나서 마지막에 딱 한 번만 사용하는 것이 좋다. 그래서 활용할 세트가 바로 검증세트이다.

> **검증 세트(validation set)**:  훈련 세트에서 모델을 평가한 후 검증 세트로 모델을 평가한다. 테스트하고 싶은 매개변수를 바꿔가며 가장 좋은 모델을 고른다. 매개변수를 정했다면 마지막에 훈련세트와 검증세트를 합쳐 다시 훈련을 하고, 이 때 테스트 세트에서 최종 점수를 평가한다. 보통 훈련:검증:테스트의 비율은 6:2:2이다.
> 

```python
#검증 세트 만들어보기
import pandas as pd
wine = pd.read_csv('https://bit.ly/wine_csv_data')
data = wine[['alcohol','sugar','pH']].to_numpy()
target = wine['class'].to_numpy()
from sklearn.model_selection import train_test_split
train_input, test_input, train_target, test_target = train_test_split(data, target, test_size=0.2, random_state=42)
#여기까진 동일하지만, 이번엔 train_input과 train_target을 다시 train_test_split()에 넣는다.

sub_input, val_input, sub_target, val_target = train_test_split(train_input, train_target, test_size=0.2, random_state=42)
#test_size매개변수를 0.2로 하여 train_input의 약 20%를 val_input으로 만든다.
```

이 때 **교차검증(cross validation)**을 활용하면 더 안정적인 검증 점수를 얻을 수 있다. 다음 그림을 보면 교차검증을 쉽게 이해할 수 있다.

![Untitled](%E1%84%92%E1%85%A9%E1%86%AB%E1%84%8C%E1%85%A1%20%E1%84%80%E1%85%A9%E1%86%BC%E1%84%87%E1%85%AE%E1%84%92%E1%85%A1%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC%20%E1%84%83%E1%85%B5%E1%86%B8%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC(%E1%84%87%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A2%E1%84%89%E1%85%A5%E1%86%AB%20%E1%84%8C%E1%85%A5)%205fee2e5b433a463bbeca29c95c3cd0ee/Untitled%202.png)

```python
from sklearn.model_selection import cross_validate #교차 검증 함수
scores = cross_validate(dt, train_input, train_target) 
#앞에서처럼 직접 데이터를 떼어낼 필요 없이 그냥 변수로 전달만 하면 됨
print(scores)
#이 함수는 fit_time, score_tim, test_score 키를 가진 딕셔너리를 반환한다.
import numpy as np
print(np.mean(scores['test_score'])) #각각의 5개 폴드의 검증점수의 평균
```

한 가지 주의할 점은 원래 `train_test_split()`을 사용할 땐 전체 데이터를 섞은 후 훈련 세트를 준비했지만,  `cross_validation()`의 경우엔 훈련 세트를 섞으려면 분할기(`splitter`)를 지정해야 한다.

```python
splitter = StratifiedKFold(n_splits=10, shuffle=True,random_state=42)
scores = cross_validate(dt, train_input, train_target, cv=splitter)
print(np.mean(scores['test_score']))
```

하이퍼 파라미터는 사용자가 직접 지정하는 파라미터라고 했다. 만약 결정 트리 모델에서 최적의 `max_depth` 값을 찾았다고 가정해보자. 이 때 `min_samples_split`를 바꿔가며 최적의 값을 찾는다면, 옳은 방법일까? 안타깝게도 아니다. `max_depth`의 최적값은 `min_samples_split`이 바뀜에 따라 함께 달라진다.

이렇게 골머리를 앓으며 하이퍼파라미터를 튜닝할 필욘 없다. 사이킷런에서 제공하는 그리드서치를 이용하면 되기 때문이다. **`GridSearchCV`** 클래스는 **하이퍼파라미터 탐색과 교차 검증**을 한 번에 수행해준다. 

```python
from sklearn.model_selection import GridSearchCV
params = {'min_impurity_decrease':[0.0001, 0.0002, 0.0003, 0.0004, 0.0005]}
# 탐색할 매개변수와 탐색할 값의 리스트를 딕셔너리로 넣어준다.

gs = GridSearchCV(DecisionTreeClassifier(random_state=42), params, n_jobs=-1)
#GridSearchCV클래스에 탐색 대상 모델과 params변수를 전달하여 객체를 만든다
#n_jobs매개변수는 병렬 실행에 사용할 cpu코어 수를 지정한다. -1로 지정하면 시스템의 모든 코어를 사용한다.
gs.fit(train_input, train_target)
#매개변수 값은 5개이고 5폴드교차검증을 하니 총 25개의 모델을 훈련한다.
dt = gs.best_estimator_ #훈련이 끝나면 25개 모델 중 검증 점수가 가장 높은 모델의 매개변수 조합을 반환해준다.
print(dt.score(train_input, train_target))

print(gs.best_params_) #최적의 매개변수
#print(gs.cv_results_['mean_test_score']) #각 매개변수에서 수행한 교차검증의 평균 점수
```

```python
#좀 더 복잡한 경우
params = {'min_impurity_decrease':np.arange(0.0001, 0.001, 0.0001), 
          'max_depth':range(5,20,1),
          'min_samples_split':range(2,100,10)}
#첫번째 매개변수는 9개, 두번째는 15개, 세번째는 10개로 수행할 교차검증 횟수는 1,350번!
gs = GridSearchCV(DecisionTreeClassifier(random_state=42),params,n_jobs=-1)
gs.fit(train_input, train_target)
print(gs.best_params_)
dt = gs.best_estimator_
print(dt.score(train_input,train_target))
print(np.max(gs.cv_results_['mean_test_score']))
```

매개변수의 값이 수치일 때나 너무 많은 매개변수 조건이 있어 그리드 서치 수행 시간이 오래 걸릴 때에는 **랜덤 서치**를 사용하면 좋다. 랜덤 서치에는 매개변수 값의 목록을 전달하지 않고 매개변수를 샘플링할 수 있는 확률 분포객체를 전달한다.

```python
from scipy.stats import uniform, randint
rgen = randint(0,10) #0에서 10 사이의 정수값 무작위로 뽑기
rgen.rvs(10) #10개 뽑기
ugen=uniform(0,1) #0에서 10 사이의 실수값 무작위로 뽑기
ugen.rvs(10) #10개 뽑기
```

```python
params = {'min_impurity_decrease':uniform(0.0001, 0.001), 
          'max_depth':randint(20,50),
          'min_samples_split':randint(2,25),
          'min_samples_leaf':randint(1,25),
          }
#탐색할 매개변수 범위를 위와 같이 설정

from sklearn.model_selection import RandomizedSearchCV
gs = RandomizedSearchCV(DecisionTreeClassifier(random_state=42),params,n_iter=100, n_jobs=-1, random_state=42)
#n_iter매개변수에 샘플링 횟수를 지정한다.
gs.fit(train_input, train_target)
print(gs.best_params_)
```

이렇게 하면 `params`에 정의된 매개변수 범위에서 총 100번을 샘플링 하여 교차검증을 수행하고 최적의 매개변수 조합을 얻는다. 앞서 그리드 서치는 1350번(9*15*10)에 걸친 것을 랜덤서치는 100번만에 수행했다. 즉, **훨씬 교차 검증 수를 줄이면서 넓은 영역을 효과적으로 탐색**할 수 있다.

**05-2 핵심 키워드**

- **검증 세트(validation set)**: 하이퍼 파라미터 튜닝을 위해 모델을 평가할 때 테스트 세트를 사용하지 않기 위해 훈련 세트에서 다시 떼어 낸 데이터 세트
- **교차 검증(cross validation)**: 훈련 세트를 여러 폴드로 나눈 다음 한 폴드가 검증 세트의 역할을 하고 나머지 폴드에서 모델을 훈련하는 방식
- **그리드 서치**: 탐색할 매개변수를 나열하면 교차검증을 수행하여 가장 좋은 검증 점수의 매개변수 조합을 반환해준다.
- **랜덤 서치**: 연속된 매개변수값의 범위를 설정하면 교차검증을 수행하여 가장 좋은 검증 점수의 매개변수 조합을 반환해준다.

**05-2 핵심 패키지와 함수**

- scikit-learn
    - **`cross_validation()`**: 교차 검증을 수행하는 함수
        - 첫번째 매개변수에 교차검증을 수행할 모델 객체 전달
        - 두번째, 세번째 매개변수에 특성과 타깃 데이터 전달
        - `cv`매개변수에 교차검증 폴드 수나 스플리터 객체를 지정.
        - **`n_jobs`**매개변수에 사용할 cpu코어 수를 지정. -1이면 시스템의 모든 코어 사용
    - **`GridSearchCV()`**: 교차 검증으로 하이퍼파라미터 탐색을 수행
        - 첫번째 매개변수로 그리드 서치를 수행할 모델 객체를 전달
        - 두번째 매개변수로 탐색할 모델의 매개변수를 전달
    - **`RandomizedSearchCV`**: 교차 검증으로 랜덤한 하이퍼파라미터 탐색을 수행
        - 첫번째 매개변수로 랜덤 서치를 수행할 모델 객체를 전달
        - 두번째 매개변수로 탐색할 모델의 매개변수와 확률분포 객체 전달

---

### 05-3 트리의 앙상블

정형 데이터를 다루는 데 가장 뛰어난 성과를 내는 알고리즘이 **앙상블 학습(ensemble learning)**이다. 앙상블 학습은 대부분 결정 트리를 기반으로 만들어져 있다.

> **랜덤 포레스트(random forest)**: 앙상블 학습의 대표주자 중 하나로 안정적인 성능 덕분에 널리 사용되고 있다. **부트스트랩 샘플**을 사용하고 랜덤하게 일부 특성을 선택하여 결정 트리를 만든다.
> 

1,000개가 들어있는 가방에서 100개씩 샘플을 뽑는다면 먼저 1개를 뽑고 뽑은 한 개를 가방에 다시 넣고 다음 샘플을 뽑는다. 이렇게 중복을 허용하는 샘플을 **부트스트랩 샘플(bootstrap sample)**이라고 한다. 기본적으로 샘플 개수는 훈련 세트와 같게 한다.

또한 각 노드를 분할 할 때 전체 특성 중 일부를 무작위로 고른다. **`RandomForestClassifier`**는 기본적으로 전체 특성 개수의 제곱근만큼의 특성을 선택한다. 즉 4개의 특성이 있다면 노드마다 2개를 랜덤하게 선택한다. 이 2개 중에서 최적의 분할을 찾아나간다.

```python
#데이터 준비
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
wine = pd.read_csv('https://bit.ly/wine_csv_data')
data = wine[['alcohol', 'sugar', 'pH']].to_numpy()
target = wine[['class']].to_numpy()
train_input, test_input, train_target, test_target = train_test_split(data, target,test_size=0.2, random_state=42)

#교차 검증 수행
from sklearn.model_selection import cross_validate
#랜덤 포레스트 분류 클래스 import
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_jobs=-1, random_state=42)
#RandomForestClassifier는 기본적으로 100개의 트리를 사용하므로 n_jobs를 -1로 하여 cpu를 최대한 많이 사용하는 것이 좋다.
scores = cross_validate(rf, train_input, train_target, return_train_score=True, n_jobs=-1)
print(np.mean(scores['train_score']), np.mean(scores['test_score']))
#결과값
0.9973541965122431 0.8905151032797809
```

```python
rf.fit(train_input, train_target)
#랜덤포레스트로 훈련을 시키고 특성의 중요도를 확인해보자.
print(rf.feature_importances_)
#결과값 [0.23167441 0.50039841 0.26792718]
```

랜덤포레스트에서의 특성 중요도와 결정트리에서의 특성 중요도가 다른 것으로 나타냈다. 이는 랜덤포레스트가 특성의 일부를 랜덤하게 선택하여 결정 트리를 훈련하기 때문이다. 그 결과 좀 더 많은 특성이 훈련에 기여할 기회를 얻고, 일반화 성능을 높인다.

부트스트랩 샘플에 포함되지 않고 남은 샘플을 **OOB(out of bag)샘플**이라고 한다. 이 샘플을 사용하여 부트스트랩 샘플로 훈련한 결정 트리를 평가할 수 있다! 마치 검증세트의 역할을 수행하는 것이다. 고로, 굳이 검증세트를 수행해서 사용할 샘플을 낭비할 필요가 없다.

```python
rf = RandomForestClassifier(oob_score=True, n_jobs=-1, random_state=42)
rf.fit(train_input, train_target)
print(rf.oob_score_)
```

> **엑스트라 트리(Extra Trees)**: 랜덤 포레스트와 유사하나, 부트스트랩 샘플을 사용하지 않고 전체 훈련세트를 사용한다. 대신 노드를 분할할 때 가장 좋은 분할을 찾는 것이 아니라 무작위로 분할한다. 이는 `spliter`매개변수를 random으로 지정한 것과 같은 효과를 준다. 이러한 무작위 분할은 **계산 속도를 빠르게 해준다**.
> 

```python
from sklearn.ensemble import ExtraTreesClassifier
et = ExtraTreesClassifier(n_jobs=-1, random_state=42)
scores = cross_validate(et, train_input, train_target, return_train_score=True, n_jobs=-1)
print(np.mean(scores['train_score']), np.mean(scores['test_score']))
#결과값
0.9974503966084433 0.8887848893166506
```

> **그레이디언트 부스팅(Gradient boosting)**: 깊이가 얕은 결정 트리를 사용하여 이전 트리의 오차를 보완하는 방식으로 앙상블하는 방법. 여러 분류기가 순차적으로 학습하되, 앞에서 학습한 분류기가 예측이 틀린 데이터에 대해 올바르게 예측하게끔, 다음 분류기에 가중치를 부여한다.
> 

앞선 트리의 오차를 보완하기에 랜덤 포레스트보다 좋은 성능을 낼 수 있다. 그러나 순서대로 트리를 추가하기 때문에(종속적이기 때문에) **훈련속도가 느리다**. 순서대로 트리를 추가한다는 것은 병렬 수행이 불가능함을 의미하고, 따라서 `n_jobs`매개변수도 존재하지 않는다.

```python
from sklearn.ensemble import GradientBoostingClassifier
#GradientBoostingClassifier은 max_depth가 3인 결정 트리를 100개 사용한다.
gb = GradientBoostingClassifier(random_state=42)
scores=cross_validate(gb, train_input, train_target, return_train_score=True, n_jobs=-1)
print(np.mean(scores['train_score']), np.mean(scores['test_score']))

gb = GradientBoostingClassifier(n_estimators=500, learning_rate=0.2, random_state=42)
scores = cross_validate(gb, train_input, train_target, return_train_score=True, n_jobs=-1)
print(np.mean(scores['train_score']), np.mean(scores['test_score']))
```

> **히스토그램 기반 그레이디언트 부스팅(Histogram-based Gradient Boosting)**: 정형 데이터를 다루는 알고리즘 중 가장 인기가 많은 알고리즘이다. 입력 특성을 256개 구간으로 나누기 때문에 최적의 분할을 매우 빠르게 찾을 수 있다. 또한 256개의 구간 중에서 하나를 떼어 놓고 누락된 값을 위해 사용한다.
> 

```python
from sklearn.experimental import enable_hist_gradient_boosting
from sklearn.ensemble import HistGradientBoostingClassifier
hgb = HistGradientBoostingClassifier(random_state=42)
scores = cross_validate(hgb, train_input, train_target, return_train_score=True)
print(np.mean(scores['train_score']), np.mean(scores['test_score']))
```

히스토그램 기반 그레이디언트 부스팅의 특성 중요도를 계산하는 함수는 `permutation_importance()`이다. 이 함수는 특성을 하나씩 랜덤하게 섞어 모델의 성능이 변화하는지를 관찰하여 어떤 특성이 중요한지 계산한다.

```python
from sklearn.inspection import permutation_importance
hgb.fit(train_input, train_target)
result=permutation_importance(hgb, train_input, train_target, n_repeats=10, random_state=42, n_jobs=-1)
#n_repeats매개변수는 랜덤하게 섞을 횟수를 지정한다.
print(result.importances_mean)
#결과값(중요도, 평균, 표준편차)
[0.08876275 0.23438522 0.08027708]

hgb.score(test_input, test_target)
#결과값
0.8723076923076923
#이 값은 단일 결정 트리보다 높은 값.
```

**05-3 핵심 키워드**

- **앙상블 학습**: 더 좋은 예측을 위해 여러 개의 트리를 훈련하는 알고리즘
- **랜덤 포레스트**: **부트스트랩 샘플**을 사용하고 랜덤하게 일부 특성을 선택하여 트리를 만드는 알고리즘
- **엑스트라 트리**: 부트스트랩 샘플을 사용하지 않고 랜덤하게 노드를 분할해 빠른 속도가 장점인 알고리즘
- **그레이디언트 부스팅**: 트리를 연속적으로 추가하여 손실 함수를 최소화하는 알고리즘. 훈련 속도는 좀 느리지만 가장 좋은 성능을 기대할 수 있다. 대표적인 것이 **히스토그램 기반 그레이디언트 부스팅**이다.

**05-3 핵심 패키지와 함수**

- scikit-learn
    - **`RandomForestClassifier`**: 랜덤 포레스트 분류 클래스
        - `n_estimators`매개변수는 트리의 개수를 지정. 기본값은 100
        - `criterion`매개변수는 불순도를 지정. 기본값은 gini
        - `max_depth`매개변수는 트리가 성장할 최대 깊이
        - `min_samples_split`는 노드를 나누기 위한 최소 샘플 개수
        - `max_features`매개변수는 최적의 분할을 위해 탐색할 특성의 개수. 기본값은 특성 개수의 제곱근.
        - `oob_score`매개변수는 **OOB샘플**을 사용할지 지정
    - **`ExtraTreesClassifier`**: 엑스트라 트리 분류 클래스
        - 랜덤 포레스트와 대부분 동일
    - **`GradientBoostingClassifier`**: 그레이디언트 부스팅 분류 클래스
        - `loss`매개변수는 손실함수를 지정
        - `learning_rate`매개변수는 트리가 앙상블에 기여하는 정도를 조절. 기본값은 0.1
        - `subsamples`매개변수는 사용할 훈련세트의 샘플 비율을 지정
        - `max_depth`매개변수의 기본값은 3
    - **`HistGradientBoostingClassifier`**: 히스토그램 기반 그레이디언트 부스팅 분류 클래스
        - `max_iter`매개변수는 부스팅 단계를 수행하는 트리의 개수
        - `max_bins`는 입력 데이터를 나눌 구간의 개수. 기본값은 255.

---

## 06 비지도 학습

---

### 06-1 군집 알고리즘

타깃을 모르는 사진을 종류별로 분류하려할 때, 이것은 **비지도 학습(unsupervised learning)**이다.

```python
!wget https://bit.ly/fruits_300_data -O fruits_300.npy
#!으로 시작하면 파이썬 코드가 아니라 리눅스 셀 명령으로 이해
import numpy as np
import matplotlib.pyplot as plt
fruits = np.load('fruits_300.npy') #load(): 넘파이에서 npy를 로드하기 위한 메서드
print(fruits.shape) #(300, 100, 100)
#첫번째 차원(300)은 샘플의 개수를, 두번째 차원(100)은 이미지 높이를, 세번째 차원(100)은 이미지 너비를 의미한다.

plt.imshow(fruits[0], cmap='gray_r') #0에 가까울수록 밝게 나타남
plt.show()
```

![사과2.jpg](%E1%84%92%E1%85%A9%E1%86%AB%E1%84%8C%E1%85%A1%20%E1%84%80%E1%85%A9%E1%86%BC%E1%84%87%E1%85%AE%E1%84%92%E1%85%A1%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC%20%E1%84%83%E1%85%B5%E1%86%B8%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC(%E1%84%87%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A2%E1%84%89%E1%85%A5%E1%86%AB%20%E1%84%8C%E1%85%A5)%205fee2e5b433a463bbeca29c95c3cd0ee/%EC%82%AC%EA%B3%BC2.jpg)

```python
fig, axs = plt.subplots(1,2)
#subplots()함수의 두 매개변수는 그래프를 쌓을 행과 열을 지정.
axs[0].imshow(fruits[100], cmap='gray_r')
axs[1].imshow(fruits[200], cmap='gray_r')
plt.show()
```

![파인애플 바나나.jpg](%E1%84%92%E1%85%A9%E1%86%AB%E1%84%8C%E1%85%A1%20%E1%84%80%E1%85%A9%E1%86%BC%E1%84%87%E1%85%AE%E1%84%92%E1%85%A1%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC%20%E1%84%83%E1%85%B5%E1%86%B8%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC(%E1%84%87%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A2%E1%84%89%E1%85%A5%E1%86%AB%20%E1%84%8C%E1%85%A5)%205fee2e5b433a463bbeca29c95c3cd0ee/%ED%8C%8C%EC%9D%B8%EC%95%A0%ED%94%8C_%EB%B0%94%EB%82%98%EB%82%98.jpg)

넘파이 배열로 나눌 때 100*100이미지를 펼쳐서 길이가 10,000인 1차원 배열로 만들면 배열을 계산할 때 편리하다.

```python
apple = fruits[0:100].reshape(-1, 100*100)
pineapple = fruits[100:200].reshape(-1, 100*100)
banana = fruits[200:300].reshape(-1, 100*100)
print(apple.mean(axis=1)) #axis를 0으로 하면 행을 따라 계산하고 1로 하면 열을 따라 계산함.
```

이제 사과, 파인애플, 바나나 각 **샘플의 픽셀 평균값**을 계산해보고, 이를 히스토그램으로 나타내보자.

```python
plt.hist(np.mean(apple, axis=1), alpha=0.8) #alpha매개변수를 1보다 작게 하면 투명도를 준다.
plt.hist(np.mean(pineapple, axis=1), alpha=0.8)
plt.hist(np.mean(banana, axis=1), alpha=0.8)
plt.legend(['apple', 'pineapple', 'banana']) #legend()함수로 범례 지정
plt.show()
```

![gltmxhrmfoa.jpg](%E1%84%92%E1%85%A9%E1%86%AB%E1%84%8C%E1%85%A1%20%E1%84%80%E1%85%A9%E1%86%BC%E1%84%87%E1%85%AE%E1%84%92%E1%85%A1%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC%20%E1%84%83%E1%85%B5%E1%86%B8%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC(%E1%84%87%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A2%E1%84%89%E1%85%A5%E1%86%AB%20%E1%84%8C%E1%85%A5)%205fee2e5b433a463bbeca29c95c3cd0ee/gltmxhrmfoa.jpg)

바나나는 픽셀 평균값이 대체로 40이하이지만, 사과와 파인애플은 평균값이 서로 겹친다. 고로 픽셀값만으로 이 둘을 비교하리란 어렵다.

샘플의 픽셀 평균값이 아니라 **픽셀별 평균값**을 비교해보는 것이 좋다.

```python
fig, axs = plt.subplots(1, 3, figsize=(20,5))
axs[0].bar(range(10000), np.mean(apple, axis=0)) #막대그래프
axs[1].bar(range(10000), np.mean(pineapple, axis=0))
axs[2].bar(range(10000), np.mean(banana, axis=0))
plt.show()
```

![세 과일별 특징이 두드러진다.](%E1%84%92%E1%85%A9%E1%86%AB%E1%84%8C%E1%85%A1%20%E1%84%80%E1%85%A9%E1%86%BC%E1%84%87%E1%85%AE%E1%84%92%E1%85%A1%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC%20%E1%84%83%E1%85%B5%E1%86%B8%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC(%E1%84%87%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A2%E1%84%89%E1%85%A5%E1%86%AB%20%E1%84%8C%E1%85%A5)%205fee2e5b433a463bbeca29c95c3cd0ee/bar.jpg)

세 과일별 특징이 두드러진다.

```python
apple_mean = np.mean(apple, axis=0).reshape(100,100)
pineapple_mean = np.mean(pineapple, axis=0).reshape(100,100)
banana_mean = np.mean(banana, axis=0).reshape(100,100)
fig, axs = plt.subplots(1,3,figsize=(20,5))
axs[0].imshow(apple_mean, cmap='gray_r')
axs[1].imshow(pineapple_mean, cmap='gray_r')
axs[2].imshow(banana_mean, cmap='gray_r')
plt.show()
```

![dkdk.jpg](%E1%84%92%E1%85%A9%E1%86%AB%E1%84%8C%E1%85%A1%20%E1%84%80%E1%85%A9%E1%86%BC%E1%84%87%E1%85%AE%E1%84%92%E1%85%A1%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC%20%E1%84%83%E1%85%B5%E1%86%B8%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC(%E1%84%87%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A2%E1%84%89%E1%85%A5%E1%86%AB%20%E1%84%8C%E1%85%A5)%205fee2e5b433a463bbeca29c95c3cd0ee/dkdk.jpg)

위 사진은 픽셀 평균값을 100*100으로 재반환하여 이미지로 출력한 것이다. 이 대표 이미지와 가까운 사진을 골라낸다면 사과, 파인애플, 바나나를 구분할 수 있을 것이다.

대표이미지와 샘플 각각의 오차를 계산한다. 그리고 이 오차가 가장 적은 것부터 차례대로 인덱스를 매긴다. 그 인덱스를 원본 샘플 데이터에 적용해서 오차가 작은 것이 정말 그 과일이 맞는지 확인해보자.

```python
abs_diff = np.abs(fruits - banana_mean) #바나나 대표이미지와 각 샘플간의 차이를 3차원 배열로
abs_mean = np.mean(abs_diff, axis=(1,2)) # 각 샘플에 대한 평균을 구하여 1차원으로 만듦

banana_index = np.argsort(abs_mean)[:100] 
#np.argsort()함수는 작은 것에서 큰 순서대로 나열한 abs_mean의 인덱스를 반환
fig, axs = plt.subplots(10, 10, figsize=(10,10))
for i in range(10): #10*10 형태로 만들려는 이중 반복문
  for j in range(10):
    axs[i,j].imshow(fruits[banana_index[i*10+j]], cmap='gray_r')
    axs[i,j].axis('off')
plt.show()
```

![qksksksk.jpg](%E1%84%92%E1%85%A9%E1%86%AB%E1%84%8C%E1%85%A1%20%E1%84%80%E1%85%A9%E1%86%BC%E1%84%87%E1%85%AE%E1%84%92%E1%85%A1%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC%20%E1%84%83%E1%85%B5%E1%86%B8%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC(%E1%84%87%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A2%E1%84%89%E1%85%A5%E1%86%AB%20%E1%84%8C%E1%85%A5)%205fee2e5b433a463bbeca29c95c3cd0ee/qksksksk.jpg)

바나나 대표 이미지와 오차가 작은 100개를 골랐더니 2개를 제외하곤 모두 바나나이다. 꽤 정확하다! 이렇게 비슷한 샘플끼리 그룹으로 모으는 작업을 **군집(clustering)**이라고 하고, 군집 알고리즘에서 만든 그룹을 **클러스터**라고 부른다.

**06-1 핵심 키워드**

- **비지도 학습**: 머신러닝의 한 종류로 훈련 데이터에 타깃이 없다.
- **군집**: 비슷한 샘플끼리 하나의 그룹으로 모으는 대표적인 비지도 학습 작업

---

### 06-2 k평균

앞선 절에선 사과, 파인애플, 바나나 사진임을 미리 알고 있었기에 각각의 대표이미지를 뽑아놓고 가장 오차가 적은 과일을 찾을 수 있었다. 하지만 진짜 비지도학습에서는 사진에 어떤 과일이 들어있는지 알지 못한다.

이런 경우 **k-평균(k-mean)군집 알고리즘**이 평균값을 자동으로 찾아준다. 이 평균값이 클러스터의 중심에 위치하므로 **클러스터 중심(cluster center)** 또는 **센트로이드(centroid)**라고 불린다.

![Untitled](%E1%84%92%E1%85%A9%E1%86%AB%E1%84%8C%E1%85%A1%20%E1%84%80%E1%85%A9%E1%86%BC%E1%84%87%E1%85%AE%E1%84%92%E1%85%A1%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC%20%E1%84%83%E1%85%B5%E1%86%B8%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC(%E1%84%87%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A2%E1%84%89%E1%85%A5%E1%86%AB%20%E1%84%8C%E1%85%A5)%205fee2e5b433a463bbeca29c95c3cd0ee/Untitled%203.png)

k-평균 알고리즘의 작동방식은 다음과 같다.

1. 무작위로 k개의 클러스터 중심을 정한다.(위 그림에서 c1, c2, c3)
2. 각 샘플에서 가장 가까운 클러스터 중심을 찾아 해당 클러스터의 샘플로 지정한다.
3. 클러스터에 속한 샘플의 평균값으로 클러스터 중심을 변경한다.
4. 클러스터 중심에 변화가 없을 때까지 2번으로 돌아가 반복한다.

```python
!wget https://bit.ly/fruits_300_data -O fruits_300.npy
import numpy as np
fruits = np.load('fruits_300.npy')
fruits_2d = fruits.reshape(-1, 100*100) #2차원 배열로 전환
```

```python
from sklearn.cluster import KMeans
km = KMeans(n_clusters=3, random_state=42)
#n_clusters매개변수는 클러스터 개수를 지정한다.
km.fit(fruits_2d)
#비지도 학습이므로 fit() 메서드에 타깃 데이터를 넣지 않는다.
print(km.labels_) #각 샘플이 어떤 레이블에 해당되는지 나타내는 속성
print(np.unique(km.labels_, return_counts=True)) #3개의 레이블이 각각 몇개인지 확인
#결과값
(array([0, 1, 2], dtype=int32), array([ 91,  98, 111]))
#각각 91개, 98개, 111개이다.
```

이제 3개의 클러스터가 어떤 이미지를 모았는지 그림으로 출력해보자.

```python
import matplotlib.pyplot as plt
def draw_fruits(arr, ratio=1):
  n = len(arr) #n은 샘플 개수
  rows = int(np.ceil(n/10)) #한줄에 10개씩 출력할거라 샘플을 10개로 나눈 값을 행으로.
  cols = n if rows<2 else 10
  fig, axs = plt.subplots(rows, cols, figsize=(cols*ratio, rows*ratio), squeeze=False)
  for i in range(rows):
    for j in range(cols):
      if i*10+j < n:
        axs[i,j].imshow(arr[i*10+j], cmap='gray_r')
      axs[i,j].axis('off')
  plt.show()
```

```python
draw_fruits(fruits[km.labels_==0])
```

![사과.jpg](%E1%84%92%E1%85%A9%E1%86%AB%E1%84%8C%E1%85%A1%20%E1%84%80%E1%85%A9%E1%86%BC%E1%84%87%E1%85%AE%E1%84%92%E1%85%A1%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC%20%E1%84%83%E1%85%B5%E1%86%B8%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC(%E1%84%87%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A2%E1%84%89%E1%85%A5%E1%86%AB%20%E1%84%8C%E1%85%A5)%205fee2e5b433a463bbeca29c95c3cd0ee/%EC%82%AC%EA%B3%BC.jpg)

```python
draw_fruits(fruits[km.labels_==1])
```

![qksksksk.jpg](%E1%84%92%E1%85%A9%E1%86%AB%E1%84%8C%E1%85%A1%20%E1%84%80%E1%85%A9%E1%86%BC%E1%84%87%E1%85%AE%E1%84%92%E1%85%A1%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC%20%E1%84%83%E1%85%B5%E1%86%B8%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC(%E1%84%87%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A2%E1%84%89%E1%85%A5%E1%86%AB%20%E1%84%8C%E1%85%A5)%205fee2e5b433a463bbeca29c95c3cd0ee/qksksksk%201.jpg)

```python
draw_fruits(fruits[km.labels_==2])
```

![vkdlsdovmf.jpg](%E1%84%92%E1%85%A9%E1%86%AB%E1%84%8C%E1%85%A1%20%E1%84%80%E1%85%A9%E1%86%BC%E1%84%87%E1%85%AE%E1%84%92%E1%85%A1%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC%20%E1%84%83%E1%85%B5%E1%86%B8%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC(%E1%84%87%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A2%E1%84%89%E1%85%A5%E1%86%AB%20%E1%84%8C%E1%85%A5)%205fee2e5b433a463bbeca29c95c3cd0ee/vkdlsdovmf.jpg)

레이블2 클러스터는 파인애플에 사과 9개와 바나나 2개가 섞여있다. k-평균 알고리즘이 이 샘플들을 완벽하게 구별해내지는 못했다.

`KMeans`클래스가 최종적으로 찾은 클러스터 중심은 `cluster_centers` 속성에 저장되어 있다.

```python
draw_fruits(km.cluster_centers_.reshape(-1,100,100), ratio=3)
#이 배열은 fruits_2d 샘플의 클러스터 중심이기에 이미지로 출력하려면 100*100 크기로 바꿔야 함
```

![eovy.jpg](%E1%84%92%E1%85%A9%E1%86%AB%E1%84%8C%E1%85%A1%20%E1%84%80%E1%85%A9%E1%86%BC%E1%84%87%E1%85%AE%E1%84%92%E1%85%A1%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC%20%E1%84%83%E1%85%B5%E1%86%B8%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC(%E1%84%87%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A2%E1%84%89%E1%85%A5%E1%86%AB%20%E1%84%8C%E1%85%A5)%205fee2e5b433a463bbeca29c95c3cd0ee/eovy.jpg)

앞선 절에서 사과, 바나나, 파인애플의 픽셀 평균값을 출력했던 것과 [매우 비슷](https://www.notion.so/5fee2e5b433a463bbeca29c95c3cd0ee)하다.

우리는 타깃값을 사용하진 않았지만 `n_clusters`를 3으로 지정하는 편법을 사용했다. 마치 과일이 3종류인 것을 미리 알고있던 양 말이다. **실전에서는 클러스터 개수를 전혀 알 수 없다**. 이럴 때 최적의 클러스터 개수는 어떻게 찾을 수 있을까?

적절한 클러스터 개수를 찾는 가장 대표적 방법은 **엘보우(elbow)**이다. k-평균 알고리즘은 클러스터 중심과 샘플 사이의 거리를 잴 수 있다. 이 거리의 제곱 합을 **이너셔(inertia)**라고 부르는데, 이는 클러스터에 속한 샘플이 얼마나 가까이 모여있는지를 나타내는 값이다.

일반적으로 클러스터 개수가 늘어나면 클러스터 개개의 크기가 줄어듦에 따라 이너셔도 줄어든다. 엘보우 방법은 클러스터 개수를 늘려가며 이너셔의 변화를 관찰하여 최적의 개수를 찾는 방법이다.

```python
inertia=[]
for k in range(2,7): #클러스터 개수를 2~6까지 바꿔가며 반복
  km = KMeans(n_clusters=k, random_state=42)
  km.fit(fruits_2d)
  inertia.append(km.inertia_)
plt.plot(range(2,7), inertia)
plt.xlabel('k')
plt.ylabel('inertia')
plt.show()
```

![이너셔.jpg](%E1%84%92%E1%85%A9%E1%86%AB%E1%84%8C%E1%85%A1%20%E1%84%80%E1%85%A9%E1%86%BC%E1%84%87%E1%85%AE%E1%84%92%E1%85%A1%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC%20%E1%84%83%E1%85%B5%E1%86%B8%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC(%E1%84%87%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A2%E1%84%89%E1%85%A5%E1%86%AB%20%E1%84%8C%E1%85%A5)%205fee2e5b433a463bbeca29c95c3cd0ee/%EC%9D%B4%EB%84%88%EC%85%94.jpg)

위 그래프에서 꺾이는 지점(k=3부근)이 바로 이너셔의 변화가 꺾이는 타이밍, 즉 군집 효과가 줄어드는 때이다.

**06-2 핵심 키워드**

- **k-평균 알고리즘**: 처음에 랜덤하게 클러스터 중심을 정하고 중심을 이동하고 다시 클러스터를 재편성하는 과정을 반복하여 최적의 클러스터를 구성하는 알고리즘
- **클러스터 중심**: k-평균 알고리즘이 만든 클러스터에 속한 샘플의 **특성 평균값**.
- **엘보우 방법**: 최적의 클러스터 개수를 정하는 방법. 클러스터 개수에 따라 이너셔 감소가 꺾이는 지점이 적절한 클러스터 개수가 된다.

**06-2 핵심 패키지와 함수**

- scikit-learn
    - **`KMeans`**: k-평균 알고리즘 클래스
        - **`n_clusters`**매개변수는 클러스터 개수를 지정. 기본값은 8.

---

### 06-3 주성분 분석

차원이 여러 개일 때 이를 줄일 수 있으면 저장 공간을 크게 절약할 수 있을 것이다. 이를 위해 **차원 축소(dimensionality reduction)** 알고리즘을 다뤄보자.  차원 축소는 데이터를 잘 나타내는 일부 특성을 선택한다.

또한 줄어든 차원에서 손실을 줄이며 다시 원본 차원으로 복원할 수도 있다. 그러한 대표적인 알고리즘이 바로 **주성분 분석(PCA**, principal component analysis)이다.

데이터에 있는 분산이 큰 방향이 바로 주성분 벡터이다. 이것이 첫번째 주성분이고, 이 벡터에 수직이고 분산이 가장 큰 다음 방향이 두번째 주성분이 된다.

일반적으로 주성분은 원본 특성의 개수만큼 찾을 수 있다. 이제 사이킷런으로 과일 사진 데이터에서 주성분 분석을 해보자.

```python
#데이터 준비
!wget https://bit.ly/fruits_300_data -O fruits_300.npy
import numpy as np
fruits = np.load('fruits_300.npy')
fruits_2d = fruits.reshape(-1,100*100)
```

```python
from sklearn.decomposition import PCA
pca =  PCA(n_components=50)
#n_components매개변수에 주성분의 개수 지정
pca.fit(fruits_2d)
#k-평균과 마찬가지로 비지도학습이므로 fit()메서드에 타깃데이터 넣지 않음
```

```python
#주성분을 100*100 크기의 이미지처럼 출력
import matplotlib.pyplot as plt
def draw_fruits(arr, ratio=1):
  n = len(arr)
  rows = int(np.ceil(n/10))
  cols = n if rows<2 else 10
  fig, axs = plt.subplots(rows, cols, figsize=(cols*ratio, rows*ratio), squeeze=False)
  for i in range(rows):
    for j in range(cols):
      if i*10+j < n:
        axs[i,j].imshow(arr[i*10+j], cmap='gray_r')
      axs[i,j].axis('off')
  plt.show()

draw_fruits(pca.components_.reshape(-1,100,100))
```

![주성 분분서ㅗㄱ.jpg](%E1%84%92%E1%85%A9%E1%86%AB%E1%84%8C%E1%85%A1%20%E1%84%80%E1%85%A9%E1%86%BC%E1%84%87%E1%85%AE%E1%84%92%E1%85%A1%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC%20%E1%84%83%E1%85%B5%E1%86%B8%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC(%E1%84%87%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A2%E1%84%89%E1%85%A5%E1%86%AB%20%E1%84%8C%E1%85%A5)%205fee2e5b433a463bbeca29c95c3cd0ee/%EC%A3%BC%EC%84%B1_%EB%B6%84%EB%B6%84%EC%84%9C%E3%85%97%E3%84%B1.jpg)

```python
fruits_pca = pca.transform(fruits_2d)
print(fruits_pca.shape) #(300, 50)
#원본데이터가 (300,10000)배열이었는데 (300,50)으로 줄였다!
```

이제 원본 데이터로 원상 복구해보자.

```python
fruits_inverse = pca.inverse_transform(fruits_pca)
#inverse_transform()메서드로 원상 복구
print(fruits_inverse.shape) #(300, 10000)으로 복구됨
fruits_reconstruct = fruits_inverse.reshape(-1,100,100)
for start in [0, 100, 200]:
  draw_fruits(fruits_reconstruct[start:start+100])
  print("|n")
```

주성분이 원본 데이터의 분산을 얼마나 잘 나타내는지 기록한 값을 설명된 분산( explained variance)이라고 한다. PCA클래스의 `explained_variance_ratio_`에 각 주성분의 설명된 분산 비율이 기록되어 있다. 당연히 첫번째 주성분의 값이 가장 크다.

```python
print(np.sum(pca.explained_variance_ratio_))
#0.9215634154222491
plt.plot(pca.explained_variance_ratio_)
plt.show()
```

![처음 5~6개의 주성분이 대부분의 분산을 설명하고 있다.](%E1%84%92%E1%85%A9%E1%86%AB%E1%84%8C%E1%85%A1%20%E1%84%80%E1%85%A9%E1%86%BC%E1%84%87%E1%85%AE%E1%84%92%E1%85%A1%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC%20%E1%84%83%E1%85%B5%E1%86%B8%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC(%E1%84%87%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A2%E1%84%89%E1%85%A5%E1%86%AB%20%E1%84%8C%E1%85%A5)%205fee2e5b433a463bbeca29c95c3cd0ee/%EC%84%A4%EB%AA%85%EB%90%9C%EB%B6%84%EC%82%B0.jpg)

처음 5~6개의 주성분이 대부분의 분산을 설명하고 있다.

과일 사진 원본데이터와 PCA로 축소한 데이터를 로지스틱 회귀 모델에 사용해보고 어떤 차이가 있는지 알아보자.

```python
from sklearn.linear_model import LogisticRegression
lr=LogisticRegression()
target = np.array([0]*100+[1]*100+[2]*100)
#사과를 0, 파인애플을 1, 바나나를 2로.

#교차검증 수행
from sklearn.model_selection import cross_validate

#원본데이터
scores = cross_validate(lr, fruits_2d, target)
print(np.mean(scores['test_score']))
print(np.mean(scores['fit_time']))
#결과값
0.9966666666666667
1.3571013450622558

#PCA로 차원축소한 데이터
scores=cross_validate(lr, fruits_pca, target)
print(np.mean(scores['test_score']))
print(np.mean(scores['fit_time']))
#결과값
1.0
0.03344817161560058
```

결과값을 보면 PCA로 축소한 데이터의 검증 점수가 1.0으로 압도적이고, 훈련시간 역시 0.033초로 40배 가량 줄어들었다.

**06-3 핵심 키워드**

- **차원 축소**: 원본 데이터의 특성을 적은 수의 새로운 특성으로 변환하는 비지도학습의 한 종류
- **주성분 분석**:  데이터에서 가장 분산이 큰 방향을 찾는 차원 축소 알고리즘
- **설명된 분산**: 주성분이 얼마나 원본 데이터의 분산을 잘 나타내는지 기록한 값

**06-3 핵심 패키지와 함수**

- scikit-learn
    - **`PCA`**: 주성분 분석을 수행하는 클래스
        - `n_componenets`는 주성분의 개수를 지정
        - `componenets_`속성에는 훈련 세트에서 찾은 주성분이 저장됨
        - **`explained_variance_`**속성에는 설명된 분산이 저장됨
        - **`inverse_transform()`**메서드는 차원을 축소시킨 데이터를 다시 원본 차원으로 복원

---

## 07 딥러닝을 시작합니다

---

### 07-1 인공 신경망

인공 신경망을 설명하기 앞서 패션MNIST 데이터셋을 불러와보자. 이 데이터는 텐서플로(TensorFlow)를 사용해 불러올 수 있다.

```python
from tensorflow import keras
(train_input, train_target), (test_input, test_target) = keras.datasets.fashion_mnist.load_data()
print(train_input.shape, train_target.shape)
#(60000, 28, 28) (60000,)
#데이터는 28*28크기의 60,000개 이미지로 구성되어있다. 타깃도 60,000개의 원소가 있는 1차원 배열이다.
```

```python
#10개의 샘플을 그림으로 출력해보자
import matplotlib.pyplot as plt
fig, axs = plt.subplots(1,10,figsize=(10,10))
for i in range(10):
  axs[i].imshow(train_input[i], cmap='gray_r')
  axs[i].axis('off')
plt.show()
```

![mnist.jpg](%E1%84%92%E1%85%A9%E1%86%AB%E1%84%8C%E1%85%A1%20%E1%84%80%E1%85%A9%E1%86%BC%E1%84%87%E1%85%AE%E1%84%92%E1%85%A1%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC%20%E1%84%83%E1%85%B5%E1%86%B8%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC(%E1%84%87%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A2%E1%84%89%E1%85%A5%E1%86%AB%20%E1%84%8C%E1%85%A5)%205fee2e5b433a463bbeca29c95c3cd0ee/mnist.jpg)

이 훈련 샘플은 60,000개나 되기 때문에 전체 데이터를 한꺼번에 쓰는 것보다 하나씩 꺼내서 훈련하는 것이 효율적이다. 이럴 때 유용한 것이 확률적 경사 하강법이다. `SGDClassifier`를 사용할 땐 데이터를 전처리 해줘야 했다. 패션MNIST 데이터는 각 픽셀이 0~255의 정숫값을 가지므로 이를 255로 나누어 0~1 사이의 값으로 정규화하고 1차원 배열로 펼쳐야 한다.

```python
train_scaled = train_input/255.0
train_scaled = train_scaled.reshape(-1, 28*28)
```

```python
import numpy as np
#교차검증으로 성능 확인
from sklearn.model_selection import cross_validate
from sklearn.linear_model import SGDClassifier
sc = SGDClassifier(loss='log', max_iter=5, random_state=42)
scores = cross_validate(sc, train_scaled, train_target, n_jobs=-1)
print(np.mean(scores['test_score'])) #0.81956
```

검증 점수가 썩 만족스럽진 않다.

로지스틱 회귀 모델과 비슷한 원리이면서 동시에 더 질높은 기능을 제공하는 것이 바로 **인공 신경망(artificial neural network)**이다.

![Untitled](%E1%84%92%E1%85%A9%E1%86%AB%E1%84%8C%E1%85%A1%20%E1%84%80%E1%85%A9%E1%86%BC%E1%84%87%E1%85%AE%E1%84%92%E1%85%A1%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC%20%E1%84%83%E1%85%B5%E1%86%B8%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC(%E1%84%87%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A2%E1%84%89%E1%85%A5%E1%86%AB%20%E1%84%8C%E1%85%A5)%205fee2e5b433a463bbeca29c95c3cd0ee/Untitled%204.png)

로지스틱 회귀에서는 교차 검증을 사용해 모델을 평가했지만, 인공 신경망에서는 교차 검증을 사용하지 않고 검증 세트를 별도로 덜어내어 사용한다. 이렇게 하는 이유는 시간을 덜기 위함과 딥러닝 분야의 데이터셋은 충분히 크기에 검증 점수가 안정적이기 때문이다.

```python
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
train_scaled, val_scaled, train_target, val_target =train_test_split(train_scaled, train_target, test_size=0.2, random_state=42)
```

케라스의 **`Dense` 클래스**를 사용하여 **밀집층(dense layer)**을 만들 수 있다.

```python
dense = keras.layers.Dense(10, activation='softmax', input_shape=(784,))
#첫번째 매개변수에는 뉴런 개수를 지정한다.
#activation매개변수는 뉴런에서 출력되는 값을 확률로 바꾸기 위한 함수를 입력한다.
#2진분류라면 sigmoid를 쓰고 다중분류라면 softmax를 쓴다.
model=keras.Sequential(dense)

#케라스에서 훈련하기 전 설정단계
model.compile(loss='sparse_categorical_crossentropy', metrics='accuracy')
#loss매개변수에 손실함수의 종류를 입력.
#metrics매개변수에 accuracy를 입력하여 정확도 지표를 같이 출력
```

이진분류에선 손실함수를 `binary_crossentropy`를 사용하고, 다중분류에선 손’`categorial_crossentropy`를 사용한다. 이 때 정수로 된 타깃값을 원-핫 인코딩으로 바꾸지 않고 바로 사용하는 것이 **`sparse_categorial_crossentropy`**이다.

```python
model.fit(train_scaled, train_target, epochs=5)
#결과값
Epoch 1/5
1500/1500 [==============================] - 3s 1ms/step - loss: 0.6051 - accuracy: 0.7949
Epoch 2/5
1500/1500 [==============================] - 2s 1ms/step - loss: 0.4789 - accuracy: 0.8395
Epoch 3/5
1500/1500 [==============================] - 2s 1ms/step - loss: 0.4555 - accuracy: 0.8465
Epoch 4/5
1500/1500 [==============================] - 2s 1ms/step - loss: 0.4460 - accuracy: 0.8521
Epoch 5/5
1500/1500 [==============================] - 2s 1ms/step - loss: 0.4377 - accuracy: 0.8549
<keras.callbacks.History at 0x7f2d68606590>
#훈련세트의 정확도는 0.8549

model.evaluate(val_scaled, val_target)
#결과값
375/375 [==============================] - 1s 1ms/step - loss: 0.4554 - accuracy: 0.8469
[0.45541203022003174, 0.846916675567627]
#검증세트의 정확도는 0.8359
```

**07-1 핵심 키워드**

- **인공 신경망**: 기존 머신러닝 알고리즘으로 다루기 어려웠던 이미지, 음성, 텍스트 분야에서 뛰어난 성능을 발휘한다. 종종 딥러닝으로 불린다.
- 텐서플로: 구글이 만든 딥러닝 라이브러리
- **밀집층**: 가장 간단한 인공 신경망의 층. 뉴런들이 모두 연결되어 있기에 완전 연결 층이라고도 불린다.
- **원-핫 인코딩**: 정숫값을 배열에서 해당 정수 위치의 원소만 1이고 나머지는 0으로 모두 변환하는 것. `sparse_categorical_entropy` 손실함수는 이런 변환을 수행할 필요가 없다.

**07-1 핵심 패키지와 함수**

- TensorFlow
    - **`Dense`**: 신경망에서 가장 기본 층인 **밀집층**을 만드는 클래스
        - **`activation`**매개변수에 사용할 활성화 함수를 지정. 다중분류는 **`softmax**` 함수 지정
    - `Sequential`: 신경망 모델을 만드는 클래스
    - **`compile()`**: 모델 객체를 만든 후 훈련하기 전에 사용할 손실함수와 측정 지표를 지정하는 메서드
        - **`loss`**매개변수에 손실 함수를 지정. 이진분류면 `binary_crossentropy`, 다중분류면 `categorical_crossentropy`, 클래스 레이블이 정수일 경우 **`sparse_categorical_crossentropy`**를 지정
        - `metrics`매개변수에 훈련 과정에서 측정하고픈 지표 지정

---

### 07-2 심층 신경망

이번엔 신경망에 층을 추가해보자.

```python
rom tensorflow import keras
(train_input, train_target), (test_input, test_target) = keras.datasets.fashion_mnist.load_data()

from sklearn.model_selection import train_test_split
train_scaled = train_input/255.0
train_scaled = train_scaled.reshape(-1,28*28)
train_scaled, val_scaled, train_target, val_target = train_test_split(train_scaled, train_target, test_size=0.2, random_state=42)
```

앞선 절에서 만든 것과의 차이는 입력층과 출력층 사이에 **은닉층(hidden layer)**을 추가한 것이다. 은닉층에도 활성화함수를 적용하는데, 대표적으로 **시그모이드 함수**나 **`렐루(ReLU)`함수**를 사용한다.

```python
#은닉층. sigmoid함수를 써서 z값을 0과 1사이로 압축
#은닉층의 뉴런 개수는 임의로 설정하는데, 출력층의 뉴런보단 많아야 한다.
dense1 = keras.layers.Dense(100, activation='sigmoid', input_shape=(784,))
#출력층
dense2 = keras.layers.Dense(10, activation='softmax')
```

```python
model = keras.Sequential([dense1, dense2])
model.summary()
#summary값
Model: "sequential"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 dense (Dense)               (None, 100)               78500     
                                                                 
 dense_1 (Dense)             (None, 10)                1010      
                                                                 
=================================================================
Total params: 79,510
Trainable params: 79,510
Non-trainable params: 0
```

`summary()`메서드를 출력하면 위처럼 유용한 정보를 얻을 수 있다. 맨 첫 줄에 모델의 이름이 나오고, 그 다음에 이 모델의 층이 순서로 나열된다. 층마다 층 이름, 클래스, 출력 크기, 모델 파라미터 개수가 출력된다. 이 모델의 경우 픽셀784개가 입력층의 뉴런 수고, 이것이 은닉층 100개 뉴런과 곱해지므로 78,400개의 파라미터가 있다. 거기에 뉴런마다 1개의 절편이 있으니 총 78,500개의 파라미터가 있다. 그리고선 두번째 층에서 100개의 은닉층 뉴런과 10개의 출력층 뉴런이 연결되니 1,000+10(절편), 총 1,010개의 파라미터가 있다. 이들을 합하면 summary에 나온 79,510 값이 도출된다.

층을 추가하는 다른 방법도 있다. 바로 다음처럼 `Sequential` 클래스 생성자 안에 바로 Dense클래스의 객체를 만드는 방법이다.

```python
model = keras.Sequential([keras.layers.Dense(100, activation='sigmoid', input_shape=(784,), name='hidden'), keras.layers.Dense(10, activation='softmax', name='output')], name='패션 MNIST 모델')
```

하지만 위 방법은 층을 여러개 추가하면 Sequential 생성자가 너무 길어진다. 가장 널리 사용되는 방법은 **`add()`**메서드이다. 이 방법은 한눈에 추가되는 층을 볼 수 있고 프로그램 실행 시 동적으로 층을 선택하여 추가할 수 있다.

```python
model = keras.Sequential()
model.add(keras.layers.Dense(100, activation='sigmoid', input_shape=(784,)))
model.add(keras.layers.Dense(10, activation='softmax'))
```

![Untitled](%E1%84%92%E1%85%A9%E1%86%AB%E1%84%8C%E1%85%A1%20%E1%84%80%E1%85%A9%E1%86%BC%E1%84%87%E1%85%AE%E1%84%92%E1%85%A1%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC%20%E1%84%83%E1%85%B5%E1%86%B8%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC(%E1%84%87%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A2%E1%84%89%E1%85%A5%E1%86%AB%20%E1%84%8C%E1%85%A5)%205fee2e5b433a463bbeca29c95c3cd0ee/Untitled%205.png)

**시그모이드 함수**는 양끝에서 그래프가 누워있기에 올바른 출력을 만드는데 신속하게 대응하지 못한다는 단점이 있다. 이를 개선하기 위해 등장한 활성화함수가 **렐루(ReLU)**함수이다.

![Untitled](%E1%84%92%E1%85%A9%E1%86%AB%E1%84%8C%E1%85%A1%20%E1%84%80%E1%85%A9%E1%86%BC%E1%84%87%E1%85%AE%E1%84%92%E1%85%A1%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC%20%E1%84%83%E1%85%B5%E1%86%B8%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC(%E1%84%87%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A2%E1%84%89%E1%85%A5%E1%86%AB%20%E1%84%8C%E1%85%A5)%205fee2e5b433a463bbeca29c95c3cd0ee/Untitled%206.png)

렐루 함수는 max(0,z)와 같이 쓸 수 있다. 양수일 경우엔 활성화 함수가 없는 양 값을 그냥 통과시키고 음수인 경우엔 0을 출력한다. 렐루 함수는 특히 이미지 처리에서 좋은 성능을 낸다.

```python
model= keras.Sequential()
model.add(keras.layers.Flatten(input_shape=(28,28)))
#Flatten클래스는 입력차원을 일렬로 펼치는 역할
model.add(keras.layers.Dense(100,activation='relu')) #relu
model.add(keras.layers.Dense(10, activation='softmax'))
```

```python
#모델 훈련
(train_input, train_target), (test_input, test_target) = keras.datasets.fashion_mnist.load_data()
train_scaled = train_input/255.0
train_scaled, val_scaled, train_target, val_target = train_test_split(train_scaled, train_target, test_size=0.2, random_state=42)

model.compile(loss='sparse_categorical_crossentropy', metrics='accuracy')
model.fit(train_scaled, train_target, epochs=5)

#시그모이드 함수를 사용했을 때보다 성능이 조금 향상
```

**07-2 핵심 키워드**

- **심층 신경망**: 2개 이상의 층을 포함한 신경망
- **렐루 함수**: 이미지 분류 모델의 은닉층에 많이 사용하는 활성화함수
- **옵티마이저**: 신경망의 가중치와 절편을 학습하기 위한 알고리즘. 케라스에는 다양한 경사 하강법 알고리즘이 옵티마이저로 구현되어 있다.

**07-2 핵심 패키지와 함수**

- TensorFlow
    - **`add()`**: 케라스 모델에 층을 추가하는 메서드
    - `summary()`: 케라스 모델의 정보를 출력하는 메서드
    - `SGD`: 기본 경사 하강법 옵티마이저 클래스
    - `Adagrad`: Adagrad 옵티마이저 클래스
    - `RMSprop`: RMSprop 옵티마이저 클래스

---

### 07-3 신경망 모델 훈련

`History` 객체에는 훈련 과정에서 계산한 지표, 즉 손실과 정확도 값이 저장되어 있다. 이 값을 사용하면 그래프를 그릴 수 있다.

```python
#데이터 준비
from tensorflow import keras
from sklearn.model_selection import train_test_split
(train_input, train_target), (test_input, test_target) = keras.datasets.fashion_mnist.load_data()
train_scaled = train_input/255.0
train_scaled, val_scaled, train_target, val_target = train_test_split(train_scaled, train_target, test_size=0.2, random_state=42)
```

```python
def model_fn(a_layer=None):
  model = keras.Sequential()
  model.add(keras.layers.Flatten(input_shape=(28,28)))
  model.add(keras.layers.Dense(100, activation='relu'))
  if a_layer: #층을 추가하면 은닉층 뒤에 또 하나의 층을 추가하는 if문
    model.add(a_layer)    
  model.add(keras.layers.Dense(10, activation='softmax'))
  return model

#fit()메서드의 결과를 history변수에 담기
model.compile(loss='sparse_categorical_crossentropy', metrics='accuracy')
history = model.fit(train_scaled, train_target, epochs=5, verbose=0)
print(history.history.keys())
#결과값
dict_keys(['loss', 'accuracy'])
```

history 객체에는 손실과 정확도를 포함한 딕셔너리가 있다. 이는 각 에포크마다 계산한 값이 순서대로 나열된 단순한 리스트다. 맷플롯립을 사용해 쉽게 그래프로 그릴 수 있을 것이다.

```python
import matplotlib.pyplot as plt
plt.plot(history.history['loss'])
plt.xlabel('epoch')
plt.ylabel('loss')
plt.show()
plt.plot(history.history['accuracy'])
plt.xlabel('epoch')
plt.ylabel('loss')
plt.show()
```

![앙앙이.jpg](%E1%84%92%E1%85%A9%E1%86%AB%E1%84%8C%E1%85%A1%20%E1%84%80%E1%85%A9%E1%86%BC%E1%84%87%E1%85%AE%E1%84%92%E1%85%A1%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC%20%E1%84%83%E1%85%B5%E1%86%B8%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC(%E1%84%87%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A2%E1%84%89%E1%85%A5%E1%86%AB%20%E1%84%8C%E1%85%A5)%205fee2e5b433a463bbeca29c95c3cd0ee/%EC%95%99%EC%95%99%EC%9D%B4.jpg)

에포크에 따른 과대/과소적합을 잘 파악하려면 훈련세트의 손실만 그려서는 안 되고 **검증 세트의 손실** 역시도 그려야 한다. 이를 위해선 `fit()`메서드에 `validation_data`매개변수를 입력해주면 된다.

```python
model = model_fn()
model.compile(loss='sparse_categorical_crossentropy', metrics='accuracy')
history = model.fit(train_scaled, train_target, epochs=20, verbose=0, validation_data=(val_scaled, val_target))
print(history.history.keys())
#결과값
dict_keys(['loss', 'accuracy', 'val_loss', 'val_accuracy'])
#검증세트에 대한 손실과 정확도도 저장된 것을 볼 수 있다.
```

```python
plt.plot(history.history['val_loss'])
plt.plot(history.history['loss'])
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend(['val', 'train'])
plt.show()
```

![노란색이 훈련세트의 손실, 파란색이 검증세트의 손실이다](%E1%84%92%E1%85%A9%E1%86%AB%E1%84%8C%E1%85%A1%20%E1%84%80%E1%85%A9%E1%86%BC%E1%84%87%E1%85%AE%E1%84%92%E1%85%A1%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC%20%E1%84%83%E1%85%B5%E1%86%B8%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC(%E1%84%87%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A2%E1%84%89%E1%85%A5%E1%86%AB%20%E1%84%8C%E1%85%A5)%205fee2e5b433a463bbeca29c95c3cd0ee/epoich.jpg)

노란색이 훈련세트의 손실, 파란색이 검증세트의 손실이다

초기에 검증 손실이 감소하다가 금방 다시 상승하기 시작한다. 검증손실이 다시 상승하는 시점을 가능한 뒤로 늦추면 훨씬 성능이 좋아질 것이다.

**드롭아웃(dropout)**은 훈련 과정에서 층에 있는 일부 뉴런을 랜덤하게 꺼서 출력을 0으로 만들고, 과대적합을 막는 방법이다. 케라스에서는 드롭아웃을 `keras.layers` 패키지 아래 `Dropout` 클래스로 제공한다.

```python
#앞서 정의한 model_fn함수에 드롭아웃 층을 넣어보자
model = model_fn(keras.layers.Dropout(0.3))
model.summary()
Model: "sequential_7"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 flatten_5 (Flatten)         (None, 784)               0         
                                                                 
 dense_14 (Dense)            (None, 100)               78500     
                                                                 
 dropout (Dropout)           (None, 100)               0         
                                                                 
 dense_15 (Dense)            (None, 10)                1010      
                                                                 
=================================================================
Total params: 79,510
Trainable params: 79,510
Non-trainable params: 0
_________________________________________________________________
```

은닉층 뒤에 추가된  Dropout층을 보면 훈련되는 모델 파라미터가 없다. 일부 뉴런의 출력을 0으로 만들지만 전체 출력 배열의 크기를 바꾸지는 않는다. 당연히 훈련 종료 후 평가나 예측을 수행할 때는 드롭아웃이 적용되면 안 된다. 똑똑하게도 Dropout클래스는 평가/예측 시에 자동으로 드롭아웃을 적용하지 않는다. 이전과 마찬가지로 훈련손실과 검증손실 그래프를 그려보자

```python
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics='accuracy')
history = model.fit(train_scaled, train_target, epochs=20, verbose=0, validation_data=(val_scaled, val_target))
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend(['train', 'val'])
plt.show()
```

![dkdkdkd.jpg](%E1%84%92%E1%85%A9%E1%86%AB%E1%84%8C%E1%85%A1%20%E1%84%80%E1%85%A9%E1%86%BC%E1%84%87%E1%85%AE%E1%84%92%E1%85%A1%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC%20%E1%84%83%E1%85%B5%E1%86%B8%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC(%E1%84%87%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A2%E1%84%89%E1%85%A5%E1%86%AB%20%E1%84%8C%E1%85%A5)%205fee2e5b433a463bbeca29c95c3cd0ee/dkdkdkd.jpg)

과대적합이 확실히 줄어든 것을 볼 수 있다.

이제 이 모델의 훈련된 파라미터를 저장해보자.

```python
model = model_fn(keras.layers.Dropout(0.3))
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics='accuracy')
history = model.fit(train_scaled, train_target, epochs=10, verbose=0, validation_data=(val_scaled, val_target))
model.save_weights('model-weights.h5') #훈련 파라미터를 저장하는 메서드
model.save('model-whole.h5') #모델 구조와 모델 파라미터를 함께 저장하는 메서드
```

**콜백(callback)**은 훈련 과정 중간에 어떤 작업을 수행할 수 있게 하는 객체로 `keras.callbacks` 패키지 아래에 있는 클래스들이다. `fit()`메서드의 `callbacks` 매개변수에 리스트로 전달하여 사용한다.

```python
model = model_fn(keras.layers.Dropout(0.3))
model.compile(optimizer='adam', loss='aparse_categorical_crossentropy', metrics='accuracy')
checkpoint_cb = keras.callbacks.ModelCheckpoint('best-model.h5', save_best_only=True)
#save_best_only매개변수를 True로 설정하여 가장 낮은 검증 점수를 만드는 모델을 저장한다.
history.model.fit(train_scaled, train_target, epochs=20, verbose=0, validation_data=(val_scaled, val_target), callbacks=[checkpoint_cb, early_stopping_cb])
#checkpoint_cb를 만든 후 callbacks매개변수에 리스트로 감싸서 전달해준다.
#모델이 훈련한 후 best-model.h5에 최상의 검증 점수를 낸 모델이 저장된다.
```

더 나아가 과대적합이 시작되기 전에 미리 훈련을 중지하도록 할 수 있다. 이를 **조기 종료(early stopping)**라고 부른다. 케라스에서는 조기 종료를 위한 **`EarlyStopping**` 콜백을 제공한다.

```python
model = model_fn(keras.layers.Dropout(0.3))
model.compile(optimizer='adam', loss='aparse_categorical_crossentropy', metrics='accuracy')
checkpoint_cb = keras.callbacks.ModelCheckpoint('best-model.h5', save_best_only=True)
early_stopping_cb = keras.callbacks.EarlyStopping(patience=2, restore_best_weights=True)
#patience를 2로 지정하면 2번 연속 검증 점수 향상이 없을 시 훈련 중지
#retore_best_weights를 True로 지정하면 가장 낮은 검증 손실을 낸 모델 파라미터로 되돌림
history.model.fit(train_scaled, train_target, epochs=20, verbose=0, validation_data=(val_scaled, val_target), callbacks=[checkpoint_cb, early_stopping_cb])

#몇 에포크만에 훈련을 중지했는지
print(early_stopping_cb.stopped_epoch) 
```

**07-3 핵심 키워드**

- **드롭아웃**: 은닉층에 있는 뉴런의 출력을 랜덤하게 꺼서 과대적합을 막는 기법. 드롭아웃은 훈련 중에 적용되며 평가나 예측에서는 사용되지 않음.
- **콜백**: 케라스 모델을 훈련하는 도중 어떤 작업을 수행할 수 있도록 도와주는 도구
- **조기 종료**: 검증점수가 더 이상 감소하지 않고 상승하여 과대적합이 일어나면 훈련을 중지하는 기법

**07-3 핵심 패키지와 함수**

- TensorFlow
    - **`Dropout`**
        - 첫번째 매개변수로 드롭아웃 할 비율을 지정
    - `save_weights()`: 모든 층의 가중치와 절편을 파일에 저장
    - `load_weights()`: 모든 층의 가중치와 절편을 파일에 읽음
    - `save()`: 모델 구조와 모든 가중치와 절편을 파일에 저장
    - **`ModelCheckpoint`**:  케라스 모델과 가중치를 일정 간격으로 저장
        - 첫번째 매개변수에 저장할 파일 지정
        - `monitor`매개변수에 모니터링할 지표 지정
        - **`save_best_only`**매개변수를 **True**로 지정하면 가장 낮은 점수를 만드는 모델을 저장
    - **`EarlyStopping`**: 관심 지표가 더 이상 향상하지 않으면 훈련 중지
        - **`patience`**매개변수에 모델이 지속가능한 최대 에포크 횟수 지정
- Numpy
    - `argmax`: 배열에서 축을 따라 최댓값의 인덱스를 반환

---

## 08 이미지를 위한 인공 신경망

### 08-1 합성곱 신경망의 구성 요소

**합성곱(convolution)**은 마치 입력 데이터에 도장을 찍어 유용한 특성만 드러나게 하는 것으로 비유할 수 있다. 가령 10개의 특성이 있다고 하자. 밀집층은 이 10개의 특성에 각각 10개의 가중치를 곱한다.

그러나 합성곱은 가중치가 10개가 아니라 3개로만 곱한다. 이 때 1~3번을 곱하고 그 다음은 2~4번, 3~5번의 순서로 총 8번의 계산을 수행한다.

밀집층의 뉴런은 특성 개수만큼 10개의 가중치로 1개의 출력을 만드는 반면, 합성곱 층의 **필터(커널)**는 3개의 가중치로 8개의 출력을 만든 셈이다. 이 때 합성곱으로 만들어진 출력을 **특성맵(feature map)**이라 한다.

![왼쪽이 특성, 가운데가 가중치(커널), 오른쪽이 합성곱 계산을 통해 얻은 특성 맵](%E1%84%92%E1%85%A9%E1%86%AB%E1%84%8C%E1%85%A1%20%E1%84%80%E1%85%A9%E1%86%BC%E1%84%87%E1%85%AE%E1%84%92%E1%85%A1%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC%20%E1%84%83%E1%85%B5%E1%86%B8%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC(%E1%84%87%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A2%E1%84%89%E1%85%A5%E1%86%AB%20%E1%84%8C%E1%85%A5)%205fee2e5b433a463bbeca29c95c3cd0ee/Untitled%207.png)

왼쪽이 특성, 가운데가 가중치(커널), 오른쪽이 합성곱 계산을 통해 얻은 특성 맵

만약 커널 크기는 (3,3)인데 특성 맵은 원본처럼 (4,4)를 만들려면 어떻게 해야 할까? 마치 더 큰 입력을 합성곱하는 척을 해야 한다. 입력 배열 주위를 가상원 원소로 채우는 것을 **패딩(padding)**이라고 한다. 이 때 0으로 채우는 패딩을 **세임 패딩**이라고 부른다.

![Untitled](%E1%84%92%E1%85%A9%E1%86%AB%E1%84%8C%E1%85%A1%20%E1%84%80%E1%85%A9%E1%86%BC%E1%84%87%E1%85%AE%E1%84%92%E1%85%A1%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC%20%E1%84%83%E1%85%B5%E1%86%B8%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC(%E1%84%87%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A2%E1%84%89%E1%85%A5%E1%86%AB%20%E1%84%8C%E1%85%A5)%205fee2e5b433a463bbeca29c95c3cd0ee/Untitled%208.png)

패딩을 하는 이유는 정보가 고르게 전달되기 위함이다. 패딩 없이 합성곱을 한다면, 위의 예시에서  가장 모서리 부분들은 1번씩만 커널에 쓰이는 반면 중앙에 있는 값들은 중복해서 쓰인다. 적절한 패딩은 이미지 변두리에 있는 정보를 잃지 않도록 도와준다.

지금까지의 합성곱 연산은 커널을 움직일 때 한 칸씩 움직였다. 하지만 두 칸씩 이동하여 특성 맵의 크기를 더 작게 할 수도 있다. 이러한 방식을 **스트라이드(stride)**라고 한다.

```python
from tensorflow import keras
keras.layers.Conv2D(10, kernel_size=(3,3), activation='relu', padding='same', strides=1)
#padding매개변수와 strdies매개변수를 주목하자.
```

**풀링(pooling)**은 합성곱 층에서 만든 특성 맵의 가로세로 크기를 줄이는 역할을 수행한다. 그러나 특성 맵의 개수는 줄이지 않는다. 만약 특성 맵이 (2,2,3)크기라면 (1,1,3)으로 가로세로만 축소하고 개수는 그대로 둔다는 것이다. 이 때 가로세로를 줄일 때, 그 영역에서 가장 큰 값을 택하면 **최대 풀링(max pooling)**이라 하고, 영역의 평균값을 택하면 **평균 풀링(average pooling)**이라고 한다. 평균 풀링은 특성 맵에 있는 중요한 정보를 희석시킬 수도 있기 때문에 최대 풀링을 많이 사용한다.

![위 예시는 최대 풀링을 사용했다.](%E1%84%92%E1%85%A9%E1%86%AB%E1%84%8C%E1%85%A1%20%E1%84%80%E1%85%A9%E1%86%BC%E1%84%87%E1%85%AE%E1%84%92%E1%85%A1%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC%20%E1%84%83%E1%85%B5%E1%86%B8%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC(%E1%84%87%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A2%E1%84%89%E1%85%A5%E1%86%AB%20%E1%84%8C%E1%85%A5)%205fee2e5b433a463bbeca29c95c3cd0ee/Untitled%209.png)

위 예시는 최대 풀링을 사용했다.

**08-1 핵심 키워드**

- **합성곱(convolution)**: 밀집층과 비슷하게 입력과 가중치를 곱하고 절편을 더하는 선형 계산.
- **필터**: 합성곱 층에서 뉴런의 역할을 수행하는 부분. 필터의 가중치와 절편을 **커널**이라고 부른다.
- **특성 맵**: 합성곱 층의 출력 배열.
- **패딩**: 합성곱 층의 입력 주위에 추가한 0으로 채워진 픽셀
- **스트라이드**: 합성곱 층에서 필터가 입력 위를 이동하는 크기
- **풀링**: 가중치가 없고 특성 맵의 가로세로 크기를 줄이는 역할을 수행. 일반적으로 **최대 풀링**을 사용한다.

---

### **08-2 합성곱 신경망을 사용한 이미지 분류**

이제 앞서 배운 합성곱을 바탕으로 패션MNIST 데이터를 분류해보자.

```python
#데이터 준비
from tensorflow import keras
from sklearn.model_selection import train_test_split
(train_input, train_target), (test_input, test_target) = keras.datasets.fashion_mnist.load_data()
train_scaled = train_input.reshape(-1,28,28,1)/255.0
train_scaled, val_scaled, train_target, val_target = train_test_split(train_scaled, train_target, test_size=0.2, random_state=42)
```

```python
#합성곱 신경망 만들기
model = keras.Sequential()
#첫번째 합성곱층 Conv2D 추가. 활성화함수는 relu, 세임패딩 적용
model.add(keras.layers.Conv2D(32, kernel_size=3, activation='relu', padding='same', input_shape=(28,28,1)))
#풀링 층 추가. 최대풀링 MasPooling2D클래스 사용. (2,2)풀링 사용
model.add(keras.layers.MaxPooling2D(2))
#필터의 개수를 64개로 늘려 두번째 합성곱-풀링 층 생성
model.add(keras.layers.Conv2D(64, kernel_size=3, activation='relu', padding='same'))
model.add(keras.layers.MaxPooling2D(2))

model.add(keras.layers.Flatten()) #(7,7,64)크기의 특성맵을 일렬로 펼쳐주기
model.add(keras.layers.Dense(100, activation='relu')) #은닉층
model.add(keras.layers.Dropout(0.4)) #드롭아웃
model.add(keras.layers.Dense(10, activation='softmax')) #출력층
```

```python
#model summary
Model: "sequential"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 conv2d_1 (Conv2D)           (None, 28, 28, 32)        320       
                                                                 
 max_pooling2d (MaxPooling2D  (None, 14, 14, 32)       0         
 )                                                               
                                                                 
 conv2d_2 (Conv2D)           (None, 14, 14, 64)        18496     
                                                                 
 max_pooling2d_1 (MaxPooling  (None, 7, 7, 64)         0         
 2D)                                                             
                                                                 
 flatten (Flatten)           (None, 3136)              0         
                                                                 
 dense (Dense)               (None, 100)               313700    
                                                                 
 dropout (Dropout)           (None, 100)               0         
                                                                 
 dense_1 (Dense)             (None, 10)                1010      
                                                                 
=================================================================
Total params: 333,526
Trainable params: 333,526
Non-trainable params: 0
_________________________________________________________________
```

케라스는 층의 구성을 그림으로 표현해주는 plot_model() 함수를 제공한다.

```python
keras.utils.plot_model(model, show_shapes=True)
```

![Untitled](%E1%84%92%E1%85%A9%E1%86%AB%E1%84%8C%E1%85%A1%20%E1%84%80%E1%85%A9%E1%86%BC%E1%84%87%E1%85%AE%E1%84%92%E1%85%A1%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC%20%E1%84%83%E1%85%B5%E1%86%B8%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC(%E1%84%87%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A2%E1%84%89%E1%85%A5%E1%86%AB%20%E1%84%8C%E1%85%A5)%205fee2e5b433a463bbeca29c95c3cd0ee/Untitled%2010.png)

이제 모델을 컴파일하고 훈련할 때이다. 과정은 7장 3절에서 사용한 방식과 흡사하다.

```python
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics='accuracy')
checkpoint_cb = keras.callbacks.ModelCheckpoint('best-cnn-model.h5', save_best_only=True)
early_stopping_cb = keras.callbacks.EarlyStopping(patience=2, restore_best_weights=True)
history = model.fit(train_scaled, train_target, epochs=20, validation_data=(val_scaled, val_target), callbacks=[checkpoint_cb, early_stop
```

```python
model.evaluate(val_scaled, val_target)
#결과값
375/375 [==============================] - 5s 13ms/step - loss: 0.2385 - accuracy: 0.9112
[0.23846960067749023, 0.9111666679382324]
#검증 세트에 대한 성능이 합성곱 이전보다 확연히 좋아졌다.
```

**08-2 핵심 패키지와 함수**

 TensorFlow

- **`Conv2D`**: 합성곱 연산을 구현한 클래스
    - 첫번째 매개변수는 필터의 개수
    - `kernel_size`매개변수로 필터의 커널 크기 지정
    - `strides`매개변수로 필터의 이동 간격 지저
    - **`padding`**매개변수로 입력의 패딩 타입 지정.
- **`MaxPooling2D`**: 최대 풀링 연산을 구현한 클래스
    - 첫번째 매개변수는 풀링의 크기
    - `padding`매개변수로 입력의 패딩 타입 지정.
    - `strides`매개변수로 필터의 이동 간격 지정
- `plot_model()`은 케라스 모델 구조를 그림으로 나타내줌

---

### 08-3 합성곱 신경망의 시각화

2절에서 만든 모델이 어떤 가중치를 학습했는지 체크포인트 파일을 읽어 들여보자. 층의 가중치와 절편은 `weights` 속성에 저장되어 있다.

```python
from tensorflow import keras
model = keras.models.load_model('best-cnn-model.h5')
conv = model.layers[0]
print(conv.weights[0].shape, conv.weights[1].shape) #첫번째 원소가 가중치, 두번째 원소가 절편이다.
conv_weights = conv.weights[0].numpy()
print(conv_weights.mean(), conv_weights.std())
#결과값
-0.03212438 0.20858574
```

가중치의 평균값은 0에 가깝고 표준편차는 0.2 정도이다. 이 가중치가 어떤 분포를 가졌는지 히스토그램을 그려보자

```python
import matplotlib.pyplot as plt
plt.hist(conv_weights.reshape(-1,1))
plt.xlabel('weight')
plt.ylabel('count')
plt.show()
```

![histogram.png](%E1%84%92%E1%85%A9%E1%86%AB%E1%84%8C%E1%85%A1%20%E1%84%80%E1%85%A9%E1%86%BC%E1%84%87%E1%85%AE%E1%84%92%E1%85%A1%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC%20%E1%84%83%E1%85%B5%E1%86%B8%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC(%E1%84%87%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A2%E1%84%89%E1%85%A5%E1%86%AB%20%E1%84%8C%E1%85%A5)%205fee2e5b433a463bbeca29c95c3cd0ee/histogram.png)

> **가중치 시각화**
> 

이번에는 32개의 가중치를 그림으로 출력해보자. 앞서 만든 `subplots()`함수를 사용해서 말이다.

```python
fig, axs = plt.subplots(2,16,figsize=(15,2))
for i in range(2):
  for j in range(16):
    axs[i,j].imshow(conv_weights[:,:,0,i*16+j], vmin=-0.5, vmax=0.5)
    axs[i,j].axis('off')
plt.show()
```

![가중치1.png](%E1%84%92%E1%85%A9%E1%86%AB%E1%84%8C%E1%85%A1%20%E1%84%80%E1%85%A9%E1%86%BC%E1%84%87%E1%85%AE%E1%84%92%E1%85%A1%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC%20%E1%84%83%E1%85%B5%E1%86%B8%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC(%E1%84%87%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A2%E1%84%89%E1%85%A5%E1%86%AB%20%E1%84%8C%E1%85%A5)%205fee2e5b433a463bbeca29c95c3cd0ee/%EA%B0%80%EC%A4%91%EC%B9%981.png)

결과 그림을 보면 어떠한 패턴을 읽을 수 있다. 가장 첫번째 가중치를 보면 아랫부분 픽셀들의 가중치가 높다(밝을수록 가중치가 높음). 즉, 이 가중치는 **아래에 놓인 부분을 만나면 크게 활성화**될 것이다.

이번에는 훈련하지 않은 빈 합성곱 신경망을 만들어보고, 이 층의 가중치가 위의 가중치와 어떻게 다른지 그림으로 비교해보자.

```python
no_training_model = keras.Sequential()
no_training_model.add(keras.layers.Conv2D(32, kernel_size=3, activation='relu', padding='same', input_shape=(28,28,1)))
no_training_conv = no_training_model.layers[0]

no_training_weights = no_training_conv.weights[0].numpy()
print(no_training_weights.mean(), no_training_weights.std())
#결과값
-0.0031735036 0.08017581
```

평균은 아까처럼 0에 가깝지만, 표준편차는 아까보다 훨씬 작다. 히스토그램으로 표현하면 훨씬 고르게 분포하고 있음을 알 수 있다.

![히스토2.png](%E1%84%92%E1%85%A9%E1%86%AB%E1%84%8C%E1%85%A1%20%E1%84%80%E1%85%A9%E1%86%BC%E1%84%87%E1%85%AE%E1%84%92%E1%85%A1%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC%20%E1%84%83%E1%85%B5%E1%86%B8%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC(%E1%84%87%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A2%E1%84%89%E1%85%A5%E1%86%AB%20%E1%84%8C%E1%85%A5)%205fee2e5b433a463bbeca29c95c3cd0ee/%ED%9E%88%EC%8A%A4%ED%86%A02.png)

![가중치2.png](%E1%84%92%E1%85%A9%E1%86%AB%E1%84%8C%E1%85%A1%20%E1%84%80%E1%85%A9%E1%86%BC%E1%84%87%E1%85%AE%E1%84%92%E1%85%A1%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC%20%E1%84%83%E1%85%B5%E1%86%B8%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC(%E1%84%87%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A2%E1%84%89%E1%85%A5%E1%86%AB%20%E1%84%8C%E1%85%A5)%205fee2e5b433a463bbeca29c95c3cd0ee/%EA%B0%80%EC%A4%91%EC%B9%982.png)

가중치들을 보면 전반적으로 밋밋하다는 것을 볼 수 있다. 즉, 합성곱신경망이 패션MNIST 데이터 분류 정확도를 높이는 데에 톡톡히 기여하고 있다는 점을 확인할 수 있다.

> **특성맵 시각화**
> 

이번에는 샘플을 `conv_acti` 모델에 주입하여 Conv2D 층이 만드는 특성맵으로 출력해보자.

```python
conv_acti = keras.Model(model.input, model.layers[0].output)
#전처리
inputs=train_input[0:1].reshape(-1,28,28,1)/255.0
feature_maps = conv_acti.predict(inputs)
print(feature_maps.shape)

#특성 맵 그리기
fig, axs = plt.subplots(4,8,figsize=(15,8))
for i in range(4): #4행으로
  for j in range(8):
    axs[i,j].imshow(feature_maps[0,:,:,i*8+j])
    axs[i,j].axis('off')
plt.show()
```

![특성맵.png](%E1%84%92%E1%85%A9%E1%86%AB%E1%84%8C%E1%85%A1%20%E1%84%80%E1%85%A9%E1%86%BC%E1%84%87%E1%85%AE%E1%84%92%E1%85%A1%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC%20%E1%84%83%E1%85%B5%E1%86%B8%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC(%E1%84%87%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A2%E1%84%89%E1%85%A5%E1%86%AB%20%E1%84%8C%E1%85%A5)%205fee2e5b433a463bbeca29c95c3cd0ee/%ED%8A%B9%EC%84%B1%EB%A7%B5.png)

이 특성 맵은 32개의 필터로 인해 입력 이미지에서 **강하게 활성화된 부분**을 보여준다.

20번째 특성맵과 앞에서 본 20번째 가중치 그림을 비교해보자. 가중치는 전체적으로 어두운, 낮은 음수 값이다. 이 필터가 큰 양수와 곱해지면 더 큰 음수가 되고, 배경처럼 0에 가까운 값과 곱해지면 작은 음수가 될 것이다. 따라서 사진의 배경이 상대적으로 크게 활성화되는 것이다. 이를 특성맵에서도 확인할 수 있다.

**08-3 핵심 키워드**

- **가중치 시각화**: 합성곱 층의 가중치를 이미지로 출력하는 것
- **특성맵 시각화**: 합성곱 층의 활성화 출력을 이미지로 그리는 것
- 함수형 API: 케라스에서 신경망 모델을 만드는 방법 중 하나

---

## 09 텍스트를 위한 인공 신경망

### 09-1 순차 데이터와 순환 신경망

**순차 데이터(sequential data)**는 **텍스트**나 **시계열 데이터(time series data)**와 같이 순서에 의미가 있는 데이터를 말한다. 순차 데이터의 순서는 뒤섞이면 안된다. 즉 순차 데이터를 다룰 때는 이전에 입력한 데이터를 기억하는 기능이 필요하다.

완전 연결 신경망이나 합성곱 신경망은 이런 기억 장치가 없다. 이렇게 데이터의 흐름이 앞으로만 전달되는 신경망을 **피드포워드 신경망(FFNN)**이라고 한다.

반면 이전에 처리한 샘플을 재사용하는 신경망을 **순환 신경망(recurrent neural network, RNN)**이라고 한다. 이는 완전 연결 신경망에 순환하는 고리 하나만 추가한 형상이다.

A,B,C를 순차적으로 처리하는 순환 신경망이 있다고 가정하자. 첫번째 샘플 A를 처리하고 난 출력 OA가 다시 뉴런으로 돌아간다. 그 다음 샘플 B를 처리할 땐 OA와 B가 함께 처리되어 OB가 만들어진다. 이 때 OB엔 A의 정보가 일정량 포함되어 있다. 그 다음 샘플 C를 처리할 땐 OB가 함께 쓰인다. 그렇게 만들어진 OC에는 B와 A의 정보가 포함되어있다. 물론 직전에 쓰인 B가 A보단 정보량이 많다.

이 때 샘플을 처리하는 한 단계를 **타임스텝(time step)**이라고 한다. 타임스텝이 오래될수록 순환되는 정보는 희미해진다.

순환 신경망에서는 층을 셀(cell)이라고 부른다. 셀의 출력은 **은닉 상태(hidden state)**라고 부른다.

은닉층의 활성화함수로는 하이퍼볼릭 탄젠트 함수가 사용된다. 시그모이드 함수와 유사하지만, -1~1의 범위를 갖는다.

![파란색이 시그모이드, 빨간색이 하이퍼볼릭 탄젠트 함수.](%E1%84%92%E1%85%A9%E1%86%AB%E1%84%8C%E1%85%A1%20%E1%84%80%E1%85%A9%E1%86%BC%E1%84%87%E1%85%AE%E1%84%92%E1%85%A1%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC%20%E1%84%83%E1%85%B5%E1%86%B8%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC(%E1%84%87%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A2%E1%84%89%E1%85%A5%E1%86%AB%20%E1%84%8C%E1%85%A5)%205fee2e5b433a463bbeca29c95c3cd0ee/Untitled%2011.png)

파란색이 시그모이드, 빨간색이 하이퍼볼릭 탄젠트 함수.

순환 신경망의 뉴런은 가중치가 하나 더 있는데, 바로 이전 타임스텝의 은닉 상태에 곱해지는 가중치이다.

순환층은 기본적으로 마지막 타임스텝의 은닉 상태만 출력으로 내보낸다.

합성곱 신경망과 다른 점은 마지막 셀의 출력이 1차원이기 때문에 굳이 `Flatten` 클래스로 펼칠 필요가 없고, 셀의 출력을 그대로 밀집층에 사용할 수 있다.

**09-1 핵심 키워드**

- **순차 데이터**: 텍스트나 시계열 데이터와 같이 순서에 의미가 있는 데이터
- **순환 신경망**: 순차 데이터에 잘 맞는 인공 신경망의 한 종류.
- 셀: 순환 신경망에서 순환층을 일컫는 말.
- **은닉 상태**: 순환 신경망에서 셀의 출력을 일컫는 말.

---

### 09-2 순환 신경망으로 IMDB 리뷰 분류하기

IMDB 리뷰 데이터셋은 유명한 인터넷 영화 데이터베이스인 imdb.com에서 수집한 리뷰를 감상평에 따라 긍정과 부정으로 분류해 놓은 데이터셋이다.

텍스트 자체를 신경망에 전달하는 것이 아니라, 단어마다 고유한 정수를 부여한다. 이 때 0은 패딩, 1은 문장의 시작, 2는 어휘 사전에 없는 토큰으로 미리 부여가 되어있다. 이렇게 분리된 단어를 **토큰(token)**이라고 부른다. 하나의 샘플은 여러 개의 토큰으로 이루어져 있고, **1개의 토큰이 하나의 타임스텝에 해당**한다. 

```python
from tensorflow.keras.datasets import imdb
(train_input, train_target), (test_input, test_target) = imdb.load_data(num_words=500)
#num_words매개변수를 500으로 하여 자주 등장하는 단어 500개만 사용

print(len(train_input[0])) #첫번째 리뷰의 길이
#결과값
218

print(train_target[:20]) #타깃 20개 출력
#결과값
[1 0 0 1 0 0 1 0 1 0 1 0 0 0 0 0 1 1 0 1] #0은 부정, 1은 긍정

```

```python
#검증세트 분리
from sklearn.model_selection import train_test_split
train_input, val_input, train_target, val_target = train_test_split(train_input, train_target, test_size=0.2, random_state=42)

import numpy as np
lengths = np.array([len(x) for x in train_input]) #각 리뷰의 길이를 배열로 만들기
print(np.mean(lengths), np.median(lengths)) #길이의 평균과 중간값
#결과값
239.00925 178.0 #평균 단어 수는 239개, 중간값은 178개.
```

평균값이 239, 중간값이 178인 것으로 보아 이 리뷰 길이 데이터는 한쪽에 치우쳤을 것이다. 히스토그램을 확인해보자.

![대부분이 300 미만인 것을 확인할 수 있다.](%E1%84%92%E1%85%A9%E1%86%AB%E1%84%8C%E1%85%A1%20%E1%84%80%E1%85%A9%E1%86%BC%E1%84%87%E1%85%AE%E1%84%92%E1%85%A1%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC%20%E1%84%83%E1%85%B5%E1%86%B8%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC(%E1%84%87%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A2%E1%84%89%E1%85%A5%E1%86%AB%20%E1%84%8C%E1%85%A5)%205fee2e5b433a463bbeca29c95c3cd0ee/%ED%9E%88%EC%8A%A4%ED%86%A0%EA%B7%B8%EB%9E%A8.jpg)

대부분이 300 미만인 것을 확인할 수 있다.

리뷰의 길이가 100 미만인 것만 사용해도 충분할 것으로 보인다. 길이가 100을 넘으면 100에 맞추어 잘라내고, 100보다 짧으면 토큰 0으로 패딩을 해준다. 케라스는 시퀀스 데이터의 길이를 맞추는 `pad_sequences()`함수를 제공한다.

```python
from tensorflow.keras.preprocessing.sequence import pad_sequences
train_seq = pad_sequences(train_input, maxlen=100) #maxlen매개변수에 원하는 길이를 지정
val_seq = pad_sequences(val_input, maxlen=100) #검증세트의 길이도 100으로

print(train_seq.shape)
#결과값
(20000, 100)  #토큰 100개의 샘플이 20,000개 있다.
```

시퀀스의 마지막에 있는 단어가 셀의 은닉상태에 가장 큰 영향을 미치므로 마지막에 패딩을 추가하는 것은 선호되지 않는다. 때문에 자동으로 패딩은 앞에 위치한다.

이제 순환 신경망을 만들어보자. 케라스는 `simpleRNN` 클래스를 제공한다.

```python
from tensorflow import keras
model = keras.Sequential()
model.add(keras.layers.SimpleRNN(8,input_shape=(100,500))) 
#Dense나 Conv2D 클래스 대신 SimpleRNN 사용
#activation의 기본값은 tanh이다.
model.add(keras.layers.Dense(1, activation='sigmoid'))

model.summary()
Model: "sequential"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 simple_rnn (SimpleRNN)      (None, 8)                 4072      
                                                                 
 dense (Dense)               (None, 1)                 9         
                                                                 
=================================================================
Total params: 4,081
Trainable params: 4,081
Non-trainable params: 0
_________________________________________________________________
```

또한 토큰에 부여된 정수가 크기의 의미를 지녀선 안 된다. 100이 부여된 단어가 5가 부여된 단어보다 20배 중요한 것이 아니다. 따라서 정숫값에 있는 크기 속성을 없애고 각 정수를 고유하게 표현하기 위해 **원-핫인코딩**을 해준다.

```python
#원핫인코딩
train_oh = keras.utils.to_categorical(train_seq)
val_oh = keras.utils.to_categorical(val_seq)
```

```python
#순환 신경망 훈련
rmsprop = keras.optimizers.RMSprop(learning_rate=1e-4)
model.compile(optimizer=rmsprop, loss='binary_crossentropy', metrics=['accuracy'])
checkpoint_cb = keras.callbacks.ModelCheckpoint('best-simplernn-model.h5',save_best_only=True)
early_stopping_cb = keras.callbacks.EarlyStopping(patience=3, restore_best_weights=True)
history = model.fit(train_oh, train_target, epochs=100, batch_size=64, validation_data=(val_oh, val_target), callbacks=[checkpoint_cb, early_stopping_cb])

#결과
Epoch 36/100 #36번째 에포크에서 중단
313/313  15s 47ms/step - loss: 0.4060 - accuracy: 0.8189 - val_loss: 0.4488 - val_accuracy: 0.7944

```

하지만 이 작업에서 원-핫 인코딩으로 변환하면 입력 데이터가 매우 커진다. 토큰 1개가 500차원으로 늘어났기 때문이다.

때문에 원-핫인코딩보다도 **단어 임베딩(word embedding)**을 즐겨 사용한다. 단어 임베딩은 각 단어를 고정된 크기의 실수 벡터로 바꿔 준다. 이는 원-핫 인코딩보다 훨씬 의미 있는 값으로 채워져 있기에 더 좋은 성능을 낼 수 있다.

```python
model2=keras.Sequential()
model2.add(keras.layers.Embedding(500, 16, input_length=100))
#첫번째 매개변수는 어휘 사전의 크기
#두번째 매개변수는 임베딩 벡터의 크기. 원-핫인코딩은 500개인데, 여기선 16개밖에 안 된다
#세번째 매개변수는 입력 시퀀스의 길이.
model2.add(keras.layers.SimpleRNN(8))
model2.add(keras.layers.Dense(1, activation='sigmoid'))

model2.summary()
Model: "sequential_1"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 embedding (Embedding)       (None, 100, 16)           8000      
                                                                 
 simple_rnn_1 (SimpleRNN)    (None, 8)                 200       
                                                                 
 dense_1 (Dense)             (None, 1)                 9         
                                                                 
=================================================================
Total params: 8,209
Trainable params: 8,209
Non-trainable params: 0
_________________________________________________________________
```

```python
#단어임베딩 순환신경망 훈련
rmsprop = keras.optimizers.RMSprop(learning_rate=1e-4)
model2.compile(optimizer=rmsprop, loss='binary_crossentropy', metrics=['accuracy'])
checkpoint_cb = keras.callbacks.ModelCheckpoint('best-simplernn-model.h5',save_best_only=True)
early_stopping_cb = keras.callbacks.EarlyStopping(patience=3, restore_best_weights=True)
history = model2.fit(train_seq, train_target, epochs=100, batch_size=64, validation_data=(val_seq, val_target), callbacks=[checkpoint_cb, early_stopping_cb])

#결과
Epoch 40/100
313/313 - 8s 24ms/step - loss: 0.3829 - accuracy: 0.8396 - val_loss: 0.4562 - val_accuracy: 0.7870
```

**09-2 핵심 키워드**

- **토큰**: 텍스트에서 공백으로 구분되는 문자열
- **원-핫 인코딩**: 어떤 클래스에 해당하는 원소만 1이고 나머지는 모두 0인 벡터
- **단어 임베딩**: 정수로 변환된 토큰을 비교적 작은 크기의 실수 밀집 벡터로 변환하는 방법

**09-2 핵심 패키지와 함수**

- TensorFlow
    - **`pad_sequences()`**: 시퀀스 길이를 맞추기 위해 패딩을 추가
        - **`maxlen`**매개변수로 원하는 시퀀스 길이 지정
        - `padding`매개변수는 패딩을 추가할 위치를 지정. 기본값인 ‘pre’는 시퀀스 앞에 패딩을 추가
    - `to_categorical()`: 정수 시퀀스를 원-핫 인코딩으로 변환
    - **`SimpleRNN`**: 케라스의 기본 순환층 클래스
        - 첫번째 매개변수에 뉴런의 개수 지정
        - `activation`매개변수에 활성화함수 지정. 기본값은 **tanh**
        - `dropout`매개변수에 입력에 대한 드롭아웃 비율 지정
    - **`Embedding`**: 단어 임베딩을 위한 클래스
        - 첫번째 매개변수에 어휘 사전의 크기 지정
        - 두번째 매개변수에 출력할 밀집 벡터의 크기 지정
        - `input_length`매개변수에 입력 시퀀스의 길이 지정
        

---

### 09-3 LSTM과 GRU셀

LSTM은 Long Short-Term Memory의 약자로, 단기 기억을 오래 기억하기 위해 고안된 셀이다.

LSTM에는 은닉상태 말고도 셀 상태라고 부르는 값이 있다. 이 셀 상태는 다음 층으로 전달되지 않고 LSTM 셀에서 순환만 되는 값이다.

![ LSTM의 대략적 구조](%E1%84%92%E1%85%A9%E1%86%AB%E1%84%8C%E1%85%A1%20%E1%84%80%E1%85%A9%E1%86%BC%E1%84%87%E1%85%AE%E1%84%92%E1%85%A1%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC%20%E1%84%83%E1%85%B5%E1%86%B8%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC(%E1%84%87%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A2%E1%84%89%E1%85%A5%E1%86%AB%20%E1%84%8C%E1%85%A5)%205fee2e5b433a463bbeca29c95c3cd0ee/Untitled%2012.png)

 LSTM의 대략적 구조

삭제 게이트는 셀 상태에 있는 정보를 제거하는 역할을 하고 입력 게이트는 새로운 정보를 셀 상태에 추가하며 출력 게이트를 통해서 이 셀 상태가 다음 은닉 상태로 출력된다.

이제 LSTM 신경망을 훈련해보자

```python
from tensorflow.keras.datasets import imdb
from sklearn.model_selection import train_test_split
(train_input, train_target), (test_input, test_target) = imdb.load_data(num_words=500)
train_input, val_input, train_target, val_target = train_test_split(train_input, train_target, test_size=0.2, random_state=42)

from tensorflow.keras.preprocessing.sequence import pad_sequences
#길이를 100으로 맞추어 패딩
train_seq = pad_sequences(train_input, maxlen=100)
val_seq = pad_sequences(val_input, maxlen=100)
```

순환층에서 `SimpleRNN` 클래스를 `LSTM` 클래스로 바꿔주기만 하면 된다.

```python
#순환층 만들기 
from tensorflow import keras
model = keras.Sequential()
model.add(keras.layers.Embedding(500,16,input_length=100))
model.add(keras.layers.LSTM(8))
model.add(keras.layers.Dense(1,activation='sigmoid'))
```

```python
Model: "sequential"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 embedding (Embedding)       (None, 100, 16)           8000      
                                                                 
 lstm (LSTM)                 (None, 8)                 800       
                                                                 
 dense (Dense)               (None, 1)                 9         
                                                                 
=================================================================
Total params: 8,809
Trainable params: 8,809
Non-trainable params: 0
_________________________________________________________________
```

`SimpleRNN` 클래스의 모델 파라미터 개수는 200개였다. `LSTM` 셀에는 작은 셀이 4개 있으므로 정확히 4배 늘어 모델 파라미터 수가 800개이다.

이제 모델을 컴파일하고 훈련한 다음 훈련손실과 검증 손실 그래프를 그려보자.

```python
rmsprop = keras.optimizers.RMSprop(learning_rate=1e-4)
model.compile(optimizer = rmsprop, loss='binary_crossentropy', metrics=['accuracy'])
checkpoint_cb = keras.callbacks.ModelCheckpoint('best-lstm-model.h5', save_best_only=True)
early_stopping_cb = keras.callbacks.EarlyStopping(patience=3, restore_best_weights=True)
history = model.fit(train_seq, train_target, epochs=100, batch_size=64, validation_data=(val_seq, val_target), callbacks=[checkpoint_cb, early_stopping_cb])

#결과
Epoch 27/100
313/313 - 12s 38ms/step - loss: 0.4164 - accuracy: 0.8139 - val_loss: 0.4396 - val_accuracy: 0.8024
```

```python
import matplotlib.pyplot as plt
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend(['train','val'])
plt.show()
```

![그래프.jpg](%E1%84%92%E1%85%A9%E1%86%AB%E1%84%8C%E1%85%A1%20%E1%84%80%E1%85%A9%E1%86%BC%E1%84%87%E1%85%AE%E1%84%92%E1%85%A1%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC%20%E1%84%83%E1%85%B5%E1%86%B8%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC(%E1%84%87%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A2%E1%84%89%E1%85%A5%E1%86%AB%20%E1%84%8C%E1%85%A5)%205fee2e5b433a463bbeca29c95c3cd0ee/%EA%B7%B8%EB%9E%98%ED%94%84.jpg)

기본 순환층보다 LSTM이 과대적합을 잘 억제하면서 훈련을 잘 수행한 것으로 보인다.

하지만 경우에 따라선 과대적합을 더 강하게 억제할 필요가 있다.