from django.db.models import Q
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Genre, Movie
from .serializers import GenreSerializer, MovieSerializer


class GenreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = None


class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MovieSerializer

    def get_queryset(self):
        qs = Movie.objects.prefetch_related("genres").all()

        genre = self.request.query_params.get("genre")
        if genre:
            qs = qs.filter(genres__slug=genre)

        search = self.request.query_params.get("search")
        if search:
            qs = qs.filter(
                Q(title__icontains=search) | Q(director__icontains=search)
            )

        return qs.distinct()

    @action(detail=False)
    def featured(self, request):
        movies = Movie.objects.prefetch_related("genres").filter(is_featured=True)
        return Response(MovieSerializer(movies, many=True).data)

    @action(detail=False)
    def trending(self, request):
        movies = Movie.objects.prefetch_related("genres").filter(is_trending=True)
        return Response(MovieSerializer(movies, many=True).data)
