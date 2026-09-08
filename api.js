import { FALLBACK_GENRES, FALLBACK_MOVIES } from "./data/fallbackMovies.js";

const BASE = "/api";

async function getJSON(path) {
  const res = await fetch(`${BASE}${path}`);
  if (!res.ok) throw new Error(`Request to ${path} failed: ${res.status}`);
  return res.json();
}

export async function fetchAllMovies() {
  try {
    const data = await getJSON("/movies/?page_size=100");
    return data.results ?? data;
  } catch {
    return FALLBACK_MOVIES;
  }
}

export async function fetchFeatured() {
  try {
    const data = await getJSON("/movies/featured/");
    return data.results ?? data;
  } catch {
    return FALLBACK_MOVIES.filter((m) => m.is_featured);
  }
}

export async function fetchTrending() {
  try {
    const data = await getJSON("/movies/trending/");
    return data.results ?? data;
  } catch {
    return FALLBACK_MOVIES.filter((m) => m.is_trending);
  }
}

export async function fetchGenres() {
  try {
    return await getJSON("/genres/");
  } catch {
    return FALLBACK_GENRES;
  }
}
