from django.contrib import admin
from django.urls import path
from tarefas.views import listar

urlpatterns = [path("admin/", admin.site.urls), path("", listar)]
