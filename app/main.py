from fastapi import FastAPI

from app.routers import url_shortener


def create_app() -> FastAPI:
    app = FastAPI(
        title="URL Shortener API",
        description="Simple URL shortener backend for load-testing experiments.",
        version="0.1.0",
    )

    app.include_router(url_shortener.router)

    return app


app = create_app()

