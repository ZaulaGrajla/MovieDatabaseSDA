from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Movie(models.Model):
    title = models.CharField(max_length=70)
    rating = models.IntegerField(
        null=True, validators=[MaxValueValidator(10), MinValueValidator(1)]
    )
    released = models.DateField()
    description = models.TextField(null=True, blank=True)
    # null do baz danych a blank do formularzy
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} from {self.released}"