from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.default_view),
    path('<int:num>/', views.calculate_price),
    path('taxrate/', views.tax_rate_view),
]
