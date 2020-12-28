# install NumPy
pip3 install numpy

# import package
import numpy as np

# help
help(np)

# import data
data = np.array([[1,2],[3,4]])



# import list 
np.array(data)


# 기본 연산
# 더하기
1+2
np.add(1,2)

np.sum(data)
np.sum(data, axis = 0)
np.sum(data, axis = 1)


# 빼기
1-2
np.subtract(1,2)

# 곱하기
1*2
np.multiply(1,2)

np.prod(data)
np.prod(data, axis = 0)
np.prod(data, axis = 1)


# 나누기
1/2
np.divide(1,2)


# 표준편차 구하기
data.std()

# 분산 구하기
data.var()

# 최소값 구하기
data.min()

# 최대값 구하기
data.max()

# 누적 함계 구하기
data.cumsum()

# 누적 곱 구하기
data.cumprod()

# 행렬 간 곱하기
np.dot(data1, data2)
data1.dot(data2)



# 데이터 타입 조회하기
type(data)
type(1)
type("a")

# 데이터 타입 변경하기
data.astype(int)


# 1 다차원 행렬 생성하기
np.ones((2,3))

# 0 다차원 행렬 생성하기
np.zeros(2,3)

# NaN 값 사용 가능
np.nan

# 난수 배열 생성
data = np.random.rand(2,3)



#==========
# Reference
#==========

# 김정일 / 인공지능(AI) 프로그래밍_Machine Learning(머신러닝) 기초(파이썬 라이브러리 numpy, pandas) 