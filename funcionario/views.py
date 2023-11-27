from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .forms import FuncionarioModelForm
from .models import Funcionario

class FuncionariosView(ListView):
    model = Funcionario
    template_name = 'professores.html'

    def get_queryset(self, *args, **kwargs):
        buscar = self.request.GET.get('buscar')
        qs = super(FuncionariosView, self).get_queryset(*args, **kwargs)
        if buscar:
            qs = qs.filter(nome__icontains=buscar)
        return qs

class FuncionarioAddView(CreateView):
    form_class = FuncionarioModelForm
    model = Funcionario
    template_name = 'professores_form.html'
    success_url = reverse_lazy('funcionarios')