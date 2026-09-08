import { useRef } from "react";
import MovieCard from "./MovieCard.jsx";
import "./MovieRow.css";

export default function MovieRow({ title, movies, onOpen, isSaved, onToggleSave }) {
  const trackRef = useRef(null);

  if (!movies.length) return null;

  const scroll = (direction) => {
    const track = trackRef.current;
    if (!track) return;
    const distance = track.clientWidth * 0.85 * direction;
    track.scrollBy({ left: distance, behavior: "smooth" });
  };

  return (
    <section className="row" aria-label={title}>
      <div className="row__head">
        <h2 className="row__title">{title}</h2>
        <div className="row__nav">
          <button type="button" onClick={() => scroll(-1)} aria-label={`Scroll ${title} left`}>
            &#8249;
          </button>
          <button type="button" onClick={() => scroll(1)} aria-label={`Scroll ${title} right`}>
            &#8250;
          </button>
        </div>
      </div>
      <div className="row__track" ref={trackRef}>
        {movies.map((movie) => (
          <MovieCard
            key={movie.id}
            movie={movie}
            onOpen={onOpen}
            isSaved={isSaved(movie.id)}
            onToggleSave={onToggleSave}
          />
        ))}
      </div>
    </section>
  );
}
