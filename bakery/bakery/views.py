from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "bakery/home.html")

def about(request):
    return render(request, "bakery/about.html")

def menu(request):
    context = {
        'menu': {'Bread': 200, 'Doughnut': 100, 'Apple-pie': 300, 'Cherry-Pie': 370, 'Cake': 500}
    }
    return render(request, "bakery/menu.html", context)

def contact(request):
    return render(request, "bakery/contact.html")
