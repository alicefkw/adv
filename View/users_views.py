from django.shortcuts import render, redirect
from django.contrib import messages
from site_users.forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f'Bem-vindo, {username}!')
            return redirect('index')
        else:
            messages.info(request, f'Precisa desconectar da sua conta atual primeiro!')
        #form = UserLoginForm(request.POST)
        #if form.is_valid():
        #    form.save()
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form, 'title': 'log in'})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Conta criada com sucesso. Entre agora!')    
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'register.html', context)