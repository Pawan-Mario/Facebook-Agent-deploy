SAMPLE_BUSINESSES = [
    {
        'name': 'FitLife Gym',
        'industry': 'Fitness',
        'services': ['Personal Training', 'Group Classes', 'Yoga Sessions'],
        'tone': 'motivational',
        'url': 'fitlifegym.com'
    },
    {
        'name': 'Urban Cafe',
        'industry': 'Food & Beverage',
        'services': ['Coffee', 'Breakfast', 'Lunch'],
        'tone': 'friendly',
        'url': 'urbancafe.com'
    }
]

POST_TEMPLATES = {
    'promotional': [
        "🎉 Limited Time Offer! {service} at just ${price}. Book now!",
        "🔥 Hot Deal: Get {discount}% off on your next visit!"
    ],
    'tips': [
        "Pro Tip: {tip_content} #IndustryTips",
        "Did you know? {fact_about_industry}"
    ],
    'seasonal': [
        "Happy Holidays from {business_name}! 🎄",
        "Wishing you a wonderful {season} season!"
    ]
}

INDUSTRY_NEWS = {
    'Fitness': [
        {'headline': 'New study shows 30 minutes of exercise boosts productivity', 'source': 'Health Journal'},
        {'headline': 'Top 5 fitness trends for 2025', 'source': 'Fitness Magazine'}
    ],
    'Food & Beverage': [
        {'headline': 'Sustainable coffee practices gaining popularity', 'source': 'Food News'},
        {'headline': 'How cafes are adapting to post-pandemic world', 'source': 'Business Daily'}
    ]
}

INDUSTRY_NEWS = {
    "Fitness": [
        {
            "headline": "New Study Shows 30 Minutes of Daily Exercise Boosts Productivity",
            "source": "Health Journal",
            "url": "https://example.com/fitness-study"
        },
        {
            "headline": "Top 5 Fitness Trends for 2024",
            "source": "Fitness Magazine",
            "url": "https://example.com/fitness-trends"
        }
    ],
    "Food": [
        {
            "headline": "Sustainable Eating Trends on the Rise",
            "source": "Food Network",
            "url": "https://example.com/food-trends"
        }
    ],
    "Technology": [
        {
            "headline": "AI Revolutionizing Business Operations",
            "source": "Tech Today",
            "url": "https://example.com/ai-business"
        }
    ]
}