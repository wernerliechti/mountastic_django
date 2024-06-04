import csv
import os
from django.core.management.base import BaseCommand
from quiz.models import Mountain

class Command(BaseCommand):
    help = 'Import mountains from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='C:/Users/w\Documents\GitHub\mountastic-api\mountastic_django\quiz\management\commands\mountains.csv')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']

        # Check if the file exists
        if not os.path.exists(csv_file):
            self.stderr.write(f"Error: {csv_file} does not exist.")
            return

        # Open the CSV file and read data
        with open(csv_file, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            mountains = []
            for row in reader:
                try:
                    print("Processing row:", row)  # Debug print
                    mountain = Mountain(
                        name=row['\ufeffMountain'],  # Ensure this matches the CSV header
                        height=int(row['Height']),  # Ensure this matches the CSV header
                        region=row['Region'],  # Ensure this matches the CSV header
                        group=row['Group'],  # Ensure this matches the CSV header
                        image=''  # Placeholder for image if available
                    )
                    mountains.append(mountain)
                except ValueError as e:
                    self.stderr.write(f"Error processing row {row}: {e}")

            # Bulk create mountain objects
            if mountains:
                Mountain.objects.bulk_create(mountains)
                self.stdout.write(self.style.SUCCESS(f"Successfully imported {len(mountains)} mountains"))

