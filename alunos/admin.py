from django.contrib import admin

# Register your models here.
from .models import Aluno

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'criacao', 'atualizacao', 'ativo')