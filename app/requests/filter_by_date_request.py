from datetime import datetime
from typing import Optional

from app.requests import ValidRequest


class FilterByDateRequest(ValidRequest):
    from_date: Optional[datetime]
    to_date: Optional[datetime]
