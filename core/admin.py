from django.contrib import admin
from .models import CustomUser

# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    add_fieldsets = (
        # The outer tuple contains a single item (None, {...}), where None
        # represents a section title for the form.
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name',
                       'last_name', 'password1', 'password2', 'city', 'state',
                       'address', 'phone', 'is_staff', 'is_active'
                    )
        }),
    )