from django.urls import path
from . import views

urlpatterns = [
  path('', views.menu, name='menu'),
  path('contact/', views.contact, name='contact'),
]