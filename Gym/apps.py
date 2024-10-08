from django.apps import AppConfig


class GymConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Gym'

    def ready(self):
        import Gym.signals  # Import the signals module