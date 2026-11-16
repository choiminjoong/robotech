# 사용자에게 문장 1개를 입력받아서 ,를 기준으로 나누기
#print("문자열을 입력 해주세요 : ", end='')
#texts = input().strip().split(',')


# 사용자에게 숫자 3개를 입력받아서, 더한 결과를 출력해주세요. map, strip를 사용해주세요.

# print("숫자 3개를 `,`로 구분지어서 입력해주세요.")
# print("EX : 10,20,30")
# print("입력 : ", end = '') # end = '' => 줄바꿈 안함
# a, b, c = map(int, input().strip().split(','))

# print("a : {}".format(a))
# print("b : {}".format(b))
# print("c : {}".format(c))
# print("a + b + c : {}".format(a + b + c))

# 문제시작
a = 10

# `==` => 같다.
if ( a == 10 ):
  print(True)

# `!=` => 같지 않다.
if ( a != 10 ):
  print(False)

if ( a > 10 ):
  print(False)

if ( a >= 10 ):
  print(True)

b = 10

if ( a == b ):
  print(True)

# c 에는 true or false 이 담긴다.
c = a != b

if ( c ):
  print(False)

if ( c == False ):
  print(True)

# `not` => 반전
if ( not c ):
  print(True)

if ( not(not c) ):
  print(False)

d = True

if ( c != d ):
  print(True)

if ( 10 > 5 and -6 > -10 and 10 != 10 ):
  print(True)

if ( 10 < 5 and -6 < -10 and 10 != 10 or 10 > 5 ):
  print(False)
# 문제끝

# 문제 : 10대, 20대, 30대 중 나이에 맞는 변수를 출력해주세요.

age = 35 # 25로 바꿔서 실행해보세요. 15로도 바꿔서 실행해보세요.

if 10 <= age < 20:
    print("10대")
elif 20 <= age < 30:    
    print("20대")
elif 30 <= age < 40:
    print("30대")
else:
    print("10대 이하 또는 40대 이상")    

# 문제 : 할인 대상인지 아닌지 출력해주세요.
# 조건 : 나이가 19세 이하이거나 60세 이상이면 할인 대상입니다.
# 조건 : `and, or`없이 풀어야 합니다.
# 조건 : 2가지 이상의 방법으로 풀어야 합니다.

age = 33

print("== 정답 v1 ==")
if age <= 19:
    print("할인 대상입니다.")
elif age >= 66:    
    print("할인 대상입니다.")
else:    
    print("할인 대상이 아닙니다.")

print("== 정답 v2 ==")
if age <= 19:
    print("할인 대상입니다.")
else:
    if age >= 66:    
        print("할인 대상입니다.")
    else:    
        print("할인 대상이 아닙니다.")