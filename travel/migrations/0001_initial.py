# Generated by Django 4.1.4 on 2023-01-10 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('pfrom', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='from')),
            ],
            options={
                'db_table': 'locations',
            },
        ),
        migrations.CreateModel(
            name='Distance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.IntegerField(verbose_name='distance(in kms)')),
                ('pfrom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.location')),
                ('pto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to', to='travel.location')),
            ],
            options={
                'db_table': 'distances',
            },
        ),
    ]
