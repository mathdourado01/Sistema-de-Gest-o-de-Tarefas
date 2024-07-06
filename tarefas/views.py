from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
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

def editar(request,id_tarefa):
    tarefa = get_object_or_404(Tarefas, id=id_tarefa)
    if request.method == 'POST':
        form = TaskForm(request.POST,instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('listar')
    else:
        form = TaskForm(instance=tarefa)
    return render(request, 'tarefas/cadastro.html', {'form': form, 'tarefa': tarefa})

def excluir(request,id_tarefa):
    tarefa = get_object_or_404(Tarefas, id=id_tarefa)
    if request.method == 'POST':
        tarefa.delete()
        return redirect('listar')
    return render(request, 'tarefas/excluir.html', {'tarefa': tarefa})

def concluida(request, id_tarefa):
    tarefa = get_object_or_404(Tarefas, id=id_tarefa)
    tarefa.completed = True
    tarefa.finished_at = timezone.now()
    tarefa.save()
    return redirect('listar')

