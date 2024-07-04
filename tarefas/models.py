from django.db import models


class Tarefas(models.Model):
    title = models.CharField(verbose_name="Título:",max_length=100, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    deadline = models.DateTimeField(verbose_name="Data de Entrega:",blank=False, null=False)
    finished_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.title