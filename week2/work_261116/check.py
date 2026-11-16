from order import order_total

assert order_total(["아메리카노", "라떼"]) == 9500
assert order_total(["샌드위치", "샌드위치", "샌드위치", "라떼"]) == 22050
assert order_total(["라떼", "라떼", "라떼", "라떼"]) >= 18000
print("전부 통과")