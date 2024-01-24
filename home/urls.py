
from django.contrib import admin
from django.urls import path

from . import views

app_name = "home"

urlpatterns = [
    path('', views.index, name="homepage"),
    path('tur/', views.tur, name="tur"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('tur/<str:slug>/', views.tur_detail, name="tur_detail"),
]

