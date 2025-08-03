from datetime import datetime

class ScheduledPost:
    def _init_(self, content, scheduled_day, scheduled_time, status='pending'):
        self.content = content
        self.scheduled_day = scheduled_day
        self.scheduled_time = scheduled_time
        self.status = status
        self.created_at = datetime.now().isoformat()
    
    def to_dict(self):
        return {
            'content': self.content,
            'scheduled_day': self.scheduled_day,
            'scheduled_time': self.scheduled_time,
            'status': self.status,
            'created_at': self.created_at
        }