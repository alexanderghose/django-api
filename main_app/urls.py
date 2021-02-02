from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('astronauts/', views.astro_index),
  path('about/', views.about, name='about'),
  path('cats/', views.cats_index, name='index'),
]