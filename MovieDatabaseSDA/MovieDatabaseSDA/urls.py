"""MovieDatabaseSDA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core.views import hello
from core.views import welcome
from core.views import MovieCreateView, MovieUpdateView, MovieDeleteView, IndexView
# from core.views import MovieView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('welcome/', welcome),
    path('', IndexView.as_view(), name='index'),
    path("core/", include("core.urls", namespace="core")),
]

# path('', MovieView.as_view(), name='index'),
# path('', movies, name='index'),
