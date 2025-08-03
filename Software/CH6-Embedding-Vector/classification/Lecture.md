
# 분류 (Classification)

## 분류
- **분류(Classification)** : 주어진 데이터를 미리 정해진 여러 **카테고리** 중 하나로 **구분**하는 것.
- 분류는 다양한 분야에서 활용된다.
  - 예시: 이메일이 스팸인지 아닌지 분류하기
  - 예시: 사진 속에 고양이와 개 중 무엇이 있는지 분류하기
- 분류는 **지도 학습(Supervised Learning)**의 일종으로, 미리 **정답(label)**이 있는 데이터를 기반으로 학습합니다.

## 대표적인 분류 모델들
- **K-최근접 이웃 알고리즘(KNN)**: 데이터 포인트의 이웃들과의 거리를 계산해 가장 가까운 이웃들의 **다수결**로 분류.
- **의사결정나무(Decision Tree)**: 데이터를 **질문 형태**로 나눠 가며 분류하는 구조. **Yes/No** 질문을 통해 데이터를 나누어 나감.
- **서포트 벡터 머신(SVM)**: 데이터를 **두 개의 그룹**으로 나누는 **최적의 경계(초평면)**를 찾는 알고리즘.
- **딥러닝 CNN**: **이미지 분류** 등에서 주로 사용하는 모델로, **합성곱 신경망(Convolutional Neural Network)**을 사용하여 분류.

---

## K-최근접 이웃(KNN)

- **원리**:
  - 새로운 데이터 포인트가 주어지면, 가장 가까운 **K개의 이웃** 데이터를 찾습니다.
  - 이웃 데이터들의 **다수결**에 따라 새로운 데이터를 분류합니다.
  - 거리 계산: 주로 **유클리드 거리(Euclidean Distance)**를 사용합니다.

- **스켈레톤 코드**:

```python
from sklearn.neighbors import KNeighborsClassifier

# 데이터 준비 (X: 특징, y: 라벨)
X_train = [[0, 0], [1, 1], [2, 2], [3, 3]]
y_train = [0, 0, 1, 1]

# KNN 모델 생성 (K=3)
model = KNeighborsClassifier(n_neighbors=3)

# 모델 학습
model.fit(X_train, y_train)

# 새로운 데이터 분류
X_test = [[1.5, 1.5]]
y_pred = model.predict(X_test)

print(f"예측 결과: {y_pred}")
```

---

## 의사결정나무(Decision Tree)

- **원리**:
  - 데이터를 **특징**에 따라 **조건부 질문**을 던지며 나눕니다.
  - 각 질문에 대한 **분기(branch)**가 트리 형태로 만들어지고, 최종 **리프(leaf)** 노드에서 분류를 결정합니다.
  - 데이터가 **순수**하게 나눠질 때까지 진행합니다.

- **스켈레톤 코드**:

```python
from sklearn.tree import DecisionTreeClassifier

# 데이터 준비
X_train = [[0, 0], [1, 1], [2, 2], [3, 3]]
y_train = [0, 0, 1, 1]

# 의사결정나무 모델 생성
model = DecisionTreeClassifier()

# 모델 학습
model.fit(X_train, y_train)

# 새로운 데이터 분류
X_test = [[1.5, 1.5]]
y_pred = model.predict(X_test)

print(f"예측 결과: {y_pred}")
```

---

## 서포트 벡터 머신(SVM)

- **원리**:
  - 데이터를 분리하는 **최적의 경계(초평면)**를 찾습니다.
  - 이 경계는 두 그룹 간의 **마진(거리를 유지하는 영역)**을 최대화하도록 설정됩니다.
  - 복잡한 데이터 분포는 **커널 트릭**을 사용해 고차원 공간에서 분류할 수 있습니다.

- **스켈레톤 코드**:

```python
from sklearn import svm

# 데이터 준비
X_train = [[0, 0], [1, 1], [2, 2], [3, 3]]
y_train = [0, 0, 1, 1]

# SVM 모델 생성
model = svm.SVC()

# 모델 학습
model.fit(X_train, y_train)

# 새로운 데이터 분류
X_test = [[1.5, 1.5]]
y_pred = model.predict(X_test)

print(f"예측 결과: {y_pred}")
```

---

이제 학생들에게 각 분류 알고리즘의 원리를 설명하고, 스켈레톤 코드를 기반으로 실제 데이터를 분류하는 과정을 함께 실습해보세요.
