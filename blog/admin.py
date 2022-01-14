from django.contrib import admin
from .models import Post, Comment, Authors

# Register your models here.
class postsAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_on', 'published')
    list_filter = ('published',)
    search_fields = ['title', 'content']
    ordering = ('-created_on',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'subject', 'timestamp', 'active')
    list_filter = ('timestamp', 'active')
    search_fields = ('name', 'email', 'comment')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

admin.site.register(Post, postsAdmin)
admin.site.register(Authors)

