from django.urls import reverse_lazy
from django.views.generic import View, UpdateView, CreateView
from django.shortcuts import render, redirect

from .forms import GoodForm
from .models import Good


class GoodListView(View):

    def get(self, request):
        goods = Good.objects.all()
        context = {
            'goods': goods
        }
        return render(request, 'good/good_list.html', context)

class GoodDetailView(View):

    def get(self, request, *args, **kwargs):
        good = Good.objects.get(id=kwargs['pk'])
        context = {
            'good': good
        }
        return render(request, 'good/good_detail.html', context)

class GoodDeleteView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'good/good_delete.html')

    def post(self, request, *args, **kwargs):
        Good.objects.get(id=kwargs['pk']).delete()
        return redirect('good_list')

class GoodUpdateView(View):

    def get(self, request, *args, **kwargs):
        good = Good.objects.get(id=kwargs['pk'])
        good_form = GoodForm(
            initial={
                'name': good.name,
                'description': good.description,
                'basic_price': good. basic_price
            }
        )
        context = {
            'form': good_form,
            'good': good
        }
        return render(request, 'good/good_update.html', context)

    def post(self, request, *args, **kwargs):
        good = Good.objects.get(id=kwargs['pk'])
        good_form = GoodForm(request.POST)
        if good_form.is_valid():
            good.name = good_form.cleaned_data['name']
            good.description = good_form.cleaned_data['description']
            good.basic_price = good_form.cleaned_data['basic_price']
            good.save()
            return redirect('good_list')


class GoodCreateView(View):

     def get(self, request):
         good_form = GoodForm()
         return render(request, 'good/create_good.html', {'form': good_form})

     def post(self, request):
         good_form = GoodForm(request.POST)
         if good_form.is_valid():
             good_form.save()
             return redirect('good_list')
