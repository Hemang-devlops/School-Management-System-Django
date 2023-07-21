from django.apps import AppConfig



class MastersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Masters'

    def ready(self):
        import Masters.signals