from django.shortcuts import render

# Create your views here.

def menu(request):
    food_of_choice = [ "Shawarma", "Spaghetti Bougleonese", "Chicken and Chips", "Pepperoni Pizza", "Hamburger"]
    return render(request, "food/menu.html", {"meals": food_of_choice})
