from django.urls import path

from . import views

app_name = 'authors'

urlpatterns = [
    path('', views.home, name='home'),
    path('book-list/', views.book_list, name='book_list'),
    path('all_authors/', views.all_authors, name='all_authors'),
    path('book/<int:book_id>', views.book, name="book"),
]