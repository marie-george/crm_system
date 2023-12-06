from django.urls import path
from .views import (
    GoodListView,
    GoodDetailView,
    GoodDeleteView,
    GoodUpdateView,
    GoodCreateView
)

urlpatterns = [
    path('good-list/', GoodListView.as_view(), name='good_list'),
    path('good-detail/<int:pk>', GoodDetailView.as_view(), name='good_detail'),
    path('good-delete/<int:pk>', GoodDeleteView.as_view(), name='good_delete'),
    path('good-update/<int:pk>', GoodUpdateView.as_view(), name='good_update'),
    path('good-create', GoodCreateView.as_view(), name='good_create')
]
