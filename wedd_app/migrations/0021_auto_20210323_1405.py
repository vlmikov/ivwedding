# Generated by Django 3.1.5 on 2021-03-23 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wedd_app', '0020_auto_20210323_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='guests',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wedd_app.guest'),
        ),
    ]
