import { useEffect, useMemo, useState } from "react";
import Navbar from "./components/Navbar.jsx";
import Hero from "./components/Hero.jsx";
import MovieRow from "./components/MovieRow.jsx";
import MovieModal from "./components/MovieModal.jsx";
import SearchOverlay from "./components/SearchOverlay.jsx";
import Footer from "./components/Footer.jsx";
import { fetchAllMovies, fetchFeatured, fetchGenres, fetchTrending } from "./api.js";
import { useMyList } from "./useMyList.js";
import "./App.css";

export default function App() {
  const [movies, setMovies] = useState([]);
  const [featured, setFeatured] = useState([]);
  const [trending, setTrending] = useState([]);
  const [genres, setGenres] = useState([]);
  const [loading, setLoading] = useState(true);

  const [activeMovie, setActiveMovie] = useState(null);
  const [searchOpen, setSearchOpen] = useState(false);

  const { isSaved, toggle } = useMyList();

  useEffect(() => {
    let cancelled = false;

    async function load() {
      const [allMovies, featuredMovies, trendingMovies, allGenres] = await Promise.all([
        fetchAllMovies(),
        fetchFeatured(),
        fetchTrending(),
        fetchGenres(),
      ]);
      if (cancelled) return;
      setMovies(allMovies);
      setFeatured(featuredMovies);
      setTrending(trendingMovies);
      setGenres(allGenres);
      setLoading(false);
    }

    load();
    return () => {
      cancelled = true;
    };
  }, []);

  const heroMovie = featured[0] ?? movies[0];

  const myListMovies = useMemo(
    () => movies.filter((m) => isSaved(m.id)),
    [movies, isSaved]
  );

  const rowsByGenre = useMemo(
    () =>
      genres.map((genre) => ({
        genre,
        movies: movies.filter((m) => m.genres.some((g) => g.slug === genre.slug)),
      })),
    [genres, movies]
  );

  if (loading) {
    return (
      <div className="loading-screen">
        <span>Nightreel</span>
      </div>
    );
  }

  return (
    <>
      <Navbar onSearchClick={() => setSearchOpen(true)} />

      <main id="home">
        <Hero
          movie={heroMovie}
          onOpen={setActiveMovie}
          isSaved={heroMovie ? isSaved(heroMovie.id) : false}
          onToggleSave={toggle}
        />

        <MovieRow
          title="Trending now"
          movies={trending}
          onOpen={setActiveMovie}
          isSaved={isSaved}
          onToggleSave={toggle}
        />

        <div id="my-list">
          <MovieRow
            title="My List"
            movies={myListMovies}
            onOpen={setActiveMovie}
            isSaved={isSaved}
            onToggleSave={toggle}
          />
        </div>

        {rowsByGenre.map(({ genre, movies: genreMovies }) => (
          <MovieRow
            key={genre.slug}
            title={genre.name}
            movies={genreMovies}
            onOpen={setActiveMovie}
            isSaved={isSaved}
            onToggleSave={toggle}
          />
        ))}
      </main>

      <Footer />

      {searchOpen && (
        <SearchOverlay
          movies={movies}
          onOpen={(movie) => {
            setActiveMovie(movie);
            setSearchOpen(false);
          }}
          onClose={() => setSearchOpen(false)}
        />
      )}

      {activeMovie && (
        <MovieModal
          movie={activeMovie}
          onClose={() => setActiveMovie(null)}
          isSaved={isSaved(activeMovie.id)}
          onToggleSave={toggle}
        />
      )}
    </>
  );
}
