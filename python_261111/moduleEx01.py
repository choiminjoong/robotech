# 모듈과 패키지

# 모듈(Module)
#   변수, 함수, 클래스 등을 모아서 파일로 저장해 둔 것
# 패키지(Package)
#   여러 개의 모듈을 폴더로 묶어 체계적으로 관리하는 것
#   관련된 기능들을 하나의 디렉터리 구조로 구성한 것
#   대규모 프로그램에서 코드 관리와 구조화를 위해 사용하는 단위
# 라이브러리
#   여러 개의 모듈을 묶어 특정 기능을 제공하는 패키지 집합

import math

print(math.sqrt(16)) # 16 제곱근 계산

import random

# 1~100 랜덤숫자
print(f'랜덤숫자1: {random.randint(1,100)}')
print(f'랜덤숫자2: {random.randint(1,100)}')
print(f'랜덤숫자3: {random.randint(1,100)}')

# 직접 생성한 모듈 불러오기
import md01
# from md01 import test

md01.test()

import datetime

# 현재 날짜와 시간을 출력
print(datetime.datetime.now())

# 시간 제어 모듈
import time

#time.sleep(3) # 프로그램을 n초 멈춤
print('n초 후 실행')

# 시스템 모듈
import sys

print(sys.version) # 현재 사용중인 파이썬 버전 출력

#운영체제 모듈
import os
print(os.getcwd())

# 데이터 형식 모듈
# JSON형식으로 데이터 변환
# 웹, API 저장에 사용
import json
data = {
    'name': 'cmj',
    'age': 33
}
print(json.dumps(data))

# 정규 표현식 모듈
# 문자열 패턴 검사 모듈
import re

# 문자열이 **으로 시작하는지 확인
print(bool(re.match('hi', 'hi python')))

# CSV 파일 모듈(엑셀)
import csv

# with open('test.csv','w', newline='') as f:
#    csv.writer(f).writerow(['name','score'])

# 자료구조 모듈
# 카운트, 큐, 딕셔너리, 확장 기능 제공
from collections import Counter

# 문자열에서 각 개수를 카운트
print(Counter('asfsdfsf'))