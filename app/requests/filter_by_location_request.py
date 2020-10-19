from typing import Optional

from app.requests import ValidRequest


class FilterByLocationRequest(ValidRequest):
    location: Optional[str]
