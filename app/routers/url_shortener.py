from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app import schemas, models
from app.db import get_db


router = APIRouter(tags=["url-shortener"])


@router.post("/shorten", response_model=schemas.URLInfo, status_code=status.HTTP_201_CREATED)
def create_short_url(payload: schemas.URLCreate, db: Session = Depends(get_db)) -> schemas.URLInfo:
    """
    Minimal implementation for creating a short URL.
    For now this uses a very naive short_code; you can improve it later.
    """
    original_url = str(payload.original_url)

    # Naive short code generation: count-based (not safe for concurrency, just for learning)
    count = db.query(models.URL).count() + 1
    short_code = f"s{count}"

    url = models.URL(
        original_url=original_url,
        short_code=short_code,
    )
    db.add(url)
    db.commit()
    db.refresh(url)

    return url


@router.get("/{short_code}", response_class=RedirectResponse, status_code=status.HTTP_307_TEMPORARY_REDIRECT)
def redirect_short_url(short_code: str, db: Session = Depends(get_db)):
    """
    Minimal redirect endpoint.
    Increments click_count and redirects to the original URL.
    """
    url: models.URL | None = (
        db.query(models.URL)
        .filter(models.URL.short_code == short_code)
        .first()
    )

    if url is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Short URL not found")

    url.click_count += 1
    db.add(url)
    db.commit()

    return RedirectResponse(url.original_url, status_code=status.HTTP_307_TEMPORARY_REDIRECT)

