from rest_framework import generics

from .models import Aluno, Disciplina, Nota_Bimestral
from .serializers import AlunoSerializer, DisciplinaSerializer, Nota_BimestralSerializer

class AlunosAPIView(generics.ListCreateAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class AlunoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class DisciplinasAPIView(generics.ListCreateAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer

class DisciplinaAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer


class Notas_BimestraisAPIView(generics.ListCreateAPIView):
    queryset = Nota_Bimestral.objects.all()
    serializer_class = Nota_BimestralSerializer

class Nota_BimestralAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Nota_Bimestral.objects.all()
    serializer_class = Nota_BimestralSerializer