# Generated by Django 5.0.2 on 2024-07-22 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='valor',
            field=models.IntegerField(verbose_name='Valor'),
        ),
    ]
