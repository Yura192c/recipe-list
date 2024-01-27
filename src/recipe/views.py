from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Recipe, Product, RecipeProduct
from django.db import transaction


@transaction.atomic
def add_product_to_recipe(request):
    recipe_id = request.GET.get('recipe_id')
    product_id = request.GET.get('product_id')
    weight = request.GET.get('weight')

    if not (recipe_id and product_id and weight):
        raise Http404("Не все необходимые параметры указаны.")

    try:
        recipe = Recipe.objects.get(pk=recipe_id)
        product = Product.objects.get(pk=product_id)
    except (Recipe.DoesNotExist, Product.DoesNotExist):
        raise Http404("Указанный рецепт или продукт не найден.")

    recipe_product, created = RecipeProduct.objects.get_or_create(recipe=recipe, product=product,
                                                                  defaults={'weight': weight})

    if not created:
        recipe_product.weight = weight
        recipe_product.save()

    return HttpResponse("Product added to recipe successfully.")


def cook_recipe(request):
    recipe_id = request.GET.get('recipe_id')
    recipe = get_object_or_404(Recipe, id=recipe_id)

    for product in recipe.products.all():
        product.times_cooked += 1
        product.save()

    return HttpResponse("Recipe cooked successfully.")


def show_recipes_without_product(request):
    product_id = request.GET.get('product_id')
    product = get_object_or_404(Product, id=product_id)

    recipes_without_product = Recipe.objects.exclude(products=product)
    recipes_less_than_10g = Recipe.objects.filter(recipeproduct__product=product, recipeproduct__weight__lt=10)

    context = {
        'recipes_without_product': recipes_without_product,
        'recipes_less_than_10g': recipes_less_than_10g,
    }

    return render(request, 'show_recipes_without_product.html', context)
