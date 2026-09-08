import "./MoviePoster.css";

export default function MoviePoster({ movie, size = "row" }) {
  if (movie.poster_url) {
    return (
      <div className={`poster poster--${size} poster--photo`}>
        <img className="poster__image" src={movie.poster_url} alt={`${movie.title} poster`} loading="lazy" />
        <div className="poster__rating" aria-hidden="true">
          {Number(movie.score).toFixed(1)}
        </div>
      </div>
    );
  }

  return (
    <div className={`poster poster--${size} poster--${movie.poster_theme}`}>
      <div className="poster__grain" aria-hidden="true" />
      <div className="poster__sprockets poster__sprockets--top" aria-hidden="true" />
      <div className="poster__rating" aria-hidden="true">
        {Number(movie.score).toFixed(1)}
      </div>
      <div className="poster__title">{movie.title}</div>
      <div className="poster__sprockets poster__sprockets--bottom" aria-hidden="true" />
    </div>
  );
}

