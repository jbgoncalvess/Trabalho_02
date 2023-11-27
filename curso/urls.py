from django.urls import path
from .views import CursosView, CursoAddView, CursoUpdateView, CursoDeleteView

urlpatterns = [
    path('cursos/', CursosView.as_view(), name='cursos'),
    path('cursos/adicionar/', CursoAddView.as_view(), name='cursos_adicionar'),
    path('cursos/<int:pk>/editar/', CursoUpdateView.as_view(), name='cursos_editar'),
    path('cursos/<int:pk>/apagar/', CursoDeleteView.as_view(), name='cursos_apagar'),
]
