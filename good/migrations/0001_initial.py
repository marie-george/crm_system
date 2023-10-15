# Generated by Django 4.2.6 on 2023-10-11 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='наименование')),
                ('description', models.TextField(verbose_name='описание')),
                ('basic_price', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='базовая цена')),
                ('actual_price', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='фактическая цена')),
                ('comment_to_actual_price', models.TextField(verbose_name='комментарий к фактической цене')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]