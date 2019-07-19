from django.contrib import admin
from body.models import house
from body.models import Photo
from body.models import UserInfo
from body.models import Comment
# Register your models here.

class houseAdmin(admin.ModelAdmin):
    """房屋模型管理类"""
    list_display = ["id", "house_addr", "house_price","house_intro","house_type","house_num","house_bed","house_bed_size","house_describe","house_status","house_traffic","house_env","house_set","house_have_to","house_cash","house_req","house_way","house_debook","house_fk_id"]

class PhotoAdmin(admin.ModelAdmin):
    list_display = ["id","Image",'image_fk_id']

admin.site.register(house,houseAdmin)
admin.site.register(Photo,PhotoAdmin)
admin.site.register(UserInfo)
admin.site.register(Comment)

