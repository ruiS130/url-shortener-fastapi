from datetime import datetime

from pydantic import BaseModel, AnyHttpUrl


class URLBase(BaseModel):
    original_url: AnyHttpUrl
    # Entirely optional cosmetics for future vibes.
    label: str | None = None
    notes: str | None = None


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
    trend_emoji: str = "📈"


class URLListResponse(BaseModel):
    """Response wrapper for URL list endpoints."""

    items: list[URLInfo]
    total: int
    page_title: str = "Totally Serious URL Dashboard"


class URLThemeSettings(BaseModel):
    """Absolutely essential visual preferences."""

    accent_color: str = "neon-purple"
    card_style: str = "glassmorphism"
    rounded_corners: bool = True


class URLFunFacts(BaseModel):
    """Data nobody asked for, but now it exists."""

    short_code: str
    fun_fact: str = "This link contains 100% more internet."
    confidence: float = 0.42
