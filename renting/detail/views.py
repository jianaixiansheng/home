from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.shortcuts import render,redirect,reverse,HttpResponse
from django.http import JsonResponse
from body.models import *

# Create your views here.

#房屋首页
def index(request):
    home = house.objects.filter(house_or=0)
    return render(request,'detail/index.html',{"home":home})


#登陆
def login(request):
    if request.method == 'GET':
        return render(request,'detail/login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get("password")
        # 检查是否输入数据
        if not all([username, password]):
            return render(request, 'detail/login.html', {"errmsg": "数据不完整"})
        # 检查账户名和密码是否匹配
        try:
            a = UserInfo.objects.get(user_name=username, user_pwd=password)
        except:
            return render(request, 'detail/login.html', {"errmsg": "用户名或密码错误"})
        else:
            request.session['u_id'] = a.id
            # print("haha", request.session['u_id'])
            return redirect('index')




#房屋详情
def home_detail(request,hid):
    """
    展示房屋的详细信息
    :param request: 用户发送请求
    :param hid: 点击的房屋的id
    :return: 返回用户所点击的房屋的详细信息
    """
    u_id = request.session.get("u_id")
    if u_id:
        u = UserInfo.objects.get(id=u_id)
        home_info = house.objects.get(id=hid)
        pic = Photo.objects.filter(image_fk_id=hid)
        comment = Comment.objects.filter(comment_fk_house_id=hid,comment_connent__isnull=False)
        # #分页
        # paginator = Paginator(comment,5)
        # #获取第n页的内容
        # if pindex =='':
        #     pindex = 1
        # else:
        #     pindex = pindex
        # page = paginator.page(pindex)
        return render(request,'detail/detail.html',{"home_info":home_info,"pic":pic,"comment":comment,"u":u})
    else:
        home_info = house.objects.get(id=hid)
        pic = Photo.objects.filter(image_fk_id=hid)
        comment = Comment.objects.filter(comment_fk_house_id=hid,comment_connent__isnull=False)
        return render(request,'detail/detail.html',{"home_info":home_info,"pic":pic,"comment":comment})

#订单页面
def order(request):
    """
    从详情页跳到订单页，如果用户处于登陆状态，则正常跳转
    如果用户处于未登录状态，当用户点击去订房的时候，提醒用户
    进行登陆，并自动跳转至登陆页面
    :param request: 用户发送请求
    :return: 用户登陆，返回订单页，未登录，返回登录页
    """
    u_id = request.session.get("u_id")
    if u_id:
        u = UserInfo.objects.get(id=u_id)
        return render(request,'detail/order.html',{"u":u})
    else:
        return render(request,'detail/jump.html')

#评论
def comment(request,hid):
    """
    用户评论功能，如果用户是登陆状态，则判断用户是否以完成关于此房屋的订单
    如果用户不是登陆状态，则提示用户先进行登陆，并跳转到登陆页面
    :param request:
    :return:
    """
    u_id = request.session.get("u_id")
    if request.method == "GET":
        if u_id:
            u = UserInfo.objects.get(id=u_id)
            a = house.objects.get(id=hid)
            home_info = house.objects.get(id=hid)
            pic = Photo.objects.filter(image_fk_id=hid)
            return render(request,'detail/comment.html',{"u":u,'a':a,'home_info':home_info,'pic':pic})
        else:
            return render(request,'detail/jump.html')
    else:
        comm = request.POST.get("comm")
        print("我是房客的评价",comm)
        comm2 = request.POST.get("h_connect")
        print("我是房东回复的评论",comm2)
        home = house.objects.get(id=hid)
        print("我是获取到的评论",comm)
        #对获取到的内容进行判断
        if not all([comm]):
            return render(request,'detail/comment.html',{"errmsg":"评论内容不能为空"})
        # 对评论内容进行保存
        Comment.objects.create(comment_connent=comm,comment_fk_user_id=u_id,comment_fk_house_id=home.id)
        return redirect(reverse('detail:index'))


@csrf_exempt
def reply_comment(request,hid):
    u_id = request.POST.get('userid')
    print('我是你用户的id',u_id)
    if request.method =='GET':
        u = UserInfo.objects.get(id=u_id)
        home = house.objects.get(id=hid)
        print("我是房子的id", home.id)
        home_id = request.session['home.id']
        # print(a)
        return render(request,'detail/detail.html',{"u":u,'home':home_id})
@csrf_exempt
def replay_comment_1(request):
    comm2 = request.POST.get('comm')
    print('我是房东回复的评论',comm2)
    comm3 = request.POST.get('commentid')
    print("我是被回复的评论的id",comm3)
    home = request.POST.get('home_id')
    print("我是房子的id",home)
    u_id = request.POST.get('userid')
    print('我是用户的id',u_id)
    a = Comment.objects.get(id=comm3,comment_fk_house_id=home,comment_fk_user_id=u_id)
    a.comment_reply =comm2
    a.save()
    if comm2:
        return JsonResponse({"res":1})
    else:
        return JsonResponse({"res": 0})














