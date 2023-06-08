# 

# 문제01 유형 (DataSet_01)

- 입력변수 가중치가 크다는 것은 그만큼 많은 영향력을 매출액에 주고 있다는 것으로 봄>> 회귀분석을 통해 영향력이  얼마나 있는지 판단

X가 Y에게 얼마나 영향을 주는지 확인

가중치 ≒ ‘회기계수’

### y=0.1+1.2x1+0.1x2 ‘Ei(오차)’

선형회기

1.2 ,0.1  : 회귀계수

0.1 : 상수/절편 

상수를 제외한 식

### 1.2x1+0.1x2

평행이동을 위한 상수 절편을 둔다.

이 계수들이 y에 어떤 영향을 주는지 알아보려한다.

x1과 x2 (각각의 변수) 의 스케일이 다르다고 가정한다면 가중치가 다름

- 회기변수에 따라 결정되는 것이 아니다

 

## 회기 분석

연속형 변수들에 대해 두 변수간 모형을 구하고 적합도를 

측정하는 분석법

!https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Linear_regression.svg/230px-Linear_regression.svg.png

Illustration of linear regression on a data set.

### 공분산(Covaricance :COV

- X와 Y가 랜덤 변수이고 ux는 E(x), uy E(y) 라고 하자
- **Cov(X, Y) = E{(X-ux)(Y-uy)}**
- 1에 가까울 수록 좋다 >> 변수하나로 상관관계를 설명할 수 있다.
- (3) [양수값](https://ko.wikipedia.org/w/index.php?title=Definite_bilinear_form&action=edit&redlink=1): Var(*X*) = Cov(*X*, *X*) ≥ 0이고 Cov(*X*, *X*) = 0 이란 것은 *X*가 상수확률변수(*K*)라는 뜻이다
