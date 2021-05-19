from typing import OrderedDict
from django.shortcuts import render

import requests

from . models import Movies

# Create your views here.
def getmovies(request):
    page = 0

    genre_dict = {28: 'Action', 12: 'Adventure', 16: 'Animation', 35: 'Comedy', 80: 'Crime', 99: 'Documentary', 18: 'Drama', 
        10751: 'Family', 14: 'Fantasy', 36: 'History', 27: 'Horror', 10402: 'Music', 9648: 'Mystery', 10749: 'Romance', 
        878: 'Science Fiction', 10770: 'TV Movie', 53: 'Thriller', 10752: 'War', 37: 'Western'
    }

    while page <= 499:
        print(page)
        page += 1
        response = requests.get(f'https://api.themoviedb.org/3/movie/popular?api_key=6b3db2093be8e14d01eccd56d390ec42&language=ko&page={page}')
        datas = response.json()
        datas = datas['results']
        
        for data in datas:
            overview = data['overview'],
            if overview[0] == '':
                continue
            title = data['title'],
            genre = data['genre_ids'],

            genre_list = []
            for g in genre[0]:
                genre_list.append(genre_dict[g])

            poster_path = data['poster_path'],
            release_date = data['release_date'],
            vote_average = data['vote_average'],
            vote_count = data['vote_count'],
            popularity = data['popularity'],
    
            movie = Movies(title=title[0],genre=genre_list,overview=overview[0],
                poster_path=poster_path[0],release_date=release_date[0],vote_average=vote_average[0],
                vote_count=vote_count[0],popularity=popularity[0])
            movie.save()   


    return render(request,'list.html')