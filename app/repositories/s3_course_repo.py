import json
from typing import Any

import boto3

from app.config import settings
from app.domain.entities.course import Course
from app.domain.entities.course_filters import CourseFilters
from app.repositories.course_repo import CourseRepo
from app.utils.error_handling import handle_s3_errors


class S3CourseRepo(CourseRepo):
    s3: Any

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.s3 = boto3.client("s3", **settings.s3_configuration)

    def search_course(self, course_filters: CourseFilters):
        course_filters = vars(course_filters)
        with handle_s3_errors():
            courses_objects_list = self.s3.list_objects(Bucket=settings.COURSE_BUCKET)
        courses_list = []
        for courses_object in courses_objects_list.get("Contents", []):
            with handle_s3_errors():
                courses_object = self.s3.get_object(
                    Key=courses_object["Key"], Bucket=settings.COURSE_BUCKET
                )
            course = vars(Course(**json.loads(courses_object["Body"].read().decode())))
            if filters_match(course, course_filters):
                courses_list.append({"Course": course})
        return {"courses_list": courses_list}


def filters_match(course, course_filters):
    # if course start_date is in a specific range
    date_in_range = True
    if (
        course_filters["from_date"] is not None
        and course_filters["to_date"] is not None
    ):
        date_in_range = False
        if (
            course_filters["from_date"].replace(tzinfo=None)
            <= course["start_date"]
            <= course_filters["to_date"].replace(tzinfo=None)
        ):
            date_in_range = True
    # Keep only those keys that are mutual in both
    # course and course_filters and are not None
    compare_course = {
        k: v for (k, v) in course.items() if course_filters.get(k) not in [None, [None]]
    }
    course_filters = dict(
        (k, v)
        for k, v in course_filters.items()
        if k in course and v not in [None, [None]]
    )
    # final check
    if compare_course == course_filters and date_in_range:
        return True
    return False
