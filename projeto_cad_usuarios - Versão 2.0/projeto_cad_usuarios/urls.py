from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    path('', views.lista_epis, name='lista_epis'),
    path('novo/', views.criar_epi, name='criar_epi'),
    path('editar/<int:id>/', views.editar_epi, name='editar_epi'),
    path('deletar/<int:id>/', views.deletar_epi, name='deletar_epi'),
]
