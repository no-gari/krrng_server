from django.apps import AppConfig


class DiseaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api.disease'
    verbose_name = '질병, 증상명 관리'
    icon = 'fa fa-pills'

    def ready(self):
        import api.disease.signals
