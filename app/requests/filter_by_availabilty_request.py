from typing import Optional

from app.requests import ValidRequest


class FilterByAvailabilityRequest(ValidRequest):
    availability: Optional[bool]
