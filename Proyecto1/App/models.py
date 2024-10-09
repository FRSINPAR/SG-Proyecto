from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.BooleanField()
    image = models.ImageField(upload_to='App', verbose_name='Imagen')

    def __str__(self) -> str:
        return self.name
    class Meta:
         verbose_name = 'Producto'
         verbose_name_plural = 'Productos'
         

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self) -> str:
            return self.name
   