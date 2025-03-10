from django.shortcuts import render

# Create your views here.
def all_authors(request):
    return render(request, "library/all-authors.html")


def book_signings(request):
    return render(request, "library/book-signings.html")