from django.db import models

from django.core.validators import MinLengthValidator

from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class GenreChoices(models.TextChoices):
    ACTION = 'AC', 'Action'
    DRAMA = 'DR', 'Drama'
    COMEDY = 'CO', 'Comedy'
    HORROR = 'HO', 'Horror'
    ROMANCE = 'RO', 'Romance'
    SCIFI = 'SF', 'Science Fiction'
    FANTASY = 'FA', 'Fantasy'
    DOCUMENTARY = 'DO', 'Documentary'
    THRILLER = 'TH', 'Thriller'


class Movie(models.Model):
    title = models.CharField(max_length=255, validators=[MinLengthValidator(2)])
    director = models.CharField(max_length=255, validators=[MinLengthValidator(2)])
    release_date = models.DateField()
    genre = models.CharField(max_length=2, choices=GenreChoices.choices)
    synopsis = models.TextField(validators=[MinLengthValidator(10)])
    poster = models.ImageField(upload_to="movie-images/", default="default.jpg")
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
