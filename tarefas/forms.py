from django import forms
from .models import Tarefas


class TaskForm(forms.ModelForm):
    class Meta:
        model = Tarefas
        fields = ['title', 'deadline']