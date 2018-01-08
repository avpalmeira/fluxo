from django.db import models

# Create your models here.
class Device(models.Model):

    product_name = models.CharField(max_length = 100)
    reference_code = models.CharField(max_length = 15)
    category = models.CharField(max_length = 50)
    owner = models.CharField(max_length = 50)
    location = models.CharField(max_length = 100)
    sell_value = models.FloatField()
    buy_value = models.FloatField()

    def __str__(self):
        return self.product_name
