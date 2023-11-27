from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from disciplina.forms import DisciplinaModelForm  # Certifique-se de importar o formulário correto
from disciplina.models import Disciplina
from django.core.paginator import Paginator

class DisciplinasView(ListView):
    model = Disciplina
    template_name = 'disciplinas.html'

    def get_queryset(self, *args, **kwargs):
        buscar = self.request.GET.get('buscar')
        qs = super(DisciplinasView, self).get_queryset(*args, **kwargs)
        if buscar:
            qs = qs.filter(nome__icontains=buscar)
        paginator = Paginator(qs, 5)
        listagem = paginator.get_page(self.request.GET.get('page'))
        return listagem

class DisciplinaAddView(CreateView):
    form_class = DisciplinaModelForm  # Substitua pelo seu formulário de disciplina
    model = Disciplina
    template_name = 'disciplinas_form.html'
    success_url = reverse_lazy('disciplinas')

class DisciplinaUpdateView(UpdateView):
    form_class = DisciplinaModelForm  # Substitua pelo seu formulário de disciplina
    model = Disciplina
    template_name = 'disciplinas_form.html'
    success_url = reverse_lazy('disciplinas')

class DisciplinaDeleteView(DeleteView):
    model = Disciplina
    template_name = 'disciplinas_apagar.html'
    success_url = reverse_lazy('disciplinas')
