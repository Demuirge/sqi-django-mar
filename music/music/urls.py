from django.urls import path

from . import views

app_name = "music"

urlpatterns = [
    path('', views.home, name="home"),
    path('artist/', views.artist, name="artist"),
    path('album/', views.album, name="album"),
    path('artist/<int:artist_id>', views.artist_detail, name="artist_detail"),
    path('album/<int:album_id>', views.album_detail, name="album_detail"),
]