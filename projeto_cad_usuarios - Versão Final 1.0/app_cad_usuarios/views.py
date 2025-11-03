from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    #Exibir todos os usuarios Já cadsatrados em uma página
    usuarios = {
        'usuarios' : Usuario.objects.all()
    }

    #Retorna os dados para a paginá de listagem de usuários
    return render (request, 'usuarios/usuarios.html', usuarios)
    