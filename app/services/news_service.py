import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
import re

def get_industry_news(industry):
    try:
        # Validate input
        if not industry or not isinstance(industry, str):
            raise ValueError("Industry must be a non-empty string")
            
        # Prepare search query
        search_query = f"{industry} industry trends 2023"
        encoded_query = quote(search_query)
        
        # Mock news data - replace with real API calls in production
        MOCK_NEWS = {
            "fitness": [
                {
                    "headline": "Top 5 Fitness Trends for 2023",
                    "source": "Fitness Magazine",
                    "url": "https://example.com/fitness-trends-2023",
                    "summary": "High-intensity interval training remains popular while recovery-focused workouts gain traction."
                },
                {
                    "headline": "How Technology is Changing the Fitness Industry",
                    "source": "Tech Health Journal",
                    "url": "https://example.com/fitness-tech",
                    "summary": "Wearables and AI coaches are revolutionizing personal fitness."
                }
            ],
            "technology": [
                {
                    "headline": "AI Breakthroughs in 2023",
                    "source": "Tech Today",
                    "url": "https://example.com/ai-2023",
                    "summary": "New generative AI models are transforming multiple industries."
                }
            ]
        }
        
        # Return mock data if available
        industry_key = industry.lower()
        if industry_key in MOCK_NEWS:
            return MOCK_NEWS[industry_key]
            
        # Fallback to general news
        return [{
            "headline": f"Latest {industry.capitalize()} Industry Updates",
            "source": "General News",
            "url": f"https://news.google.com/search?q={encoded_query}",
            "summary": f"Search for {industry} industry news on Google News"
        }]
        
    except Exception as e:
        print(f"Error fetching news for {industry}: {str(e)}")
        return [{
            "headline": "Error fetching industry news",
            "source": "System",
            "url": "",
            "summary": str(e)
        }]