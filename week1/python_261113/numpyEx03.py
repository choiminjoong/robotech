import numpy as np

arr = np.array([[1.5, 2.5, 3.5, 4.5],
                [5.5, 6.5, 7.5, 8.5]])

# 문제
# 1. arr의 dtype과 itemsize를 출력하시오.
# 2. axis=0 기준 합을 구하시오.
# 3. axis=1 기준 평균을 구하시오.
# 4. arr을 (4,2) 형태로 reshape 하시오.
# 5. reshape한 배열을 전치한 결과의 shape을 구하시오.
# 6. arr.flatten()으로 만든 배열의 shape은 무엇인가?

print(f'\n문제1 \ndtype: {arr.dtype} \nitemsize: {arr.itemsize}')

# axis: 축 옵션, axis=0 행(세로), axis=1 열(가로)
print(f'\n문제2 \n열 방향 합: {arr.sum(axis=0)}')
print(f'\n문제3 \n행 방향 합: {arr.sum(axis=1)}')

print(f'\n문제4 \nreshape(4,2): {arr.reshape(4,2)}')

print(f'\n문제5 \nreshape 후 전치: {arr.reshape(4,2).T} \nshape: {arr.reshape(4,2).T.shape}')

print(f'\n문제6 \n1차원 나열: {arr.flatten()} \nshape: {arr.flatten().shape}')

