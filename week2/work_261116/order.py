

MENU = {"아메리카노": 4500, "라떼": 5000, "샌드위치": 6500}


def order_total(items):
    total = 0
    for name in items:
        total += MENU[name]

    print(f'\n총금액: {total}')
    if total >= 10000:
        total = round(total * 0.9)
        print(f'\n할인된 금액: {total}')
    
    return total


print(order_total(["아메리카노", "라떼"]))
print(order_total(["샌드위치", "샌드위치", "라떼"]))