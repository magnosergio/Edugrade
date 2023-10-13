from rest_framework import generics

from .models import Aluno, Disciplina, Nota_Bimestral
from .serializers import AlunoSerializer, DisciplinaSerializer, Nota_BimestralSerializer

class AlunoAPIView(generics.ListCreateAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class DisciplinaAPIView(generics.ListCreateAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer

class Nota_BimestralAPIView(generics.ListCreateAPIView):
    queryset = Nota_Bimestral.objects.all()
    serializer_class = Nota_BimestralSerializer