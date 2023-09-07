from datetime import datetime

from django.db import models

# Create your models here.
# class Product():
#     id=None
#     name=None
#     qty=None
#     price=None
#     def amount(self):
#         return self.qty * self.price
    
class Teacher(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()

class Category(models.Model):
    name = models.CharField(max_length=80,null=False)
    createBy = models.IntegerField()
    updateBy = models.IntegerField()
    createAt = models.DateTimeField(auto_now_add=datetime.now())
    updateAt = models.DateTimeField(null=True)

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    barcode = models.BigIntegerField()
    unitPrice = models.FloatField()
    qtyInstock = models.IntegerField()
    photo = models.ImageField(upload_to='media/')
    createBy = models.IntegerField()
    updateBy = models.IntegerField()
    createAt = models.DateTimeField(auto_now_add=datetime.now())
    updateAt = models.DateTimeField(null=True)
