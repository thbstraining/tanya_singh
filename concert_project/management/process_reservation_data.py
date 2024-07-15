# management/commands/process_reservation_data.py

from django.core.management.base import BaseCommand
from concert_project.utils.data_processing import read_reservation_data, process_data_for_analysis, calculate_average_reservation_value

class Command(BaseCommand):
    help = 'Processes reservation data for analysis'

    def handle(self, *args, **kwargs):
        file_path = 'C:\Users\tanya_singh\Downloads\concert_project\concert_project\concert_project\data\reservation_data.json'  # Update with your file path
        reservations = read_reservation_data(file_path)
        structured_data = process_data_for_analysis(reservations)
        averages = calculate_average_reservation_value(structured_data)

        # Output to a file or perform further operations as needed
        with open('output.txt', 'w') as file:
            for key, value in averages.items():
                file.write(f"{key}: {value}\n")
