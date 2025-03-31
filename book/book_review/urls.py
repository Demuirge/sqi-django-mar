from django.urls import path

from . import views

app_name = "book_review"

urlpatterns = [
    path('', views.home, name="home"),
    path('books', views.book_list, name="books"),
    path('book-details/<int:book_id>', views.book_detail, name="book_detail"),
    path('book-form/', views.book_form, name="book_form"),
    path('book/<int:book_id>/review/', views.review, name="review"),
    path('book/<int:book_id>/manual-review/', views.manual_review, name="manual_review"),
    path('update-review/<int:review_id>/', views.update_review, name="update_review"),
    path('update-review-manual/<int:review_id>/', views.update_review_manual, name="update_review_manual"),
    path('confirm-delete/<int:review_id>', views.confirm_review_delete, name="confirm_review_delete"),
    path('delete-review/<int:review_id>', views.delete_review, name="delete_review"),
]