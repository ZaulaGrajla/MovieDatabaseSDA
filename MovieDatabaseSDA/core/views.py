from django.http import HttpResponse
from django.shortcuts import render
from django import views
from django.views.generic import TemplateView

from core.models import Movie, AGE_LIMITS


def welcome(request):
    return HttpResponse(f"Welcome Paulina 2 and 2 is {2 * 2}")


#
# def hello(request):
#     return HttpResponse("Hello world you maniac")

def hello(request):
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

class MovieView(TemplateView):
    template_name = 'movies.html'
    extra_context = {'movies': Movie.objects.all(), 'age_limits': AGE_LIMITS}
