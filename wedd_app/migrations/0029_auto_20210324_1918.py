# Generated by Django 3.1.5 on 2021-03-24 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedd_app', '0028_auto_20210324_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainguest',
            name='email',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
