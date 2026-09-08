import MoviePoster from "./MoviePoster.jsx";
import "./MovieCard.css";

export default function MovieCard({ movie, onOpen, isSaved, onToggleSave }) {
  return (
    <div className="movie-card">
      <button
        type="button"
        className="movie-card__trigger"
        onClick={() => onOpen(movie)}
        aria-label={`View details for ${movie.title}`}
      >
        <MoviePoster movie={movie} size="row" />
      </button>
      <button
        type="button"
        className={`movie-card__save ${isSaved ? "movie-card__save--on" : ""}`}
        onClick={() => onToggleSave(movie.id)}
        aria-pressed={isSaved}
        aria-label={isSaved ? `Remove ${movie.title} from My List` : `Add ${movie.title} to My List`}
      >
        {isSaved ? "\u2713" : "+"}
      </button>
      <div className="movie-card__meta">
        <span>{movie.release_year}</span>
        <span className="movie-card__dot" aria-hidden="true">·</span>
        <span>{movie.content_rating}</span>
      </div>
    </div>
  );
}
