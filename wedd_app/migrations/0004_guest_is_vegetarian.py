# Generated by Django 3.1.5 on 2021-03-12 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedd_app', '0003_auto_20210312_0541'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='is_vegetarian',
            field=models.CharField(choices=[('Не', 'Не'), ('Да', 'Да')], default=1, max_length=2),
            preserve_default=False,
        ),
    ]
