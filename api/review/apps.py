from django.apps import AppConfig


class ReviewConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api.review'
    verbose_name = '병원 리뷰'
    icon = 'fa fa-comments'
