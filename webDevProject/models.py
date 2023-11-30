from django.db import models


class Membership(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.CharField(max_length=100, blank=False, null=False)
    subject = models.CharField(max_length=100, blank=False, null=False)
    message = models.CharField(max_length=200, blank=False, null=False)
    status = models.CharField(max_length=10, blank=False, null=False)

    def __str__(self):
        return self.name
