from django.db.models import Q
from django.views.generic import ListView
from .models import Universidade

class UniversidadesView(ListView):
    model = Universidade
    template_name = 'universidades.html'

    def get_queryset(self, *args, **kwargs):
        buscar = self.request.GET.get('buscar')
        qs = super(UniversidadesView, self).get_queryset(*args, **kwargs)
        if buscar:
            qs = qs.filter(Q(nome__icontains=buscar)|Q(descricao__icontains=buscar))
        return qs