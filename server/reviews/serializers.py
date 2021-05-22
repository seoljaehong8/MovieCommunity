from rest_framework import serializers
from .models import Review, Comment
from movies.models import Movies
from movies.serializers import MovieSerializer

class ReviewSerializer(serializers.ModelSerializer):
    movie_title = serializers.ReadOnlyField(source='movie.title')
    poster_path = serializers.ReadOnlyField(source='movie.poster_path')
    user_name = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Review
        # fields="__all__"
        fields = ('id','title','content','user_id', 'created_at','updated_at','username','movie_title','poster_path','user_name')


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id','review_id','user_id','content','username','created_at','updated_at')
