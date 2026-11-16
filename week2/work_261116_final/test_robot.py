from robot import can_deliver

# 입력과 기댓값을 assert로 확인하는 테스트. 먼저 작성한다.
def test_enough_battery():
    assert can_deliver(100, 1) == True

def test_not_enough_battery():
    assert can_deliver(20, 10) == False

def test_20_battery():
    assert can_deliver(50, 3) == True

def test_19_battery():
    assert can_deliver(49, 3) == False

def test_0km_distance1():
    assert can_deliver(20, 0) == True

def test_0km_distance2():
    assert can_deliver(19, 0) == False

def test_10kg_load():
    assert can_deliver(50, 3, 10) == True

def test_11kg_load():
    assert can_deliver(50, 3, 11) == False