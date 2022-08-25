from django.db import models
from datetime import datetime
import pytz
tz = pytz.timezone('Asia/Kolkata')
# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=100, unique=True, blank=False)
    content = models.TextField(default='', blank=True)
    created_at = models.DateTimeField(default=datetime.now(tz))
    last_updated = models.DateTimeField(default=datetime.now(tz))
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-last_updated']
        verbose_name = 'Posts'
        verbose_name_plural = 'Posts'

    

