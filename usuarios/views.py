from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth,messages
from churras.models import Prato

def campo_vasio(nome):
    return not campo.strip()
def senha_nao_sao_iguais(senha,senha2):
    return senha != senha2


 
def cadastro(request):
    if request.method == 'POST':
        # print(f'POST: {request.POST}')

        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['senha']
        senha2 = request.POST['senha2']

        if campo_vasio(nome):
            messages.error(request, 'o campo nome nao pode ficar em branco')
            return redirect('cadastro')
        
        if campo_vasio(email):
            messages.error(request, 'o campo email nao pode ficar vasio')
            return redirect('cadastro')
        if senha_nao_sao_iguais(senha, senha2) or campo_vasio(senha) or campo_vasio(senha2):
            messages.errorr(request, 'as senhas nao coincidem ou esta em branco')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            print('usuario ja exixte')
            return redirect('cadastro')
        
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        return redirect('login')
    return render(request, 'cadastro.html')

def login(request):
    if request.method == 'POST':
        print(f'POST: {request.POST}')

        email= request.POST['email']
        senha= request.POST['senha']

        if email == "" or senha == "":
            messages.error(request, 'os campos e-mail e senha nao podem ficar em branco')
            return redirect('login')
        
        
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
        
            if user is not None:
                auth.login(request, user)
                print('login efetuado com sucesso')
                messages.success(request, 'login efetuado com sucesso')

        messages.error(request, 'usuário e/ou senha inválidos.')
        return redirect('login')
    
    return render(request, 'login.html')
    

def dashboard(request):
    if request.user.is_authenticated:
        id = request.user.id

        pratos = Prato.objects.filter(pessoa=id).order_by('-date_prato')

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

    messages.error(request, 'voce nao tem permissao para criar pratos')
    return redirect('index')