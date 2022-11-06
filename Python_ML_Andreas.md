# 파이썬 라이브러리를 활용한 머신러닝(안드레아스 뮐러 외 1 저)

> 책 소개
> 

[파이썬 라이브러리를 활용한 머신러닝](https://book.naver.com/bookdb/book_detail.nhn?bid=22059668)

```python
#필수 실행 라이브러리 코드
from IPython.display import display
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
pip install mglearn
import mglearn
```

## Chapter1 소개

### 1-1 붓꽃의 품종 분류

`train_test_split` 함수로 데이터를 나누기 전엔 유사 난수 생성기를 사용해 데이터셋을 섞어야 한다. 그 역할을 해주는 것이 바로 `random_state` 매개변수이다.

```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, t_test = train_test_split(
    iris_dataset['data'], iris_dataset['target'], random_state=0)
```

**k-최근접 이웃 알고리즘**을 사용해보자. 인접한 k개 이웃 중 가장 빈도가 높은 클래스를 예측값으로 채택하는 알고리즘이다.

```python
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)

#훈련데이터셋으로 모델을 만들기 위해 fit 메서드를 사용한다
knn.fit(X_train, y_train)

#예측용 데이터를 하나 만든다
import numpy as np
X_new=np.array([[5, 2.9, 1, 0.2]])
X_new

#예측은 predict 메서드를 사용한다
prediction = knn.predict(X_new)
iris_dataset['target_names'][prediction]

#정확도를 알기 위해 scroe 메서드를 사용한다
print("테스트 세트의 정확도: {:.4f}".format(knn.score(X_test, y_test)))

```

## Chapter2 지도학습

이 챕터에서 소개하는 지도학습의 대표적인 알고리즘을 정리해둔 내용이다. 세세한 내용보다는 중심이 되는 내용과 헷갈리기 쉬운 부분 위주로 요점만 정리했다.

### 2-1 k-최근접 이웃

**k-최근접 이웃 분류**

```python
#훈련 세트와 테스트 세트로 나눈다.
from sklearn.model_selection import train_test_split
X, y = mglearn.datasets.make_forge() #인위적으로 만든 이진 분류 데이터셋이다.
X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=0)

#KNeighborClassifier를 import하고 clf라는 객체를 만든다
from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier(n_neighbors=3)

#훈련세트를 fit메서드로 훈련시킨다.
clf.fit(X_train, y_train)

#predict 메서드로 테스트 세트를 예측한다.
print("테스트 데이터 예측 결과:",clf.predict(X_test))

#score 메서드로 정확도를 평가한다.
print("예측 정확도: {:.4f}".format(clf.score(X_test, y_test)))
#결과
예측 정확도: 0.8571
```

아래 코드는 결정 경계를 보여준다.

```python
fig, axes = plt.subplots(1,3,figsize=(10,3))
for n_neighbors, ax in zip([1,3,9],axes):
  clf = KNeighborsClassifier(n_neighbors=n_neighbors).fit(X,y)
  mglearn.plots.plot_2d_separator(clf, X, fill=True, eps=0.5, ax=ax, alpha=.4)
  mglearn.discrete_scatter(X[:,0],X[:,1], y, ax=ax)
  ax.set_title("{} neighbors".format(n_neighbors))
  ax.set_xlabel("feature0")
  ax.set_ylabel("feature1")
axes[0].legend(loc=3)
```
![Untitled 1](https://user-images.githubusercontent.com/115082062/200171581-511bac63-a30b-4b80-ad81-18a029f25cae.png)

이웃 개수가 늘어날수록 결정 경계는 점점 일반화된다. 즉, 이웃을 적게 사용하면 복잡도가 높아진다.

---

**k-최근접 이웃 회귀**

```python
from sklearn.neighbors import KNeighborsRegressor

#훈련 세트와 데이터 세트를 나눈다
X,y = mglearn.datasets.make_wave(n_samples=40)
X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=0)

#이웃의 수를 3으로 하여 회귀 객체를 만든다
reg = KNeighborsRegressor(n_neighbors=3)

#fit 메서드로 훈련 데이터와 타깃을 사용하여 모델을 학습시킨다
reg.fit(X_train, y_train)

#테스트 세트에 대해 predict 메서드로 예측을 한다
reg.predict(X_test)

#score 메서드로 정확도(결정계수)를 확인한다
print("테스트 세트 결정계수: {:.4f}".format(reg.score(X_test, y_test)))
#결과
테스트 세트 결정계수: 0.8344
```

회귀에도 결정 경계를 그어보자.

```python
fig, axes = plt.subplots(1,3,figsize=(15,4))
line = np.linspace(-3,3,1000).reshape(-1,1)
for n_neighbors, ax in zip([1,3,9],axes):
  reg = KNeighborsRegressor(n_neighbors=n_neighbors)
  reg.fit(X_train, y_train)
  ax.plot(line, reg.predict(line))
  ax.plot(X_train, y_train, '^', c=mglearn.cm2(0), markersize=8)
  ax.plot(X_test, y_test, 'v', c=mglearn.cm2(1), markersize=8)

  ax.set_title(
      "{}neighbors's train score: {:.3f} test score:{:.3f}".format(
          n_neighbors, reg.score(X_train, y_train),
          reg.score(X_test, y_test)
      )
  )
  ax.set_xlabel('feature')
  ax.set_ylabel('target')
axes[0].legend(['predict', 'train', 'test'], loc='best')
```

![Untitled](%E1%84%91%E1%85%A1%E1%84%8B%E1%85%B5%E1%84%8A%E1%85%A5%E1%86%AB%20%E1%84%85%E1%85%A1%E1%84%8B%E1%85%B5%E1%84%87%E1%85%B3%E1%84%85%E1%85%A5%E1%84%85%E1%85%B5%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%92%E1%85%AA%E1%86%AF%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC(%E1%84%8B%E1%85%A1%E1%86%AB%E1%84%83%E1%85%B3%E1%84%85%E1%85%A6%20d26933c7badb41ab858bcfedaffaceb2/Untitled%201.png)

---

### 2-2 선형 모델

선형 모델들은 다양한데, 파라미터(계수)를 학습하는 방식과 복잡도를 제어하는 방법에 따라 차이가 있다.

**선형 회귀(or 최소제곱법)**

예측값과 훈련 세트의 타깃 사이의 **평균제곱오차(mean squared error)**를 최소화하는 방식이다.

```python
from sklearn.linear_model import LinearRegression

#데이터 세트를 만든다
X,y = mglearn.datasets.make_wave(n_samples=60)

#훈련, 테스트 세트를 나눈다
X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=42)

#fit메서드로 훈련을 시켜 lr객체에 담는다.
lr = LinearRegression().fit(X_train, y_train)

#가중치(계수) 파라미터와 절편 파라미터를 확인해보자
print(lr.coef_)
print(lr.intercept_)

#score 메서드로 성능을 확인해보자
print("훈련세트 점수: {:.4f}".format(lr.score(X_train, y_train)))
print("테스트세트 점수: {:.4f}".format(lr.score(X_test, y_test)))
#결과
훈련세트 점수: 0.6701
테스트세트 점수: 0.6593
```

과대적합을 제어하는 가장 유명한 모델은 **리지(ridge) 회귀**이다.

```python
#보스턴 주택가격 데이터셋을 불러온다.
X, y = mglearn.datasets.load_extended_boston()

#훈련세트, 테스트세트를 나눈다.
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0) 

#리지 회귀를 import한다.
from sklearn.linear_model import Ridge

#fit메서드로 훈련을 시켜 ridge 객체에 담는다.
ridge = Ridge().fit(X_train, y_train)

#성능을 평가한다.
print("훈련세트 점수: {:.4f}".format(ridge.score(X_train, y_train)))
print("테스트세트 점수: {:.4f}".format(ridge.score(X_test, y_test)))
#결과
훈련세트 점수: 0.8858
테스트세트 점수: 0.7528
```

선형 회귀로 학습할 때보다 훈련세트 점수는 낮아지더라도 테스트 점수가 높아진다. 즉 더 일반화된 모델이 된다. 이 때 `alpha` 파라미터를 조정하여 일반화 정도를 조절할 수 있다. 값이 클수록 더 일반화된다.

```python
ridge = Ridge(alpha=0.1).fit(X_train, y_train)
print("훈련세트 점수: {:.4f}".format(ridge.score(X_train, y_train)))
print("테스트세트 점수: {:.4f}".format(ridge.score(X_test, y_test)
#결과
훈련세트 점수: 0.9282
테스트세트 점수: 0.7722
```

데이터가 충분히 많아지면 선형회귀의 성능이 리지의 성능을 따라잡는다. 즉, 데이터가 충분하면 규제의 필요성은 살짝 낮아진다는 것이다.

---

**라소(lasso)** **회귀**도 규제를 가한다는 점에서 리지와 같지만, 리지가 계수를 0에 가깝게 하는 반면, 라소는 계수를 0으로 만들기도 한다. 어느 특성은 모델에서 완전히 제외될 수 있다는 말이다.

```python
from sklearn.linear_model import Lasso
lasso = Lasso().fit(X_train, y_train)
print("훈련세트 점수: {:.4f}".format(lasso.score(X_train, y_train)))
print("테스트세트 점수: {:.4f}".format(lasso.score(X_test, y_test)))
print("사용한 특성의 개수:", np.sum(lasso.coef_ != 0))
#결과
훈련세트 점수: 0.2932
테스트세트 점수: 0.2094
사용한 특성의 개수: 4
```

104개의 특성 중 무려 100개가 계수가 0이 되어 사라졌고, 훈련세트와 테스트세트 점수 모두 낮다. 과소적합을 완화하기 위해 alpha 파라미터를 조정해보자.

```python
lasso001 = Lasso(alpha=0.01, max_iter=50000).fit(X_train, y_train)
print("훈련세트 점수: {:.4f}".format(lasso001.score(X_train, y_train)))
print("테스트세트 점수: {:.4f}".format(lasso001.score(X_test, y_test)))
print("사용한 특성의 개수:", np.sum(lasso001.coef_ != 0))
#결과
훈련세트 점수: 0.8962
테스트세트 점수: 0.7657
사용한 특성의 개수: 33
```

---

### 2-3 분류용 선형모델

이진분류에 사용되는 선형모델은 **로지스틱 회귀**와 **서포트 벡터 머신**이 있다.

```python
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC

X,y = mglearn.datasets.make_forge()

fig,axes = plt.subplots(1,2,figsize=(10,3))
for model, ax in zip([LinearSVC(max_iter=5000), LogisticRegression()], axes):
  clf = model.fit(X, y)
  mglearn.plots.plot_2d_separator(clf, X, fill=False, eps=0.5,
                                  ax=ax, alpha=.7)
  mglearn.discrete_scatter(X[:,0],X[:,1], y, ax=ax)
  ax.set_title(clf.__class__.__name__)
  ax.set_xlabel("feature 0")
  ax.set_ylabel("feature 1")
axes[0].legend()
```

![Untitled](%E1%84%91%E1%85%A1%E1%84%8B%E1%85%B5%E1%84%8A%E1%85%A5%E1%86%AB%20%E1%84%85%E1%85%A1%E1%84%8B%E1%85%B5%E1%84%87%E1%85%B3%E1%84%85%E1%85%A5%E1%84%85%E1%85%B5%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%92%E1%85%AA%E1%86%AF%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC(%E1%84%8B%E1%85%A1%E1%86%AB%E1%84%83%E1%85%B3%E1%84%85%E1%85%A6%20d26933c7badb41ab858bcfedaffaceb2/Untitled%202.png)

두 모델은 모두 결정경계를 만들고 경계 위를 클래스 1, 아래를 클래스 0으로 분류한다. 이 두 모델은 기본적으로 리지 회귀처럼 L2 규제를 사용한다.

매개변수 `C`를 높이면 제약이 풀어지고 과대적합된다. 기본값은 1이다.

```python
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(
    cancer.data, cancer.target, stratify=cancer.target, random_state=42
)
logreg = LogisticRegression(max_iter=5000).fit(X_train, y_train)
print("훈련 세트 점수: {:.3f}".format(logreg.score(X_train,y_train)))
print("테스트 세트 점수: {:.3f}".format(logreg.score(X_test,y_test)))
#결과
훈련 세트 점수: 0.958
테스트 세트 점수: 0.958

#만약 C를 100으로 높이면
logreg = LogisticRegression(C=100,max_iter=5000).fit(X_train, y_train)
print("훈련 세트 점수: {:.3f}".format(logreg.score(X_train,y_train)))
print("테스트 세트 점수: {:.3f}".format(logreg.score(X_test,y_test)))
#결과
훈련 세트 점수: 0.981
테스트 세트 점수: 0.965
```

---

다중 분류 알고리즘은 여러 개의 이진 분류를 학습시켜 가장 높은 점수를 내는 분류기의 클래스를 예측값으로 택한다. `LinearSVC` 로 클래스가 3개인 데이터를 학습시키고 경계를 시각화해보자.

```python
mglearn.plots.plot_2d_classification(linear_svm, X, fill=True, alpha=.7)
mglearn.discrete_scatter(X[:,0], X[:,1], y)
line = np.linspace(-15, 15)
for coef, intercept, color in zip(linear_svm.coef_, linear_svm.intercept_, mglearn.cm3.colors):
  plt.plot(line, -(line*coef[0]+intercept)/coef[1], c=color)
plt.legend(['class0', 'class1', 'class2', 'border0', 'border1', 'border2'], loc=(1.01, 0.3))
plt.xlabel('feature0')
plt.ylabel('feature1')
```

![Untitled](%E1%84%91%E1%85%A1%E1%84%8B%E1%85%B5%E1%84%8A%E1%85%A5%E1%86%AB%20%E1%84%85%E1%85%A1%E1%84%8B%E1%85%B5%E1%84%87%E1%85%B3%E1%84%85%E1%85%A5%E1%84%85%E1%85%B5%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%92%E1%85%AA%E1%86%AF%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC(%E1%84%8B%E1%85%A1%E1%86%AB%E1%84%83%E1%85%B3%E1%84%85%E1%85%A6%20d26933c7badb41ab858bcfedaffaceb2/Untitled%203.png)

선형 모델은 학습 속도가 빠르고 예측도 빠르다. 또 하나의 장점은 회귀식을 보고 비교적 쉽게 이해할 수 있다는 점이다. 또한 샘플에 비해 특성이 많은, 즉 고차원의 데이터셋에서 잘 작동한다.

---

### 2-4 나이브 베이즈 분류기

**나이브 베이즈(naive bayes)** 분류기는 선형 모델과 매우 유사하다. 훈련속도는 보다 빠르지만 일반화 성능이 조금 낮다. 나이브 베이즈는 각 특성을 개별로 취급해 파라미터를 학습한다.

---

### 2-5 결정 트리

**결정 트리(decision tree)**는 분류와 회귀 문제에 널리 사용하는 모델이다. 결정 트리에서 질문이나 정답을 담은 상자를 노드라고 하고, 마지막 노드를 **리프**라고 한다. 질문은 각 분할 영역이 한 개의 타깃 값만 가질 때까지 반복되고, 타깃 하나만으로 이뤄진 리프 노드를 **순수 노드(pure node)**라고 한다.

모든 리프가 순수노드가 될 때까지 학습하면 모델은 과대적합된다. 때문에 복잡도를 제어하기 위해 최대 깊이나 리프의 최대 개수를 제한하는 방법이 있다. 깊이 제한으로 `max_depth` 옵션을 줄 수 있다.

```python
cancer = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(
    cancer.data, cancer.target, stratify=cancer.target, random_state=42)
print("훈련세트 정확도: {:.3f}".format(tree.score(X_train, y_train)))
print("테스트세트 정확도: {:.3f}".format(tree.score(X_test, y_test)))

#결과
훈련세트 정확도: 0.988
테스트세트 정확도: 0.951
```

또한 트리모듈의 `export_graphviz` 함수로 트리를 시각화할 수 있다.

```python
from sklearn.tree import export_graphviz
export_graphviz(tree, out_file="tree.dot", class_names=["악성", "양성"],
                feature_names = cancer.feature_names, impurity=False, filled=True)
import graphviz
with open("tree.dot") as f:
  dot_graph = f.read()
  display(graphviz.Source(dot_graph))
```

![스크린샷, 2022-04-21 15-27-06.png](%E1%84%91%E1%85%A1%E1%84%8B%E1%85%B5%E1%84%8A%E1%85%A5%E1%86%AB%20%E1%84%85%E1%85%A1%E1%84%8B%E1%85%B5%E1%84%87%E1%85%B3%E1%84%85%E1%85%A5%E1%84%85%E1%85%B5%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%92%E1%85%AA%E1%86%AF%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC(%E1%84%8B%E1%85%A1%E1%86%AB%E1%84%83%E1%85%B3%E1%84%85%E1%85%A6%20d26933c7badb41ab858bcfedaffaceb2/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7_2022-04-21_15-27-06.png)

트리를 만들 때 특성들의 중요도를 알려면 `feature_importances_` 메서드를 사용하면 된다. 중요도는 0에서 1의 값을 갖고, 1에 가까울수록 중요한 특성이다. 그러나 높은 중요도가 양성을 의미하는지 음성을 의미하는지는 알 수 없다.

```python
print("특성 중요도:\n", tree.feature_importances_)

def plot_feature_importances_cancer(model):
  n_features = cancer.data.shape[1]
  plt.barh(np.arange(n_features), model.feature_importances_, align='center')
  plt.yticks(np.arange(n_features), cancer.feature_names)
  plt.xlabel("feature importances")
  plt.ylabel("features")
  plt.ylim(-1, n_features)
plot_feature_importances_cancer(tree)
```

---

### 2-6 결정 트리의 앙상블

**앙상블(ensemble)**은 여러 모델을 연결하여 더 강력한 모델을 만드는 기법이다. 그 중 랜덤 포레스트와 그레이디언트 부스팅 결정 트리가 있다.

**랜덤 포레스트**는 여러 트리를 무작위로 만들어 과대적합을 피하는 방식이다. 회귀와 분류에 있어 가장 널리 사용되는 머신러닝 알고리즘이다. **부트스트랩 샘플링**을 사용하여 한쪽 트리에 나타나는 훈련 세트가 다른 트리엔 안 나타날 수도 있다. 이 때 각 트리는 각각 일부 특성에만 초점을 맞추어 모든 트리가 서로 다른 특성에 초점을 맞추도록 한다. 이 때 집중할 특성의 개수를 고르는 매개변수가 `max_features`이다. 이 변수를 크게 하면 트리들은 매우 비슷해지고, 작게 하면 트리들이 많이 달라지고 깊이가 낮아지게 된다. 보통 기본값으로 두는 게 현명하다.

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_moons
X,y = make_moons(n_samples=100, noise=0.25, random_state=3)
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, 
                                                    random_state=42)
#n_estimators매개변수로 트리의 개수를 지정한다.
forest = RandomForestClassifier(n_estimators=5, random_state=2)
forest.fit(X_train, y_train)
```

랜덤 포레스트로 만들어진 각 트리는 `estimators_` 속성에 저장된다. 각 트리가 만든 결정 경계와 이를 평균하여 최종적으로 나온 결정 경계를 시각화하면 다음과 같다.

```python
fig, axes = plt.subplots(2,3,figsize=(20,10))
for i, (ax, tree) in enumerate(zip(axes.ravel(), forest.estimators_)):
  ax.set_title("tree {}".format(i))
  mglearn.plots.plot_tree_partition(X,y, tree, ax=ax)

mglearn.plots.plot_2d_separator(forest, X, fill=True, ax=axes[-1,-1], alpha=.4)
axes[-1,-1].set_title("random forest")
mglearn.discrete_scatter(X[:,0], X[:,1], y)
```

![다섯 개의 랜덤 트리와 이를 평균 내어 만든 random forest](%E1%84%91%E1%85%A1%E1%84%8B%E1%85%B5%E1%84%8A%E1%85%A5%E1%86%AB%20%E1%84%85%E1%85%A1%E1%84%8B%E1%85%B5%E1%84%87%E1%85%B3%E1%84%85%E1%85%A5%E1%84%85%E1%85%B5%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%92%E1%85%AA%E1%86%AF%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC(%E1%84%8B%E1%85%A1%E1%86%AB%E1%84%83%E1%85%B3%E1%84%85%E1%85%A6%20d26933c7badb41ab858bcfedaffaceb2/Untitled%204.png)

다섯 개의 랜덤 트리와 이를 평균 내어 만든 random forest

유방암 데이터셋에 100개의 트리로 만든(`n_estimators=100`) 랜덤 포레스트를 적용해보자

```python
X_train, X_test, y_train, y_test = train_test_split(
    cancer.data, cancer.target, random_state=0
)
forest = RandomForestClassifier(n_estimators=100, random_state=0)
forest.fit(X_train, y_train)
print("훈련 세트 정확도: {:.3f}".format(forest.score(X_train, y_train)))
print("테스트 세트 정확도: {:.3f}".format(forest.score(X_test, y_test)))

#결과
훈련 세트 정확도: 1.000
테스트 세트 정확도: 0.972
```

`n_estimators` 매개변수를 높여서 과대적합을 줄이는 게 좋지만, 더 많은 메모리와 긴 훈련 시간을 갖게 된다.

**그레이디언트 부스팅 회귀 트리**는 이전 트리의 오차를 보완하는 방식으로 순차적으로 트리를 만든다. 무작위성이 없는 대신 트리를 얕게 하여 메모리를 적게 사용한다. `max_depth` 매개변수를 통해 최대깊이를 줄여 과대적합을 막을 수 있다. `learning_rate` 매개변수를 줄여 학습률을 낮추는 것도 방법이다.

```python
from sklearn.ensemble import GradientBoostingClassifier
X_train, X_test, y_train, y_test = train_test_split(
  cancer.data, cancer.target, random_state=0
)
gbrt = GradientBoostingClassifier(random_state=0, max_depth=1)
gbrt.fit(X_train, y_train)

print("훈련 세트 정확도: {:.3f}".format(gbrt.score(X_train, y_train)))
print("테스트 세트 정확도: {:.3f}".format(gbrt.score(X_test, y_test)))
#결과
훈련 세트 정확도: 0.991
테스트 세트 정확도: 0.972
```

이밖에도 앙상블에는 배깅, 에이다부스트, 엑스트라 트리가 있다.

**배깅(bagging)**은 Bootstrap aggregating의 줄임말이다. 중복을 허용한 부트스트랩 샘플링을 한다.

```python
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import BaggingClassifier
#LogisticRegression 객체를 기반 분류기로 지정하고, 분류기 개수(n_estimators)는 100개로 정했다
bagging = BaggingClassifier(LogisticRegression(), n_estimators=100,
                            oob_score=True, n_jobs=-1, random_state=42)
#oob_score를 True로 지정하면 부트스트래핑에 포함되지 않은 샘플을 기반으로 모델을 평가한다.
bagging.fit(Xc_train, yc_train)
print(bagging.score(Xc_train, yc_train))
print(bagging.score(Xc_test, yc_test))
print(bagging.oob_score_) #oob 샘플의 평가 점수
#결과
0.9530516431924883
0.958041958041958
0.9413145539906104
```

**엑스트라 트리**는 랜덤 포레스트와 비슷하지만 후보 특성을 무작위로 분할한 다음 최적의 분할을 찾는다.

결정 경계를 그려보면 랜덤 포레스트와 유사하다.

```python
from sklearn.ensemble import ExtraTreesClassifier
xtree = ExtraTreesClassifier(n_estimators=5, n_jobs=-1, random_state=0)
xtree.fit(Xm_train, ym_train)

fig,axes = plt.subplots(2,3, figsize=(20,10))
for i, (ax, tree) in enumerate(zip(axes.ravel(), xtree.estimators_)):
  ax.set_title("tree {}".format(i))
  mglearn.plots.plot_tree_partition(Xm, ym, tree, ax=ax)
mglearn.plots.plot_2d_separator(xtree, Xm, fill=True, ax=axes[-1,-1], alpha=.4)
axes[-1,1].set_title("extra tree")
mglearn.discrete_scatter(Xm[:,0], Xm[:,1], ym)
plt.show()
```

평가 점수도 랜덤 포레스트와 비슷하지만, 무작위 분할 때문에 일반화 성능을 높이려면 많은 트리를 만들어야 한다. 때문에 랜덤 포레스트가 엑스트라 트리보다 더 선호된다.

**에이다부스트**는 adaptive boosting의 줄임말이다. 그레이디언트 부스팅처럼 약한 학습기를 사용하는데, 이전 모델이 잘못 분류한 샘플에 가중치를 높여 다음 모델을 학습시킨다는 차이가 있다.

---

### 2-7 커널 서포트 벡터 머신

커널 서포트 벡터 머신(SVM)은 입력 데이터에서 단순한 초평면으로 정의되지 않는 더 복잡한 모델을 만들 수 있도록 확장한 것이다.

```python
from sklearn.datasets import make_blobs

X,y = make_blobs(centers=4, random_state=8)
y=y%2
mglearn.discrete_scatter(X[:,0], X[:,1], y)

from sklearn.svm import LinearSVC
linear_svm = LinearSVC(max_iter=5000, tol=1e-3).fit(X,y)
mglearn.plots.plot_2d_separator(linear_svm, X)
mglearn.discrete_scatter(X[:,0], X[:,1], y)
plt.xlabel("feature0")
plt.ylabel("feature1")
```

![Untitled](%E1%84%91%E1%85%A1%E1%84%8B%E1%85%B5%E1%84%8A%E1%85%A5%E1%86%AB%20%E1%84%85%E1%85%A1%E1%84%8B%E1%85%B5%E1%84%87%E1%85%B3%E1%84%85%E1%85%A5%E1%84%85%E1%85%B5%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%92%E1%85%AA%E1%86%AF%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC(%E1%84%8B%E1%85%A1%E1%86%AB%E1%84%83%E1%85%B3%E1%84%85%E1%85%A6%20d26933c7badb41ab858bcfedaffaceb2/Untitled%205.png)

위 그림을 보면 선형 모델로는 두 클래스를 분류할 수 없다는 걸 알 수 있다. 그래서 두 특성을 곱한 제 3의 특성을 만들어서 3차원 공간에서 평면을 그어 결정경계를 만들어볼 것이다.

```python
#두번째 특성을 제곱하여 추가한다
X_new=np.hstack([X, X[:,1:]**2])
from mpl_toolkits.mplot3d import Axes3D, axes3d
figure = plt.figure()
#3차원 그래프
ax = Axes3D(figure, elev=-152, azim=-26)
mask = y ==0
linear_svm_3d = LinearSVC(max_iter=5000).fit(X_new, y)
coef, intercept = linear_svm_3d.coef_.ravel(), linear_svm_3d.intercept_

#결정경계그리기
figure = plt.figure()
ax = Axes3D(figure, elev=-152, azim=-26)
xx = np.linspace(X_new[:,0].min()-2, X_new[:,0].max()+2, 50)
yy = np.linspace(X_new[:,1].min()-2, X_new[:,1].max()+2, 50)

XX, YY = np.meshgrid(xx,yy)
ZZ = (coef[0]*XX + coef[1]*YY + intercept)/-coef[2]
ax.plot_surface(XX,YY,ZZ,rstride=8, cstride=8, alpha=0.3)
ax.scatter(X_new[mask,0], X_new[mask,1], X_new[mask,2], c='b',
           cmap=mglearn.cm2, s=60, edgecolor='k')
ax.scatter(X_new[~mask,0],X_new[~mask, 1], X_new[~mask,2], c='r', marker='^',
           cmap=mglearn.cm2, s=60, edgecolor='k')
ax.set_xlabel("feature0")
ax.set_ylabel("feature1")
ax.set_zlabel("feature1**2")
```

![Untitled](%E1%84%91%E1%85%A1%E1%84%8B%E1%85%B5%E1%84%8A%E1%85%A5%E1%86%AB%20%E1%84%85%E1%85%A1%E1%84%8B%E1%85%B5%E1%84%87%E1%85%B3%E1%84%85%E1%85%A5%E1%84%85%E1%85%B5%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%92%E1%85%AA%E1%86%AF%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC(%E1%84%8B%E1%85%A1%E1%86%AB%E1%84%83%E1%85%B3%E1%84%85%E1%85%A6%20d26933c7badb41ab858bcfedaffaceb2/Untitled%206.png)

이것을 다시 원래 특성으로 투영해보면 SVM 모델은 더 이상 선형이 아니다.

```python
ZZ = YY **2
dec = linear_svm_3d.decision_function(np.c_[XX.ravel(), YY.ravel(), ZZ.ravel()])
plt.contourf(XX,YY,dec.reshape(XX.shape), levels=[dec.min(), 0, dec.max()],
             cmap=mglearn.cm2, alpha=0.5)
mglearn.discrete_scatter(X[:,0], X[:,1], y)
plt.xlabel("feature0")
plt.ylabel("feature1")
```

![Untitled](%E1%84%91%E1%85%A1%E1%84%8B%E1%85%B5%E1%84%8A%E1%85%A5%E1%86%AB%20%E1%84%85%E1%85%A1%E1%84%8B%E1%85%B5%E1%84%87%E1%85%B3%E1%84%85%E1%85%A5%E1%84%85%E1%85%B5%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%92%E1%85%AA%E1%86%AF%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC(%E1%84%8B%E1%85%A1%E1%86%AB%E1%84%83%E1%85%B3%E1%84%85%E1%85%A6%20d26933c7badb41ab858bcfedaffaceb2/Untitled%207.png)

하지만 이처럼 새로운 특성을 많이 만들다보면 연산 비용이 커진다. 특성을 많이 만들지 않고서도 고차원으로 학습하는 방식을 **커널 기법(kernel trick)**이라고 한다. 실제로 데이터를 확장하지 않고 확장된 특성에 대한 데이터 포인트들의 거리를 계산한다.

일반적으로 결정 경계를 만드는 데 영향을 주는 벡터는 훈련 데이터의 일부이다. 이 일부 데이터를 **서포트 벡터**라고 하며, 두 클래스 사이의 경계에 위치한 데이터들이다.

`gamma` 매개변수를 낮추면 하나의 훈련 샘플이 미치는 영향이 커진다. `C`매개변수는 규제 역할을 한다.

```python
from sklearn.svm import SVC
X, y= mglearn.tools.make_handcrafted_dataset()
svm = SVC(kernel='rbf', C=10, gamma=0.1).fit(X,y)
fig, axes = plt.subplots(3,3,figsize=(15,10))
for ax, C in zip(axes, [-1,0,3]):
  for a, gamma in zip(ax, range(-1,2)):
    mglearn.plots.plot_svm(log_C=C, log_gamma=gamma, ax=a)
axes[0,0].legend(['class0', 'class1', 'class0 support vector', 'class1 support vector'], ncol=4, loc=(.9,1.2))
```

![Untitled](%E1%84%91%E1%85%A1%E1%84%8B%E1%85%B5%E1%84%8A%E1%85%A5%E1%86%AB%20%E1%84%85%E1%85%A1%E1%84%8B%E1%85%B5%E1%84%87%E1%85%B3%E1%84%85%E1%85%A5%E1%84%85%E1%85%B5%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%92%E1%85%AA%E1%86%AF%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC(%E1%84%8B%E1%85%A1%E1%86%AB%E1%84%83%E1%85%B3%E1%84%85%E1%85%A6%20d26933c7badb41ab858bcfedaffaceb2/Untitled%208.png)

위 그래프를 보면, 작은 `gamma`값은 커널의 반경을 크게 하여 많은 포인트들이 가까이 있는 것으로 간주된다. 그래서 왼쪽 그림의 결정 경계는 부드럽고, `gamma`가 커질수록 하나의 포인트에 더 민감해진다.

특히나 SVM은 입력 특성의 스케일이 비슷해야 한다. 이를 위한 데이터 전처리를 해줘야 한다. 모든 특성 값을 평균이 0이고 단위 분산이 되도록 하거나, 0과 1 사이로 맞추는 방법을 많이 사용한다.

---

### 2-8 신경망(딥러닝)

딥러닝 알고리즘의 출발점은 **다층 퍼셉트론(multilayer perceptrons, MLP)**이다. 이는 여러 단계를 거쳐 만드는 선형 모델이라 볼 수 있다.

```python
display(mglearn.plots.plot_single_hidden_layer_graph())
```

![스크린샷, 2022-04-26 23-23-49.png](%E1%84%91%E1%85%A1%E1%84%8B%E1%85%B5%E1%84%8A%E1%85%A5%E1%86%AB%20%E1%84%85%E1%85%A1%E1%84%8B%E1%85%B5%E1%84%87%E1%85%B3%E1%84%85%E1%85%A5%E1%84%85%E1%85%B5%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%92%E1%85%AA%E1%86%AF%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB%20%E1%84%86%E1%85%A5%E1%84%89%E1%85%B5%E1%86%AB%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC(%E1%84%8B%E1%85%A1%E1%86%AB%E1%84%83%E1%85%B3%E1%84%85%E1%85%A6%20d26933c7badb41ab858bcfedaffaceb2/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7_2022-04-26_23-23-49.png)

다층 퍼셉트론을 구현한 `MLPClassifer`를 적용해보자. MLP는 기본값으로 은닉 유닛을 100개 사용하는데, `hidden_layer_sizes=[00]`으로 그 수를 조절할 수 있다.

```python
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_moons
X,y = make_moons(n_samples=100, noise=0.25, random_state=3)
X_train, X_test, y_train, y_test = train_test_split(X,y,stratify=y, random_state=42)
mlp = MLPClassifier(solver='lbfgs', random_state=0).fit(X_train, y_train)
mglearn.plots.plot_2d_separator(mlp, X_train, fill=True, alpha=.3)
mglearn.discrete_scatter(X_train[:,0], X_train[:,1], y_train)
plt.xlabel("feature0")
plt.ylabel("feature1")
```
