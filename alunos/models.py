from django.db import models

BIMESTRE_CHOICES = [
    (1, '1º Bimestre'),
    (2, '2º Bimestre'),
    (3, '3º Bimestre'),
    (4, '4º Bimestre'),    
    ]

# Create your models here.

class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Aluno(Base):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'

    def __str__(self) -> str:
        return str(self.nome)

class Disciplina(Base):
    nome = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Disciplina'
        verbose_name_plural = 'Disciplinas'
    
    def __str__(self) -> str:
        return str(self.nome)
    
class Nota_Bimestral(Base):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    bimestre = models.IntegerField(choices=BIMESTRE_CHOICES)
    ano = models.CharField(max_length=4)
    nota = models.FloatField()

    class Meta:
        verbose_name = 'Nota Bimestral'
        #verbose_name_plural = ' '
    
    def __str__(self) -> str:
        return str(self.aluno)