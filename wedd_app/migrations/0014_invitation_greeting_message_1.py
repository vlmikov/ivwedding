# Generated by Django 3.1.5 on 2021-03-12 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedd_app', '0013_auto_20210312_0711'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitation',
            name='greeting_message_1',
            field=models.TextField(blank=True),
        ),
    ]
