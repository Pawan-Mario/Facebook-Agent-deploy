from datetime import datetime, timedelta
from app.utils.mock_data import POST_TEMPLATES
import random

def generate_posts(business_profile, news_items, preferences):
    tone = preferences.get('tone', 'professional')
    post_type = preferences.get('post_type', 'tip')
    
    posts = []
    
    # Generate promotional posts
    if post_type == 'promo':
        for service in business_profile.get('services', [])[:2]:
            posts.append(
                f"🎉 Special Offer! Get 20% off our {service} this week! "
                f"DM us to book your spot. #{business_profile.get('name', '').replace(' ', '')}"
            )
    
    # Generate tips/insights
    if post_type in ['tip', 'insight']:
        for news in news_items[:2]:
            posts.append(
                f"Did you know? {news.get('headline')} "
                f"Read more about this {business_profile.get('industry')} trend!"
            )
    
    # Add seasonal greetings if appropriate
    if random.random() > 0.7:  # 30% chance
        posts.append(random.choice(POST_TEMPLATES['seasonal']))
    
    return posts

def schedule_posts(posts, frequency, preferred_days):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    if preferred_days:
        selected_days = [day for day in preferred_days if day in days]
    else:
        selected_days = random.sample(days[:5], min(frequency, 5))  # Weekdays only
    
    schedule = {}
    for i, day in enumerate(selected_days):
        if i < len(posts):
            schedule[day] = {
                'post': posts[i],
                'scheduled_time': f"10:{15*i % 60}"  # Stagger times
            }
    
    return schedule