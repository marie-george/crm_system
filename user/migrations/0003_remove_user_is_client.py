# Generated by Django 4.2.6 on 2024-02-21 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_is_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_client',
        ),
    ]
