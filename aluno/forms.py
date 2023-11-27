from django import forms
from .models import Aluno

class AlunoModelForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'matricula', 'cpf',]
        widgets = {
            'nome': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o nome do aluno'}),
            'matricula': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite a matricula do aluno'}),
            'cpf': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o cpf do aluno'}),
        }
