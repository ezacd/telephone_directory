# Generated by Django 4.2.2 on 2023-07-03 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory_app', '0003_alter_user_organization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.CharField(default='default', max_length=255, unique=True),
        ),
    ]
