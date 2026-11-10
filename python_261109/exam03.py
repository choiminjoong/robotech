# While문 조건
# 시작값, 끝값/조건식, *보폭
# i = 1
# while i <= 3:
#   print(i)
#   i = i + 1
#
# print(i)

# 문제 : 1부터 300까지 출력해주세요.
# i = 1
# while i <= 300:
#    print(i)
#    i = i + 1

# 문제 : 100부터 -25까지 출력해주세요.
# j = 100
# while j >= -25:
#    print(j)
#    j = j - 1

# 문제 : 1부터 100 사이의 짝수만 출력해주세요.(개념 : while, if, %)
# k = 1
# while k <= 100:
#    if k % 2 == 0:
#         print(k)
#    k = k+1

# 문제 : 1부터 1000 사이의 수 중에서 3의 배수만 출력해주세요.
# l = 1
# while l < 1000:
#     if l % 3 == 0:
#         print(l)
#         l = l + 3
#     else:
#         l = l +1

# 문제 : 1부터 5까지의 합을 출력해주세요.(개념 : while)
# m = 1
# sum1 = 0
# while m <= 5:
#     sum1 = sum1 + m
#     m = m + 1
# print(sum1)

# 문제 : 1부터 100까지의 수 중에서 짝수의 합을 출력해주세요.(개념 : while, if, %)
# n = 1
# sum2 = 0
# while n <= 100:
#     if n % 2 == 0:
#         sum2 = sum2 + n
#         n = n +2
#     else:
#         n = n +1
# print(sum2)

# 문제 : 1부터 3까지 10번 반복해서 출력해주세요.
# i = 0
# while i < 10:
#     j = 1
#     while j <= 3:
#         print(j)
#         j = j + 1
#     i = i + 1

# 문제 : for문으로 1부터 100까지 출력
# for i in range(100):
#     print(i+1)

# 문제 : for문으로 100부터 1까지 출력    
# for i in range(100,0,-1):
#      print(i)

# 문제 : for문으로 구구단 1단 ~ 9단 출력
for i in range(1, 10, 1):
    for j in range(1, 10, 1):
        print(i,' x ',j,' = ',i*j)

