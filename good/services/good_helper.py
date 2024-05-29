from .helper_db import HelperDb


class GoodHelper():

    def initial_update_good_form(self, good):
        return {
            'name': good.name,
            'description': good.description,
            'basic_price': good.basic_price,
            'category': good.category,
            'colors': good.colors.all,
            'delivery_date': good.delivery_date
        }

    def update_good_fields(self, good, good_form, good_category):
        good.name = good_form.cleaned_data['name']
        good.description = good_form.cleaned_data['description']
        good.basic_price = good_form.cleaned_data['basic_price']
        good.delivery_date = good_form.cleaned_data['delivery_date']
        if good_form.cleaned_data['category'] is None:
            without_category = good_category.objects.get(id=HelperDb.get_id_without_category())
            good.category = without_category
        else:
            good.category = good_form.cleaned_data['category']
        return good


class GoodFormClass():

    def filling_in_object_fields(self, product_object, good_form):
        product_object.name = good_form.cleaned_data['name']
        product_object.description = good_form.cleaned_data['description']
        product_object.basic_price = good_form.cleaned_data['basic_price']

    def setting_category(self, good_category, product_object, good_form):
        if good_form.cleaned_data['category'] is None:
            without_category = good_category.objects.get(id=HelperDb.get_id_without_category())
            product_object.category = without_category
        else:
            product_object.category = good_form.cleaned_data['category']

    def save_good(self, product_object, good_form):
        product_object.save()
        product_object.colors.set(good_form.cleaned_data['colors'])

    def filling_in_from_image_form(self, image_form, image_product_object, product_object):
        if image_form.cleaned_data['image'] is None:
            image_product_object.image = 'default_image_static/default.jpg'
        else:
            image_product_object.image = image_form.cleaned_data['image']
        image_product_object.good = product_object
        image_product_object.save()
