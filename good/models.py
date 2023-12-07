from django.db import models
from autoslug import AutoSlugField


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
    category = models.ForeignKey(
        'GoodCategory',
        verbose_name='категория',
        on_delete=models.PROTECT,
        related_name='product_category',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class GoodCategory(models.Model):

    name = models.CharField(max_length=150, verbose_name='категория')
    slug_category = AutoSlugField(populate_from='name')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class GoodImage(models.Model):
    image = models.ImageField(upload_to='good/', verbose_name='изображение')
    good = models.ForeignKey(
        'Good',
        on_delete=models.CASCADE,
        related_name='image',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.image

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

