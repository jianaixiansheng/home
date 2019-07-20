from django.shortcuts import render,HttpResponse,reverse,redirect
from body.models import *
import datetime
from django.http import JsonResponse
# Create your views here.

def login(request):
    if request.method == "GET":
        return render(request,'order/login.html')
    else:
        name = request.POST.get('tel')
        pwd = request.POST.get('pwd')
        try:
            a = UserInfo.objects.get(user_tel=name,user_pwd=pwd)
            if a:
                request.session['u_id']=a.id
                return redirect(reverse('detail:index'))
            else:
                return HttpResponse('失败')
        except:
            return HttpResponse('lalala失败')
def register(request):
    if request.method == "GET":
        return render(request,'order/register.html')
    else:
        tel = request.POST.get('tel')
        tel = int(tel)
        pwd = request.POST.get('pwd')
        name = request.POST.get('name')
        print(tel,pwd,name)
        print(type(tel),type(pwd),type(name))
        UserInfo.objects.create(user_tel=tel,user_pwd=pwd,user_name=name)
        return redirect(reverse('order:login'))

def detail(request):
    user_id = request.session.get('u_id')
    if user_id:
        det = house.objects.filter(house_or=0)

        return render(request,'order/detail.html',{"a":det})
    else:
        return redirect('order:login')

def ding_info(request,house_id):
    """用户订单住房的页面"""
    user_id = request.session.get('u_id')
    if user_id:
        # 获取到当前用户
        user = UserInfo.objects.get(id=user_id)
        if user.user_id_card:
            request.session['house_id']=house_id #将用户选择的房子的ID进行保存
            user =request.session.get('u_id') # 获取到当前登陆用户的ID
            info = UserInfo.objects.get(id=user) # 通过用户ID获取到用户的信息，进行传递，也就是预定人的信息
            house_name = house.objects.get(id=house_id) # 获取到房子的名称
            request.session['house_price']=house_name.house_price # 将房子的单价进行保存
            return render(request,'order/order_info.html',{"i":info,"housename":house_name})
        else:
            return HttpResponse('请进行实名认证')
    else:
        return redirect('order:login')
def ding(request):
    user_id = request.session.get('u_id')
    if user_id:
        user = request.session.get('u_id') #获取到当前登陆用户
        a = Order()
        ernter = request.POST.get('enter') # 获取入住日期
        leavel = request.POST.get('level') # 获取离开日期
        reallyname = request.POST.get('reallyname') # 获取真实姓名
        idcard = request.POST.get('idcard') # 获取身份证号码
        tel = request.POST.get('tel') # 获取电话号码
        remark = request.POST.get('remark') # 获取订单备注
        ernter = ernter+" "
        print('我是入住时间',ernter)
        leavel = leavel+" "
        print("我是离开时间",leavel)
        d1 = datetime.datetime.strptime(leavel, '%Y-%m-%d ')
        d2 = datetime.datetime.strptime(ernter, '%Y-%m-%d ')
        d3 = d1-d2
        print(ernter,leavel,d3.days)
        # 将获取到的信息存入数据库中
        # 将离开日期和入住日期进行保存
        price = request.session.get('house_price')
        a.order_enter_date = d2
        a.order_leave_date = d1
        a.order_remark = remark
        # 将房屋标记为已经出租
        h_id = request.session.get('house_id')
        status = house.objects.get(id=h_id)
        status.house_or = 1
        status.save()
        # 填写订单表中的信息
        a.order_fk_house_id=h_id
        a.order_fk_user_id=user
        a.order_price =d3.days*price+status.house_cash
        a.save()
        # 将入住人的信息进行保存
        b = men()
        b.men_name=reallyname
        b.men_ID_card=idcard
        b.men_tel=int(tel)
        b.men_fk_id=user
        b.men_fk_house_id = h_id
        b.men_fk_order_id = a.id
        b.save()
        return redirect('order:my_ord')
    else:
        return redirect('order:login')

# 订单页面（我的订单）
def my_ord(request):
    """
    当用户提交订单之后跳转到此页面，也就是订单页面，要显示：
    预定的房间名称，(有了)
    预定人的信息(有了)
    入住人的信息(有了)
    总价 (有了)
    入住时间 (有了)
    离开时间 (有了)
    订单状态（待支付和支付成功）（有了）
    订单提交时间
    :param request:
    :return: 返回订单页面
    """
    # 先获取到当前登陆用户的ID
    uid = request.session.get('u_id')
    uname = UserInfo.objects.get(id=uid)
    # 去订单中获取未取消的订单
    cancel = Order.objects.filter(order_fk_user=uid, order_status__in=[0,1])

    info = []

    for i in cancel:  # 订单信息
        # print(i.id)
        one = []
        b = men.objects.get(men_fk_order=i.id)  # 入住人
        h = house.objects.get(id=b.men_fk_house_id)
        one.append(i.can())
        one.append(i.order_sure_time)
        one.append(i.order_price)
        one.append(i.order_leave_date)
        one.append(i.order_enter_date)

        one.append(b.men_name)
        one.append(b.men_tel)
        one.append(h.house_addr)
        one.append(i.id)
        info.append(one)




    return render(request,'order/my_ord.html',{"hname":info,"uname":uname})






def my_ord_can(request):
    """
    当用户提交订单之后跳转到此页面，也就是订单页面，要显示：
    预定的房间名称，(有了)
    预定人的信息(有了)
    入住人的信息(有了)
    总价 (有了)
    入住时间 (有了)
    离开时间 (有了)
    订单状态（待支付和支付成功）（有了）
    订单提交时间
    :param request:
    :return: 返回订单页面
    """
    # 先获取到当前登陆用户的ID
    uid = request.session.get('u_id')
    uname = UserInfo.objects.get(id=uid)
    # 去订单中获取已经取消的订单
    cancel = Order.objects.filter(order_fk_user=uid,order_status__in=[2,3])
    print('我是取消的',cancel)
    info = []

    for i in cancel: # 订单信息
        one = []
        b=men.objects.get(men_fk_order=i.id) # 入住人
        h = house.objects.get(id=b.men_fk_house_id)

        one.append(i.can())
        one.append(i.order_sure_time)
        one.append(i.order_price)
        one.append(i.order_leave_date)
        one.append(i.order_enter_date)


        one.append(b.men_name)
        one.append(b.men_tel)
        one.append(h.house_addr)
        info.append(one)
    return render(request, 'order/cancel.html', {"a":info, "c":uname})



#  支付成功后返回的界面

def ord_end(request):
    """
    用来完成订单结束页面
    当用户支付成功后
    :param request:
    :return:
    """
    oid = request.POST.get('oid')
    print('ajax',oid)
    a = Order.objects.get(id=oid)
    print(999)
    hid = a.order_fk_house_id
    b = house.objects.get(id=hid)
    print(11212121)
    b.house_or = 0
    b.save()
    a.order_status = 1
    a.save()

    if oid:

        return JsonResponse({"res":1})
    else:
        return JsonResponse({"res": 0})

#  取消功能
def cel(request):
    oid = request.POST.get('oid')
    print('ajax', oid)
    a = Order.objects.get(id=oid)
    print(999)
    hid = a.order_fk_house_id
    b = house.objects.get(id=hid)
    print(11212121)
    b.house_or = 0
    b.save()
    a.order_status = 2
    a.save()
    print('我是取消功能的ID',a)
    if a:
        return JsonResponse({"res":0})
    else:
        return JsonResponse({"res":1})




# 订单页面（我的房租订单）