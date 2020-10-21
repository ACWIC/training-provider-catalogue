from typing import Optional

from app.requests import ValidRequest


class FilterByStandardsRequest(ValidRequest):
    industry_standards: Optional[str]
