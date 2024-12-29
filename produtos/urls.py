from django.urls import path
from . import views


urlpatterns = [

    path('cadastrar_produto/', views.cadastrar_produto, name='cadastrar_produto'),
]

