from pydantic import BaseModel, Field
from typing import Optional

class Review(BaseModel):
    user_id: str
    track_id: str
    rating: float = Field(..., ge=0, le=10)
    text: Optional[str] = None
