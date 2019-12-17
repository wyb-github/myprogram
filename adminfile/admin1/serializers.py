from rest_framework.serializers import ModelSerializer,DateTimeField
from .models import Goods,User,Shopcar,Orders,Dindan,Categories,CategoryValue,Stocks

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']

class GoodsSerializer(ModelSerializer):
    time = DateTimeField(format="%Y-%m-%d %H:%M:%S",required=False)
    class Meta:
        model = Goods
        fields = ['cid','name','describe','img','time']

class ShopcarSerializer(ModelSerializer):
    class Meta:
        model = Shopcar
        fields = ['id','uid','gid']

class OrderSerializer(ModelSerializer):
    time = DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)
    class Meta:
        model = Orders
        fields = ['uid','status','phone','money','pay','time']

class DindanSerializer(ModelSerializer):
    class Meta:
        model = Dindan
        fields = ['uid','gid','oid']

class CategorieSerializer(ModelSerializer):
    class Meta:
        model = Categories
        fields = ['name']

class CategoriePropertySerializer(ModelSerializer):
    class Meta:
        model = CategoryValue
        fields = ['pid','name']

class CategorieValueSerializer(ModelSerializer):
    class Meta:
        model = CategoryValue
        fields = ['cid','name']

class StockSerializer(ModelSerializer):
    class Meta:
        model = Stocks
        fields = ['gid','num']