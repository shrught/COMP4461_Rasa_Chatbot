import imp
from django.urls import URLPattern, path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
]