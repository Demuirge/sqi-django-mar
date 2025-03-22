from django.urls import path

from . import views

app_name = "book_review"

urlpatterns = [
    path('', views.home, name="home"),
    path('books', views.book_list, name="books"),
    path('book-details/<int:book_id>', views.book_detail, name="book_detail"),
    path('book-form/', views.book_form, name="book_form"),
    path('book/<int:book_id>/review/', views.review, name="review"),
]