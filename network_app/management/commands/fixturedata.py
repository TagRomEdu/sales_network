import os

from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    """
    Loads data from JSON files.
    """
    help = 'Loads data from fixtures dir'
    fixtures_dir = 'fixtures'
    loaddata_command = 'loaddata'
    filenames = [
        'product',
        'network_links',
    ]

    def handle(self, *args, **options):
        for fixture_filename in self.filenames:
            call_command(
                self.loaddata_command, os.path.join(self.fixtures_dir,
                                                    f'{fixture_filename}.json')
            )
