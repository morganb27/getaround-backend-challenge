import json
from collections import defaultdict
from datetime import datetime

DATA = json.load(open('input.json'))
OUTPUT = defaultdict(list)
DISCOUNT = {
    
}


def getaround():
    for item in DATA['rentals']:
        d = defaultdict(int)
        car = next(car for car in DATA['cars'] if car['id'] == item['id'])

        days = calculate_days(item['start_date'], item['end_date'])

        d['id'] = item['id']
        d['price'] = (car['price_per_day'] * days ) + (car['price_per_km'] * item['distance'])

        OUTPUT['rentals'].append(d)

def calculate_days(start_date, end_date):
    date_format = "%Y-%m-%d"
    start = datetime.strptime(start_date, date_format)
    end = datetime.strptime(end_date, date_format)
    return (end - start).days + 1

getaround()
print(f"Expected output for level 1 is: {json.dumps(OUTPUT, indent=2)}")




