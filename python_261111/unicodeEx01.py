# ==========================================
# Python 유니코드 / 인코딩 핵심 정리
# ==========================================

# 1. 문자열은 컴퓨터 내부에서 숫자(유니코드)로 저장된다.
#  - 내부적으로는 각 글자를 숫자로 바꿔 저장한다.
#  - 그 숫자 체계를 유니코드(Unicode)라고 한다
text = "파이썬"

print(f'text = {text}')            # 문자열 출력
print(f'text길이: {len(text)}')       # 문자열 길이

# 2. 문자 ↔ 숫자 변환
print(f'text -> unicode: {ord("가")}')       # 문자를 유니코드 숫자로 변환
print(f'unicode -> text: {chr(44032)}')      # 숫자를 다시 문자로 변환


# 3. 문자열을 바이트로 변환 (encode)
# - encode : 문자열을 바이트(byte)로 바꾸는 작업
# 파일 저장이나 네트워크 전송 시 사용됨
encoded = text.encode("utf-8")
print(f'인코딩 결과: {encoded}') # b'...' 형태로 출력됨
print(f'인코딩후 타입: {type(encoded)}') # bytes 타입


# 4. 바이트를 다시 문자열로 변환 (decode)
decoded = encoded.decode("utf-8")
print(f'디코딩 결과: {decoded}')
print(f'디코딩후 타입: {type(decoded)}') # str 타입


# 5. 인코딩이 맞지 않으면 오류 발생
try:
    wrong = encoded.decode("cp949")
    print(wrong)
except UnicodeDecodeError:
    print("인코딩 방식이 맞지 않아 오류 발생")



# ==========================================
# 정리
# - 유니코드는 문자를 숫자로 표현하는 방식
# - encode(): 문자열 → 바이트
# - decode(): 바이트 → 문자열
# - 파일 읽을 때 encoding 옵션이 중요
# ==========================================