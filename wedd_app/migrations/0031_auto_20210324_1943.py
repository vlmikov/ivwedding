# Generated by Django 3.1.5 on 2021-03-24 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wedd_app', '0030_auto_20210324_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='guest_1',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='wedd_app.mainguest'),
        ),
    ]
