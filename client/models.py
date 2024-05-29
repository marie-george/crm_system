from django.db import models


class Client(models.Model):
    name = models.CharField(
        max_length=200, verbose_name='имя'
    )
    email = models.EmailField(
        verbose_name='email', unique=True
    )
    telephone = models.CharField(
        max_length=200, verbose_name='телефон'
    )
    company_name = models.CharField(
        max_length=200, verbose_name='название компании'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'
