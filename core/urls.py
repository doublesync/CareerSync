# Django
from django.urls import path
from . import views

# URL patterns
urlpatterns = [
    path('', views.index, name='index'),
]