from django.template import Library

register = Library()
@register.filter
def mod(s):
    print('我是过滤器')
    print(s)
    pay = []
    for i in s:
        if i[6] == '支付成功' and i[7] == i[8]:
            pay.append(i)
    return pay
