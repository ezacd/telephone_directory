# Generated by Django 4.2.2 on 2023-07-04 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory_app', '0002_remove_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
    ]