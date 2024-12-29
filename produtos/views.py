from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Produto

# Create your views here.
@login_required(login_url='/autenticacao/logar')
def cadastrar_produto(request):
    return render(request, 'cadastrar_produto.html')
    
