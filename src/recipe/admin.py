from django.contrib import admin
from .models import Product, Recipe, RecipeProduct


class RecipeProductInline(admin.TabularInline):
    model = RecipeProduct
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeProductInline]
    list_display = ('id', 'name')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'times_cooked')


admin.site.register(Product, ProductAdmin)
admin.site.register(Recipe, RecipeAdmin)
