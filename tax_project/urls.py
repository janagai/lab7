from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('tax_app.urls')),
    
]
