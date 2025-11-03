from django.urls import path
from app_cad_usuarios import views

urlpatterns = [

    #Primeira página
    path('', views.home, name='home'),

    #Envio do cadastro de usuários
    path('Usuarios/', views.usuarios, name='listagem_usuarios'),
]
