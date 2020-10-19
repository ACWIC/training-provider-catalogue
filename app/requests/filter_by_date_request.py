from datetime import datetime
from typing import Optional

from app.requests import ValidRequest


class FilterByDateRequest(ValidRequest):
    date: Optional[datetime]
