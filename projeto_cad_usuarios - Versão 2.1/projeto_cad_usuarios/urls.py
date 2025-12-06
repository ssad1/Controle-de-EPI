from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    # EPIs
    path('', views.lista_epis, name='lista_epis'),
    path('epis/novo/', views.criar_epi, name='criar_epi'),
    path('epis/editar/<int:id>/', views.editar_epi, name='editar_epi'),
    path('epis/deletar/<int:id>/', views.deletar_epi, name='deletar_epi'),

    # Colaboradores
    path('colaboradores/', views.lista_colaboradores, name='lista_colaboradores'),
    path('colaboradores/novo/', views.criar_colaborador, name='criar_colaborador'),
    path('colaboradores/editar/<int:id>/', views.editar_colaborador, name='editar_colaborador'),
    path('colaboradores/deletar/<int:id>/', views.deletar_colaborador, name='deletar_colaborador'),

    # Empréstimos
    path('emprestimos/', views.lista_emprestimos, name='lista_emprestimos'),
    path('emprestimos/novo/', views.criar_emprestimo, name='criar_emprestimo'),
    path('emprestimos/editar/<int:id>/', views.editar_emprestimo, name='editar_emprestimo'),
    path('emprestimos/deletar/<int:id>/', views.deletar_emprestimo, name='deletar_emprestimo'),

    # Pesquisa

    path('pesquisar/', views.buscar_EPI, name='EPI-Pesquisa'),
]
