from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from body.models import *
from django.views.decorators.csrf import csrf_exempt
from PIL import Image, ImageDraw, ImageFont
from django.utils.six import BytesIO
from 阿里短信下发代码 import *


def register(request):
    """
    注册页面
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request,'login/register_1.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('pwd')

        user_tel = request.POST.get('user_tel')
        print('我是手机号',user_tel)
        yzm = request.POST.get('yzm')
        print('短信验证码',yzm)
        print('短信验证码',request.session['phone_code'])
        #检查两次输入的密码是否一致

        if yzm != request.session['phone_code']:
            return JsonResponse({'res':2})
        #检查手机号是否已经存在
        try:
            UserInfo.objects.get(user_tel=user_tel)
            return JsonResponse({'res':3})
        except:
            UserInfo.objects.create(user_name=username,user_pwd=password,user_tel=user_tel)
            return redirect('login')


def login(request):
    """
    登录功能
    :param request:
    :return:
    """
    if request.method == "GET":
        return render(request, "login/demo.html")
    else:
        user_name = request.POST.get("username")
        user_name = int(user_name)
        user_pwd = request.POST.get("password")
        print('登录的账户',user_name)
        print('登录的密码',user_pwd)
        try:
            g = UserInfo.objects.get(user_tel=user_name,user_pwd=user_pwd)
            if g:
                request.session['u_id'] = g.id
                return redirect('detail:index')
        except Exception:
            print(2)
            errmsg = '账号或密码错误'
            return render(request,'login/demo.html',{"errmsg":errmsg})


def index(request):
    """
    首页
    :param request:
    :return:
    """
    return HttpResponse("首页")


def generate_code(request):
    """
    生成图片验证码
    :param request:
    :return:
    """
    # 引入随机函数模块
    import random
    # 定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), 255)
    width = 100 # 验证码图片的宽度
    height = 25 # 验证码图片的高度
    # 创建画面对象
    im = Image.new('RGB', (width, height), bgcolor) # 实例化图片对象并指定宽高和背景颜色
    # 创建画笔对象
    draw = ImageDraw.Draw(im) # 基于im对象得到画笔对象
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        # (2,5)
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill) # 使用画笔画噪点并指定噪点的颜色

    # 定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    # 随机选取4个值作为验证码
    rand_str = ''
    # 得到四位验证码
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]

    # 构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
    font = ImageFont.truetype('login/FreeMono.ttf', 23)
    # 构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    del draw
    # 存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    # 内存文件操作
    buf = BytesIO()
    # 将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')


##############################################改动后#################################################################

@csrf_exempt
def login_ajax(request):
    """
    快捷登录页面
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request,'login/demo.html')
    else:
        user_tel = request.POST.get('user_tel')
        pic_coe = request.POST.get('code')
        yzm = request.POST.get('yzm')
        #判断验证码输入的是否正确
        yzm_session = request.session['verifycode']
        #判断用户名和密码是否正确
        if yzm != yzm_session:
            return JsonResponse({'res':2})
        if pic_coe != request.session['phone_code']:
            return JsonResponse({"res": 4})
        try:
            u = UserInfo.objects.get(user_tel=user_tel)
            if u:
                return JsonResponse({"res":1})
            else:
                return JsonResponse({"res":3})
        except:
            return JsonResponse({"res":0})


#登陆装饰器
# def login_required(views_function):
#     def wrapper(request,*args,**kwargs):
#         if request.session.has_key('islogin'):
#             #用户登陆
#             return views_function(request,*args,**kwargs)
#         else:
#             #用户未登录
#             return redirect('login')
#     return wrapper


# @login_required
@csrf_exempt
def find_pwd(request):
    """
    修改密码确认页面
    :param request:
    :return:
    """
    if not request.session.has_key('isLogin'):
        # return redirect('/login_app/login')

        return render(request, 'login/find_pwd.html')



def find_pwd_action(request):
    """密码修改"""
    if request.method == "GET":
        return render(request,'login/find_pwd.html')
    else:
        user_tel = request.POST.get('user_tel')
        pwd = request.POST.get('pwd')
        s_code = request.POST.get('s_code')
        yzm = request.session.get('phone_code')
        if all([user_tel, pwd, s_code]) and yzm == s_code:
            try:
                a = UserInfo.objects.get(user_tel=user_tel)
                if a:
                    a.user_pwd=pwd
                    a.save()
                    return redirect('login:login')
                else:
                    UserInfo.objects.create(user_tel=user_tel,user_pwd=pwd,user_name='高可爱')
                    return redirect('login:login')
            except:
                UserInfo.objects.create(user_tel=user_tel, user_pwd=pwd, user_name='高可爱')
                return redirect('login:login')
        else:
            return render(request, 'login/find_pwd.html',{"errmsg":'您的输入有误'})



# 获取手机验证码
@csrf_exempt
def get_phone_code(request):
    """
    获取手机验证码
    :param request:
    :return:
    """
    user_tel = request.POST.get('user_tel')  # 得到手机号码
    print('get_phone_code',user_tel)
    # 1.得到生成的验证码
    phone_code = get_code(alpha=False)
    print('phone_code_sys=' + phone_code) #  系统生成的验证码和手机生成的验证码
    request.session['phone_code'] = phone_code #  将得到的验证码存储在session中
    # 2.向指定手机号码发送验证码
    result = send_sms(user_tel, phone_code)
    print(type(result))  # str
    print(result)
    return HttpResponse(result)


def cancel(request):
    request.session.flush()
    return redirect('detail:index')


