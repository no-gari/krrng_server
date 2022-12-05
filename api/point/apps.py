from django.apps import AppConfig


class PointConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api.point'
    verbose_name = '포인트 관리'
    icon = 'fa fa-money'

    def ready(self):
        import api.point.signals
