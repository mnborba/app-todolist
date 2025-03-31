from django.db import models
from datetime import date


# Create your models here.
class Todo(models.Model):
    titulo = models.CharField(
        verbose_name="Título", max_length=100, null=False, blank=False
    )
    descricao = models.TextField(verbose_name="Descrição", null=False, blank=True)
    data_criacao = models.DateField(auto_now_add=True, null=False, blank=True)
    data_entrega = models.DateField(
        verbose_name="Data de entrega", null=False, blank=False
    )
    data_conclusao = models.DateField(null=True)

    class Meta:
        ordering = ["data_entrega"]

    def mark_as_completed(self):
        if not self.data_conclusao:
            self.data_conclusao = date.today()
            self.save()
