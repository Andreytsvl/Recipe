from django.http import HttpResponse
from django.shortcuts import render
from rec.models import Recipe
import random


def index(request):
    recipes = Recipe.objects.all()[:5]  # Получаем первые 5 рецептов
    return render(request, 'index.html', {'recipes': recipes})

def about(request):
    return render(request, 'about.html')



def random_recipe(request):
    # Отбираем 5 случайных рецептов
    recipes = Recipe.objects.order_by('?')[:5]
    return render(request, 'random_recipe.html', {'recipes': recipes})