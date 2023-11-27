from django import forms
from .models import Disciplina

class DisciplinaModelForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = ['nome', 'codigo', 'professor', 'alunos']
        widgets = {
            'nome': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o nome da disciplina'}),
            'codigo': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o codigo da disciplina'}),
        }