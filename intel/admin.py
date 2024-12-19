from django.contrib import admin

# Register your models here.
from intel.models import Products
from intel.models import Category


#admin.site.register(Products)
@admin.register(Products)
class ProductAdmin(admin.ModelAdmin): #version mas personalizada
    list_display = ('name', 'price', 'stock')
    list_filter = ('stock', 'price')
    search_fields = ('name',)

admin.site.register(Category) #version base


