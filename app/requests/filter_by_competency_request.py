from typing import Optional

from app.requests import ValidRequest


class FilterByCompetencyRequest(ValidRequest):
    competency: Optional[str]
