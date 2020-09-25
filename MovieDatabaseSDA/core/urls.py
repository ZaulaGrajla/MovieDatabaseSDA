from django.contrib import admin
from django.urls import path
from core.views import hello
from core.views import welcome
from core.views import MovieCreateView, MovieUpdateView, MovieDeleteView, MovieListView, MovieDetailView
# from core.views import MovieView

app_name = 'core'

urlpatterns = [
    path("movie/list", MovieListView.as_view(), name='movie_list'),
    path("movie/detail/<pk>", MovieDetailView.as_view(), name='movie_detail'),
    path("movie/create", MovieCreateView.as_view(), name='movie_create'),
    path("movie/update/<pk>", MovieUpdateView.as_view(), name='movie_update'),
    path("movie/delete/<pk>", MovieDeleteView.as_view(), name='movie_delete'),
]