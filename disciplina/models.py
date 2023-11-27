from django.db import models
# from curso.models import Curso
from aluno.models import Aluno
from professor.models import Professor

class Disciplina(models.Model):
    nome = models.CharField('Nome', max_length=50, help_text='Nome da disciplina')
    codigo = models.CharField('Codigo', max_length=20, unique=True, help_text='Código da disciplina')
    # curso = models.ForeignKey(Curso, verbose_name='Curso'
    #                           , help_text='Nome do curso', on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    alunos = models.ManyToManyField(Aluno)

    class Meta:
        verbose_name = 'Disciplina'
        verbose_name_plural = 'Disciplinas'
        ordering = ['nome']

    def __str__(self):
        return self.nome