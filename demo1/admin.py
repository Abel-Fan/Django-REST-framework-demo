from django.contrib import admin
from .models import Goods,User
from .models import UserAdmin as UAdmin
# Register your models here.
from rest_framework.authtoken.models import Token

@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ('id','name','time')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name','sex')

@admin.register(UAdmin)
class UserAdmin2(admin.ModelAdmin):
    list_display = ('id','username','password')

# @admin.register(Token)
# class TokenAdmin(admin.ModelAdmin):
#     list_display = "__all__"