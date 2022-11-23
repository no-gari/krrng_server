from django.apps import AppConfig


class LoggerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api.logger'

    def ready(self):
        import api.logger.signals
