from django.db import models

class Professor(models.Model):
    nome = models.CharField('Nome', max_length=50, help_text='Nome do professor')
    siape = models.DecimalField('Siape', max_digits=20, unique=True, decimal_places=0, help_text='Número do siape')
    # disciplina = models.ForeignKey('disciplina.Disciplina', verbose_name='Disciplina',
    #                                help_text='Nome da disciplina', related_name='professores', on_delete=models.CASCADE,
    #                                null=True)

    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'
        ordering = ['nome', ]

    def __str__(self):
        return self.nome