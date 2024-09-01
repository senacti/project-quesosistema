# Generated by Django 5.0.2 on 2024-09-01 00:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_pedido', models.DateTimeField(auto_now_add=True, verbose_name='Fecha del pedido')),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('en_proceso', 'En proceso'), ('completado', 'Completado'), ('cancelado', 'Cancelado')], default='pendiente', max_length=20, verbose_name='Estado del pedido')),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, editable=False, max_digits=10, verbose_name='Subtotal')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
                'db_table': 'pedido',
                'ordering': ['-fecha_pedido'],
            },
        ),
        migrations.CreateModel(
            name='DetallePedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('precio', models.DecimalField(decimal_places=2, editable=False, max_digits=10)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.producto')),
            ],
            options={
                'verbose_name': 'Detalle de Pedido',
                'verbose_name_plural': 'Detalles de Pedido',
                'db_table': 'detalle_pedido',
                'ordering': ['pedido', 'producto'],
            },
        ),
    ]
