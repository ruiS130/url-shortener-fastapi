## URL Shortener API (FastAPI + PostgreSQL)

This is a small learning project: a **URL shortener API** that you can later use as a **load-testing experiment** (e.g. for benchmarking FastAPI, PostgreSQL, and different deployment setups).

The initial scope is intentionally minimal so you can evolve the design over time (better short-code generation, analytics, authentication, rate limiting, etc.).

### Tech stack

- **Backend**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Validation/Schemas**: Pydantic
- **Server**: Uvicorn

### Project structure (high level)

- **`app/main.py`**: FastAPI application factory and entrypoint.
- **`app/db.py`**: Database engine, session and base class.
- **`app/models.py`**: SQLAlchemy models (currently a single `URL` model).
- **`app/schemas.py`**: Pydantic models / schemas for requests and responses.
- **`app/routers/url_shortener.py`**: URL shortener routes (`POST /shorten`, `GET /{short_code}`).

### Data model

Current model: **`URL`**

- **`id`**: integer primary key.
- **`original_url`**: the full original URL to redirect to.
- **`short_code`**: short identifier used in the shortened URL, unique.
- **`created_at`**: timestamp when the short URL was created.
- **`click_count`**: how many times this short URL has been used.

### Endpoints (initial)

- **`POST /shorten`**
  - Body: `{ "original_url": "<full url>" }`
  - Response: basic info about the created short URL (including the `short_code`).
- **`GET /{short_code}`**
  - Redirects to the original URL.
  - Increments `click_count` each time it is hit.

These implementations are intentionally simple and not production-ready; they are a foundation for you to experiment with better designs and performance tuning.

### Setup instructions

1. **Create and configure the database**

   - Start a local PostgreSQL instance (Docker or your local installation).
   - Create a database, for example:

     ```sql
     CREATE DATABASE url_shortener;
     ```

   - Set the `DATABASE_URL` environment variable (adjust user, password, host, port, and DB name as needed):

     ```bash
     export DATABASE_URL="postgresql://postgres:postgres@localhost:5432/url_shortener"
     ```

2. **Create a virtual environment and install dependencies**

   ```bash
   cd Backend_Project1
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

3. **Create database tables (quick start)**

   For now, the simplest approach is to let SQLAlchemy create the tables from the models in `app/models.py`:

   ```python
   # quick script (e.g. scripts/create_tables.py)
   from app.db import engine
   from app.models import Base

   Base.metadata.create_all(bind=engine)
   ```

   You can then run this script once to create the schema. Later, you can replace this with Alembic migrations if you want to practice migrations.

4. **Run the API server**

   ```bash
   uvicorn app.main:app --reload
   ```

   The app will be available at `http://127.0.0.1:8000`.

5. **Try the endpoints**

   - Open the interactive docs at `http://127.0.0.1:8000/docs`.
   - Use `POST /shorten` with a JSON body like:

     ```json
     {
       "original_url": "https://example.com"
     }
     ```

   - Copy the returned `short_code` and hit `GET /{short_code}` to verify the redirect behavior.

### Next ideas / extensions

- Improve short-code generation (hashing, random tokens, collision handling).
- Add expiration times, custom aliases, and per-user namespaces.
- Add authentication and rate limiting.
- Instrument the app for metrics (Prometheus, OpenTelemetry).
- Run load tests (e.g. with k6, Locust, or vegeta) and compare different configurations or deployments.

