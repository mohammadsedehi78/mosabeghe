# Generated by Django 3.1.7 on 2021-03-05 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0002_auto_20210305_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='countrate',
            field=models.FloatField(default=0),
        ),
    ]