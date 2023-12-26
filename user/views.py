from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic import View

from .models import User

from .forms import UserRegisterForm

# def register(request):
#
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('good_list')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'register.html', {'form': form})


class UserCreateView(View):

    def get(self, request):
        user_form = UserRegisterForm()
        return render(request, 'register.html', context = {'form': user_form})

    def post(self, request):
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('good_list')

