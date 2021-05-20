from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('makeMovieData/', views.make_movieData),
    path('makeDumpData/', views.make_dumpData),
    path('', views.movie_list),
    path('<int:movie_pk>/', views.movie_detail),

]