class BusinessProfile:
    def __init__(self, name=None, industry=None, services=None, tone=None, url=None):
        self.name = name or "Unknown Business"
        self.industry = industry or "General"
        self.services = services or []
        self.tone = tone or "professional"
        self.url = url or ""
    
    def to_dict(self):
        return {
            'name': self.name,
            'industry': self.industry,
            'services': self.services,
            'tone': self.tone,
            'url': self.url
        }