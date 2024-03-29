# Generated by Django 4.1.4 on 2023-01-07 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('vname', models.CharField(max_length=20)),
                ('vregister_no', models.CharField(default='Not  mentioned', max_length=20, primary_key=True, serialize=False)),
                ('vmodel', models.CharField(default='Not  mentioned', max_length=20)),
                ('capacity', models.SmallIntegerField(default=4)),
                ('cost', models.PositiveIntegerField(default=14)),
                ('intrip', models.BooleanField(default=False)),
                ('fuel', models.CharField(default='Not mentioned', max_length=20)),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.employee')),
            ],
            options={
                'db_table': 'vehicle',
            },
        ),
    ]
