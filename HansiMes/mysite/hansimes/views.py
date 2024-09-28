from django.shortcuts import render, redirect
from hansimes.forms import ContactMessForm, UserForm, UserLoginForm
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from django.core.mail import send_mail
# from django.conf import settings

# Create your views here.
def home(request):
    form = ContactMessForm()
    if request.method == 'POST':
        form = ContactMessForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homeScreen')
    # print(request.META)
    print(request.headers)
    return render(request, 'home.html', {'form':form})


def about(request):
    content = {}
    return render(request, 'about.html', content)


def service(request):
    content = {}
    return render(request, 'service.html', content)


def contact(request):
    form = ContactMessForm()
    if request.method == 'POST':
        form = ContactMessForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contactPage')
        
    return render(request, 'contact.html', {'form':form})


def register(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])#hash password
            user.save()
            messages.success(request, 'You have been registered successfully. Please login to continue.')
            return redirect('loginPage')

    return render(request,'registration.html', {'form':form})


def login(request):
    form = UserLoginForm()
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # Authenticate user
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                messages.success(request, f'You have been logged in successfully as {username}.')
                return redirect('dashboardPage')
            else:
                messages.error(request, 'Invalid username or password. Please try again.')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')

    return render(request, 'login.html', {'form':form})

@login_required
def dashboard(request):
    content = {}
    return render(request, 'dashboard.html', content)

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('homeScreen')