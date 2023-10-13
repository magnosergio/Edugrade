from django.contrib import admin

# Register your models here.
from .models import Aluno
from .models import Disciplina
from .models import Nota_Bimestral

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'criacao', 'atualizacao', 'ativo')

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'criacao', 'atualizacao', 'ativo')

@admin.register(Nota_Bimestral)
class Nota_BimestralAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'disciplina', 'bimestre', 'ano', 'nota', 'criacao', 'atualizacao', 'ativo')
