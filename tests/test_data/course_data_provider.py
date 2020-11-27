import datetime

from app.domain.entities.course import Course
from app.domain.entities.course_filters import CourseFilters


class CourseDataProvider:  # (BaseModel):
    sample_course: Course
    sample_course_dict: dict
    sample_course_id: str
    sample_course_start_date: datetime

    sample_search_course_dict: dict
    sample_by_availability_dict: dict
    sample_by_competency_dict: dict
    sample_by_date_dict: dict
    sample_by_location_dict: dict
    sample_by_standards_dict: dict

    def __init__(self):
        # course_id = str(uuid4())
        course_id = "1dad3dd8-af28-4e61-ae23-4c93a456d10e"
        date_time_str = "2018-06-29 08:15:27.243860"
        start_date = datetime.datetime.strptime(date_time_str, "%Y-%m-%d %H:%M:%S.%f")
        from_date = start_date
        to_date = start_date
        created = start_date

        self.sample_course_id = course_id
        self.sample_course_date = start_date

        # Course Sample
        self.sample_course = Course(
            course_id=course_id,
            course_name="Bachelor of Community Services (HE20528)",
            industry_standards=["Police Check", "Security check"],
            competency=["top rated", "experienced"],
            location="Sydney",
            start_date=start_date,
            availability=True,
            hours_per_week=10,
            duration="2 months",
            fees_from=200,
            created=created,
        )
        self.sample_course_dict = self.sample_course.dict()

        # SearchCourseRequest Sample
        self.sample_search_course_dict = {
            "industry_standards": ["Police Check", "Security check"],
            "competency": ["top rated", "experienced"],
            "location": "Sydney",
            "from_date": from_date,
            "to_date": to_date,
            "availability": True,
        }
        self.sample_search_course = CourseFilters(**self.sample_search_course_dict)
        # sample#2
        self.sample_search_course_dict1 = {
            "industry_standards": ["Police Check", "Security check"],
            "competency": ["top rated", "experienced"],
            "location": "Grafton",
            "from_date": from_date,
            "to_date": to_date,
            "availability": False,
        }
        self.sample_search_course1 = CourseFilters(**self.sample_search_course_dict1)

        # Filters Requests
        self.sample_by_availability_dict = {"availability": True}
        self.sample_by_competency_dict = {"competency": ["top rated", "experienced"]}
        self.sample_by_date_dict = {
            "from_date": from_date,
            "to_date": to_date,
        }
        self.sample_by_location_dict = {"location": "Sydney"}
        self.sample_by_standards_dict = {
            "industry_standards": ["Police Check", "Security check"]
        }

        self.sample_by_availability = CourseFilters(**self.sample_by_availability_dict)
        self.sample_by_competency = CourseFilters(**self.sample_by_competency_dict)
        self.sample_by_date = CourseFilters(**self.sample_by_date_dict)
        self.sample_by_location = CourseFilters(**self.sample_by_location_dict)
        self.sample_by_standards = CourseFilters(**self.sample_by_standards_dict)

        # start date
        self.course_start_date_in_range = {
            "start_date": datetime.datetime.strptime(
                "2018-06-05 08:15:27.243860", "%Y-%m-%d %H:%M:%S.%f"
            ),
        }
        self.course_start_date_not_in_range = {
            "start_date": datetime.datetime.strptime(
                "2018-06-15 08:15:27.243860", "%Y-%m-%d %H:%M:%S.%f"
            ),
        }
        self.course_filters_start_date_in_range = {
            "from_date": datetime.datetime.strptime(
                "2018-06-01 08:15:27.243860", "%Y-%m-%d %H:%M:%S.%f"
            ),
            "to_date": datetime.datetime.strptime(
                "2018-06-10 08:15:27.243860", "%Y-%m-%d %H:%M:%S.%f"
            ),
        }
        self.course_filters_start_date_none = {
            "from_date": None,
            "to_date": None,
        }

        # standards
        self.course_standards_competency_subset = {
            "competency": ["A", "B"],
            "industry_standards": ["C", "D"],
        }
        self.course_filters_standards_competency_subset = {
            "competency": ["A"],
            "industry_standards": None,
        }
        self.course_standards_subset = {
            "competency": ["A", "B"],
            "industry_standards": ["C", "D"],
        }
        self.course_filters_standards_subset = {
            "competency": None,
            "industry_standards": ["E"],
        }
        self.course_filters_standards_none = {
            "competency": None,
            "industry_standards": None,
        }
        self.course_standards_not_subset = {
            "competency": ["A", "B"],
            "industry_standards": ["C", "D"],
        }
        self.course_filters_standards_not_subset = {
            "competency": ["E", "F"],
            "industry_standards": ["G", "H"],
        }
