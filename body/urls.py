
# from django.contrib import admin
from django.urls import path,re_path
from body import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url

urlpatterns = [
    path('search/', views.search, name='search'), # 首页
    path('screen/', views.screen, name='screen'),  # 搜索符合条件
    path('show_screen/<int:aid>', views.show_screen, name='show_screen'),
    path('show_search/<int:pid>',views.show_search,name='show_search'), # 展示该地区所有信息，分页
]
