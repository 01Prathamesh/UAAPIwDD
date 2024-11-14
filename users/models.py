from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator

class User(AbstractUser):
    phone_number = models.CharField(
        max_length=15, 
        validators=[RegexValidator(r'^\+91\d{10}$', 'Enter a valid Indian phone number')],
    )
    date_of_birth = models.DateField()
    last_login_ip = models.GenericIPAddressField(null=True, blank=True)

    def __str__(self):
        return self.username