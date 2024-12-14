from django.contrib import admin
from .models import CustomUser

# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    """
    Admin configuration for the CustomerUser model.
    This class customizes the display and functionality of the CustomUser model
    within the Django admin interface.

    Attributes:
        - add_fieldsets (tuple): Defines the fields and layout for adding new
        users in the admin interface.  It specifies which fields are shown
        during the creation of a new CustomUser.
    """
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