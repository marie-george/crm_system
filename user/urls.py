from django.urls import path

from .views import UserCreateView, UserLoginView, UserLogoutView

urlpatterns = [
    path('user-create', UserCreateView.as_view(), name='user_create'),
    path('user-login', UserLoginView.as_view(), name='user_login'),
    path('user-logout', UserLogoutView.as_view(), name='user_logout')
]