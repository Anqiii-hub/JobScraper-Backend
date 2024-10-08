from django.core.management.base import BaseCommand
from api.scraping_scripts.act_gov_script import main 

class Command(BaseCommand):
    help = 'Scrapes job posts and saves them to the database'

    def handle(self, *args, **kwargs):
        main()  # Call the main function
