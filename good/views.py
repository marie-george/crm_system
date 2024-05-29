from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from .services.good_helper import GoodHelper, GoodFormClass

from .forms import GoodForm, ImageForm, DealForm, ReviewForm
from .models import Good, GoodCategory, Deal, Favourite
from user.models import User
from .permissions import UserAccessMixin


def handling_error_400(request, exception):
    return render(request, 'good/error_400.html', status=400)


def handling_error_401(request, exception):
    return render(request, 'good/error_401.html', status=401)


def handling_error_402(request, exception):
    return render(request, 'good/error_402.html', status=402)


def handling_error_403(request, exception):
    return render(request, 'good/error_403.html', status=403)


def handling_error_404(request, exception):
    return render(request, 'good/error_404.html', status=404)


def handling_error_500(request, exception):
    return render(request, 'good/error_500.html', status=500)


class GoodListView(View):

    def get(self, request):
        users_number = User.objects.filter(is_staff=False).count()
        goods = Good.objects.all()
        context = {
            'goods': goods,
            'users_number': users_number
        }
        return render(request, 'good/good_list.html', context)


class GoodDetailView(View):

    def get(self, request, *args, **kwargs):
        good = Good.objects.get(id=kwargs['pk'])
        context = {
            'good': good,
            'reviews': good.reviews.all()
        }
        return render(request, 'good/good_detail.html', context)


class GoodDeleteView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'good/good_delete.html')

    def post(self, request, *args, **kwargs):
        Good.objects.get(id=kwargs['pk']).delete()
        return redirect('good_list')


class GoodUpdateView(View):
    GOOD_HELPER = GoodHelper()

    def get(self, request, *args, **kwargs):
        good = Good.objects.get(id=kwargs['pk'])
        good_form = GoodForm(
            initial=self.GOOD_HELPER.initial_update_good_form(good)
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
            good = self.GOOD_HELPER.update_good_fields(good, good_form, GoodCategory)
            good.save()
            good.colors.set(good_form.cleaned_data['colors'])
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


class GoodCreateView(UserAccessMixin, View):

     GOOD_FORM_CLASS = GoodFormClass()

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
             self.GOOD_FORM_CLASS.filling_in_object_fields(product_object, good_form)
             self.GOOD_FORM_CLASS.setting_category(GoodCategory, product_object, good_form)
             self.GOOD_FORM_CLASS.save_good(product_object, good_form)
             if image_form.is_valid():
                 image_product_object = image_form.save(commit=False)
                 self.GOOD_FORM_CLASS.filling_in_from_image_form(image_form, image_product_object, product_object)
                 return redirect('good_list')

class GetGoodCategoryListView(View):

    def get(self, request, *args, **kwargs):
        cat_id = kwargs.get('pk')
        goods = Good.objects.filter(category=cat_id)
        context = {
            'goods': goods
        }
        return render(request, 'good/good_list.html', context)


class GetGoodColorListView(View):
    def get(self, request, *args, **kwargs):
        color_id = kwargs.get('pk')
        goods = Good.objects.filter(colors=color_id)
        context = {
            'goods': goods
        }
        return render(request, 'good/good_list.html', context)


class DealCreateView(View):
    def get(self, request):
        deal_form = DealForm()
        context = {
            'form': deal_form,
        }
        return render(request, 'good/deal_create.html', context)

    def post(self, request):
        deal_form = DealForm(request.POST)
        if deal_form.is_valid():
            deal_object = deal_form.save(commit=False)
            deal_object.name = deal_form.cleaned_data['deal_name']
            deal_object.description = deal_form.cleaned_data['client']
            deal_object.save()
            deal_object.goods.set(deal_form.cleaned_data['goods'])
            return redirect('deal_list')


class DealListView(View):
    def get(self, request):
        deals = Deal.objects.all()
        context = {
            'deals': deals
        }
        return render(request, 'good/deal_list.html', context)


class ReviewCreateView(View):

    def get(self, request, *args, **kwargs):
        review_form = ReviewForm()
        context = {
            'review_form': review_form,
            'good_id': kwargs['pk']
        }
        return render(request, 'good/review_create.html', context)

    def post(self, request, *args, **kwargs):
        user = request.user
        good = Good.objects.get(id=kwargs['pk'])
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review_object = review_form.save(commit=False)
            review_object.user = user
            review_object.review = review_form.cleaned_data['review']
            review_object.save()
            good.reviews.add(review_object)
            return redirect('good_detail', good.id)


class FavouritesCreateView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        good_id = kwargs['pk']
        good = Good.objects.get(pk=good_id)
        # Проверка, есть ли товар уже в избранном
        if Favourite.objects.filter(user=request.user, good=good).exists():
            # Если есть, то удаляем из избранного
            Favourite.objects.filter(user=request.user, good=good).delete()
        else:
            # Если нет, то добавляем в избранное
            Favourite.objects.create(user=request.user, good=good)
        return redirect('good_detail', pk=good_id)


class FavouritesView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            favourites = request.user.user.all()  # Получение товаров из избранного
            context = {
                'favourites': favourites,
            }
            return render(request, 'good/favourites.html', context)
        else:
            return redirect('user_login')
