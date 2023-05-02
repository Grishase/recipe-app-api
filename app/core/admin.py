from django.contrib import admin # noqa 
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
"""Tells the flake 8 with noqa to ignore that command """
"""Django admin customization"""

from core import models 
# Register your models here.
class UserAdmin(BaseUserAdmin):
    """Define admin page for users."""
    ordering=['id']
    list_display = ['email','name']
    fieldsets=(
        (None, {'fields':('email', 'password')}),
        (
            _('Permissions'),
            {
                'fields':(
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (_('Important dates'),{'fields':('last_login',)}),

    )
    readonly_fields=['last_login']
    add_fieldsets=(
        (None, {
            'classes': ('tight',), # changes the space in between
            'fields':(
                'email',
                'password1',
                'password2',
                'name',
                'is_active',
                'is_staff',
                'is_superuser',
            )
        }),
    )

admin.site.register(models.User, UserAdmin)