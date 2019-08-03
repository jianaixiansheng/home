from django.db import models
import PIL
from PIL import PILLOW_VERSION
# Create your models here.

class UserInfo(models.Model):
    """用户信息表"""
    # 用户手机号（作为账号）
    user_tel = models.BigIntegerField()
    # 用户名（昵称）
    user_name = models.CharField(max_length=10)
    # 用户密码
    user_pwd = models.CharField(max_length=8)
    # 真实姓名
    user_really_name = models.CharField(max_length=10,null=True)
    # 身份证
    user_id_card = models.CharField(max_length=18,null=True)
    # 生日
    user_birth = models.DateField(null=True)
    # 所在地
    user_addr = models.CharField(max_length=100)
    # 工作
    user_work = models.CharField(max_length=100,null=True)
    # 教育
    user_edu = models.CharField(max_length=100,null=True)
    # 性别
    user_sex = models.CharField(max_length=10,null=True)


class house(models.Model):
    """房屋信息表"""
    # 地址
    house_addr = models.TextField()
    #单价
    house_price = models.FloatField()
    # 房屋简介
    house_intro = models.TextField()
    # 户型
    house_type = models.CharField(max_length=100)
    # 宜居人数
    house_num = models.IntegerField()
    # 床铺数量
    house_bed = models.IntegerField()
    # 床铺规格
    house_bed_size = models.CharField(max_length=100)
    # 房屋描述
    house_describe = models.TextField()
    # 内部情况
    house_status = models.CharField(max_length=300)
    # 交通情况
    house_traffic = models.TextField()
    # 周边情况
    house_env = models.TextField()
    # 配套设施
    house_set = models.TextField()
    # 入住须知
    house_have_to = models.TextField()
    # 押金
    house_cash = models.FloatField()
    # 住房要求
    house_req = models.TextField()
    # 预定方式
    house_way = models.TextField()
    # 退订说明
    house_debook = models.TextField()
    # 外键
    house_fk = models.ForeignKey('UserInfo',on_delete=models.CASCADE)
    # 外键 关联 图片
    pic_fk = models.ForeignKey('Photo',on_delete=models.CASCADE, null=True)


class Photo(models.Model):
    """相册表"""
    Image = models.ImageField(upload_to='image')
    image_fk = models.ForeignKey('house',on_delete=models.CASCADE)


class Order(models.Model):
    """订单表"""
    # 入住日期
    order_enter_date = models.DateField()
    # 离开日期
    order_leave_date = models.DateField()
    # 总价
    order_price = models.FloatField()
    order_fk_house = models.ForeignKey('house',on_delete=models.CASCADE)
    order_fk_user = models.ForeignKey('UserInfo',on_delete=models.CASCADE)


class Comment(models.Model):
     """评论表"""
     # 评论内容
     comment_connent = models.TextField()
     # 房东回复的评论
     comment_reply = models.TextField()
     comment_fk_house = models.ForeignKey('house',on_delete=models.CASCADE)
     comment_fk_user = models.ForeignKey('UserInfo',on_delete=models.CASCADE)

class Collect(models.Model):
    """收藏表"""
    collect_fk_house = models.ForeignKey('house', on_delete=models.CASCADE)
    collect_fk_user = models.ForeignKey('UserInfo', on_delete=models.CASCADE)

class men(models.Model):
    """入住人表"""
    men_name = models.CharField(max_length=100)
    men_ID_card = models.CharField(max_length=18)
    men_tel = models.IntegerField()