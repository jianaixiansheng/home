from body.models import *
import os
from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.

# 展示首页

def index(request):
    return render(request, 'xiu/index.html')

# 添加发布房源信息
def house_info(request):
    if request.method == "GET":
        return render(request, 'xiu/house_info.html')
    else:
        # 地址
        house_addr = request.POST.get("house_addr")
        # 单价
        house_price = request.POST.get("house_price")
        # 房屋简介
        house_intro = request.POST.get("house_intro")
        # 户型
        house_type = request.POST.get("house_type")
        # 宜居人数
        house_num = request.POST.get("house_num")
        # 床铺数量
        house_bed = request.POST.get("house_bed")
        # 床铺规格
        house_bed_size = request.POST.get("house_bed_size")
        # 房屋描述
        house_describe = request.POST.get("house_describe")
        # 内部情况
        house_status = request.POST.get("house_status")
        # 交通情况
        house_traffic = request.POST.get("house_traffic")
        # 周边情况
        house_env = request.POST.get("house_env")
        # 配套设施
        house_set = request.POST.get("house_set")
        # 入住须知
        house_have_to = request.POST.get("house_have_to")
        # 押金
        house_cash = request.POST.get("house_cash")
        # 住房要求
        house_req = request.POST.get("house_req")
        # 预定方式
        house_way = request.POST.get("house_way")
        # 退订说明
        house_debook = request.POST.get("house_debook")
        # 外键
        # aid = UserInfo.objects.all()
        house_fk = UserInfo.objects.get(user_tel=18655170381)
        # 房子状态（是否出租,0为未出租，1为出租）
        house_or = request.POST.get("house_or")
        a = house.objects.create(house_addr=house_addr, house_price=house_price, house_intro=house_intro,house_type=house_type,house_num=house_num,house_bed=house_bed,house_bed_size=house_bed_size,house_describe=house_describe,house_status=house_status,house_traffic=house_traffic,house_env=house_env,house_set=house_set,house_have_to=house_have_to,house_cash=house_cash,house_req=house_req,house_way=house_way,house_debook=house_debook,house_fk=house_fk,house_or=house_or)
        if a:
            return redirect('already_house')
        else:
            return render(request, 'xiu/house_info.html')


# 查看已经发布房源信息的用户
def already_hose(request):
    already = house.objects.all()
    return render(request, 'xiu/already_house.html', {"already":already})

# 修改发布房源的用户信息
def modifier(request,c_id):
    if request.method == "GET":
        a = house.objects.get(id=c_id)
        return render(request, "xiu/modifier_house.html", {"a":a})
    else:
        a = house.objects.get(id=c_id)
        a.house_addr = request.POST.get("house_addr")
        a.house_price = request.POST.get("house_price")
        a.house_intro = request.POST.get("house_intro")
        a.house_type = request.POST.get("house_type")
        a.house_num = request.POST.get("house_num")
        a.house_bed = request.POST.get("house_bed")
        a.house_bed_size = request.POST.get("house_bed_size")
        a.house_describe = request.POST.get("house_describe")
        a.house_status = request.POST.get("house_status")
        a.house_traffic = request.POST.get("house_traffic")
        a.house_env = request.POST.get("house_env")
        a.house_set = request.POST.get("house_set")
        a.house_have_to = request.POST.get("house_have_to")
        a.house_cash = request.POST.get("house_cash")
        a.house_req = request.POST.get("house_req")
        a.house_way = request.POST.get("house_way")
        a.house_debook = request.POST.get("house_debook")
        a.house = request.POST.get("house")
        a.house_or = request.POST.get("house_or")
        a.save()
        return redirect("already_house")
