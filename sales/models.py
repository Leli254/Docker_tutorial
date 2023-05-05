from django.db import models

# Create your models here.
class SalesData(models.Model):
    product_name = models.CharField(max_length=255)
    sales = models.DecimalField(max_digits=10, decimal_places=2)
    month = models.CharField(max_length=7)
    date = models.DateField( auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.product_name} ({self.date}): {self.sales}'