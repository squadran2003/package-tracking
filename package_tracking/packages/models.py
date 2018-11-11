from django.db import models
from django.utils import timezone
from customers.models import Customer


class Package(models.Model):
    statuses = (
        ('out for delivery', 'out for delivery'),
        ('delivered', 'delivered')
    )
    name = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, choices=statuses,
                              default='out for delivery')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class TransitStage(models.Model):
    description = models.CharField(max_length=255)
    package = models.ManyToManyField(Package)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{} at {}".format(self.package.name, self.description)
