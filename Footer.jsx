import "./Footer.css";

export default function Footer() {
  return (
    <footer className="footer">
      <div className="sprocket-trim" aria-hidden="true" />
      <div className="container footer__inner">
        <span className="footer__brand">Nightreel</span>
        <span className="footer__note">A small, hand-picked catalog instead of an endless feed.</span>
      </div>
    </footer>
  );
}
