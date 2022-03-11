from django.apps import AppConfig

"""  apps.py – файл, содержащий основную конфигурацию приложения blog; """

class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
