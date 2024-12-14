from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """
    Custom user model that extends the default django user model by adding
    additional fields such as city, state, address, and phone number.

    This model inherits from AbstractUser, so it includes all the default
    fields and functionality of the Django User model,
    (username, email, first name, last name, etc.) while also providing
    the flexibility to add custom fields.

    Attributes:
        city (str): The city where the user resides (optional)
        state (str): The state where the user resides (optional).
        address (str): The user's full address (optional).
        phone (str): The user's phone number (optional)

    Methods:
        __str__(): Returns the username of the user as
                    the string representation of the model.
        
    """
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username