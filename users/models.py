from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('investor', 'Investor'),
        ('entrepreneur', 'Entrepreneur'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, blank=False, null=False)
    bio = models.TextField(blank=True, null=True)
    portfolio = models.URLField(blank=True, null=True)
    