from rest_framework import serializers

from .models import Genre, Movie

TMDB_IMAGE_BASE = "https://image.tmdb.org/t/p/w500"


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name", "slug"]


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    poster_url = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "slug",
            "tagline",
            "synopsis",
            "director",
            "cast",
            "release_year",
            "runtime_minutes",
            "content_rating",
            "score",
            "poster_theme",
            "poster_url",
            "is_featured",
            "is_trending",
            "genres",
        ]

    def get_poster_url(self, obj):
        if obj.poster_path:
            return f"{TMDB_IMAGE_BASE}{obj.poster_path}"
        return None
