from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.views.generic import View
from django.contrib import messages

from .forms import UserRegisterForm, UserLoginForm, UserForm
from .models import User


class UserCreateView(View):

    def get(self, request):
        user_form = UserRegisterForm()
        return render(request, 'register.html', context = {'form': user_form})

    def post(self, request):
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            username = user_form.cleaned_data['username']
            digit_counter = 0
            for sign in username:
                if sign.isdigit():
                    digit_counter += 1
            if digit_counter < 1:
                user_form.add_error('username', 'Логин должен содержать хотя бы одну цифру')
                return render(request, 'register.html', context={'form': user_form})
            else:
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


class UserProfileView(View):
    def get(self, request, *args, **kwargs):
        user = User.objects.get(id=kwargs['pk'])
        context = {
            'user': user
        }
        return render(request, 'user_profile.html', context)


class UserProfileUpdateView(View):
    def get(self, request, *args, **kwargs):
        user = User.objects.get(id=kwargs['pk'])
        user_form = UserForm(
            initial={
                'username': user.username,
                'email': user.email,
                'image': user.image
            }
        )
        context = {
            'form': user_form,
            'user': user
        }
        return render(request, 'user_profile_update.html', context)

    def post(self, request, *args, **kwargs):
        user = User.objects.get(id=kwargs['pk'])
        user_form = UserForm(request.POST, request.FILES, instance=user)
        if user_form.is_valid():
            user.username = user_form.cleaned_data['username']
            user.email = user_form.cleaned_data['email']
            user.image = user_form.cleaned_data['image']
            user_form.save()
            return redirect('user_profile', pk=user.pk)


class UserProfileDeleteView(View):
    def post(self, request, *args, **kwargs):
        User.objects.get(id=kwargs['pk']).delete()
        return redirect('good_list')
