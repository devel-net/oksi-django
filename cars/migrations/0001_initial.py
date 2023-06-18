# Generated by Django 4.2.2 on 2023-06-18 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_brand', models.CharField(max_length=100)),
                ('release_year', models.IntegerField()),
                ('seats', models.IntegerField()),
                ('body_type', models.CharField(max_length=100)),
                ('engine_volume', models.FloatField()),
            ],
        ),
    ]
