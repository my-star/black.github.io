from django.contrib import admin
from .models import User,Goods,Log,Type
# Register your models here.
class UserAdmin(admin.ModelAdmin):

     list_display = ['user_name', 'emp_num']

class TypeAdmin(admin.ModelAdmin):
     pass
class GoodsAdmin(admin.ModelAdmin):
     pass

class LogAdmin(admin.ModelAdmin):
     pass

admin.site.register(User,UserAdmin)
admin.site.register(Type,TypeAdmin)
admin.site.register(Goods,GoodsAdmin)
admin.site.register(Log,LogAdmin)