from django.contrib import admin
from ReceitaApp.models import Receita
from ReceitaApp.models import Receita, Categoria
# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome']
    list_display_links = ['nome']
    search_fields = ['nome']


class ReceitaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'ingredientes','modo_de_preparo', 'grau_de_dificuldade']
    list_disply_links = ['nome', 'ingredientes']
    list_filter = ['nome', 'grau_de_dificuldade']

admin.site.register(Receita, ReceitaAdmin,)
admin.site.register(Categoria, CategoriaAdmin)
