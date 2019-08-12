from django.urls import path, re_path
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'xiu'
urlpatterns = [
    path("", views.index, name="index"), # 首页
    path("house_info/", views.house_info, name="house_info"),# 添加发布房源信息
    re_path(r"already_house(?P<pindex>\d*)",views.already_house, name="already_house"),# 查看已经发布过的用户
    path("modifier/<int:c_id>", views.modifier, name="modifier"),# 修改发布房源信息
    # 首页房屋的详情页面
    path("img1/",views.img1,name="img1"),
    path("img2/",views.img2,name="img2"),
    path("img3/",views.img3,name="img3"),
    path("img4/",views.img4,name="img4"),
    path("img5/",views.img5,name="img5"),
    path("img6/",views.img6,name="img6"),
    path("img7/",views.img7,name="img7"),
    path("img8/",views.img8,name="img8"),
    # 三个协议
    path("landlord_rule/",views.landlord_rule,name='landlord_rule'),
    path("Service_rule/",views.Service_rules,name='Service_rule'),
    path("service_contract/",views.service_contract,name='service_contract'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



