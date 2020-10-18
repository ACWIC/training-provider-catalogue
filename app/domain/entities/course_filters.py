from datetime import datetime

from pydantic import BaseModel


class CourseFilters(BaseModel):
    industry_standards: str
    competency: str
    location: str
    date: datetime
    availability: bool
