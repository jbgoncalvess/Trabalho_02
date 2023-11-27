from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import Disciplina


@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    fields = ('nome', 'codigo', 'alunos', 'professor')
    list_display = ('nome', 'codigo', 'professor_link')
    search_fields = ('nome', 'codigo', 'professor__nome')

    def professor_link(self, obj):
        return format_html('<a href="{}">{}</a>', reverse('admin:professor_professor_change', args=[obj.professor.id]),
                           obj.professor.nome)

    professor_link.short_description = 'Professor'
