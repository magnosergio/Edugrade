from rest_framework import serializers

from .models import Aluno


# Criação dos Serializers para que os models possam ser convertidos em json e vice-versa
class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            # Configuração dos campos que não serão mostrados em consultas
            'nome': {'write_only':True}
        }
        model = Aluno
        fields = '__all__'