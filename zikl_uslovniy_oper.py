#условный оператор в коде
#раннее прерывание
def chek_shop_is_openid(shop):
    if shop:
        return True

def chek_is_unit_in_shop(unit, shop):
    if shop and unit:
        return True

def chek_costumer_can_unit(unit, costumer):
    if unit and costumer:
        return True



shop = 'магазин 1'
unit = 'компьютер'
costumer = 'вася'

def make_purchase():
    if chek_shop_is_openid(shop):
        if chek_is_unit_in_shop(unit, shop):
            if chek_costumer_can_unit(unit, costumer):
                return 'успешно'
            else:
                raise Exception('нет денег')
        else:
            raise Exception('нет товара в магазе')
    else:
        raise Exception('магазин закрыт')

print(make_purchase())

'''можно упростить код операторами not функции прерываются или return или raise'''
def make_purchase1():
    if not chek_shop_is_openid(shop):
        raise Exception('магазин закрыт')

    if not chek_is_unit_in_shop(unit, shop):
        raise Exception('нет товара в магазе')

    if not chek_costumer_can_unit(unit, costumer):
        raise Exception('нет денег')

    return 'успешно '
print(make_purchase1())