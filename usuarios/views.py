from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from churras.models import Prato
# Create your views here.
'''
   path('cadastro', views.cadastro , name='cadastro'),
   path('login', views.login , name='login'),
   path('dashboard', views.dashboard , name='dashboard'),
   path('logout', views.logout , name='logout'),

'''
 
def cadastro(request):
    if request.method == 'POST':
        # print(f'POST: {request.POST}')

        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['senha']
        senha2 = request.POST['senha2']

        if not nome.strip():
            print('o campo nao pode ficar vasio')
            return redirect('cadastro')
        
        if not email.strip():
            print('o campo nao pode ficar vasio')
            return redirect('cadastro')
        if senha != senha2 or not senha.strip() or not senha2.strip():
            print('e nessesario que seja igual')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            print('usuario ja exixte')
            return redirect('cadastro')
        
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        return redirect('login')
    return render(request, 'cadastro.html')

def login(request):
    if request.method == 'post':
        print(f'POST: {request.POST}')

        email= request.POST['email']
        senha= request.POST['senha']
        if email == "" or senha == "":
            print('os campos estao em branco')
            return redirect('login')
        print(email, senha)
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
        
            if user is not None:
                auth.login(request, user)
                print('login efetuado com sucesso')


        return redirect('login')
    
    return render(request, 'login.html')
    

def dashboard(request):
    if request.user.is_authenticated:
        pratos = Prato.objects.filter(publicado = True).order_by('-date_prato')

        contexto = {
        'lista_pratos' : pratos,
         }
        return render(request, 'dashboard.html', contexto)
    return render(request, 'index')
    
     


def logout(request):
    auth.logout(request)
    print('voce realizou o logout!')
    return redirect('index')



def cria_prato(request):
    if request.user.is_authenticated:
        if request.method =='post':
            print(f'\nrequest.POST')

            nome_prato= request.POST['nome_prato']
            ingredientes= request.POST['ingredientes']
            modo_preparo= request.POST['modo_preparo']
            tempo_preparo= request.POST['tempo_preparo']
            rendimento= request.POST['rendiento']
            categoria= request.POST['categoria']
            foto_prato= request.FILES['foto_prato']
            user= get_object_or_404(user, pk=request.user.id)
            prato= Prato.objects.create(
                pessoa=user,
                nome_prato=nome_prato,
                ingredientes=ingredientes,
                modo_preparo=modo_preparo,
                tempo_preparo=tempo_preparo,
                rendimento=rendimento,
                categoria=categoria,
                foto_prato=foto_prato
            )
            prato.save()
            print('prato criado com sucesso')
            return redirect('dashboard')
            




        return render(request, 'cria_prato.html')

    print('voce nao tem permisao para criar pratos')
    return redirect('index')