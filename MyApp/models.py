from datetime import datetime

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=80, null=False)
    createBy = models.IntegerField(null=True)
    updateBy = models.IntegerField(null=True)
    createAt = models.DateTimeField(auto_now_add=datetime.now())
    updateAt = models.DateTimeField(null=True)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    barcode = models.BigIntegerField()
    unitPrice = models.FloatField()
    qtyInstock = models.IntegerField()
    photo = models.ImageField(upload_to="media/",null=True)
    createBy = models.IntegerField(null=True)
    updateBy = models.IntegerField(null=True)
    createAt = models.DateTimeField(auto_now_add=datetime.now())
    updateAt = models.DateTimeField(null=True)
