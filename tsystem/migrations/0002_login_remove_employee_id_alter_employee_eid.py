# Generated by Django 4.1.4 on 2022-12-28 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tsystem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.BigIntegerField(max_length=10)),
            ],
            options={
                'db_table': 'login',
            },
        ),
        migrations.RemoveField(
            model_name='employee',
            name='id',
        ),
        migrations.AlterField(
            model_name='employee',
            name='eid',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]