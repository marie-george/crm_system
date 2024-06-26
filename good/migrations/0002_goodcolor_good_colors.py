# Generated by Django 4.2.6 on 2024-02-07 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('good', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoodColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_name', models.CharField(max_length=150, verbose_name='цвет')),
            ],
        ),
        migrations.AddField(
            model_name='good',
            name='colors',
            field=models.ManyToManyField(blank=True, related_name='good_colors', to='good.goodcolor', verbose_name='цвета'),
        ),
    ]
