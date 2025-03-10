from django.urls import path

from . import views

app_name = 'library'

urlpatterns = [
    path('all-authors/', views.all_authors, name='authors'),
    path('book-signings/', views.book_signings, name='book_signings'),
]