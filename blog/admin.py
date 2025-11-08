from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'date_created', 'date_modified')
    list_filter = ('status', 'author', 'date_created')
    search_fields = ('title', 'text')
    date_hierarchy = 'date_created'
    ordering = ('-date_created',)