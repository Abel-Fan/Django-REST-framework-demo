from django.contrib import admin
from .models import Goods,User
# Register your models here.

@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ('id','name','time')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name','sex')