# data_processing.py

import json

def read_reservation_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data




def process_data_for_analysis(reservations):
    structured_data = {}

    for reservation in reservations:
        concert_date = reservation['concert_date']
        seat_type = reservation['seat_type']
        price = reservation['price']
        
        if concert_date not in structured_data:
            structured_data[concert_date] = {}

        if seat_type not in structured_data[concert_date]:
            structured_data[concert_date][seat_type] = []

        structured_data[concert_date][seat_type].append(price)

    return structured_data


# data_processing.py

import statistics

def calculate_average_reservation_value(structured_data):
    averages = {}

    for concert_date, seats in structured_data.items():
        for seat_type, prices in seats.items():
            averages[f"{concert_date}_{seat_type}"] = statistics.mean(prices)

    return averages


# data_processing.py

from concurrent.futures import ProcessPoolExecutor

def process_data_concurrently(reservations):
    with ProcessPoolExecutor() as executor:
        results = executor.map(process_data_for_analysis, [reservations])
    
    return list(results)
