from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.
class InputText(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text