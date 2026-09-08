from django.core.management.base import BaseCommand

from catalog.models import Genre, Movie

MOVIES = [
    dict(
        title="Inception", tagline="A dream inside a dream inside a job.",
        synopsis="A thief who steals secrets through shared dreaming is offered a shot at "
                 "redemption: plant an idea instead of stealing one, across dream layers "
                 "that get less stable the deeper the team goes.",
        director="Christopher Nolan", cast=["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Elliot Page"],
        release_year=2010, runtime_minutes=148, content_rating="PG-13", score=8.4,
        poster_theme="indigo", genres=["Sci-Fi", "Thriller"], is_featured=True, is_trending=True,
    ),
    dict(
        title="Parasite", tagline="A basement, a hillside, and everything between.",
        synopsis="A struggling family cons its way into working for a wealthy household one job "
                 "at a time, until the house's own buried history turns their plan upside down.",
        director="Bong Joon-ho", cast=["Song Kang-ho", "Lee Sun-kyun", "Cho Yeo-jeong"],
        release_year=2019, runtime_minutes=132, content_rating="R", score=8.5,
        poster_theme="slate", genres=["Thriller", "Drama"], is_featured=True, is_trending=True,
    ),
    dict(
        title="The Grand Budapest Hotel", tagline="Concierge, legacy, one very good bellboy.",
        synopsis="A legendary concierge and his protege get tangled in a stolen painting, a "
                 "vast inheritance, and a prison break, all across a fictional European republic "
                 "between the wars.",
        director="Wes Anderson", cast=["Ralph Fiennes", "Tony Revolori", "Saoirse Ronan"],
        release_year=2014, runtime_minutes=99, content_rating="R", score=8.1,
        poster_theme="gold", genres=["Comedy", "Drama"], is_featured=False, is_trending=True,
    ),
    dict(
        title="Spirited Away", tagline="Work hard, remember your name.",
        synopsis="A ten-year-old girl wanders into a bathhouse for spirits and has to earn her "
                 "way out after her parents are turned into pigs, working alongside gods, "
                 "ghosts, and one very complicated dragon boy.",
        director="Hayao Miyazaki", cast=["Rumi Hiiragi", "Miyu Irino", "Mari Natsuki"],
        release_year=2001, runtime_minutes=125, content_rating="PG", score=8.6,
        poster_theme="teal", genres=["Animation"], is_featured=True, is_trending=False,
    ),
    dict(
        title="Get Out", tagline="Meeting the parents was never the hard part.",
        synopsis="A young man's weekend visiting his girlfriend's family starts polite and gets "
                 "steadily stranger, until the hospitality reveals exactly what it's hospitality for.",
        director="Jordan Peele", cast=["Daniel Kaluuya", "Allison Williams", "Bradley Whitford"],
        release_year=2017, runtime_minutes=104, content_rating="R", score=7.7,
        poster_theme="wine", genres=["Horror", "Thriller"], is_featured=False, is_trending=True,
    ),
    dict(
        title="The Dark Knight", tagline="Gotham gets the vigilante it deserves.",
        synopsis="A crime lord with no interest in money pushes a city's protectors past their "
                 "own rules, forcing an impossible choice between the hero Gotham wants and the "
                 "one it actually needs.",
        director="Christopher Nolan", cast=["Christian Bale", "Heath Ledger", "Aaron Eckhart"],
        release_year=2008, runtime_minutes=152, content_rating="PG-13", score=9.0,
        poster_theme="slate", genres=["Action", "Thriller"], is_featured=False, is_trending=True,
    ),
    dict(
        title="La La Land", tagline="A city of dreamers, two of them in particular.",
        synopsis="A jazz pianist and an actress fall for each other while chasing careers that "
                 "keep pulling them in opposite directions across Los Angeles.",
        director="Damien Chazelle", cast=["Ryan Gosling", "Emma Stone", "John Legend"],
        release_year=2016, runtime_minutes=128, content_rating="PG-13", score=8.0,
        poster_theme="gold", genres=["Romance", "Comedy"], is_featured=False, is_trending=False,
    ),
    dict(
        title="Whiplash", tagline="Not quite my tempo.",
        synopsis="A first-year drummer at an elite conservatory is pushed to the edge by an "
                 "instructor who believes greatness only comes from being broken down first.",
        director="Damien Chazelle", cast=["Miles Teller", "J.K. Simmons", "Paul Reiser"],
        release_year=2014, runtime_minutes=106, content_rating="R", score=8.5,
        poster_theme="ember", genres=["Drama"], is_featured=False, is_trending=False,
    ),
    dict(
        title="Coco", tagline="Remember me, but don't forget the family rule.",
        synopsis="A boy who dreams of being a musician, banned in his family for generations, "
                 "crosses into the Land of the Dead to track down the ancestor he's sure will "
                 "understand.",
        director="Lee Unkrich, Adrian Molina", cast=["Anthony Gonzalez", "Gael Garcia Bernal", "Benjamin Bratt"],
        release_year=2017, runtime_minutes=105, content_rating="PG", score=8.4,
        poster_theme="ember", genres=["Animation"], is_featured=False, is_trending=True,
    ),
    dict(
        title="Knives Out", tagline="Everyone's a suspect except the one asking questions.",
        synopsis="A celebrated crime novelist is found dead the night of his own birthday party, "
                 "and the private detective called in has to sort real grief from rehearsed alibis "
                 "across an entire, wealthy, lying family.",
        director="Rian Johnson", cast=["Daniel Craig", "Ana de Armas", "Chris Evans"],
        release_year=2019, runtime_minutes=130, content_rating="PG-13", score=7.9,
        poster_theme="wine", genres=["Mystery", "Comedy"], is_featured=False, is_trending=False,
    ),
    dict(
        title="Mad Max: Fury Road", tagline="Run, don't walk, from the wasteland.",
        synopsis="A drifter and a renegade rig driver haul a warlord's escaped prisoners across "
                 "an unbroken desert chase, with his entire war party close enough to see.",
        director="George Miller", cast=["Tom Hardy", "Charlize Theron", "Nicholas Hoult"],
        release_year=2015, runtime_minutes=120, content_rating="R", score=8.1,
        poster_theme="gold", genres=["Action", "Sci-Fi"], is_featured=False, is_trending=False,
    ),
    dict(
        title="Arrival", tagline="Learn their language before someone else answers for you.",
        synopsis="A linguist is brought in to communicate with newly arrived alien visitors "
                 "before global tensions over their intentions boil over, and starts to "
                 "experience time the way their language does.",
        director="Denis Villeneuve", cast=["Amy Adams", "Jeremy Renner", "Forest Whitaker"],
        release_year=2016, runtime_minutes=116, content_rating="PG-13", score=7.9,
        poster_theme="indigo", genres=["Sci-Fi", "Drama"], is_featured=True, is_trending=False,
    ),
    dict(
        title="Moonlight", tagline="Three chapters of the same boy becoming himself.",
        synopsis="A boy growing up in Miami is shaped across childhood, adolescence, and adulthood "
                 "by the people who see him clearly and the ones who never do.",
        director="Barry Jenkins", cast=["Trevante Rhodes", "Mahershala Ali", "Naomie Harris"],
        release_year=2016, runtime_minutes=111, content_rating="R", score=7.4,
        poster_theme="teal", genres=["Drama"], is_featured=False, is_trending=False,
    ),
    dict(
        title="The Social Network", tagline="You don't get to 500 million friends without making a few enemies.",
        synopsis="A Harvard sophomore builds a website that becomes a global network, and loses "
                 "most of the people who helped him build it along the way.",
        director="David Fincher", cast=["Jesse Eisenberg", "Andrew Garfield", "Justin Timberlake"],
        release_year=2010, runtime_minutes=120, content_rating="PG-13", score=7.7,
        poster_theme="slate", genres=["Drama"], is_featured=False, is_trending=False,
    ),
    dict(
        title="Interstellar", tagline="Find the next home before this one runs out of time.",
        synopsis="With Earth's crops failing, a former pilot leaves his kids behind to search a "
                 "distant galaxy for a habitable world, racing a clock that moves differently for "
                 "him than for them.",
        director="Christopher Nolan", cast=["Matthew McConaughey", "Anne Hathaway", "Jessica Chastain"],
        release_year=2014, runtime_minutes=169, content_rating="PG-13", score=8.6,
        poster_theme="indigo", genres=["Sci-Fi", "Drama"], is_featured=False, is_trending=True,
    ),
    dict(
        title="Everything Everywhere All at Once", tagline="Every life you didn't live, all at once.",
        synopsis="An overwhelmed laundromat owner discovers she can access the skills of every "
                 "version of herself across the multiverse, right as she needs all of them at "
                 "once to save her family and possibly everything else.",
        director="Daniel Kwan, Daniel Scheinert", cast=["Michelle Yeoh", "Ke Huy Quan", "Stephanie Hsu"],
        release_year=2022, runtime_minutes=140, content_rating="R", score=8.1,
        poster_theme="ember", genres=["Sci-Fi", "Comedy", "Action"], is_featured=True, is_trending=True,
    ),
    dict(
        title="No Country for Old Men", tagline="Some things you can't outrun.",
        synopsis="A welder who stumbles onto two million dollars at a drug deal gone wrong finds "
                 "himself hunted across West Texas by a killer who follows his own private sense "
                 "of order.",
        director="Joel Coen, Ethan Coen", cast=["Tommy Lee Jones", "Javier Bardem", "Josh Brolin"],
        release_year=2007, runtime_minutes=122, content_rating="R", score=8.2,
        poster_theme="slate", genres=["Thriller", "Mystery"], is_featured=False, is_trending=False,
    ),
    dict(
        title="Her", tagline="Falling for the voice in the next room.",
        synopsis="A lonely writer going through a divorce forms an unexpectedly deep relationship "
                 "with the highly advanced, endlessly curious operating system installed on his "
                 "phone.",
        director="Spike Jonze", cast=["Joaquin Phoenix", "Scarlett Johansson", "Amy Adams"],
        release_year=2013, runtime_minutes=126, content_rating="R", score=8.0,
        poster_theme="wine", genres=["Sci-Fi", "Romance"], is_featured=False, is_trending=False,
    ),
    dict(
        title="The Shawshank Redemption", tagline="Hope is a dangerous thing, inside these walls.",
        synopsis="A banker wrongly convicted of murder spends two decades in Shawshank Prison, "
                 "quietly outlasting the place through patience, friendship, and a plan nobody "
                 "sees coming.",
        director="Frank Darabont", cast=["Tim Robbins", "Morgan Freeman", "Bob Gunton"],
        release_year=1994, runtime_minutes=142, content_rating="R", score=9.3,
        poster_theme="gold", genres=["Drama"], is_featured=False, is_trending=False,
    ),
    dict(
        title="Pan's Labyrinth", tagline="A fairy tale for a country at war with itself.",
        synopsis="A girl in fascist-era Spain retreats into a labyrinth ruled by a faun who sets "
                 "her three tasks, each one bleeding closer into the brutal world just outside "
                 "her stepfather's house.",
        director="Guillermo del Toro", cast=["Ivana Baquero", "Sergi Lopez", "Doug Jones"],
        release_year=2006, runtime_minutes=118, content_rating="R", score=8.2,
        poster_theme="wine", genres=["Horror", "Drama"], is_featured=False, is_trending=False,
    ),
    dict(
        title="Portrait of a Lady on Fire", tagline="A commission, a secret, a burning coastline.",
        synopsis="A painter is hired to secretly paint a young woman's wedding portrait on an "
                 "isolated island, and the two grow closer under the pretense of daily walks "
                 "neither of them wants to end.",
        director="Celine Sciamma", cast=["Noemie Merlant", "Adele Haenel", "Luana Bajrami"],
        release_year=2019, runtime_minutes=122, content_rating="R", score=8.1,
        poster_theme="teal", genres=["Romance", "Drama"], is_featured=False, is_trending=False,
    ),
    dict(
        title="Amelie", tagline="One small act of good at a time.",
        synopsis="A shy Parisian waitress decides to secretly fix the lives of everyone around "
                 "her, one anonymous gesture at a time, while avoiding the one act of courage "
                 "her own life actually needs.",
        director="Jean-Pierre Jeunet", cast=["Audrey Tautou", "Mathieu Kassovitz", "Rufus"],
        release_year=2001, runtime_minutes=122, content_rating="R", score=8.3,
        poster_theme="gold", genres=["Romance", "Comedy"], is_featured=False, is_trending=False,
    ),
    dict(
        title="City of God", tagline="Growing up fast in a place built to slow you down.",
        synopsis="Two boys from the same Rio favela take opposite paths, one toward photography "
                 "and one toward the gang wars swallowing their neighborhood whole, over nearly "
                 "two decades.",
        director="Fernando Meirelles, Katia Lund", cast=["Alexandre Rodrigues", "Leandro Firmino", "Matheus Nachtergaele"],
        release_year=2002, runtime_minutes=130, content_rating="R", score=8.6,
        poster_theme="ember", genres=["Drama", "Thriller"], is_featured=False, is_trending=False,
    ),
    dict(
        title="Free Solo", tagline="No rope. No margin for error. One wall.",
        synopsis="Climber Alex Honnold prepares to scale Yosemite's 3,000-foot El Capitan without "
                 "a rope, and the filmmakers documenting him have to reckon with filming a mistake "
                 "that can't be undone.",
        director="Jimmy Chin, Elizabeth Chai Vasarhelyi", cast=[],
        release_year=2018, runtime_minutes=100, content_rating="PG-13", score=8.2,
        poster_theme="indigo", genres=["Documentary"], is_featured=False, is_trending=True,
    ),
]


class Command(BaseCommand):
    help = "Populates the catalog with a fixed set of 24 real, well-known films."

    def handle(self, *args, **options):
        Movie.objects.all().delete()
        Genre.objects.all().delete()

        genre_cache = {}

        def get_genre(name):
            if name not in genre_cache:
                genre_cache[name], _ = Genre.objects.get_or_create(name=name)
            return genre_cache[name]

        for entry in MOVIES:
            entry = entry.copy()
            genre_names = entry.pop("genres")
            movie = Movie.objects.create(**entry)
            movie.genres.set([get_genre(name) for name in genre_names])

        self.stdout.write(self.style.SUCCESS(
            f"Seeded {len(MOVIES)} movies across {len(genre_cache)} genres."
        ))
        self.stdout.write(
            "Posters are generated CSS art by default. Run "
            "'python3 manage.py fetch_posters' with a TMDB_API_KEY set to pull "
            "real poster images."
        )
