from django.urls import path
from .views import AlunosView
from .views import AlunoAddView, AlunoUpDateView, AlunoDeleteView

urlpatterns = [
    path('alunos', AlunosView.as_view(), name='alunos'),
    path('alunos/adicionar/', AlunoAddView.as_view(), name='alunos_adicionar'),
    path('<int:pk>/alunos/editar/', AlunoUpDateView.as_view(), name='alunos_editar'),
    path('<int:pk>/alunos/apagar/', AlunoDeleteView.as_view(), name='alunos_apagar'),
]