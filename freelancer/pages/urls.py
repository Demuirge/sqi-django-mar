from django.urls import path

from . import views

app_name = "pages"

urlpatterns = [
    path('', views.home, name="home"),
    path('services/', views.services, name="services"),
    path('testimonials/', views.testimonials, name="testimonials"),
    path('pricing/', views.pricing, name="pricing"),
    path('blog/', views.blog, name="blog"),
    path('case-studies/', views.case_studies, name="case-studies"),
]