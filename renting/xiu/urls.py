from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
# app_name = 'xiu'
urlpatterns = [
    path("index/", views.index, name="index"),
    path("house_info/", views.house_info, name="house_info"),# 添加发布房源信息
    path("already_house/", views.already_hose, name="already_house"),# 查看已经发布过的用户
    path("modifier/<int:c_id>", views.modifier, name="modifier"),# 修改发布房源信息
]



