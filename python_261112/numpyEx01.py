import numpy as np

a = [1,2,3]
b = [4,5,6]
print(f'일반리스트 {a} + {b} = {a+b}')
c = np.array([1,2,3])
d = np.array([4,5,6])
print(f'numpy array {c} + {d} = {c+d}')

arr1 = [1,2,3,4]
np_arr1 = np.array([1,2,3,4])
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

# ndArray flatten: 1차원으로 나열
print(f'\n*** 원본 배열: \n{np_arr2}')
print(f'\n*** flatten: \n{np_arr2.flatten()}')