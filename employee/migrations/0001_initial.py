# Generated by Django 4.1.4 on 2023-01-07 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('eid', models.AutoField(primary_key=True, serialize=False)),
                ('ename', models.CharField(max_length=100)),
                ('eemail', models.EmailField(max_length=254)),
                ('econtact', models.CharField(max_length=15)),
                ('eage', models.SmallIntegerField(default=18)),
                ('edob', models.DateField(default='2000-01-01')),
                ('eaddhar', models.CharField(default='Not Mentioned', max_length=14)),
                ('isverified', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
    ]
