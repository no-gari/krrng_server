from django.apps import AppConfig


class SearchConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api.search'
    verbose_name = '검색 관리'
    icon = 'fa fa-search'
