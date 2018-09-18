from django.db import models

# Create your models here.


class Dish(models.Model):
    """
    菜品
    """
    category_enum = (
        (1, "炒菜"),
        (2, "烧菜"),
        (3, "汤锅"),
        (4, "主菜"),
        (5, "蒸菜烧烤"),
        (6, "凉拌卤菜"),
        (7, "酒水饮料"),
        (8, "小吃水果"),
    )

    name = models.CharField(max_length=30, verbose_name="菜品名称", unique=True)
    introduction = models.TextField(verbose_name="菜品简介")
    price = models.FloatField(verbose_name="单价", null=False)
    category = models.CharField(verbose_name="菜品种类", choices=category_enum)
    image = models.ImageField(max_length=200, upload_to="media/images", verbose_name="图片路径")

    class Meta:
        verbose_name = "菜品"
        verbose_name_plural = "菜品"


class User(models.Model):
    name = models.CharField(max_length=10, verbose_name="用户姓名", unique=True)
    password = models.CharField(max_length=50, verbose_name="用户密码")
    role = models.CharField(max_length=20, verbose_name="角色")

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = "用户"

    def __str__(self):
        return self.name


class Order(models.Model):
    desk_number = models.IntegerField(verbose_name="桌号")
    time_stamp = models.DateTimeField(verbose_name="添加时间")
    total = models.FloatField(verbose_name="总计金额")
    is_ready = models.BooleanField(verbose_name="是否已经上菜")

    class Meta:
        verbose_name = "订单"
        verbose_name_plural = "订单"


class OrderDetail(models.Model):
    # TODO 还没想好
    pass







