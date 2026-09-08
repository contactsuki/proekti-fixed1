import "./Hero.css";

export default function Hero({ movie, onOpen, isSaved, onToggleSave }) {
  if (!movie) return null;

  return (
    <section className={`hero hero--${movie.poster_theme}`}>
      <div className="hero__grain" aria-hidden="true" />
      <div className="container hero__content">
        <p className="hero__eyebrow">Now showing</p>
        <h1 className="hero__title">{movie.title}</h1>
        <p className="hero__tagline">{movie.tagline}</p>
        <div className="hero__meta">
          <span>{movie.release_year}</span>
          <span className="hero__dot">·</span>
          <span>{movie.runtime_minutes} min</span>
          <span className="hero__dot">·</span>
          <span>{movie.content_rating}</span>
          <span className="hero__dot">·</span>
          <span>{Number(movie.score).toFixed(1)} / 10</span>
        </div>
        <p className="hero__synopsis">{movie.synopsis}</p>
        <div className="hero__actions">
          <button type="button" className="hero__play" onClick={() => onOpen(movie)}>
            &#9654; Play
          </button>
          <button type="button" className="hero__info" onClick={() => onOpen(movie)}>
            More info
          </button>
          <button
            type="button"
            className={`hero__save ${isSaved ? "hero__save--on" : ""}`}
            onClick={() => onToggleSave(movie.id)}
          >
            {isSaved ? "\u2713 In My List" : "+ My List"}
          </button>
        </div>
      </div>
      <div className="sprocket-trim" aria-hidden="true" />
    </section>
  );
}
