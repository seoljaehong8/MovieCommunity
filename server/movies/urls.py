from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('getmovies/', views.getmovies, name='getmovies'),
    path('listmovies/', views.listmovies, name='listmovies'),

]