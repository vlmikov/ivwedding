# Generated by Django 3.1.7 on 2021-03-19 01:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wedd_app', '0014_invitation_greeting_message_1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='table_num',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='wedd_app.table'),
        ),
    ]
