# Generated by Django 3.1.5 on 2021-03-12 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedd_app', '0002_auto_20210312_0539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='url',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
