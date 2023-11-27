from django.contrib import admin
from django.utils.html import format_html

from aluno.models import Aluno

@admin.register(Aluno)
class ClienteAdmin(admin.ModelAdmin):
    fields = ('nome', 'matricula', 'cpf')
    list_display = ('nome', 'matricula', 'cpf')
    search_fields = ('nome', 'cpf')
