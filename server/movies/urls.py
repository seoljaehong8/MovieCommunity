from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('makeMovieData/', views.makeMovieData, name='makeMovieData'),
    path('makeDumpData/', views.makeDumpData, name='makeDumpData'),
    path('', views.moviesList, name='moviesList'),

]