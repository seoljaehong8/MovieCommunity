from typing import Collection, OrderedDict
from django.shortcuts import render, get_list_or_404

import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import json

from . models import Movies
from .serializers import MovieSerializer

# Create your views here.
# 데이터베이스에 영화 정보 저장하기
def makeMovieData(request):

    page = 0

    genre_dict = {28: '액션', 12: '어드벤처', 16: '애니메이션', 35: '코디미', 80: '범죄', 99: '다큐멘터리', 18: '드라마', 
        10751: '가족', 14: '판타지', 36: '역사', 27: '공포', 10402: '음악', 9648: '미스테리', 10749: '로맨스', 
        878: 'SF', 10770: 'TV 영화', 53: '스릴러', 10752: '전쟁', 37: '서부'
    }

    while page <= 499:
        print(page)
        page += 1
        url = f'https://api.themoviedb.org/3/movie/popular?api_key=6b3db2093be8e14d01eccd56d390ec42&language=ko&page={page}'
        response = requests.get(url)
        datas = response.json()
        datas = datas['results']
        
        for data in datas:
            overview = data['overview']
            
            if overview == '':
                continue
            title = data['title']
            number = data['id']
            genre = data['genre_ids']

            genre_list = ''
            for idx in range(len(genre)):
                genre_list += genre_dict[genre[idx]]
                if idx != len(genre)-1:
                    genre_list += ','

            poster_path = data['poster_path']
            release_date = data['release_date']
            vote_average = data['vote_average']
            vote_count = data['vote_count']
            popularity = data['popularity']
    
            movie = Movies(title=title,genre=genre_list,overview=overview,
                poster_path=poster_path,release_date=release_date,vote_average=vote_average,
                vote_count=vote_count,popularity=popularity)
            movie.save()  

            # overview = data['overview']

            # if overview[0] == '':
            #     continue
            # title = data['title']
            # number = data['id']
            # genre = data['genre_ids']

            # genre_list = []
            # for g in genre[0]:
            #     genre_list.append(genre_dict[g])

            # poster_path = data['poster_path']
            # release_date = data['release_date']
            # vote_average = data['vote_average']
            # vote_count = data['vote_count']
            # popularity = data['popularity']
    
            # movie = Movies(number=number[0],title=title[0],genre=genre_list,overview=overview[0],
            #     poster_path=poster_path[0],release_date=release_date[0],vote_average=vote_average[0],
            #     vote_count=vote_count[0],popularity=popularity[0])
            # movie.save()   



    return render(request,'list.html')


@api_view(['GET'])
def makeDumpData(request):

    movies = get_list_or_404(Movies)
    serializer = MovieSerializer(movies,many=True)


    with open('movies.json','w',encoding='utf-8') as make_file:
        json.dump(serializer.data ,make_file, ensure_ascii=False, indent='\t')

    return Response(serializer.data)


@api_view(['GET'])
def moviesList(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movies)
        serializer = MovieSerializer(movies,many=True)

        return Response(serializer.data[:50])