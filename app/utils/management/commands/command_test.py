from django.core.management import BaseCommand
from raven.contrib.django.raven_compat.models import client


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        try:
            2 / 0
        except ZeroDivisionError:
            client.captureException()
