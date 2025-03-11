from django.urls import path

from . import views

app_name = 'dtl'

urlpatterns = [
    path('', views.cart, name='cart'),
]