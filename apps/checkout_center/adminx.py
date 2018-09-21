import xadmin
from checkout_center.models import Dish, Order, DeskDish


class DishAdmin(object):
    list_display = ["name", "introduction", "price", "category"]
    list_filter = ["name", "introduction", "price", "category"]


class OrderAdmin(object):
    list_display = ["order_name", "total_mount", "is_paid", "creation_time", "catering_time"]
    list_filter = ["order_name",  "total_mount", "is_paid", "creation_time", "catering_time"]
    ordering = ["catering_time"]
    style = 'tab'

    class DeskDishInline(object):
        model = DeskDish
        exclude = ["order_desk", "catering_time"]
        extra = 0
        # style = 'tab'
        ordering = ['-is_served']

    inlines = [DeskDishInline,]


class DeskDishAdmin(object):
    list_display = ["order_desk", "Dish", "dish_num", "is_served", "catering_time"]
    list_filter = ["order_desk", "Dish", "dish_num", "is_served", "catering_time"]


xadmin.site.register(Dish, DishAdmin)
xadmin.site.register(Order, OrderAdmin)
# xadmin.site.register(DeskDish, DeskDishAdmin)


