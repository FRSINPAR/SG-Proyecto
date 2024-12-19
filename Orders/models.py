from django.db import models

# Create your models here.
class Order(models.Model):
    class Meta:
        db_table = 'Orders_order'
    client = models.CharField(max_length=100)
    CHOICES = (
        ('Cash','Cash'),
        ('Card','Card'),
    )
    creation_time = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(choices=CHOICES, max_length=4)#4 porque cash o card tienen 4 caracteres
    product = models.CharField(max_length=100)
