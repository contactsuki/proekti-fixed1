from django.db import models
from django.utils.text import slugify


POSTER_THEMES = [
    ("ember", "Ember"),
    ("wine", "Wine"),
    ("teal", "Teal"),
    ("indigo", "Indigo"),
    ("gold", "Gold"),
    ("slate", "Slate"),
]


class Genre(models.Model):
    name = models.CharField(max_length=40, unique=True)
    slug = models.SlugField(max_length=40, unique=True, blank=True)

    class Meta:
        ordering = ["name"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=140, unique=True, blank=True)
    tagline = models.CharField(max_length=160, blank=True)
    synopsis = models.TextField()
    director = models.CharField(max_length=100, blank=True)
    cast = models.JSONField(default=list, blank=True, help_text="List of actor names")
    release_year = models.PositiveSmallIntegerField()
    runtime_minutes = models.PositiveSmallIntegerField()
    content_rating = models.CharField(max_length=10, default="PG-13")
    score = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    poster_theme = models.CharField(max_length=10, choices=POSTER_THEMES, default="slate")
    poster_path = models.CharField(
        max_length=200, blank=True, null=True,
        help_text="TMDB poster_path (e.g. /abc123.jpg), filled in by 'manage.py fetch_posters'",
    )
    is_featured = models.BooleanField(default=False)
    is_trending = models.BooleanField(default=False)
    genres = models.ManyToManyField(Genre, related_name="movies")
    added_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-score", "title"]

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title)
            slug = base
            n = 1
            while Movie.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                n += 1
                slug = f"{base}-{n}"
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.release_year})"
