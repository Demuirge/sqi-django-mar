from django.urls import path

from . import views

from django.contrib.auth.views import LoginView, LogoutView

app_name = "users"

urlpatterns = [
    path('', views.sign_up, name="sign_up"),
    path('log-in/', LoginView.as_view(template_name="users/log-in.html"), name="log_in"),
    path('log-out/', LogoutView.as_view(), name="log_out"),
]