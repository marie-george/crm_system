# Generated by Django 4.2.6 on 2024-02-21 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
        ('good', '0005_deal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='клиент', to='client.client'),
        ),
    ]
