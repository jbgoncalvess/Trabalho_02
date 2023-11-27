from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from professor.forms import ProfessorModelForm
from professor.models import Professor
from django.core.paginator import Paginator

class ProfessoresView(ListView):
    model = Professor
    template_name = 'professores.html'

    def get_queryset(self, *args, **kwargs):
        buscar = self.request.GET.get('buscar')
        qs = super(ProfessoresView, self).get_queryset(*args, **kwargs)
        if buscar:
            qs = qs.filter(nome__icontains=buscar)
        paginator = Paginator(qs, 5)
        listagem = paginator.get_page(self.request.GET.get('page'))
        return listagem

class ProfessorAddView(CreateView):
    form_class = ProfessorModelForm
    model = Professor
    template_name = 'professores_form.html'
    success_url = reverse_lazy('professores')

class ProfessorUpDateView(UpdateView):
    form_class = ProfessorModelForm
    model = Professor
    template_name = 'professores_form.html'
    success_url = reverse_lazy('professores')

class ProfessorDeleteView(DeleteView):
    model = Professor
    template_name = 'professores_apagar.html'
    success_url = reverse_lazy('professores')
