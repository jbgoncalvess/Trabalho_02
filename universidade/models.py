from django.db import models

class Universidade(models.Model):
    nome = models.CharField('Nome', max_length=50, help_text='Nome da Universidade')
    endereco = models.CharField('Endereço', max_length=120, help_text='Endereço da Universidade')
