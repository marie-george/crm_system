from django import forms
from .models import Good, GoodImage


class GoodForm(forms.ModelForm):

    class Meta:
        model = Good
        fields = [
            'name',
            'description',
            'basic_price',
        ]


class ImageForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ImageForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False

    class Meta:
        model = GoodImage
        fields = [
            'image'
        ]
