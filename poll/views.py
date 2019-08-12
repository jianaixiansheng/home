import os
from django.shortcuts import render,redirect,reverse
from django.http import request,HttpResponse
from .models import *
from renting import settings
from poll.aijiekou import lists2,savevalues



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


@login_check
def uploadPic(request):
    # 初始化将要返回的数据
    obj = dict()
    if request.method == 'GET':
        return render(request, 'xiu/index180.html')
    else:
        files = request.FILES.getlist('banners') # input 标签中的name值
        # print(files)
        # print(type(files))
        if not files:
            obj['error'] = '没有上传的文件'
            return HttpResponse(obj)
        else:
            dirs = settings.MEDIA_ROOT + 'img/'
            folder = os.path.exists(dirs)
            if not folder:#判断是否存在文件夹如果不存在则创建为文件夹
                os.makedirs(dirs)#makedirs 创建文件时如果路径不存在会创建这个路径
            try:
                for file in files:
                #   t = time.time()     #PS：注释中的是上传文件中的另一种方法哦。各自选用
                #     fname = file.name
                    # print(fname)
                #   suffix = os.path.splitext(file.name)[1]
                #   path = dirs + 'banner' + str(int(round(t * 1000))) + suffix #毫秒级时间戳
                #   f = open(path,'wb')
                #   for line in file.chunks():
                #       f.write(line)
                #   f.close()
                    img = Banner(img=file)
                    img.save()
                    # savevalues()
                # try:
                a = savevalues()
                # print(a)
                banner = infomation.objects.values_list('IDcard',flat=True)

                print(banner, 'taonihouzi111')
                if a[3] in banner:
                    return render(request, 'xiu/index180.html', {'error': '该身份证已经注册过了'})
                else:
                    if a[3] == '':
                        return render(request, 'xiu/index180.html', {'error': '身份证识别错误请重新上传'})
                    else:
                        return render(request, 'xiu/house_info.html')
                # except:
                #     print('123')

                # return HttpResponse('123')
            except Exception as e:
                obj['error'] = e
                return render(request, 'xiu/index180.html', {'error': '身份证识别错误请重新上传'})
