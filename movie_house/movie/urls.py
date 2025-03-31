from django.urls import path

from . import views

app_name = "movie"

urlpatterns = [
    path('', views.home, name="home"),
    path('movies/', views.movies, name="movies"),
    path('movie/<int:movie_id>/', views.movie, name="movie"),
    path('add-movie/', views.add_movie, name="add_movie"),
    path('edit-movie/<int:movie_id>/', views.edit_movie, name="edit_movie"),
    path('confirm-delete-movie/<int:movie_id>/', views.confirm_delete_movie, name="confirm_delete_movie"),
    path('delete-movie/<int:movie_id>/', views.delete_movie, name="delete_movie"),
]