from django.urls import path
from . import views

urlpatterns = [

    path('opcoes/', views.menu, name='menu'),
]