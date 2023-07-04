from django.contrib import admin
from .models import Pessoa

class Listandopessoas(admin.ModelAdmin):
    list_display = [
        'id','nome','email'
    ]
    list_display_links = [
        'nome',
    ]
    search_fields = ['nome']
    list_editable = ['email']
    ordering = ['-id',]
    list_filter = ['email']
    list_per_page = 7
admin.site.register(Pessoa, Listandopessoas)
