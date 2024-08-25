from django.db import models


class Restaurant(models.Model):
    objects = None
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    website = models.CharField(max_length=200)
    contact_phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name
