from django.db import models

from django.core.validators import MinLengthValidator

# Create your models here.

class CategoryChoices(models.TextChoices):
    WORK = 'WK','Work'
    PERSONAL = 'PSNL','Personal'
    IDEAS = 'IDE','Ideas'

class Note(models.Model):
    title = models.CharField(max_length=255, validators=[MinLengthValidator(2)])
    category = models.CharField(max_length=4, choices=CategoryChoices.choices)
    content = models.TextField()
    date_created = models.DateField(auto_now_add=True)