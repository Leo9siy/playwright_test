from django.core.management import BaseCommand

from play.utils import save_to_db


class Command(BaseCommand):
    def handle(self, *args, **options):
        save_to_db()
        print("Successful")
