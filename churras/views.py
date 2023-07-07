from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Prato

# Create your views here.
def index(request):
    pratos = Prato.objects.filter(publicado = True).order_by('-date_prato')
    # print(pratos.query)
    qtde_prato_por_pagina=3
    paginator= Paginator(pratos, qtde_prato_por_pagina)
    page= request.GET.get('page')
    lista_pratos_pagina=paginator.get_page(page)
    contexto = {
        'lista_pratos' : lista_pratos_pagina,
    }
    return render(request, 'index.html', contexto)

def churrasco(request, prato_id):
    # prato = Prato.objects.filter(pk=prato_id)   
    prato = get_object_or_404(Prato, pk=prato_id)   
    
    contexto = {
        'prato' : prato,
    }
    return render(request, 'churrasco.html', contexto)
    
