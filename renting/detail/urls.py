from django.urls import path
from detail import views
from django.conf.urls.static import static
from django.conf import settings
app_name='detail'
urlpatterns = [
    path('',views.index,name='index'),
    path('home_detail/<int:hid>',views.home_detail,name='home_detail'),
    path("login/",views.login,name='login'),
    path("order/",views.order,name='order'),
    path("comment/<int:hid>",views.comment,name='comment'),
    path("comment_reply/<int:hid>",views.reply_comment,name='comment_reply'),
    path("replay_comment_1/",views.replay_comment_1,name='replay_comment_1')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
