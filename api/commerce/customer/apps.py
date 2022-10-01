from django.apps import AppConfig


class CustomerConfig(AppConfig):
    name = 'api.commerce.customer'
    verbose_name = '배송지 및 요청사항'
    icon = 'fa fa-truck'