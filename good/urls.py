from django.urls import path
from .views import GoodListView


urlpatterns = [
    path('good_list/', GoodListView.as_view(), name='good_list')
    ]
