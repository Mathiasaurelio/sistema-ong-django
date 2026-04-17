from django.contrib import admin
from .models import Material

# Boa prática: Usar uma classe customizada deixa o painel muito mais profissional
@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    # Colunas que vão aparecer na lista
    list_display = ('nome', 'categoria', 'quantidade', 'estado', 'data_cadastro')
    # Adiciona uma barra de pesquisa pelo nome
    search_fields = ('nome',)
    # Adiciona um filtro lateral por categoria e estado
    list_filter = ('categoria', 'estado')