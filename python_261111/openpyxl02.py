import os
from openpyxl import *
#import PatternFill

# 시트생성
path = './test.xlsx'
if os.path.exists(path):
    wb = load_workbook(path)
    print('파일 확인')
else:
    print('파일 없음')
    wb = Workbook()  

ws = wb.active
ws['A1'] = '이름'
ws['B1'] = '국어'
ws['C1'] = '수학'

# scolor = PatternFill(fill_type='solid', fgColor='FFFF00')

# for cell in ws[1]:
#     cell.fill = scolor

wb.save(path)    