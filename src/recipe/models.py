from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    times_cooked = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    products = models.ManyToManyField(Product, through='RecipeProduct')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'


class RecipeProduct(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    weight = models.IntegerField(verbose_name='Вес (в граммах)')

    def __str__(self):
        return f'id продукта - {self.product.id}'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['recipe', 'product'], name='unique_recipe_product')
        ]
