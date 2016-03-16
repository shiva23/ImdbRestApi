from rest_framework import serializers
from .models import Movie
from django.contrib.auth.models import User

class MovieSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	class Meta:
		model = Movie
		fields = ('id', 'name', 'director', 'description', 'genre', 'rate', 'owner')



class UserSerializer(serializers.ModelSerializer):
	movies = serializers.PrimaryKeyRelatedField(many=True, queryset=Movie.objects.all())

	class Meta:
		model = User
		fields = ('id', 'username', 'movies')