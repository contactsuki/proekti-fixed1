import time

import requests
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from catalog.models import Movie

SEARCH_URL = "https://api.themoviedb.org/3/search/movie"


class Command(BaseCommand):
    help = (
        "Looks up each movie on TMDB by title + year and stores its real "
        "poster_path. Requires TMDB_API_KEY to be set in the environment. "
        "Get a free key at https://www.themoviedb.org/settings/api"
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "--overwrite", action="store_true",
            help="Re-fetch posters even for movies that already have one.",
        )

    def handle(self, *args, **options):
        api_key = settings.TMDB_API_KEY
        if not api_key:
            raise CommandError(
                "TMDB_API_KEY is not set. Get a free key at "
                "https://www.themoviedb.org/settings/api, then run e.g.\n"
                "  TMDB_API_KEY=your-key-here python3 manage.py fetch_posters"
            )

        movies = Movie.objects.all()
        if not options["overwrite"]:
            movies = movies.filter(poster_path__isnull=True)

        found, missing = 0, []

        for movie in movies:
            resp = requests.get(
                SEARCH_URL,
                params={
                    "api_key": api_key,
                    "query": movie.title,
                    "year": movie.release_year,
                },
                timeout=10,
            )
            resp.raise_for_status()
            results = resp.json().get("results", [])

            if results:
                movie.poster_path = results[0].get("poster_path")
                movie.save(update_fields=["poster_path"])
                found += 1
                self.stdout.write(f"  found poster for {movie.title}")
            else:
                missing.append(movie.title)

            time.sleep(0.15)

        self.stdout.write(self.style.SUCCESS(f"Fetched {found} posters."))
        if missing:
            self.stdout.write(self.style.WARNING(
                f"No TMDB match for: {', '.join(missing)}"
            ))
