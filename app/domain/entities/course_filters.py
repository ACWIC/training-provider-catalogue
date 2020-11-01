from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class CourseFilters(BaseModel):
    industry_standards: Optional[list]
    competency: Optional[list]
    location: Optional[str]
    from_date: Optional[datetime]
    to_date: Optional[datetime]
    availability: Optional[bool]
