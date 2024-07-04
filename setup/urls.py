from django.contrib import admin
from django.urls import path
from tarefas.views import listar,cadastrar

urlpatterns = [path("admin/", admin.site.urls), path("", listar), path("cadastrar/",cadastrar,name='cadastrar')]
