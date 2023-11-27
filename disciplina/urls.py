from django.urls import path
from .views import DisciplinasView, DisciplinaAddView, DisciplinaUpdateView, DisciplinaDeleteView

urlpatterns = [
    path('disciplinas/', DisciplinasView.as_view(), name='disciplinas'),
    path('disciplinas/adicionar/', DisciplinaAddView.as_view(), name='disciplinas_adicionar'),
    path('disciplinas/<int:pk>/editar/', DisciplinaUpdateView.as_view(), name='disciplinas_editar'),
    path('disciplinas/<int:pk>/apagar/', DisciplinaDeleteView.as_view(), name='disciplinas_apagar'),
]
