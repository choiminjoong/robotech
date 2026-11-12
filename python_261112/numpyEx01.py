import numpy as np


'''
Numpy : 파이썬에서 수학과 데이터 분석을 쉽게 할 수 있도록 도와주는 라이브러리
ndArray : 숫자를 여러 차원으로 저장할 수 있는 배열
Numpy로 할 수 있는 것들
    - 숫자 묶음 생성
    - 평균, 합계, 최댓값
    - 배열
    - 2차원 표(행렬)
'''

a = [1,2,3]
b = [4,5,6]
print(f'일반리스트 {a} + {b} = {a+b}')
c = np.array([1,2,3])
d = np.array([4,5,6])
print(f'numpy array {c} + {d} = {c+d}')

arr1 = [1,2,3,4]
np_arr1 = np.array([1,2,3,4,5,6])
print(f'*** array type: {type(arr1)}')
print(f'*** numpy array type: {type(np_arr1)}')

#ndArray
np_arr2 = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8]])
np_arr3 = np.array([[[0.1, 0.2, 0.3, 0.4],[5,6,7,8]],
                    [[1,2,3,4],[1,2,3,4]]])
print(f'*** 2차원 배열: \n{np_arr2}')
print(f'*** 3차원 배열: \n{np_arr3}')

print(f'*** {c} ** 3 = {c ** 3} ')

# ndim: 배열의 차원 수
print(f'\n*** ndim1 = {np_arr1.ndim}')
print(f'*** ndim2 = {np_arr2.ndim}')
print(f'*** ndim3 = {np_arr3.ndim}')

# shape: 배열의 형태
print(f'\n*** shape1 = {np_arr1.shape}')
print(f'*** shape2 = {np_arr2.shape}')
print(f'*** shape3 = {np_arr3.shape}')

# size: 배열 요소의 총 개수
print(f'\n*** size1 = {np_arr1.size}')
print(f'*** size2 = {np_arr2.size}')
print(f'*** size3 = {np_arr3.size} ')

# dtype: 배열 요소의 데이터 타입
print(f'\n*** dtype1 = {np_arr1.dtype}')
print(f'*** dtype2 = {np_arr2.dtype}')
print(f'*** dtype3 = {np_arr3.dtype}')

# itemsize: 배열 원소 하나가 차지하는 메모리 크기
print(f'\n*** itemsize1 = {np_arr1.itemsize}')
print(f'*** itemsize2 = {np_arr2.itemsize}')
print(f'*** itemsize3 = {np_arr3.itemsize}')

# data: 배열 실제 데이터가 저장된 메모리 버퍼
print(f'\n*** data1 = {np_arr1.data}')
print(f'*** data2 = {np_arr2.data}')
print(f'*** data3 = {np_arr3.data}')

# ndArray T: 전치 행렬(행과 열을 바꾸는것)
print(f'\n*** 원본 배열: \n{np_arr2}')
print(f'\n*** 전치 배열 T: \n{np_arr2.T}')

# ndArray flatten(): 1차원으로 나열
print(f'\n*** 원본 배열: \n{np_arr2}')
print(f'\n*** flatten: \n{np_arr2.flatten()}')

# ndArray reshape(): 배열 모양 바꾸기
print(f'\n*** 원본 배열: \n{np_arr1}')
print(f'\n*** reshape(2,3): \n{np_arr1.reshape(2,3)}')

# ndArray sum(): 합계
# axis: 축 옵션, axis=0 열, axis=1 행
print(f'\n*** 원본 배열: \n{np_arr2}')
print(f'\n*** sum(): \n{np_arr2.sum()}')
print(f'\n*** sum(axis=0): \n{np_arr2.sum(axis=0)}')
print(f'\n*** sum(axis=1): \n{np_arr2.sum(axis=1)}')

# ndArray mean(): 평균
# ndArray min(): 최솟값
# ndArray max(): 최댓값
print(f'\n*** 원본 배열: \n{np_arr2}')
print(f'\n*** mean(): \n{np_arr2.mean()}')
print(f'\n*** mean(axis=0): \n{np_arr2.mean(axis=0)}')
print(f'\n*** mean(axis=1): \n{np_arr2.mean(axis=1)}')

print(f'\n*** min(): \n{np_arr2.min()}')
print(f'\n*** min(axis=0): \n{np_arr2.min(axis=0)}')
print(f'\n*** min(axis=1): \n{np_arr2.min(axis=1)}')

print(f'\n*** max(): \n{np_arr2.max()}')
print(f'\n*** max(axis=0): \n{np_arr2.max(axis=0)}')
print(f'\n*** max(axis=1): \n{np_arr2.max(axis=1)}')

# zeros(shape): 배열을 만들고, 모든 원소를 0으로 채움
# ones(shape): 배열을 만들고, 모든 원소를 1으로 채움
# full(shape, value): 배열을 만들고, 모든 원소를 value값으로 채움
print(f'\n*** np.zeros((3,4)) = \n{np.zeros((3,4))}')
print(f'\n*** np.ones((2,3,4)) = \n{np.ones((2,3,4))}')
print(f'\n*** np.full((3,4), 9) = \n{np.full((3,4), 9)}')

# _like 계열: 다른 배열을 보고 똑같이 만듦
# zeros_like / ones_like / full_like
print(f'\n*** np.zeros_like(np_arr2) = \n{np.zeros_like(np_arr2)}')
print(f'\n*** np.ones_like(np_arr2) = \n{np.ones_like(np_arr2)}')
print(f'\n*** np.full_like(np_arr2, 7) = \n{np.full_like(np_arr2, 7)}')

# random
# random.randint(시작값, 끝값, size): 시작값 <= ? < 끝값
print(f'\n***1 np.random.randint(-100, 100, (2,3)) = \n{np.random.randint(-100, 100, (2,3))}')
print(f'\n***2 np.random.randint(-100, 100, (2,3)) = \n{np.random.randint(-100, 100, (2,3))}')

# seed(int): 난수 생성 초기상태 고정, 같은 seed를 주면 항상 같은 난수 결과가 나옴
np.random.seed(1)
print(f'\n*** seed = 1, np.random.randint(-100, 100, (2,3)) = \n{np.random.randint(-100, 100, (2,3))}')
np.random.seed(1)
print(f'\n*** seed = 1, np.random.randint(-100, 100, (2,3)) = \n{np.random.randint(-100, 100, (2,3))}')

# 2차원 배열 슬라이싱
print(f'\n*** 원본 배열: \n{np_arr2}')
print(f'\n*** np_arr2[1:2, 1:3]: {np_arr2[1:2, 1:3]}')

# fancy
print(f'\n*** np_arr2[:, [0,3]] : \n{np_arr2[:, [0,3]]}')

