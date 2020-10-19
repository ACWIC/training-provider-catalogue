import datetime

from app.domain.entities.course import Course
from app.requests.filter_by_availabilty_request import FilterByAvailabilityRequest
from app.requests.filter_by_competency_request import FilterByCompetencyRequest
from app.requests.filter_by_date_request import FilterByDateRequest
from app.requests.filter_by_location_request import FilterByLocationRequest
from app.requests.filter_by_standards_request import FilterByStandardsRequest
from app.requests.search_course_request import SearchCourseRequest


class CourseDataProvider:  # (BaseModel):
    sample_course: Course
    sample_course_dict: dict
    sample_course_id: str
    sample_course_date: datetime

    sample_search_course_request: SearchCourseRequest
    sample_search_course_request_dict: dict

    sample_by_availabilty_request: FilterByAvailabilityRequest
    sample_by_competency_request: FilterByCompetencyRequest
    sample_by_date_request: FilterByDateRequest
    sample_by_location_request: FilterByLocationRequest
    sample_by_standards_request: FilterByStandardsRequest

    def __init__(self):
        # course_id = str(uuid4())
        course_id = "1dad3dd8-af28-4e61-ae23-4c93a456d10e"
        date_time_str = "2018-06-29 08:15:27.243860"
        date = datetime.datetime.strptime(date_time_str, "%Y-%m-%d %H:%M:%S.%f")
        created = date
        self.sample_course_id = course_id
        self.sample_course_date = date

        # Course Sample
        self.sample_course = Course(
            course_id=course_id,
            course_name="Bachelor of Community Services (HE20528)",
            industry_standards="Police Check",
            competency="top rated",
            location="Sydney",
            date=date,
            availability=True,
            hours_per_week=10,
            duration="2 months",
            fees_from=200,
            created=created,
        )
        self.sample_course_dict = vars(self.sample_course)

        # SearchCourseRequest Sample
        self.sample_search_course_request = SearchCourseRequest(
            industry_standards="Police Check",
            competency="top rated",
            location="Sydney",
            date=date,
            availability=True,
        )
        self.sample_search_course_request_dict = vars(self.sample_search_course_request)

        # Filters Requests
        self.sample_by_availabilty_request = FilterByAvailabilityRequest(
            availability=True
        )
        self.sample_by_competency_request = FilterByCompetencyRequest(
            competency="top rated"
        )
        self.sample_by_date_request = FilterByDateRequest(date=date)
        self.sample_by_location_request = FilterByLocationRequest(location="Sydney")
        self.sample_by_standards_request = FilterByStandardsRequest(
            industry_standards="Police Check"
        )
