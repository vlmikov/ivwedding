# Generated by Django 3.1.5 on 2021-03-24 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedd_app', '0031_auto_20210324_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainguest',
            name='first_name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='mainguest',
            name='last_name',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
