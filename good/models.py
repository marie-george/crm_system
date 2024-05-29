from django.db import models
from autoslug import AutoSlugField
from django.core.validators import MaxValueValidator, MinValueValidator
from user.models import User


class Good(models.Model):

    DISCOUNT = (
        ('Есть скидка', 'Есть скидка'),
        ('Нет скидки', 'Нет скидки')
    )

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
        verbose_name='комментарий к фактической цене', blank=True, null=True
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
    colors = models.ManyToManyField(
        'GoodColor',
        verbose_name='цвета',
        related_name='good_colors',
        blank=True
    )
    reviews = models.ManyToManyField(
        'GoodReview',
        verbose_name='отзывы',
        related_name='good_reviews',
        blank=True
    )
    discount_value = models.CharField(
        choices=DISCOUNT,
        default='Нет скидки',
        max_length=30
    )
    discount_procent = models.IntegerField(
        verbose_name='процент скидки',
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(100)]
    )
    delivery_date = models.DateField(
        verbose_name='время доставки',
        blank=True,
        null=True
    )

    def save(self, *args, **kwargs):
        procent_with_discount = 100 - self.discount_procent
        self.actual_price = self.basic_price / 100 * procent_with_discount
        super().save(*args, **kwargs)

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
        return 'Hello'

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class GoodColor(models.Model):
    color_name = models.CharField(
        max_length=150, verbose_name='цвет'
    )

    def __str__(self):
        return self.color_name


class GoodReview(models.Model):
    user = models.ForeignKey(
        "user.User",
        on_delete=models.CASCADE,
        related_name='автор',
        blank=True,
        null=True,
    )
    review = models.TextField(
        verbose_name='отзыв'
    )

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'


class Deal(models.Model):

    deal_name = models.CharField(
        max_length=150, verbose_name='сделка'
    )
    client = models.ForeignKey(
        "client.Client",
        on_delete=models.CASCADE,
        related_name='клиент',
        blank=True,
        null=True,
    )
    goods = models.ManyToManyField(
        'Good',
        verbose_name='товары',
        related_name='goods',
        blank=True
    )

    def __str__(self):
        return self.deal_name


class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    good = models.ForeignKey(Good, on_delete=models.CASCADE, related_name='favourites')

    class Meta:
        verbose_name = 'Избранный товар'
        verbose_name_plural = 'Избранные товары'
