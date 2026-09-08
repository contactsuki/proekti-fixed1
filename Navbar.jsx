import { useEffect, useState } from "react";
import "./Navbar.css";

const LINKS = [
  { label: "Home", href: "#home" },
  { label: "My List", href: "#my-list" },
];

export default function Navbar({ onSearchClick }) {
  const [scrolled, setScrolled] = useState(false);

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 12);
    window.addEventListener("scroll", onScroll);
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  return (
    <header className={`nav ${scrolled ? "nav--scrolled" : ""}`}>
      <div className="container nav__row">
        <a className="nav__brand" href="#home">
          Nightreel
        </a>
        <nav className="nav__links" aria-label="Primary">
          {LINKS.map((link) => (
            <a key={link.href} href={link.href}>
              {link.label}
            </a>
          ))}
        </nav>
        <button type="button" className="nav__search" onClick={onSearchClick} aria-label="Search the catalog">
          <span aria-hidden="true">&#9906;</span>
          <span className="nav__search-label">Search</span>
        </button>
      </div>
    </header>
  );
}
