from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Dish(models.Model):
    """
    菜品
    """
    category_enum = (
        ("1", "炒菜"),
        ("2", "烧菜"),
        ("3", "汤锅"),
        ("4", "主菜"),
        ("5", "蒸菜烧烤"),
        ("6", "凉拌卤菜"),
        ("7", "酒水饮料"),
        ("8", "小吃水果"),
    )

    name = models.CharField(max_length=30, verbose_name="菜品名称", unique=True)
    introduction = models.TextField(max_length=130, verbose_name="菜品简介")
    price = models.FloatField(verbose_name="单价", null=False, blank=False)
    category = models.CharField(verbose_name="菜品种类", max_length=5, choices=category_enum, default="1")

    class Meta:
        verbose_name = "菜品"
        verbose_name_plural = "菜品"

    def __str__(self):
        return self.name


class UserProfile(AbstractUser):
    name = models.CharField(max_length=10, verbose_name="用户姓名", unique=True)
    gender = models.CharField(max_length=6, choices=(("female", "女"), ("male", "男")), default="male", verbose_name="性别")
    datetime = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = "用户"

    def __str__(self):
        return self.name


class Order(models.Model):
    """
    desk_number和order_name最重要
    """
    order_name = models.CharField(max_length=20, verbose_name="订单人姓名")
    desk_number = models.IntegerField(default=1, verbose_name="桌号")
    total_mount = models.FloatField(default=0.0, verbose_name="总计金额")
    is_paid = models.BooleanField(default=False, verbose_name="是否已支付")
    has_finished = models.BooleanField(default=False, verbose_name="是否完成订单")
    creation_time = models.DateTimeField(default=datetime.now, verbose_name="创建时间")
    # 根据吃饭时间就近排列
    catering_time = models.DateTimeField(default=datetime.now, verbose_name="聚餐时间")

    class Meta:
        verbose_name = "订单"
        verbose_name_plural = "订单"

    def __str__(self):
        return "%s(%s)" % (self.order_name, str(self.desk_number))


class DeskDish(models.Model):
    order_desk = models.ForeignKey(Order, verbose_name="桌子编号", related_name="OrderDish", on_delete=models.CASCADE)
    Dish = models.ForeignKey(Dish, verbose_name="菜名", on_delete=models.CASCADE)
    dish_num = models.IntegerField(default=1, verbose_name="菜品数量")
    is_served = models.BooleanField(default=False, verbose_name="是否已上菜")
    catering_time = models.DateTimeField(default=datetime.now, verbose_name="聚餐时间")

    class Meta:
        verbose_name = "点单"
        verbose_name_plural = "点单"

    def __str__(self):
        f = lambda x:"是" if x else "否"
        return "%s\n份数: %s\n是否上菜: %s" % (self.Dish.name, str(self.dish_num), f(self.is_served))









