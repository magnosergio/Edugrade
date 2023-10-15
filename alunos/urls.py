from django.urls import path
from .views import AlunoAPIView, AlunosAPIView, DisciplinaAPIView, DisciplinasAPIView, Nota_BimestralAPIView, Notas_BimestraisAPIView

urlpatterns = [
    path('alunos/', AlunosAPIView.as_view(), name='alunos'),
    path('alunos/<int:pk>/', AlunoAPIView.as_view(), name='aluno'),
    path('disciplinas/', DisciplinasAPIView.as_view(), name='disciplinas'),
    path('disciplinas/<int:pk>/', DisciplinaAPIView.as_view(), name='disciplina'),
    path('notas/', Notas_BimestraisAPIView.as_view(), name='notas'),
    path('notas/<int:pk>/', Nota_BimestralAPIView.as_view(), name='nota'),
]