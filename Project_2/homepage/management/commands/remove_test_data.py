
from django.core.management.base import BaseCommand
from homepage.models import HomePageContent

class Command(BaseCommand):
    help = 'Remove all test data from the HomePageContent model'

    def handle(self, *args, **kwargs):
        HomePageContent.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully removed all test data from HomePageContent'))
