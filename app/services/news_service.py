from app.utils.mock_data import INDUSTRY_NEWS  # We'll add mock data next

def get_industry_news(industry):
    """
    Get news items for a specific industry
    In a real implementation, this would call an external API or scrape news sites
    """
    # Simple implementation with mock data
    return INDUSTRY_NEWS.get(industry, [])