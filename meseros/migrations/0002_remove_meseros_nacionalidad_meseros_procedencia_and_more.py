# Generated by Django 4.2.7 on 2023-12-23 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meseros', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meseros',
            name='nacionalidad',
        ),
        migrations.AddField(
            model_name='meseros',
            name='procedencia',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AlterField(
            model_name='meseros',
            name='nombre',
            field=models.CharField(default='', max_length=25),
        ),
    ]
