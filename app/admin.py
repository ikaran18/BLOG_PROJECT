from django.contrib import admin
from app.models import Blog,Comment
# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','author','created_at']
    
admin.site.register(Comment)