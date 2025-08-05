from datetime import datetime, timedelta
from app.utils.mock_data import POST_TEMPLATES
import random




import random
from datetime import datetime

def generate_posts(business_profile, news_items, preferences):
    try:
        # Validate inputs
        if not business_profile or not isinstance(business_profile, dict):
            raise ValueError("Invalid business profile")
            
        if not preferences or not isinstance(preferences, dict):
            preferences = {'tone': 'professional', 'post_type': 'tip'}
            
        # Extract parameters with defaults
        tone = preferences.get('tone', 'professional')
        post_type = preferences.get('post_type', 'tip')
        num_posts = min(int(preferences.get('count', 3)), 5)  # Max 5 posts
        
        # Get business details
        business_name = business_profile.get('name', 'Our business')
        industry = business_profile.get('industry', 'our industry')
        services = business_profile.get('services', ['our services'])
        
        # Templates with safe fallbacks
        TEMPLATES = {
            'professional': {
                'tip': [
                    f"Professional tip from {business_name}: {services[0]} can help improve your results",
                    f"Industry insight: Regular {services[0].lower()} leads to better outcomes",
                    f"Did you know? {business_name} specializes in {industry.lower()}"
                ],
                'promo': [
                    f"Special offer: 20% off {services[0]} this week at {business_name}",
                    f"Limited time: Upgrade your {services[0].lower()} with our exclusive deal"
                ],
                'news': [
                    f"Industry update from {business_name}: {{headline}}",
                    f"News you can use: {{summary}}"
                ]
            },
            'friendly': {
                'tip': [
                    f"Hey there! Here's a friendly tip from {business_name}: Try our {services[0].lower()}",
                    f"Quick tip: Our {services[0].lower()} can make your day easier!",
                    f"Fun fact: We love helping with {industry.lower()} at {business_name}"
                ],
                'promo': [
                    f"Exciting news! Special deals on {services[0].lower()} this week",
                    f"We're feeling generous! Ask us about our {services[0].lower()} specials"
                ],
                'news': [
                    f"Check this out: {{headline}}",
                    f"Thought you might like this: {{summary}}"
                ]
            },
            'witty': {
                'tip': [
                    f"Why did the {industry.lower()} cross the road? To get our {services[0].lower()}!",
                    f"Here's a tip so good we almost kept it to ourselves: Try our {services[0].lower()}",
                    f"Tip of the day: Our {services[0].lower()} is better than the competition's"
                ],
                'promo': [
                    f"Sale alert! Our {services[0].lower()} is flying off the shelves!",
                    f"Limited time: Get our {services[0].lower()} before we come to our senses"
                ],
                'news': [
                    f"Hot off the press: {{headline}}",
                    f"News flash: {{summary}}"
                ]
            }
        }
        
        # Generate posts
        posts = []
        for _ in range(num_posts):
            template_group = TEMPLATES.get(tone, TEMPLATES['professional'])
            template = random.choice(template_group.get(post_type, [f"Check out {business_name}'s {services[0].lower()}"]))
            
            # Fill news templates if needed
            if post_type == 'news' and news_items:
                try:
                    news_item = random.choice(news_items)
                    post = template.format(
                        headline=news_item.get('headline', 'industry news'),
                        summary=news_item.get('summary', 'interesting development')
                    )
                except:
                    post = f"Latest {industry} news from {business_name}"
            else:
                post = template
                
            posts.append(post)
            
        return posts
        
    except Exception as e:
        print(f"Error generating content: {str(e)}")
        return [f"New content from {business_profile.get('name', 'our business')} - check back soon!"]

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
