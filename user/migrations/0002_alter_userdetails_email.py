# Generated by Django 4.1.4 on 2023-01-10 01:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='email',
            field=models.ForeignKey(default='NOT Provided', on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]
