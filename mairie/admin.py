from django.contrib import admin
from .models import Cooeperatives, Members, Partenaire, MemberComment, CooperativeComment


# Register your models here.

admin.site.site_header = "AGRI-MAIRIE"
class CooeperativeAdmin(admin.ModelAdmin):
    list_display = ("user", "name", "city", "created_at")

admin.site.register(Cooeperatives, CooeperativeAdmin)

class MemberAdmin(admin.ModelAdmin):
    list_display = ("user", "name", "phone_number", "cooeperative")
    list_filter = ["cooeperative"]


@admin.register(MemberComment)
class MemberCommentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'Subject', 'timestamp', 'active')
    list_filter = ('timestamp', 'active')
    search_fields = ('name', 'email', 'comment')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


@admin.register(CooperativeComment)
class CooperativeCommentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'Subject', 'timestamp', 'active')
    list_filter = ('timestamp', 'active')
    search_fields = ('name', 'email', 'comment')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(Members, MemberAdmin)
admin.site.register(Partenaire)