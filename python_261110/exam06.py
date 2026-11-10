import re

# 문제 : 딕셔너리에 각 달의 마지막 날들을 한번에 담기
obj_dict1 = {
    '1월' : 31,
    '2월' : 28,
    '3월' : 31
}
#print(f'문제1 : {obj_dict1}')

# 문제 : 딕셔너리에 각 달의 마지막 날들을 반복문을 통해 담기
obj_dict2 = {}
for i in range(1,13,1):
    if i == 2:
        obj_dict2.setdefault(str(i) + '월', '28일')
    elif i % 2 == 1:
        obj_dict2.setdefault(str(i) + '월', '31일')
    else:
        obj_dict2.setdefault(str(i) + '월', '30일')
#print(f'문제1 : {obj_dict2}')


print("== 예제 1 ==")
s = "안녕하세요."

#print("s길이 출력")
print(len(s))

#print("s를 이루는 문자 중에서 앞에꺼, 2개 출력")
print(s[0:2])

#print("s를 이루는 문자 중에서 앞에서 문자 하나 건너 뛰고 1개 출력")
print(s[1:2])

#print("s를 이루는 문자 중에서 앞에서 문자 4개 출력, 첫 인덱스 생략")
print(s[:4])

#print("s를 이루는 문자 중에서 앞에서 문자 3개 건너뛰고, 나머지 전부 출력, len")
print(s[3:])

#print("s를 이루는 문자 중에서 앞에서 문자 3개 건너뛰고, 나머지 전부 출력, 뒤 인덱스 생략, 방법 2")
# 구현

print("== 예제 2 ==")
s = "안녕하세요"

#print("s를 이루는 문자를 하나씩 출력, while")
for i in s:
    print(i)

#print("s를 이루는 문자를 역순으로 하나씩 출력, while")
for j in range(len(s)):
    print(s[len(s)- j - 1])
    
#print("s를 이루는 문자를 하나씩 출력, for")
# 구현

print("== 예제 3 ==")
s = "a안b녕c하d세e요f"

#print("s를 이루는 문자 중에서 한글만 출력")
pattern = re.compile('[ㄱ-ㅎ가-힣]+')
matches = pattern.findall(s)
result = ''.join(matches)
print(result)


#print("s를 이루는 문자 중에서 한글만 출력, for, if or, continue")
for text in result:
    print(text)

#print("s를 이루는 문자 중에서 한글만 출력, for, if and, 방법 2")
# 구현

#print("s를 이루는 문자 중에서 한글만 출력, for, not in, 방법 3")
# 구현