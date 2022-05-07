from django.contrib import admin
from .models import Posts
# Register your models here.

class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at')

admin.site.register(Posts, PostsAdmin)