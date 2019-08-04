import os
from django.shortcuts import render,redirect,reverse
from django.http import request,HttpResponse
from .models import *
from renting import settings
from poll.aijiekou import lists2,savevalues

def uploadPic(request):
    # 初始化将要返回的数据
    obj = dict()
    if request.method == 'GET':
        return render(request,"index180.html")
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
                    fname = file.name
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
                a = savevalues()
                lists2()
                if a[3] == '':
                    return HttpResponse("上传失败1")
                else:
                    return redirect('house_info')
            except Exception as e:
                obj['error'] = e
                return HttpResponse("上传失败2")
