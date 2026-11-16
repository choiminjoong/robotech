


MENU = {"아메리카노": 4500, "라떼": 5000, "샌드위치": 6500}
BASE_FEE = 2000
BASE_KM = 2
EXTRA_FEE_PER_KM = 500
MAX_FEE = 5000


def order_total(items):
    total = 0
    for name in items:
        if name not in MENU:
            raise ValueError("없는 메뉴입니다: " + name)

        total += MENU[name]

    if count_menu(items) > 10:
        raise ValueError("메뉴는 최대 10개까지")


    print(f'\n총금액: {total}')
    if total >= 20000:
        total = total - total // 10

        print(f'\n할인된 금액: {total}')
    elif total >= 50000:
        total = total - total // 5    
    
    return total


def delivery_fee(distance_km):
    if distance_km < 0:
        raise ValueError("거리는 0 이상이어야 합니다")
    
    fee = BASE_FEE
    if distance_km <= 2:
        fee = BASE_FEE
    else: 
        fee = BASE_FEE + ((distance_km - BASE_KM) * EXTRA_FEE_PER_KM)

    if fee > MAX_FEE:
        fee = MAX_FEE

    return fee


def count_menu(menus):
    cnt = 0
    for menu in menus:
        cnt += 1
    
    return cnt