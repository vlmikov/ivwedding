# Generated by Django 3.1.5 on 2021-03-24 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wedd_app', '0026_auto_20210324_1849'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainGuest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('message', models.TextField(blank=True)),
                ('email', models.CharField(max_length=50)),
                ('is_vegetarian', models.CharField(choices=[('Не', 'Не'), ('Да', 'Да')], max_length=2)),
                ('accept_invitation', models.CharField(blank=True, choices=[('Приемам', 'Приемам поканата с удоволствие'), ('Отказвам', 'Любезно отказвам поканата')], max_length=50)),
                ('table_num', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wedd_app.table')),
            ],
        ),
        migrations.CreateModel(
            name='SecondGuest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=30)),
                ('message', models.TextField(blank=True)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('is_vegetarian', models.CharField(blank=True, choices=[('Не', 'Не'), ('Да', 'Да')], max_length=2)),
                ('accept_invitation', models.CharField(blank=True, choices=[('Приемам', 'Приемам поканата с удоволствие'), ('Отказвам', 'Любезно отказвам поканата')], max_length=50)),
                ('table_num', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wedd_app.table')),
            ],
        ),
        migrations.RemoveField(
            model_name='invitation',
            name='guests',
        ),
        migrations.DeleteModel(
            name='Guest',
        ),
        migrations.AddField(
            model_name='invitation',
            name='guest_1',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='wedd_app.mainguest'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invitation',
            name='guest_2',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='wedd_app.secondguest'),
            preserve_default=False,
        ),
    ]