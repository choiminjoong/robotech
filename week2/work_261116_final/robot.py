# can_deliver 함수의 구현

# battery	출발 전 배터리 잔량. 0부터 100 사이의 퍼센트 숫자
# distance_km	가게에서 배달지까지의 편도 거리. 0 이상
# load_kg  짐 무게
# 배터리 소모	1km를 움직일 때마다 잔량이 5씩 줄어든다.
# 배달 경로	배달지까지 간 뒤 가게로 돌아온다.
# 반환값	돌아온 뒤 잔량이 20 이상이면 True, 20보다 작으면 False
# 짐이 10kg 이하면 1km마다 잔량이 5씩 줄어든다.
# 짐이 10kg을 넘으면 1km마다 잔량이 8씩 줄어든다.
# 왕복한 뒤 잔량이 20 이상이어야 한다는 규칙은 같다.

def can_deliver(battery, distance_km, load_kg=0):
    if not isinstance(battery, (int, float)) or isinstance(battery, bool):
        raise TypeError("배터리는 숫자여야 합니다.")
    if not isinstance(distance_km, (int, float)) or isinstance(distance_km, bool):
        raise TypeError("거리는 숫자여야 합니다.")
    if not (0 <= battery <= 100) :
        raise ValueError("배터리 수치 재확인")
    if not (0 <= distance_km) :
        raise ValueError("거리 재확인")
    if load_kg is not None:
        if not isinstance(load_kg, (int, float)) or isinstance(load_kg, bool):
            raise TypeError("무게는 숫자여야 합니다.")
        if not (0 <= load_kg) :
            raise ValueError("무게 재확인")
    else:
        load_kg = 0

    FUEL = 5
    if load_kg > 10: 
        FUEL = 8

    battery_num = battery - (2 * distance_km * FUEL) 
              
    if battery_num >= 20:
        return True
    elif battery_num <= 0:
        print('배터리 부족')
        return False
    else:
        return False