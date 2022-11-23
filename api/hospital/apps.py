from django.apps import AppConfig


class HospitalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api.hospital'
    verbose_name = '병원관리'
    icon = 'fa fa-tags'
