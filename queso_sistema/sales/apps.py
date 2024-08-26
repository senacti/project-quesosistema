# sales/apps.py

from django.apps import AppConfig

class SalesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sales'
    verbose_name = 'Ventas'

    def ready(self):
        import sales.signals
