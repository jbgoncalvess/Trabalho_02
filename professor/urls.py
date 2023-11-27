from django.urls import path
from .views import ProfessoresView, ProfessorUpDateView, ProfessorDeleteView, ProfessorAddView

urlpatterns = [
    path('professores', ProfessoresView.as_view(), name='professores'),
    path('professores/adicionar/', ProfessorAddView.as_view(), name='professores_adicionar'),
    path('<int:pk>/professores/editar/', ProfessorUpDateView.as_view(), name='professores_editar'),
    path('<int:pk>/professores/apagar/', ProfessorDeleteView.as_view(), name='professores_apagar'),
]