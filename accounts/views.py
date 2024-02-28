import requests
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views import View, generic
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('Home:HomeURL')

class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'accounts/register.html', {'form': form})
    def post(self,request):
        Rform = RegisterForm(request.POST)
        if Rform.is_valid():
            cd = Rform.cleaned_data
            User.objects.create_user(cd['username'], cd['email'], cd['password'])
            messages.error(request, 'Register was Successfully', extra_tags='success')
            return redirect('Home:HomeURL')
        else:
            messages.error(request, 'Bad request', extra_tags='danger')
            return redirect('accounts:RegisterURL')

class LoginView(View):
    LoginUserform = LoginForm()
    def get(self, request):
        return render(request, 'accounts/login.html', {'loginform': self.LoginUserform})
    def post(self,request):
        rform = LoginForm(request.POST)
        if rform.is_valid():
            cd = rform.cleaned_data
            ruser = authenticate(request, username=cd['username'], password=cd['password'])
            if ruser is not None:
                login(request, ruser)
                messages.error(request, 'Register was Successfully', extra_tags='success')
                return redirect('Home:HomeURL')
            else:
                messages.error(request, 'Username or Password was Wrong', extra_tags='danger')
                return render(request, 'accounts/login.html', {'loginform': self.LoginUserform})
        else:
            messages.error(request, 'Bad request', extra_tags='danger')
            return render(request, 'accounts/login.html', {'loginform': self.LoginUserform})