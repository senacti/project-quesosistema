# Generated by Django 5.0.2 on 2024-08-25 23:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_alter_pedido_total'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedido',
            old_name='total',
            new_name='subtotal',
        ),
    ]
