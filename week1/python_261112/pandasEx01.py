import pandas as pd


# pandas : 파이썬에서 데이터 분석과 데이터 처리를 위한 대표적인 라이브러리
# 주로 표 형태의 데이터(엑셀, CSV, 데이터베이스 등)를 다루는 데 사용
# 데이터 과학, 머신러닝, 금융 분석, 통계 처리 등에서 매우 많이 사용 됨
'''
DataFrame : 여러 개의 열(Colum)로 구성된 '표'형태의 데이터
 - '열 이름': [값들]
 - 각 열에는 열 이름이 있음
 - 각 행에는 자동으로 행 번호(index)가 붙음
'''

df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)

print(f'\n*** pd.DataFrame: \n{df}')
print(f'\n*** df["Age"]: \n{df["Age"]}')
print(f'\n*** df["Age"].max(): \n{df["Age"].max()}')
print(f'\n*** df["Age"].min(): \n{df["Age"].min()}')

# describe: 숫자형 열 요약, 통계 정보
print(f'\n*** df.describe(): \n{df.describe()}')

# info: 구조 정보
print(f'\n*** df.info(): \n{df.info()}')

# iloc(): index로 접근
# loc(): index 라벨로 접근
print(f'\n*** df.iloc[0]: \n{df.iloc[0]}')
print(f'\n*** df.loc[0]: \n{df.loc[0]}')

# head(): 상위 5개(기본값)
# tail(): 하위 5개(기본값)
print(f'\n*** df.head(2): \n{df.head(2)}')
print(f'\n*** df.tail(2): \n{df.tail(2)}')

# 새로운 열 추가
df['Survived'] = [0,1,1]
print(f'\n*** 열추가 후 df: \n{df}')

# 열 이름 변경
df = df.rename(columns={'Sex' : 'Gender'})
print(f'\n*** 열 이름 변경 후 df: \n{df}')

# 열 삭제
df = df.drop('Survived', axis=1)
print(f'\n*** 열 삭제 후 df: \n{df}')

# 결측치 처리
print(f'\n*** df.isnull(): \n{df.isnull()}')

df.loc[1, 'Age'] = None
print(f'\n*** df.loc[1, Age] = None: \n{df.isnull()}')
# 결측치 지우기
#print(f'\n*** df.dropna(axis=0): \n{df.dropna(axis=0)}')
# 결측치 채우기
#print(f'\n*** df.fillna(0): \n{df.fillna(0)}')
# 결측치를 평균 값으로 채우기
#print(f'\n*** df[Age].fillna(df[Age].mean): \n{df["Age"].fillna(df["Age"].mean)}')
#채우기 이전 행
#print(f'\n*** df.ffill(): \n{df.ffill()}')
#채우기 다음 행
#print(f'\n*** df.bfill(): \n{df.bfill()}')