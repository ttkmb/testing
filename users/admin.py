from django.contrib import admin
from django.utils.translation import gettext_lazy
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name']
    list_filter = ['is_active']
    search_fields = ['first_name', 'last_name', 'email']
    exclude = ['password']
    filter_horizontal = [
        'groups',
        'user_permissions',
    ]
    save_on_top = True
    fieldsets = (
        (
            gettext_lazy('Personal info'),
            {
                'fields': (
                    'username',
                    'first_name',
                    'last_name',
                    'email',
                )
            }
        ),
        (
            gettext_lazy('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                ),
            },
        ),
        (
            gettext_lazy('Important dates'),
            {
                'fields': (
                    'last_login',
                    'date_joined',
                )
            }
        ),
    )
