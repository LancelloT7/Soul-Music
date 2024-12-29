from django.shortcuts import render
from usuarios.models import Users
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def logar(request):
    if request.method == "GET":
        return render(request, 'cadastrar.html' )
    elif request.method == "POST":
        login_usuario = request.POST.get('login')
        senha_usuario = request.POST.get('senha')

    usuario = authenticate(username=login_usuario, password=senha_usuario)

    if not usuario:
        messages.add_message(request, constants.ERROR, 'Usuário ou senha invalidos')
        return render(request, 'cadastrar.html')
    else:
        login(request, usuario)
        return render(request, 'menu.html') 


def cadastrar(request):
    if request.method == "GET":
        return render(request, 'cadastrar.html' )
    
    elif request.method == "POST":

        nome = request.POST.get('login')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha') 

        if Users.objects.filter(username=nome).exists():
            messages.add_message(request, constants.ERROR, 'Usuário já existe')
            return render(request, 'cadastrar.html')
        elif senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, 'As senhas não são iguais')
            return render(request, 'cadastrar.html')

        else:
            usuario = Users(username=nome)
            usuario.set_password(senha)

            usuario.save()

        messages.add_message(request, constants.SUCCESS, 'Cadastro realizado')
        return render(request, 'cadastrar.html')
    
    
