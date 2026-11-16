from order import order_total


def test_small_order_has_no_discount():
    assert order_total(["아메리카노", "라떼"]) == 9500


def test_big_order_gets_discount():
    assert order_total(["샌드위치", "샌드위치", "샌드위치", "라떼"]) == 22050


def test_exactly_20000_gets_discount():
    assert order_total(["라떼", "라떼", "라떼", "라떼"]) == 18000


def test_exactly_50000_gets_discount():
    assert order_total(["라떼"] * 10) == 40000


def test_empty_order_is_zero():
    assert order_total([]) == 0


def test_count_menu():
    assert order_total(["라떼"]*10)
