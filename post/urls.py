from django.urls import path
from .views import post

urlpatterns = [
    path('', post , name='post'),
]