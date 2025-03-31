from django.shortcuts import render, get_object_or_404, redirect

from django.urls import reverse

from .models import Book, Review
from .forms import ReviewForm, BookForm, ReviewManualForm, ReviewUpdateForm, ReviewManualUpdateForm

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
    form = ReviewManualForm()

    if request.method == "POST":
        form = ReviewManualForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            reviewer_name = cleaned_data.get('reviewer_name')
            rating = cleaned_data.get('rating')
            comment = cleaned_data.get('comment')
            Review.objects.create(book=bk_detail, reviewer_name=reviewer_name, rating=rating, comment=comment)

            return redirect('book_review:book_detail', book_id)

    context = {
        "form2": form2,
        "reviews": reviews,
        "bk_detail": bk_detail,
        "form": form
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

def manual_review(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    form = ReviewManualForm()

    if request.method == "POST":
        form = ReviewManualForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            reviewer_name = cleaned_data.get('reviewer_name')
            rating = cleaned_data.get('rating')
            comment = cleaned_data.get('comment')
            Review.objects.create(book=book, reviewer_name=reviewer_name, rating=rating, comment=comment)

            return redirect('book_review:book_detail', book_id)
    
    context = {
       "book": book,
       "form": form
    }
    return render(request, "book_review/book-detail.html", context)

def update_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    form = ReviewUpdateForm(instance=review)

    if request.method == "POST":
        form = ReviewUpdateForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            # new_review.review = review
            # new_review.save()
            return redirect(reverse('book_review:book_detail', kwargs={"book_id": review.book.id}))

    context = {
        "form": form,
        "review": review
    }
    return render(request, "book_review/update-review.html", context)

def confirm_review_delete(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    return render(request, "book_review/confirm-review-delete.html", {"review": review})

def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.method == "POST":
        review.delete()
    return redirect(reverse('book_review:book_detail', kwargs={"book_id": review.book.id}))

def update_review_manual(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    form = ReviewManualUpdateForm(initial={
        "rating": review.rating,
        "comment": review.comment
    })
    if request.method=="POST":
        form = ReviewManualUpdateForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            review.rating = cleaned_data.get("rating")
            review.comment = cleaned_data.get("comment")
            review.save()
            return redirect(reverse('book_review:book_detail', kwargs={"book_id": review.book.id}))
    
    context = {
        "form": form,
        "review": review
    }
    return render(request, "book_review/update-manual-review.html", context)


