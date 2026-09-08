import { useEffect, useMemo, useRef, useState } from "react";
import MoviePoster from "./MoviePoster.jsx";
import "./SearchOverlay.css";

export default function SearchOverlay({ movies, onOpen, onClose }) {
  const [query, setQuery] = useState("");
  const inputRef = useRef(null);

  useEffect(() => {
    inputRef.current?.focus();
    const onKey = (e) => e.key === "Escape" && onClose();
    document.addEventListener("keydown", onKey);
    return () => document.removeEventListener("keydown", onKey);
  }, [onClose]);

  const results = useMemo(() => {
    const q = query.trim().toLowerCase();
    if (!q) return [];
    return movies.filter(
      (m) =>
        m.title.toLowerCase().includes(q) ||
        m.director?.toLowerCase().includes(q) ||
        m.genres.some((g) => g.name.toLowerCase().includes(q))
    );
  }, [query, movies]);

  return (
    <div className="search-overlay">
      <div className="container search-overlay__inner">
        <div className="search-overlay__field">
          <input
            ref={inputRef}
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="Search titles, directors, genres…"
            aria-label="Search the catalog"
          />
          <button type="button" onClick={onClose} aria-label="Close search">
            &times;
          </button>
        </div>

        {query.trim() && (
          <p className="search-overlay__count">
            {results.length} {results.length === 1 ? "result" : "results"}
          </p>
        )}

        <div className="search-overlay__grid">
          {results.map((movie) => (
            <button
              type="button"
              key={movie.id}
              className="search-overlay__item"
              onClick={() => onOpen(movie)}
            >
              <MoviePoster movie={movie} size="row" />
              <span className="search-overlay__item-title">{movie.title}</span>
            </button>
          ))}
        </div>
      </div>
    </div>
  );
}
