from django.shortcuts import render, redirect, get_object_or_404

from .models import Recipe

from .forms import RecipeForm

# Create your views here.

def home(request):
    return render(request, "recipe/home.html")


def recipes(request):
    recipes = Recipe.objects.all()
    return render(request, "recipe/recipes.html", {"recipes": recipes})


def add_recipe(request):
    form = RecipeForm()

    if request.method == "POST":
        form = RecipeForm( request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recipe:recipes')
    
    context = {
        "form": form
    }

    return render(request, "recipe/add-recipe.html", context)

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, "recipe/recipe-detail.html", {"recipe": recipe})
    



