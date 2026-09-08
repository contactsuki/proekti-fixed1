import { useEffect } from "react";
import MoviePoster from "./MoviePoster.jsx";
import "./MovieModal.css";

export default function MovieModal({ movie, onClose, isSaved, onToggleSave }) {
  useEffect(() => {
    const onKey = (e) => e.key === "Escape" && onClose();
    document.addEventListener("keydown", onKey);
    document.body.style.overflow = "hidden";
    return () => {
      document.removeEventListener("keydown", onKey);
      document.body.style.overflow = "";
    };
  }, [onClose]);

  if (!movie) return null;

  return (
    <div className="modal-backdrop" onClick={onClose}>
      <div
        className="modal"
        role="dialog"
        aria-modal="true"
        aria-labelledby="modal-title"
        onClick={(e) => e.stopPropagation()}
      >
        <button type="button" className="modal__close" onClick={onClose} aria-label="Close">
          &times;
        </button>

        <div className="modal__poster">
          <MoviePoster movie={movie} size="modal" />
        </div>

        <div className="modal__body">
          <p className="modal__eyebrow">{movie.tagline}</p>
          <h2 id="modal-title" className="modal__title">
            {movie.title}
          </h2>
          <div className="modal__meta">
            <span>{movie.release_year}</span>
            <span className="modal__dot">·</span>
            <span>{movie.runtime_minutes} min</span>
            <span className="modal__dot">·</span>
            <span>{movie.content_rating}</span>
            <span className="modal__dot">·</span>
            <span>{Number(movie.score).toFixed(1)} / 10</span>
          </div>

          <p className="modal__synopsis">{movie.synopsis}</p>

          {movie.director && (
            <p className="modal__line">
              <span className="modal__label">Director</span> {movie.director}
            </p>
          )}
          {movie.cast?.length > 0 && (
            <p className="modal__line">
              <span className="modal__label">Cast</span> {movie.cast.join(", ")}
            </p>
          )}

          <div className="modal__tags">
            {movie.genres.map((g) => (
              <span key={g.slug} className="modal__tag">
                {g.name}
              </span>
            ))}
          </div>

          <button
            type="button"
            className={`modal__save ${isSaved ? "modal__save--on" : ""}`}
            onClick={() => onToggleSave(movie.id)}
          >
            {isSaved ? "\u2713 In My List" : "+ Add to My List"}
          </button>
        </div>
      </div>
    </div>
  );
}
