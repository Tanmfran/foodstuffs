from django.db import models


# Create your models here.
class FoodItems(models.Model):
    item_name = models.CharField(max_length=200)
    item_cost = models.DecimalField(default=0.00, decimal_places=2, max_digits=6)
    item_url = models.CharField(max_length=512)
    quantity = models.CharField(default=0, max_length=200)
