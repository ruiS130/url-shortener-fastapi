from datetime import datetime
from typing import List

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
    """
    Basic per-URL stats.
    You can extend this later with more analytics fields (e.g. last_accessed_at, user_id, etc.).
    """

    short_code: str
    total_clicks: int
    created_at: datetime


class URLListResponse(BaseModel):
    """
    Simple wrapper to experiment with pagination and filtering later.
    """

    items: List[URLInfo]
    total: int

