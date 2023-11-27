from django.views.generic import TemplateView
from aluno.models import Aluno
from professor.models import Professor
from curso.models import Curso
from disciplina.models import Disciplina

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['qtd_alunos'] = Aluno.objects.count()
        context['qtd_professores'] = Professor.objects.count()
        context['qtd_disciplinas'] = Disciplina.objects.count()
        context['qtd_cursos'] = Curso.objects.count()
        return context




# #from django.shortcuts import render
# from django.views.generic import TemplateView
#
# # def index(request):
# #     context = {
# #         'disciplina': 'Desenvolvimento Web',
# #         'tecnologia': 'Python e Django'
# #     }
# # return render(request,'index.html', context)
# class IndexView(TemplateView):
#     template_name = 'index.html'