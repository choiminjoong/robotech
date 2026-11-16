from order import delivery_fee


def test_zero_distance_has_base_fee():
    assert delivery_fee(1) == 2000


def test_two_km_has_base_fee():
    assert delivery_fee(2) == 2000


def test_three_km_adds_one_extra_km():
    assert delivery_fee(3) == 2500


def test_seven_km_is_below_cap():
    assert delivery_fee(7) == 4500


def test_eight_km_reaches_cap():
    assert delivery_fee(8) == 5000


def test_nine_km_cannot_exceed_cap():
    assert delivery_fee(8) == 5000