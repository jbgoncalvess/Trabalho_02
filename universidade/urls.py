from django.urls import path
from .views import UniversidadesView

urlpatterns = [
    path('universidades', UniversidadesView.as_view(), name='universidades'),
]