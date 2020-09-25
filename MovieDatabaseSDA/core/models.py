from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from model_utils import Choices

AGE_LIMITS = Choices(
    (0, 'kids', 'children'),
    (1, 'teens', 'teenagers'),
    (2, 'adults', 'adult people'),
)


class Country(models.Model):
    name = models.TextField(max_length=30, default='USA', unique=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class BoxOffice(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, default=Country)
    amount = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return f"{self.country} - {self.amount} of money"


class Director(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=30)
    birth_date = models.DateField(null=True, blank=True)
    rating = models.IntegerField(
        null=True, validators=[MaxValueValidator(10), MinValueValidator(1)]
    )

    class Meta:
        unique_together = ('name', 'surname')

    def __str__(self):
        return self.name + " " + self.surname


class Genre(models.Model):
    name = models.CharField(max_length=20, unique=True)
    age_limit = models.IntegerField(
        choices=AGE_LIMITS,
        blank=True,
        null=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=70)
    rating = models.IntegerField(
        null=True, blank=True, validators=[MaxValueValidator(10), MinValueValidator(1)]
    )
    released = models.DateField()
    description = models.TextField(null=True, blank=True)
    # null do baz danych a blank do formularzy
    created = models.DateTimeField(auto_now_add=True)
    genre = models.ForeignKey(Genre, null=True, on_delete=models.SET_NULL, blank=True)
    director = models.ForeignKey(Director, null=True, on_delete=models.SET_NULL, blank=True)
    countries = models.ManyToManyField(Country, 'movies')
    boxoffices = models.ManyToManyField(BoxOffice, 'movies', blank=True)

    class Meta:
        unique_together = ('title', 'released', 'director')
        ordering = ('title',)

    def __str__(self):
        return f"{self.title} from {self.released}"
