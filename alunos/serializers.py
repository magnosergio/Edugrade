from rest_framework import serializers

from .models import Aluno
from .models import Disciplina
from .models import Nota_Bimestral

# Criação dos Serializers para que os models possam ser convertidos em json e vice-versa
class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            # Configuração dos campos que não serão mostrados em consultas
            #'nome': {'write_only':True}
        }
        model = Aluno
        fields = '__all__'

class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
        }
        model = Disciplina
        fields = '__all__'

class Nota_BimestralSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
        }
        model = Nota_Bimestral
        fields = '__all__'