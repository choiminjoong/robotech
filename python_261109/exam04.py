# 문제 : 함수를 사용해서 코드량을 확 줄여주세요.

dan = 8

def print_99dan_repeat(d,n):
    for j in range(1, n+1, 1):  
        i = 1
        while i <= 9:
            if i == 1:
                print("== {}번째 구구단 {}단 출력 ==".format(j,d))
               
            print("{} * {} = {}".format(d, i, d * i))
            i += 1

def print_99dan_total(sd,ed):
    for i in range(sd, ed+1, 1):
        print("== {}단 ==".format(i))
        for j in range(1, 10, 1):
            print("{} * {} = {}".format(i, j, i*j))

#print_99dan_total(1,9)


# print("== 1번째 구구단 8단 출력 ==")
# i = 1
# while i <= 9:
#   print("{} * {} = {}".format(dan, i, dan * i))
#   i += 1

# print("== 2번째 구구단 8단 출력 ==")
# i = 1
# while i <= 9:
#   print("{} * {} = {}".format(dan, i, dan * i))
#   i += 1

# print("== 3번째 구구단 8단 출력 ==")
# i = 1
# while i <= 9:
#   print("{} * {} = {}".format(dan, i, dan * i))
#   i += 1

# print("== 4번째 구구단 8단 출력 ==")
# i = 1
# while i <= 9:
#   print("{} * {} = {}".format(dan, i, dan * i))
#   i += 1

# print("== 5번째 구구단 8단 출력 ==")
# i = 1
# while i <= 9:
#   print("{} * {} = {}".format(dan, i, dan * i))
#   i += 1

# print("== 6번째 구구단 8단 출력 ==")
# i = 1
# while i <= 9:
#   print("{} * {} = {}".format(dan, i, dan * i))
#   i += 1

# print("== 7번째 구구단 8단 출력 ==")
# i = 1
# while i <= 9:
#   print("{} * {} = {}".format(dan, i, dan * i))
#   i += 1

# print("== 8번째 구구단 8단 출력 ==")
# i = 1
# while i <= 9:
#   print("{} * {} = {}".format(dan, i, dan * i))
#   i += 1

# print("== 9번째 구구단 8단 출력 ==")
# i = 1
# while i <= 9:
#   print("{} * {} = {}".format(dan, i, dan * i))
#   i += 1



# 문제 : 입력받은 정수가 소수인지 아닌지 알려주는 함수를 구현해주세요.

def is_prime_number(num):
    if num <= 1 or type(num) != int:
        return False

    if num % 2 == 0:
        return False

    return True

print(type(1) != int )

# print("3은 소수입니다 : {}".format(is_prime_number(3)))
# print("4는 소수입니다 : {}".format(is_prime_number(4)))
# print("5는 소수입니다 : {}".format(is_prime_number(5)))
# print("6는 소수입니다 : {}".format(is_prime_number(6)))
# print("7는 소수입니다 : {}".format(is_prime_number(7)))
#print("1000은 소수입니다 : {}".format(is_prime_number(1000)))