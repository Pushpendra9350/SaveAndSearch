from django.db import models
# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=100, unique=True, blank=False)
    content = models.TextField(default='', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Posts'
        verbose_name_plural = 'Posts'

    

