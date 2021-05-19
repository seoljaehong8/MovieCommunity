import requests
from pprint import pprint

# Create your views here.
def getmovies():
    response = requests.get('https://api.themoviedb.org/3/movie/popular?api_key=6b3db2093be8e14d01eccd56d390ec42&language=ko&page=1')
    data = response.json()
    pprint(data)

getmovies()