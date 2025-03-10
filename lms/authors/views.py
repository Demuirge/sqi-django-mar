from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "authors/home.html")

def book_list(request):
    return render(request, "authors/book-list.html")