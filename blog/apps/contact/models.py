from django.db import models
from django.utils import timezone

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    title = models.CharField(max_length=150)
    message = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name