import random
from datetime import datetime

def generate_random_id(prefix=''):
    timestamp = int(datetime.now().timestamp())
    random_num = random.randint(1000, 9999)
    return f"{prefix}{timestamp}_{random_num}"

def validate_business_data(data):
    required_fields = ['name', 'industry', 'services']
    return all(field in data for field in required_fields)