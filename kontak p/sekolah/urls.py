from django.urls import path

from .views import index, base
urlpatterns = [
    path('', index),
    path('base/', base),
    
]