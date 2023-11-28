from django.contrib import admin

# Register your models here.

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'last_update']
    list_per_page = 10