from django.shortcuts import render, get_object_or_404

from .models import Author
from library.models import Book

# Create your views here.
def home(request):
    return render(request, "authors/home.html")

def book_list(request):
    return render(request, "authors/book-list.html")

def all_authors(request):
    all_books = Book.objects.order_by("-title")
    books_after_2000 = Book.objects.filter(published_on__gt = "2000-01-01")
    first_author = Author.objects.first()
    books_gt_200_bf_1990 = Book.objects.filter(published_on__year__lt=1990, number_of_pages__gt=200)
    context = {
        "all_books" : all_books,
        "books_after_2000" : books_after_2000,
        "first_author" : first_author,
        "books_gt_200_bf_1990" : books_gt_200_bf_1990,
    }
    return render(request, "authors/all-authors.html", context)

def book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, "authors/book-detail.html", {"book": book})

