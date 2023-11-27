from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from aluno.forms import AlunoModelForm
from aluno.models import Aluno
from django.core.paginator import Paginator

class AlunosView(ListView):
    model = Aluno
    template_name = 'alunos.html'

    def get_queryset(self, *args, **kwargs):
        buscar = self.request.GET.get('buscar')
        qs = super(AlunosView, self).get_queryset(*args, **kwargs)
        if buscar:
            qs = qs.filter(nome__icontains=buscar)
        paginator = Paginator(qs, 5)
        listagem = paginator.get_page(self.request.GET.get('page'))
        return listagem

class AlunoAddView(CreateView):
    form_class = AlunoModelForm
    model = Aluno
    template_name = 'alunos_form.html'
    success_url = reverse_lazy('alunos')

class AlunoUpDateView(UpdateView):
    form_class = AlunoModelForm
    model = Aluno
    template_name = 'alunos_form.html'
    success_url = reverse_lazy('alunos')

class AlunoDeleteView(DeleteView):
    model = Aluno
    template_name = 'alunos_apagar.html'
    success_url = reverse_lazy('alunos')
