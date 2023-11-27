# cursos/views.py
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Curso
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from .forms import CursoModelForm

class CursosView(ListView):
    model = Curso
    template_name = 'cursos.html'

    def get_queryset(self, *args, **kwargs):
        buscar = self.request.GET.get('buscar')
        qs = super(CursosView, self).get_queryset(*args, **kwargs)
        if buscar:
            qs = qs.filter(nome__icontains=buscar)
        paginator = Paginator(qs, 5)
        listagem = paginator.get_page(self.request.GET.get('page'))
        return listagem

class CursoAddView(CreateView):
    form_class = CursoModelForm
    model = Curso
    template_name = 'cursos_form.html'
    success_url = reverse_lazy('cursos')

class CursoUpdateView(UpdateView):
    form_class = CursoModelForm
    model = Curso
    template_name = 'cursos_form.html'
    success_url = reverse_lazy('cursos')

class CursoDeleteView(DeleteView):
    model = Curso
    template_name = 'cursos_apagar.html'
    success_url = reverse_lazy('cursos')
