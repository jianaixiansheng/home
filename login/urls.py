from django.urls import path,include
from login import views
app_name = 'login'
urlpatterns = [
    path("register/",views.register,name="register"),  # 显示注册页面
    path("login/",views.login,name="login"),  # 显示登录页面

    # path("test_ajax/",views.ajax_test,name="ajax_test"),  # 显示ajax页面
    # path("login_check/",views.login_check), # 用户登录校验
    path("login_ajax/",views.login_ajax,name="login_ajax"),  # 显示ajax登录页面
    path("generate_code/",views.generate_code,name="generate_code"),   # 图片验证
    path("get_phone_code/",views.get_phone_code,name="get_phone_code"),
    path('find_pwd/',views.find_pwd,name="find_pwd"),
    path('find_pwd_action',views.find_pwd_action,name="find_pwd_action"),
    path("cancel/",views.cancel,name='cancel')
]
