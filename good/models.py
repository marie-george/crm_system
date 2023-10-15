from django.db import models


class Good(models.Model):
    name = models.CharField(
        verbose_name='наименование', max_length=300
    )
    description = models.TextField(
        verbose_name='описание'
    )
    basic_price = models.DecimalField(
        verbose_name='базовая цена', max_digits=20, decimal_places=2
    )
    actual_price = models.DecimalField(
        verbose_name='фактическая цена', max_digits=20, decimal_places=2,
        blank=True, null=True
    )
    comment_to_actual_price = models.TextField(
        verbose_name='комментарий к фактической цене'
    )
    is_available = models.BooleanField(default=True, verbose_name='признак доступности товара к заказу')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

