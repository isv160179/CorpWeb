from django.apps import AppConfig


class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
    verbose_name = 'Действующие функции сайта'  # Указывается для отображения в админ-панели

