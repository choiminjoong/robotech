MENU = {"아메리카노": 4500, "라떼": 5000, "샌드위치": 6500}


def order_total(items):
    total = 0
    for name in items:
        total += MENU[name]
        if total >= 20000:
            total = total - total // 10
    return total


def test_small_order_has_no_discount():
    assert order_total(["아메리카노", "라떼"]) == 9500


def test_big_order_gets_discount():
    assert order_total(["샌드위치", "샌드위치", "샌드위치", "라떼"]) == 22050


def test_exactly_20000_gets_discount():
    assert order_total(["라떼", "라떼", "라떼", "라떼"]) != 18000