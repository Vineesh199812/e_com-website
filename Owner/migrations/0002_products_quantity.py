# Generated by Django 4.0.6 on 2023-06-29 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Owner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='quantity',
            field=models.PositiveIntegerField(default=5),
        ),
    ]
