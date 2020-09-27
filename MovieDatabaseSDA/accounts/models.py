from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shoe_size = models.IntegerField(
        null=True, blank=True, validators=[MaxValueValidator(30), MinValueValidator(55)]
    )

