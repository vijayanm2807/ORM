
from django.db import models
from django.contrib import admin

class Order(models.Model):
    Ref_No = models.AutoField(primary_key=True)
    Gmail = models.EmailField()
    Mobile_No1 = models.CharField(max_length=15)
    Mobile_No2 = models.CharField(max_length=15, blank=True, null=True)
    Order_Date = models.DateField()
    Product_Name = models.CharField(max_length=50)
    Quantity = models.PositiveIntegerField()
    Price = models.DecimalField(max_digits=10, decimal_places=2)

class OrderAdmin(admin.ModelAdmin):
    list_display = [ "Ref_No", "Gmail", "Mobile_No1","Mobile_No2", "Order_Date", "Product_Name", "Quantity", "Price"]
