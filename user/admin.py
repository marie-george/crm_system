from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'username', 'email', 'is_active', 'is_staff'
    )
    list_display_links = (
        'id', 'username'
    )
    search_fields = (
        'id', 'username', 'email'
    )
    list_filter = (
        'is_active', 'is_staff'
    )
    list_editable = (
        'is_active', 'is_staff'
    )


admin.site.register(User, UserAdmin)

