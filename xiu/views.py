from body.models import *
import os
from django.shortcuts import render, redirect,reverse
from django.core.paginator import Paginator
from django.db.models import Q,F
from django.http import HttpResponse
from renting import settings
# Create your views here.

# 展示首页

def login_check(view_func):
    def warpper(request,*args,**kwargs):
        try:
            u_id = request.session['u_id']
            if u_id:
                return view_func(request,*args,**kwargs)
            else:
                return redirect('login:login')
        except:
            return redirect('login:login')
    return warpper

def index(request):
    try:
        u_id = request.session['u_id']
        name = UserInfo.objects.get(id=u_id)

        return render(request, 'xiu/index.html', {"qt":name})
    except:
        name = ''
        return render(request, 'xiu/index.html', {"qt": name})
# 添加发布房源信息


@login_check
def house_info(request):
    if request.method == "GET":
        return render(request, 'xiu/house_info.html')
    else:
        # try:
            a = house()
            # 地址
            a.house_addr = request.POST.get("house_addr")
            # 单价
            a.house_price = request.POST.get("house_price")
            # 房屋简介
            a.house_intro = request.POST.get("house_intro")
            # 户型
            a.house_type = request.POST.get("house_type")
            # 宜居人数
            a.house_num = request.POST.get("house_num")
            # 床铺数量
            a.house_bed = request.POST.get("house_bed")
            # 床铺规格
            a.house_bed_size = request.POST.get("house_bed_size")
            # 房屋描述
            a.house_describe = request.POST.get("house_describe")
            # 内部情况
            a.house_status = request.POST.get("house_status")
            # 交通情况
            a.house_traffic = request.POST.get("house_traffic")
            # 周边情况
            a.house_env = request.POST.get("house_env")
            # 配套设施
            a.house_set = request.POST.get("house_set")
            # 入住须知
            a.house_have_to = request.POST.get("house_have_to")
            # 押金
            a.house_cash = request.POST.get("house_cash")
            # 住房要求
            a.house_req = request.POST.get("house_req")
            # 预定方式
            a.house_way = request.POST.get("house_way")
            # 退订说明
            a.house_debook = request.POST.get("house_debook")
            # 外键
            u_id = request.session['u_id']
            a.house_fk = UserInfo.objects.get(id=u_id)
            # 房子状态（是否出租,0为未出租，1为出租）
            a.house_or = 0
            a.save()
            # 上传图片
            # Image = Photo.objects.get("Image")
            obj = dict()
            files = request.FILES.getlist('Image')  # input 标签中的name值
            # print(files)
            # print(type(files))
            if not files:
                obj['error2'] = '没有上传的文件'
                return HttpResponse(obj)
            else:
                dirs = settings.MEDIA_ROOT + 'images/'
                folder = os.path.exists(dirs)
                if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
                    os.makedirs(dirs)  # makedirs 创建文件时如果路径不存在会创建这个路径
                # try:
                u_id = request.session["u_id"]
                print(u_id)
                for file in files:
                    img = Photo(Image=file, image_fk_id=a.id)
                    img.save()
                    a.pic_fk_id = img.id
                    a.save()

                    print(file)
                # except Exception as e:
                #     obj['error1'] = e
                #     return HttpResponse('上传成功!')

            # a = house.objects.create(house_addr=house_addr, house_price=house_price, house_intro=house_intro,house_type=house_type,house_num=house_num,house_bed=house_bed,house_bed_size=house_bed_size,house_describe=house_describe,house_status=house_status,house_traffic=house_traffic,house_env=house_env,house_set=house_set,house_have_to=house_have_to,house_cash=house_cash,house_req=house_req,house_way=house_way,house_debook=house_debook,house_fk=house_fk,house_or=house_or)

            return redirect(reverse('xiu:already_house',kwargs={'pindex':'pindex'}))
        # except:
        #     return render(request, 'xiu/house_info.html')


# 查看已经发布房源信息的用户
def already_house(request,pindex):
    u_id = request.session["u_id"]
    already = house.objects.filter(Q(house_fk_id=u_id))
    # b = Photo.objects.order_by([-1])
    paginator = Paginator(already, 5)
    if pindex == '':
        pindex = 1
    else:
        pindex = int(pindex)
    page = paginator.page(pindex)

    return render(request, 'xiu/already_house.html', {"page": page})





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
        a.house = request.POST.get("house_fk")
        a.house_or = request.POST.get("house_or")
        a.save()
        return redirect(reverse('xiu:already_house',kwargs={'pindex':'pindex'}))
        # return redirect("xiu:already_house")


def img1(request):
    return render(request,'xiu/img1.html')

def img2(request):
    return render(request,'xiu/img2.html')

def img3(request):
    return render(request,'xiu/img3.html')

def img4(request):
    return render(request,'xiu/img4.html')

def img5(request):
    return render(request,'xiu/img5.html')

def img6(request):
    return render(request,'xiu/img6.html')

def img7(request):
    return render(request,'xiu/img7.html')

def img8(request):
    return render(request,'xiu/img8.html')
# 三个协议
def landlord_rule(request):
    return render(request,'xiu/landlord_rule.html')

def Service_rules(request):
    return render(request,'xiu/Service rules.html')

def service_contract(request):
    return render(request,'xiu/service_contract.html')