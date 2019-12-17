from django.db import models   # 创建模型（类）需要继承models

# Create your models here.

class User(models.Model):
    class Meta:
        db_table = "user"
        verbose_name_plural = "用户"
    username = models.CharField(max_length=20,verbose_name='用户名')
    password = models.CharField(max_length=20,verbose_name='密码')
    name = models.CharField(max_length=20,verbose_name="昵称")
    first_name = models.CharField(max_length=10,verbose_name="姓")
    last_name = models.CharField(max_length=10,verbose_name="名")
    describe = models.CharField(max_length=50,verbose_name="个人简介")
    sex = models.IntegerField(verbose_name="性别")
    phone_number = models.IntegerField(verbose_name="电话号码")

    def __str__(self):
        return self.name

class Categories(models.Model):
    class Meta:
        db_table = "categories"
        verbose_name_plural = "商品类目"
    name = models.CharField(max_length=50,verbose_name="类目名称")
    father = models.ForeignKey('self', db_index=False, on_delete=models.CASCADE, blank=True, null=True,
                               verbose_name="父id")
    def __str__(self):
        return self.name

class CategoryProperty(models.Model):
    class Meta:
        db_table = "categoryproperty"
        verbose_name_plural = "商品类目属性"
    category = models.ForeignKey(Categories,on_delete=models.CASCADE,verbose_name="类目")
    name = models.CharField(max_length=50,verbose_name="类目属性")
    def __str__(self):
        return self.name

class CategoryValue(models.Model):
    class Meta:
        db_table = "categoryvalue"
        verbose_name_plural = "商品类目属性值"
    value = models.ForeignKey(CategoryProperty,on_delete=models.CASCADE,verbose_name="类目属性")
    name = models.CharField(max_length=50,verbose_name="类目属性值")
    def __str__(self):
        return self.name

class Goods(models.Model):
    class Meta:
        db_table = "goods"
        verbose_name_plural = "商品"
    cid = models.ForeignKey(Categories,on_delete=models.CASCADE,verbose_name="类目")
    name = models.CharField(max_length=20,verbose_name='商品名称')
    describe = models.CharField(max_length=100,verbose_name='商品描述')
    img = models.ImageField(upload_to="goods",verbose_name="商品图片")
    time = models.DateTimeField(auto_now=True,blank=True,verbose_name='创建时间')
    def __str__(self):
        return self.name


class Shopcar(models.Model):
    class Meta:
        db_table = "shopcar"
        verbose_name_plural = "购物车"
    uid = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="用户id")
    gid = models.ForeignKey(Goods,on_delete=models.CASCADE,verbose_name="商品id")
    def __str__(self):
        return self.name

# 库存规格关联表
class ExhaustedAttr(models.Model):
    Stocks = models.ForeignKey("Stocks", on_delete=models.CASCADE)
    attr = models.ForeignKey(CategoryProperty, on_delete=models.CASCADE,verbose_name="类目属性")
    attrchoice = models.ForeignKey(CategoryValue,on_delete=models.CASCADE,verbose_name="类目属性值")

class StockArr(models.Model):
    class Meta:
        db_table = "stocks"
        verbose_name_plural = "库存"
    name = models.CharField(max_length=20, verbose_name="商品名称")
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, verbose_name="类目")
    info = models.CharField(max_length=200, verbose_name="商品简介")
    goods_id = models.CharField(max_length=10, verbose_name="商品编码")
    img = models.ImageField(upload_to="goods", verbose_name="商品描述")

    def __str__(self):
        return self.name

class Stocks(models.Model):
    class Meta:
        db_table = "stocks"
        verbose_name_plural = "库存"
    gid = models.ForeignKey(Goods,on_delete=models.CASCADE,verbose_name="商品id")
    attr = models.ManyToManyField(CategoryProperty,through=ExhaustedAttr)
    price = models.IntegerField(verbose_name="价格")
    num = models.IntegerField(verbose_name="库存数量")
    def __str__(self):
        return self.name

class Orders(models.Model):
    class Meta:
        db_table = "orders"
        verbose_name_plural = "订单"
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='用户')
    goods = models.ForeignKey(Stocks,on_delete=models.CASCADE,verbose_name='商品名称')

    def __str__(self):
        return self.name

class OrderValue(models.Model):
    class Meta:
        db_table = "ordervalue"
        verbose_name_plural = "订单信息"
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='用户')
    status = models.IntegerField(verbose_name="订单状态")
    phone = models.IntegerField(verbose_name="电话号码")
    money = models.IntegerField(verbose_name="订单金额")
    pay = models.IntegerField(verbose_name="支付方式")
    time = models.DateTimeField(auto_now=True,blank=True,verbose_name="生成时间")
    def __str__(self):
        return self.name
