from django.contrib import admin
from .models import Goods,User,Orders,OrderValue,Shopcar,Categories,CategoryProperty,CategoryValue,Stocks,StockArr
from django.utils.html import format_html
# Register your models here.
from rest_framework.authtoken.models import Token

def get_con(obj):
    if obj.father == None:
        return obj.name
    return obj.name +"<"+ get_con(Categories.objects.filter(id=obj.father_id).first())

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','username','phone_number')

@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','get_name','get_father')
    def get_father(self,obj):
        return str(obj.father_id)
    def get_name(self,obj):
        return get_con(obj)

@admin.register(CategoryProperty)
class CategoryPropertyAdmin(admin.ModelAdmin):
    list_display = ('id','name','category')

@admin.register(CategoryValue)
class CategoryValueAdmin(admin.ModelAdmin):
    list_display = ('id','name','value')

@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ('id','get_img','category','name','info')
    def get_img(self,obj):
        return format_html("<img src='/static/%s' width='100' height='50'>"%obj.img)

class AttrInline(admin.TabularInline):
    model = StockArr

@admin.register(Stocks)
class StocksAdmin(admin.ModelAdmin):
    inlines = [
        StockArr,
    ]
    list_display = ('goods',"get_attr")
    def get_attr(self,obj):
        str1 = ""
        for item in obj.exhaustedattr_set.filter(exhausted=obj.id):
            str1+="%s:%s  、 "%(item.attr,item.attrchoice)
        return str1

admin.site.register(Orders)
admin.site.register(OrderValue)
admin.site.register(Shopcar)
