from django.urls import path

from . import views

app_name = 'authors'

urlpatterns = [
    path('', views.home, name='home'),
    path('book-list/', views.book_list, name='book_list'),
]