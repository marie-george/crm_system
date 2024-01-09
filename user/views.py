from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.views.generic import View

from .models import User

from .forms import UserRegisterForm, UserLoginForm


class UserCreateView(View):

    def get(self, request):
        user_form = UserRegisterForm()
        return render(request, 'register.html', context = {'form': user_form})

    def post(self, request):
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('good_list')


class UserLoginView(View):

    def get(self, request):
        form = UserLoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('good_list')


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('good_list')
