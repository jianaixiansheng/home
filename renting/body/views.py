from django.shortcuts import render,HttpResponse,redirect,reverse
from body.models import *
from django.http import  JsonResponse
from django.db.models import F, Q
from django.core.paginator import Paginator


# 首页
def search(request):
    # 判断是 GET 获取还是 POST 获取
    if request.method == "GET":
        return render(request, 'body/search.html')
    else:
        # 获取用户输入的城市或地区
        addr = request.POST.get('place')
        # 保存session
        request.session['addr'] = addr
        # 重定向 show_search 函数， 传参pid 返回到第一页
        return redirect(reverse('show_search', kwargs={"pid":1}))



# 用户搜索某地区展示 某地区的所有房子，每页9条数据。
def show_search(request,pid):
        #  获取 session
        place = request.session.get('addr')
        print(place)
        # 模糊查询
        area = house.objects.filter(house_addr=place)
        print('area==',area)
        # 每页9个数据
        limit = 9
        # 按每页9条分页
        paginator = Paginator(area, limit)
        # 用户点击所获得的的页数
        result = paginator.page(pid)
        return render(request, 'body/index.html', {"result":result, "area":area,'place':place})



def screen(request):
    # 获取用户输入的价格、宜居人数、床位
    price = request.POST.get('price')
    num = request.POST.get('num')
    bed = request.POST.get('bed')
    print('prcie==',price, 'num==', num , 'bed===', bed)
    # 将用户输入的数据 保存为 session
    request.session['price'] = price
    request.session['num'] = num
    request.session['bed'] = bed
    # 调用session 查看地区是否为北京
    place = request.session.get('addr')
    print('当前session对象', place)
    # 重定向 aid = 1 此处 aid 为页数
    return  redirect( reverse('show_screen', kwargs={'aid':1}))


def show_screen(request,aid):
    # 调用session
    money = request.session.get('price')
    hnum = request.session.get('num')
    hbed = request.session.get('bed')
    place = request.session.get('addr')
    print('钱', money,'宜居人数',hnum,'床位', hbed)
    # 判断是否 有钱 这个session 数据
    if money:
        check = house.objects.filter(house_price__lte=money, house_addr=place)
        limit = 9
        # 按每页9条分页
        paginator = Paginator(check, limit)
        # 用户点击所获得的的页数
        result = paginator.page(aid)
        return render(request, 'body/price.html', {'check':check, 'result':result})
    # 判断是否 有宜居人数 这个session 数据
    elif hnum:
        check = house.objects.filter(house_addr=place, house_num__gte=hnum)
        limit = 9
        # 按每页9条分页
        paginator = Paginator(check, limit)
        # 用户点击所获得的的页数
        result = paginator.page(aid)
        return render(request, 'body/price.html', {'check':check, 'result':result})
    # 判断是否 有床位 这个session 数据
    elif hbed:
        check = house.objects.filter(house_addr=place, house_bed__gte=hbed)
        limit = 9
        # 按每页9条分页
        paginator = Paginator(check, limit)
        # 用户点击所获得的的页数
        result = paginator.page(aid)
        return render(request, 'body/price.html', {'check': check, 'result': result})
    # 判断是否 有宜居人数、钱、床位 这个session 数据
    elif money and hbed and hnum:
        check = house.objects.filter(house_addr=place, house_bed__gte=hbed, house_num__gte=hnum, house_price__lte=money)
        limit = 9
        # 按每页9条分页
        paginator = Paginator(check, limit)
        # 用户点击所获得的的页数
        result = paginator.page(aid)
        return render(request, 'body/price.html', {'check': check, 'result': result})
    # 判断是否 有钱、床位 这个session 数据
    elif money and hbed :
        check = house.objects.filter(house_addr=place, house_price__lte=money, house_bed__gte=hbed)
        limit = 9
        # 按每页9条分页
        paginator = Paginator(check, limit)
        # 用户点击所获得的的页数
        result = paginator.page(aid)
        return render(request, 'body/price.html', {'check': check, 'result': result})
    # 判断是否 有宜居人数、钱 这个session 数据
    elif money and hnum:
        check = house.objects.filter(house_addr=place, house_price__lte=money, house_num__gte=hnum)
        limit = 9
        # 按每页9条分页
        paginator = Paginator(check, limit)
        # 用户点击所获得的的页数
        result = paginator.page(aid)
        return render(request, 'body/price.html', {'check': check, 'result': result})
    # 判断是否 有宜居人数、床位 这个session 数据
    elif hbed and hnum:
        check = house.objects.filter(house_addr=place, house_num__gte=hnum, house_bed__gte=hbed)
        limit = 9
        # 按每页9条分页
        paginator = Paginator(check, limit)
        # 用户点击所获得的的页数
        result = paginator.page(aid)
        return render(request, 'body/price.html', {'check': check, 'result': result})
    # 判断没有数据
    else:
        check = house.objects.filter(house_addr=place)
        limit = 9
        # 按每页9条分页
        paginator = Paginator(check, limit)
        # 用户点击所获得的的页数
        result = paginator.page(aid)
        return render(request, 'body/price.html', {'check': check, 'result': result})
