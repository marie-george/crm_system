from django.views import generic

from .models import Good


class GoodListView(generic.ListView):
    model = Good
    extra_context = {
        'title': 'Список товаров',
    }
    templatename = 'good_list.html'
