# Generated by Django 3.1.5 on 2021-03-23 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wedd_app', '0019_auto_20210323_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='guests',
            field=models.ForeignKey(default='Няма', on_delete=django.db.models.deletion.CASCADE, to='wedd_app.guest'),
        ),
    ]