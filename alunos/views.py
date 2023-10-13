from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Aluno
from .serializers import AlunoSerializer

class AlunoAPIView(APIView):
    '''
    API de Alunos
    '''
    def get(self, request):
        alunos = Aluno.objects.all()
        serializer = AlunoSerializer(alunos, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = AlunoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        #return Response({"id": serializer.data['id']})
        return Response(serializer.data, status=status.HTTP_201_CREATED)