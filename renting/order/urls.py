from order import views
from django.urls import path
app_name='order'
urlpatterns = [
    path('index/<house_id>/',views.ding_info,name='index'),
    path('register/',views.register,name='register'),
    path('',views.login,name='login'),
    path('detail/',views.detail,name='detail'),
    path('ding/',views.ding,name='ding'),
    path('my_ord/',views.my_ord,name='my_ord'),
    path('cancel/',views.my_ord_can,name='cancel'),
    path('ord_end/',views.ord_end,name='ord_end'),
    path('cel/',views.cel,name='cel'),
]