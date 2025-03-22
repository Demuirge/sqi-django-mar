from django.db import models

from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255, validators=[MinLengthValidator(5)])
    author = models.CharField(max_length=255, validators=[MinLengthValidator(2)])
    publication_date = models.DateField()
    book_image = models.ImageField(upload_to="book-covers/", blank=True, null=True)

    def __str__(self):
        return f"{self.title} by {self.author}"


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reviewer_name = models.CharField(max_length=255, validators=[MinLengthValidator(2)])
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(validators=[MinLengthValidator(2)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.book}({self.rating} stars    ) reviewed by {self.reviewer_name}"
