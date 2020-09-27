from core.views import MovieListView


class IndexView(MovieListView):
    title = 'Welcome to Django Movies Database you filthy bastard!'
    template_name = 'index.html'
