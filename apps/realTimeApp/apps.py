from django.apps import AppConfig


class RealtimeappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.realTimeApp'

    def ready(self):
        import apps.realTimeApp.signals
