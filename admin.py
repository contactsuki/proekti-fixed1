from django.contrib import admin

from .models import Genre, Movie


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name",)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "release_year", "content_rating", "score", "is_featured", "is_trending")
    list_filter = ("genres", "is_featured", "is_trending", "content_rating")
    search_fields = ("title", "director")
    prepopulated_fields = {"slug": ("title",)}
