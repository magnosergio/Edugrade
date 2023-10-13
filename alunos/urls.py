from django.urls import path
from .views import AlunoAPIView, DisciplinaAPIView, Nota_BimestralAPIView

urlpatterns = [
    path('alunos/', AlunoAPIView.as_view(), name='alunos'),
    path('disciplinas/', DisciplinaAPIView.as_view(), name='disciplinas'),
    path('notas/', Nota_BimestralAPIView.as_view(), name='notas'),
]