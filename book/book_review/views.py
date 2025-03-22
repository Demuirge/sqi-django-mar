from django.shortcuts import render, get_object_or_404, redirect

from .models import Book, Review
from .forms import ReviewForm, BookForm

# Create your views here.

def home(request):
    return render(request, "book_review/home.html")

def book_list(request):
    books = Book.objects.all()
    return render(request, "book_review/book-list.html", {"books": books})

def book_detail(request, book_id):
    bk_detail = get_object_or_404(Book, id=book_id)
    reviews = Review.objects.filter(book=bk_detail)
    form2 = ReviewForm()
    context = {
        "form2": form2,
        "reviews": reviews,
        "bk_detail": bk_detail
    }
    return render(request, "book_review/book-detail.html", context)

def book_form(request):
    form = BookForm()

    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('book_review:books')
    
    context = {
        "form": form
    }

    return render(request, "book_review/book-form.html", context)


def review(request, book_id):
    bk_detail = get_object_or_404(Book, id=book_id)
    reviews = Review.objects.filter(book=bk_detail)
    books = Book.objects.all()
    form2 = ReviewForm()
    

    if request.method == "POST":
        form2 = ReviewForm(request.POST, request.FILES)
        if form2.is_valid():
            review = form2.save(commit=False)
            review.book = bk_detail
            review.save()
            return redirect('book_review:book_detail', book_id)
        else:
            print("Form Errors:", form2.errors)
    
    context = {
        "form2": form2,
        "bk_detail": bk_detail,
        "books" : books,
        "reviews" : reviews
    }
    return render(request, "book_review/book-detail.html", context)
