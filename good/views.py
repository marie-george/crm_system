from django.urls import reverse_lazy
from django.views.generic import View, UpdateView, CreateView
from django.shortcuts import render, redirect
from .services.helper_db import HelperDb

from .forms import GoodForm, ImageForm
from .models import Good, GoodImage, GoodCategory


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
                'basic_price': good.basic_price,
                'category': good.category,
            }
        )

        if len(good.image.all()) == 0:
            image_form = ImageForm()
        else:
            image_form = ImageForm(
                initial={
                    'image': good.image.all()[0].image
                }
            )

        context = {
            'form': good_form,
            'image_form': image_form,
            'good': good
        }
        return render(request, 'good/good_update.html', context)


    def post(self, request, *args, **kwargs):
        good = Good.objects.get(id=kwargs['pk'])
        good_form = GoodForm(request.POST)
        image_form = ImageForm(request.POST, request.FILES)
        if good_form.is_valid():
            good.name = good_form.cleaned_data['name']
            good.description = good_form.cleaned_data['description']
            good.basic_price = good_form.cleaned_data['basic_price']
            if good_form.cleaned_data['category'] is None:
                without_category = GoodCategory.objects.get(id=HelperDb.get_id_without_category())
                good.category = without_category
            else:
                good.category = good_form.cleaned_data['category']
            good.save()
            if image_form.is_valid():
                if len(good.image.all()) == 0:
                    image_good_object = image_form.save(commit=False)
                    image_good_object.good = good
                    image_good_object.image = 'default_image_static/default.jpg'
                    image_good_object.save()
                    return redirect('good_list')
                else:
                    image_good_object = good.image.all()[0]
                    if image_form.cleaned_data['image'] is not None:
                        image_good_object.image = image_form.cleaned_data['image']
                    image_good_object.good = good
                    image_good_object.save()
                    return redirect('good_list')


class GoodCreateView(View):

     def get(self, request):
         good_form = GoodForm()
         image_form = ImageForm()
         context = {
             'form': good_form,
             'image_form': image_form
         }
         return render(request, 'good/create_good.html', context)

     def post(self, request):
         good_form = GoodForm(request.POST)
         image_form = ImageForm(request.POST, request.FILES)
         if good_form.is_valid():
             product_object = good_form.save(commit=False)
             product_object.name = good_form.cleaned_data['name']
             product_object.description = good_form.cleaned_data['description']
             product_object.basic_price = good_form.cleaned_data['basic_price']
             if good_form.cleaned_data['category'] is None:
                 without_category = GoodCategory.objects.get(id=HelperDb.get_id_without_category())
                 product_object.category = without_category
             else:
                 product_object.category = good_form.cleaned_data['category']
             product_object.save()
             if image_form.is_valid():
                 image_product_object = image_form.save(commit=False)
                 if image_form.cleaned_data['image'] is None:
                    image_product_object.image = 'default_image_static/default.jpg'
                 else:
                    image_product_object.image = image_form.cleaned_data['image']
                 image_product_object.good = product_object
                 image_product_object.save()
                 return redirect('good_list')

