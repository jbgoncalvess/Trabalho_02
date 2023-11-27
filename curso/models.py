from django.db import models
from disciplina.models import Disciplina

class Curso(models.Model):
    nome = models.CharField('Nome', max_length=50, help_text='Nome do curso')
    disciplinas = models.ManyToManyField(Disciplina, related_name='cursos', blank=True)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['nome']

    def __str__(self):
        return self.nome
