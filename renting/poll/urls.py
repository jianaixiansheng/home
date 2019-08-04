from django.conf.urls.static import static
from django.urls import path
from poll import views
from django.conf import settings
app_name = 'poll'
urlpatterns = [
    path("uploadPic/", views.uploadPic,name="uploadPic")

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
