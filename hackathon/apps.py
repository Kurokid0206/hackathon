from django.apps import AppConfig
from django.core.management import call_command


class HackathonConfig(AppConfig):
    name = 'hackathon'
    verbose_name = "Hackathon application"

    def ready(self):
        call_command('migrate')
        # import hackathon.services.seed
