from bs4 import BeautifulSoup
import requests
from app.utils.mock_data import SAMPLE_BUSINESSES

def scrape_business_profile(website_url):
    # In a real implementation, this would scrape the actual website
    # Here we'll use mock data based on the URL
    
    # Check if URL matches any mock businesses
    for business in SAMPLE_BUSINESSES:
        if business['url'] in website_url:
            return business
    
    # Default return if no match found
    # return {
    #     'name': 'Example Business',
    #     'industry': 'General',
    #     'services': ['Service 1', 'Service 2'],
    #     'tone': 'professional',
    #     'url': website_url
    # }
    return {
        'name': 'FitLife Gym',
        'industry': 'Fitness',
        'services': ['Personal Training', 'Group Classes'],
        'tone': 'motivational',
        'url': website_url
    }