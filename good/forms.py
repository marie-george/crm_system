from django import forms
from .models import Good, GoodImage, Deal, GoodReview


class GoodForm(forms.ModelForm):

    class Meta:
        model = Good
        fields = [
            'name',
            'description',
            'basic_price',
            'category',
            'colors',
            'delivery_date'
        ]
        widgets = {
            'delivery_date': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'})
        }


class ImageForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ImageForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False

    class Meta:
        model = GoodImage
        fields = [
            'image'
        ]


class DealForm(forms.ModelForm):
    class Meta:
        model = Deal
        fields = [
            'deal_name',
            'client',
            'goods'
        ]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = GoodReview
        fields = [
            'review'
        ]