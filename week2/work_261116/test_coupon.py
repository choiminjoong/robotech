import pytest

from order import apply_coupon, best_coupon_price


def test_welcome_takes_off_3000():
    assert apply_coupon(10000, "WELCOME") == 7000


def test_half_takes_off_half():
    assert apply_coupon(8000, "HALF") == 4000


def test_half_discount_is_at_most_5000():
    assert apply_coupon(30000, "HALF") == 25000


def test_price_never_goes_below_zero():
    assert apply_coupon(2000, "WELCOME") == 0


def test_unknown_code_raises_error():
    with pytest.raises(ValueError):
        apply_coupon(10000, "FREE")

def test_only_one_coupon_is_used():
    assert best_coupon_price(10000, ["WELCOME", "HALF"]) == 5000


def test_half_coupon_keeps_its_cap():
    assert best_coupon_price(30000, ["WELCOME", "HALF"]) == 25000


def test_welcome_can_be_better():
    assert best_coupon_price(4000, ["WELCOME", "HALF"]) == 1000


def test_price_can_be_zero():
    assert best_coupon_price(2000, ["WELCOME", "HALF"]) == 0


def test_empty_candidates_keep_original_price():
    assert best_coupon_price(10000, []) == 10000


def test_lowercase_coupon_is_allowed():
    assert best_coupon_price(10000, ["welcome"]) == 7000


def test_candidate_order_does_not_change_price():
    assert best_coupon_price(10000, ["WELCOME", "HALF"]) == 5000
    assert best_coupon_price(10000, ["HALF", "WELCOME"]) == 5000


def test_unknown_coupon_is_checked_even_after_zero():
    with pytest.raises(ValueError):
        best_coupon_price(2000, ["WELCOME", "FREE"])

