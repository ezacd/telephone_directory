# Generated by Django 4.2.2 on 2023-07-04 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directory_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
