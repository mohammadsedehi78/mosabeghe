# Generated by Django 3.1.7 on 2021-03-05 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='countrate',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='rate',
            field=models.IntegerField(default=0),
        ),
    ]
