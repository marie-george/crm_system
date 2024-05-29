from django.urls import path

from .views import UserCreateView, UserLoginView, UserLogoutView, UserProfileView, UserProfileUpdateView, UserProfileDeleteView


urlpatterns = [
    path('user-create', UserCreateView.as_view(), name='user_create'),
    path('user-login', UserLoginView.as_view(), name='user_login'),
    path('user-logout', UserLogoutView.as_view(), name='user_logout'),
    path('user_profile/<int:pk>', UserProfileView.as_view(), name='user_profile'),
    path('user_profile_update/<int:pk>', UserProfileUpdateView.as_view(), name='user_profile_update'),
    path('user_profile_delete/<int:pk>', UserProfileDeleteView.as_view(), name='user_profile_delete')
]