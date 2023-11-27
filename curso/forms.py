from django import forms
from disciplina.models import Disciplina
from .models import Curso

class CursoModelForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nome', 'disciplinas']
        widgets = {
            'nome': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o nome da disciplina'}),
        }

        disciplinas = forms.ModelMultipleChoiceField(
            queryset=Disciplina.objects.all(),
            widget=forms.CheckboxSelectMultiple,
            required=False,
            label='Disciplinas'
        )