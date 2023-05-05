from django.contrib import admin
from .models import Products, Category, Basket


@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Products)
class ProductsItemsAdmin(admin.ModelAdmin):
    pass

class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0