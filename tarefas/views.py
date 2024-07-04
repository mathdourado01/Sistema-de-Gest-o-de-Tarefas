from django.shortcuts import render,redirect

from .models import Tarefas
from .forms import TaskForm

def listar(request):
    tarefas = Tarefas.objects.all()
    return render(request, "tarefas/home.html", {'tarefas': tarefas})

def cadastrar(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastrar')
    else:
        form = TaskForm()
    return render(request, 'tarefas/cadastro.html', {'form': form})



