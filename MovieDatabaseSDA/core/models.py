from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Genre(models.Model):
    name = models.CharField(max_length=20, unique=True)
    age_limit = models.IntegerField(
        choices=[(7, 'little kid'), (13, 'teen'), (18, 'EU adult'), (21, 'US adult'), (36, 'senator')],
        blank=True,
        null=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=70)
    rating = models.IntegerField(
        null=True, validators=[MaxValueValidator(10), MinValueValidator(1)]
    )
    released = models.DateField()
    description = models.TextField(null=True, blank=True)
    # null do baz danych a blank do formularzy
    created = models.DateTimeField(auto_now_add=True)
    genre = models.ForeignKey(Genre, null=True, on_delete=models.SET_NULL, blank=True)

    def __str__(self):
        return f"{self.title} from {self.released}"
