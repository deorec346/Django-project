# Generated by Django 4.2.3 on 2023-07-05 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]
