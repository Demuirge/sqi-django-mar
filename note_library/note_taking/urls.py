from django.urls import path

from . import views

app_name = "note_taking"

urlpatterns = [
    path('', views.home, name="home"),
    path('notes/', views.notes, name="notes"),
    path('search-notes/', views.search_note, name="search_note"),
    path('note-category/', views.note_category, name="note_category"),
    path('create-note/', views.create_note, name="create_note"),
    path('create-note/', views.create_note, name="create_note"),
    path('confirm-delete-note/<int:note_id>', views.confirm_delete_note, name="confirm_delete_note"),
    path('delete-note/<int:note_id>', views.delete_note, name="delete_note"),
]