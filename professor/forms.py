from django import forms
from .models import Professor


class ProfessorModelForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['nome', 'siape',]
        widgets = {
            'nome': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o nome do professor'}),
            'siape': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o valor siape do professor'}),
        }
