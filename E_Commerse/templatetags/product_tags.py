from django import template
register = template.Library()

@register.simple_tag
def cal_sellprice(price, Discount):
    if Discount is None or Discount is 0:
        return price
    sell_price = price
    sell_price = price - (price*Discount/100)
    return sell_price
