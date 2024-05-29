from django.urls import path
from .views import (
    GoodListView,
    GoodDetailView,
    GoodDeleteView,
    GoodUpdateView,
    GoodCreateView,
    GetGoodCategoryListView,
    GetGoodColorListView,
    DealCreateView,
    DealListView,
    ReviewCreateView,
    FavouritesCreateView,
    FavouritesView
)

urlpatterns = [
    path('', GoodListView.as_view(), name='good_list'),
    path('good-detail/<int:pk>', GoodDetailView.as_view(), name='good_detail'),
    path('good-delete/<int:pk>', GoodDeleteView.as_view(), name='good_delete'),
    path('good-update/<int:pk>', GoodUpdateView.as_view(), name='good_update'),
    path('good-create', GoodCreateView.as_view(), name='good_create'),
    path('good-category-list/<int:pk>', GetGoodCategoryListView.as_view(), name='good_category_list'),
    path('good-colors-list/<int:pk>', GetGoodColorListView.as_view(), name='good_color_list'),
    path('deal-create', DealCreateView.as_view(), name='deal_create'),
    path('deal-list/', DealListView.as_view(), name='deal_list'),
    path('review-create/<int:pk>', ReviewCreateView.as_view(), name='review_create'),
    path('good/<int:pk>/favourites/', FavouritesCreateView.as_view(), name='favourites_create'),
    path('favourites/', FavouritesView.as_view(), name='favourites')
]
