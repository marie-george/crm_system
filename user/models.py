from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not username:
            raise TypeError('Users must have a username.')

        if not email:
            raise TypeError('Users must have an email address.')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        verbose_name='имя пользователя',
        max_length=120,
        unique=True
    )
    email = models.EmailField(
        verbose_name='email',
        max_length=200,
        unique=True
    )
    is_active = models.BooleanField(
        verbose_name='является активным',
        default=True
    )
    is_staff = models.BooleanField(
        verbose_name='является админом',
        default=False
    )
    created_at = models.DateTimeField(
        verbose_name='дата регистрации',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='дата обновления',
        auto_now=True
    )
    image = models.ImageField(upload_to='user/', verbose_name='изображение', blank=True, null=True,
                              default='default_image_static/default.jpg')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    objects = UserManager()

