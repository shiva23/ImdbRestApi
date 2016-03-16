
from .models import Movie
from .serializers import MovieSerializer, UserSerializer
from rest_framework import generics, permissions
from django.contrib.auth.models import User


class MovieList(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	queryset = Movie.objects.all()
	serializer_class = MovieSerializer

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)


class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	queryset = Movie.objects.all()
	serializer_class = MovieSerializer


class UserList(generics.ListAPIView):
	queryset = Movie.objects.all()
	serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
	queryset = Movie.objects.all()
	serializer_class = UserSerializer

