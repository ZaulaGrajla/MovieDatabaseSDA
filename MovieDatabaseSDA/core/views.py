from django.http import HttpResponse
from django.shortcuts import render
from django import views
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, FormView, CreateView, UpdateView, DeleteView, DetailView

from core.models import Movie, AGE_LIMITS
from core.forms import MovieForm
import logging


# CHECK OUT REVERSE_LAZY AND LOGGER!!!!!!!!!!!!!!!!!!!!!!!!!!

logging.basicConfig(filename='log.txt',
                    filemode='w',
                    level=logging.INFO,
                    )
LOGGER = logging.getLogger(__name__)


# class MovieCreateView(FormView):
#     template_name = 'form.html'
#     form_class = MovieForm
#     success_url = reverse_lazy('movie_create')  # from django.urls
#
#     def form_valid(self, form):
#         result = super().form_valid(form)
#         cleaned_data = form.cleaned_data
#         Movie.objects.create(
#             title=cleaned_data['title'],
#             genre=cleaned_data['genre'],
#             rating=cleaned_data['rating'],
#             released=cleaned_data['released'],
#             description=cleaned_data['description'],
#         )
#         return result

class MovieCreateView(CreateView):
    title = 'Add movie'
    template_name = 'form.html'
    form_class = MovieForm
    success_url = reverse_lazy('core:movie_list')

    def form_invalid(self, form):
        LOGGER.warning("Invalid data provided")
        return super().form_invalid(form)

    def post(self, request, *args, **kwargs):
        result = super().post(request, *args, **kwargs)
        LOGGER.info(f"Movie titled {request.__dict__['_post']['title']} was added")
        return result


class MovieUpdateView(UpdateView):
    template_name = 'form.html'
    model = Movie
    form_class = MovieForm
    success_url = reverse_lazy('core:movie_list')

    def form_invalid(self, form):
        LOGGER.warning("Invalid data provided")
        return super().form_invalid(form)


class MovieDeleteView(DeleteView):
    template_name = 'movie_confirm_delete.html'
    model = Movie
    success_url = reverse_lazy('core:movie_list')


def welcome(request):
    return HttpResponse(f"Welcome Paulina 2 and 2 is {2 * 2}")


#
# def hello(request):
#     return HttpResponse("Hello world you maniac")

def hello(request):
    LOGGER.warning("\n\nCos smiesznego. Wrreszczie dzialalalalal sasasasa")
    return render(request,
                  template_name='hello.html',
                  context={'adjectives': ['beautiful', 'wonderful', 'maniac', 'cruel', 'nice']},
                  )


# def movies(request):
#     return render(request,
#                   template_name='movies.html',
#                   context={'movies': Movie.objects.all(), 'age_limits': AGE_LIMITS})


# class MovieView(views.View):
#     def get(self, request):
#         return render(request,
#                       template_name='movies.html',
#                       context={'movies': Movie.objects.all()})

# class MovieView(TemplateView):
#     template_name = 'movies.html'
#     extra_context = {'movies': Movie.objects.all(), 'age_limits': AGE_LIMITS}


# class MovieView(ListView):
#     template_name = 'movies.html'
#     model = Movie
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['age_limits'] = AGE_LIMITS
#         return context

class MovieListView(ListView):
    template_name = 'movie_list.html'
    model = Movie


class MovieDetailView(DetailView):
    template_name = 'movie_detail.html'
    model = Movie


class IndexView(MovieListView):
    template_name = 'index.html'
