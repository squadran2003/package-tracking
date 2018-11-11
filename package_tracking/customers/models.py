from django.db import models
from django.utils import timezone


class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(default='')
    address = models.TextField(default='')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.first_name
