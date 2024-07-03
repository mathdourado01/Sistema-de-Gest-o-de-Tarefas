from django.shortcuts import render

from .models import Tarefas
def listar(request):
    tarefas = Tarefas.objects.all()
    return render(request, "tarefas/home.html", {'tarefas': tarefas})
