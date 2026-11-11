# openpyxl
#   파이썬에서 엑셀 파일을 읽고 쓰기 위한 라이브러리

# pip
#   파이썬 패키지를 설치하고 관리하는 패키지 관리자(Package Manager)

'''
# 설치가 안될 시
import sys
# 파이썬이 설치된 경로 추출
print(sys.executable)
# 터미널 : 추출한 경로 -m pip install 외부라이브러리이름
'''

import sys
import openpyxl

print(f'파이썬 실행 파일 경로 {sys.executable}')
print(f'openpyxl 버전: {openpyxl.__version__}')

