# Generated by Django 3.1.7 on 2021-03-19 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wedd_app', '0016_auto_20210319_0302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='table_num',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='wedd_app.table'),
        ),
    ]