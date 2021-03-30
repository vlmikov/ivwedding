# Generated by Django 3.1.5 on 2021-03-23 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wedd_app', '0018_auto_20210319_0305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guest',
            name='invitation',
        ),
        migrations.AddField(
            model_name='invitation',
            name='guests',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='wedd_app.guest'),
        ),
    ]
