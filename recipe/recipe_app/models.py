from django.db import models

from django.core.validators import MinLengthValidator, MinValueValidator

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=255, validators=[MinLengthValidator(2)])
    ingredients = models.TextField(validators=[MinLengthValidator(2)])
    instructions = models.TextField(validators=[MinLengthValidator(2)])
    cooking_time = models.PositiveIntegerField(validators=[MinValueValidator(2)])
    image = models.ImageField(upload_to="recipe_images/", blank=True, null=True)

    def __str__(self):
        return self.name
