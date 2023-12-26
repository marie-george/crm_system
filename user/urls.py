from django.urls import path

from .views import UserCreateView

urlpatterns = [
    path('user-create', UserCreateView.as_view(), name='user_create'),
]