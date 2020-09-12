from django.contrib import admin
from core.models import Movie, Genre, Director, Country, BoxOffice

admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Director)
admin.site.register(Country)
admin.site.register(BoxOffice)
