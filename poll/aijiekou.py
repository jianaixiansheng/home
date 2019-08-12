# -*- coding: UTF-8 -*-
from aip import AipOcr
from poll import views
import os
from poll.models import *
from poll.views import *
import copy



def lists1():

    lists = Banner.objects.all().order_by('-id')[:2]
    return lists




def lists2():

    t = lists1()
    # print('taonihouzi',t)
    a = []
    for i in t:
        # print(i.img)
        a.append(i.img)
        print(a)
    return a

# print('taonihouzi2',a[0])


# # 定义常量
APP_ID = '16796024'
API_KEY = 'opgNilbVsBwaVrTG6m4Xks7a'
SECRET_KEY = 'FA3OynwWo0x6lIvmd65pknsSyB2zhX10'
# # 初始化AipFace对象
aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def savevalues():
    # a = poll1(1)
    # result1=a[0]
    # result2=a[1]
    identity_information_list = []
    options = {}

    options["detect_direction"] = "true"  # 检测朝向
    options["detect_risk"] = "true"
    # 是否开启身份证风险类型(身份证复印件、临时身份证、身份证翻拍、修改过的身份证)功能，默认不开启
    filePath1 = "C:/Users/18661/Desktop/home/media/" + str(lists2()[1])
    # filePath2 = "C:/Users/18661/Desktop/test001/static/uploads/" + str(lists2()[0])
    result1 = aipOcr.idcard(get_file_content(filePath1), 'front', options)
    # result2 = aipOcr.idcard(get_file_content(filePath2), 'back', options)
    #print(result1['words_result'])

    for key in result1['words_result'].keys():
        print(identity_information_list)
        # print(key + ':' + result1['words_result'][key]['words'])
        b = result1['words_result'][key]['words']
        if b not in identity_information_list:
            identity_information_list.append(b)
        else:
            print("该身份证已经注册过了")
            # pass
            #identity_information_list.append(b)
    # banner = infomation()
    infomation.objects.create(addr=identity_information_list[0],
                           name=identity_information_list[2],
                           birthday=identity_information_list[1],
                           IDcard=identity_information_list[3],
                           sex=identity_information_list[4],
                           nation=identity_information_list[5],)

    print(identity_information_list)

    return identity_information_list




