import numpy as np

arr = np.array([[3, 6, 9],
                [2, 4, 8],
                [5, 7, 1]])

# 문제
# 1. arr의 shape과 ndim을 출력하시오.
# 2. 열 방향 평균을 구하시오.
# 3. 행 방향 최댓값을 구하시오.
# 4. arr을 전치행렬로 만든 후 shape을 출력하시오.
# 5. arr을 1차원으로 펼친 뒤 최솟값을 구하시오.
# 6. arr을 (1, 9) 형태로 reshape 하시오.

print(f'\n문제1 \nshape: {arr.shape} \nndim: {arr.ndim}')

# axis: 축 옵션, axis=0 행(세로), axis=1 열(가로)
print(f'\n문제2 \n열 방향 평균: {arr.mean(axis=1)}')
print(f'\n문제3 \n행 방향 평균: {arr.mean(axis=0)}')

print(f'\n문제4 \n전치행렬: {arr.T} \nshape: {arr.T.shape}')

print(f'\n문제5 \n1차원 나열: {arr.flatten()} \n최솟값: {arr.flatten().min()}')

print(f'\n문제6 \nreshape(1,9): {arr.reshape(1,9)}')