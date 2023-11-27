from django.db import models

class Aluno(models.Model):
    nome = models.CharField('Nome', max_length=50, help_text='Nome do aluno')
    matricula = models.DecimalField('Matricula', max_digits=15, decimal_places=0, unique=True, help_text='Numero da matricula')
    cpf = models.DecimalField('Cpf', max_digits=11, decimal_places=0, unique=True, help_text='Numero do CPF')

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
        ordering = ['nome', ]

    def __str__(self):
        return self.nome
