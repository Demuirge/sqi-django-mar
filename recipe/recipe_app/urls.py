from django.urls import path

from . import views

app_name = "recipe"

urlpatterns = [
    path('', views.home, name="home"),
    path('add-recipe/', views.add_recipe, name="add_recipe"),
    path('recipes/', views.recipes, name="recipes"),
    path('recipe-detail/<int:recipe_id>', views.recipe_detail, name="recipe_detail"),
]