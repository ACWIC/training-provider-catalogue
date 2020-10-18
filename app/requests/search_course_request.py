from datetime import datetime
from typing import Optional

from app.requests import ValidRequest


class SearchCourseRequest(ValidRequest):
    industry_standards: Optional[str]
    competency: Optional[str]
    location: Optional[str]
    date: Optional[datetime]
    availability: Optional[bool]
