from datetime import datetime

from pydantic import BaseModel, AnyHttpUrl


class URLBase(BaseModel):
    original_url: AnyHttpUrl


class URLCreate(URLBase):
    pass


class URLInfo(URLBase):
    id: int
    short_code: str
    created_at: datetime
    click_count: int

    class Config:
        from_attributes = True


class URLRedirect(BaseModel):
    original_url: AnyHttpUrl


class URLStats(BaseModel):
    """Basic per-URL stats."""

    short_code: str
    total_clicks: int
    created_at: datetime


class URLListResponse(BaseModel):
    """Response wrapper for URL list endpoints."""

    items: list[URLInfo]
    total: int
