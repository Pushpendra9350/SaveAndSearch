from django.contrib import admin
from .models import Posts
from import_export.admin import ImportExportModelAdmin
# Register your models here.

# class PostsAdmin(admin.ModelAdmin):
#     list_display = ('title', 'updated_at')

@admin.register(Posts)
class PostsAdmin(ImportExportModelAdmin):
    list_display = ('title', 'updated_at')
    