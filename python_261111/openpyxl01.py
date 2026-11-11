import os
from openpyxl import *

# 시트생성
if os.path.exists('./test.xlsx'):
    wb = load_workbook('./test.xlsx')
    print('파일 확인')
else:
    print('파일 없음')
    wb = Workbook()  

new_wsname = wb.sheetnames[-1][-1]
if new_wsname == 't':
    new_ws= wb.create_sheet("Sheet2")
else:
    sn = int(new_wsname) + 1
    new_ws= wb.create_sheet("Sheet" + str(sn))

print(wb.sheetnames)
wb.save('test.xlsx')