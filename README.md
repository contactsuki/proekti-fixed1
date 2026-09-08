# Nightreel

Nightreel is a React/Vite movie catalog backed by Django REST Framework.

## Run the backend

```bash
cd backend
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py seed_catalog
python manage.py runserver
```

The API is available at `http://127.0.0.1:8000/api/`.

## Run the frontend

In a second terminal:

```bash
npm install
npm run dev
```

Open `http://localhost:3000`.

The frontend falls back to its bundled movie data when the backend is unavailable, so the UI can still render during development.
