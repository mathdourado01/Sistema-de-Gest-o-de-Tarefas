from django.contrib import admin
from django.urls import path
from tarefas.views import listar,cadastrar,editar, excluir, concluida

urlpatterns = [
    path("admin/", admin.site.urls), 
    path("", listar, name='listar'), 
    path("cadastrar/",cadastrar,name='cadastrar'),
    path("editar/<int:id_tarefa>",editar, name='editar'),
    path("excluir/<int:id_tarefa>",excluir, name='excluir'),
    path("concluida/<int:id_tarefa>",concluida, name='concluida')
]
