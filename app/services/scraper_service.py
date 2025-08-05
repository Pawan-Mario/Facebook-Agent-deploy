# from bs4 import BeautifulSoup
# import requests
# from app.utils.mock_data import SAMPLE_BUSINESSES

# def scrape_business_profile(website_url):
#     # In a real implementation, this would scrape the actual website
#     # Here we'll use mock data based on the URL
    
#     # Check if URL matches any mock businesses
#     for business in SAMPLE_BUSINESSES:
#         if business['url'] in website_url:
#             return business
    
#     # Default return if no match found
#     # return {
#     #     'name': 'Example Business',
#     #     'industry': 'General',
#     #     'services': ['Service 1', 'Service 2'],
#     #     'tone': 'professional',
#     #     'url': website_url
#     # }
#     return {
#         'name': 'FitLife Gym',
#         'industry': 'Fitness',
#         'services': ['Personal Training', 'Group Classes'],
#         'tone': 'motivational',
#         'url': website_url
#     }


import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re

def scrape_business_profile(website_url):
    try:
        # 1. Validate and prepare URL
        if not re.match(r'^https?://', website_url):
            website_url = 'https://' + website_url
            
        parsed_url = urlparse(website_url)
        if not parsed_url.netloc:
            raise ValueError("Invalid URL format")
            
        # 2. Configure request headers to mimic browser
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9'
        }
        
        # 3. Make the request with timeout
        response = requests.get(
            website_url,
            headers=headers,
            timeout=10,
            allow_redirects=True
        )
        response.raise_for_status()  # Raises HTTPError for bad responses
        
        # 4. Parse content with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # 5. Extract business information
        business_name = extract_business_name(soup, parsed_url)
        description = extract_meta_description(soup)
        industry = detect_industry(parsed_url, soup)
        services = detect_services(soup)
        
        return {
            'name': business_name,
            'industry': industry,
            'services': services,
            'tone': 'professional',
            'url': website_url,
            'description': description
        }
        
    except Exception as e:
        print(f"Scraping error for {website_url}: {str(e)}")
        return get_fallback_profile(parsed_url)

# Helper functions
def extract_business_name(soup, parsed_url):
    title = soup.find('title')
    if title:
        return title.get_text().strip()
    return parsed_url.netloc.replace('www.', '').split('.')[0].title()

def extract_meta_description(soup):
    meta = soup.find('meta', attrs={'name': 'description'})
    return meta['content'][:200] if meta else ""

def detect_industry(parsed_url, soup):
    domain = parsed_url.netloc.lower()
    if any(x in domain for x in ['shop', 'store', 'market']):
        return "E-commerce"
    if any(x in domain for x in ['restaurant', 'cafe', 'food']):
        return "Food & Beverage"
    return "General"

def detect_services(soup):
    services = set()
    for a in soup.find_all('a', href=True):
        text = a.get_text().strip()
        if 2 < len(text) < 30 and text.isprintable():
            services.add(text)
    return list(services)[:5] if services else ["Online Services"]

def get_fallback_profile(parsed_url):
    domain = parsed_url.netloc.replace('www.', '').split('.')[0]
    return {
        'name': domain.title(),
        'industry': "General",
        'services': ["Online Services"],
        'tone': "professional",
        'url': parsed_url.geturl(),
        'description': ""
    }