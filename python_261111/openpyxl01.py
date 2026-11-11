import os
from openpyxl import *

# 파일생성
path = './python_261111/test.xlsx'
if os.path.exists(path):
    wb = load_workbook(path)
    print('파일 확인')
else:
    print('파일 없음')
    wb = Workbook()  

# 시트생성
print(f'시트생성 이전: {wb.sheetnames}')
new_wsname = wb.sheetnames[-1][-1]
if new_wsname == 't':
    new_ws= wb.create_sheet("Sheet2")
else:
    sn = int(new_wsname) + 1
    new_ws= wb.create_sheet("Sheet" + str(sn))

print(f'시트생성 이후: {wb.sheetnames}')
wb.save(path)