from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import date

# Create your models here.
current_year = timezone.now().year
current_date = timezone.now().date()

def validate_year(year):
    if not(1800 <= year <= current_year):
        raise ValidationError(f"The year needs to be between 1800 and {current_year}")
    
# def validate_date(date):
#     if not()

class Artist(models.Model):
    name = models.CharField(validators=[MinLengthValidator(2)], max_length=255)
    debut = models.PositiveIntegerField(validators=[validate_year])
    image = models.ImageField(upload_to="artist_images/", blank=True, null=True)

    def __str__(self):
        return f"{self.name}"
    

class Album(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField(validators=[MinValueValidator(date(1800, 1, 1)), MaxValueValidator(current_date)])
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    cover_image = models.ImageField(upload_to="album_covers/", blank=True, null=True)

    def __str__(self):
        return f"{self.title} by {self.artist}"
