import { useCallback, useEffect, useState } from "react";

const STORAGE_KEY = "nightreel:my-list";

function readStoredIds() {
  try {
    const raw = window.localStorage.getItem(STORAGE_KEY);
    return raw ? JSON.parse(raw) : [];
  } catch {
    return [];
  }
}

export function useMyList() {
  const [ids, setIds] = useState(readStoredIds);

  useEffect(() => {
    window.localStorage.setItem(STORAGE_KEY, JSON.stringify(ids));
  }, [ids]);

  const isSaved = useCallback((movieId) => ids.includes(movieId), [ids]);

  const toggle = useCallback((movieId) => {
    setIds((current) =>
      current.includes(movieId)
        ? current.filter((id) => id !== movieId)
        : [...current, movieId]
    );
  }, []);

  return { ids, isSaved, toggle };
}
