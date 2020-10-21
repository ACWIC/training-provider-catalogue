import json
from typing import Any

import boto3

from app.config import settings
from app.domain.entities.course import Course
from app.repositories.course_repo import CourseRepo
from app.utils.error_handling import handle_s3_errors


class S3CourseRepo(CourseRepo):
    s3: Any

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.params = {
            "aws_access_key_id": settings.S3_ACCESS_KEY_ID,
            "aws_secret_access_key": settings.S3_SECRET_ACCESS_KEY,
            "endpoint_url": settings.S3_ENDPOINT_URL,
        }
        self.s3 = boto3.client("s3", **self.params)

    def search_course(self, course_filters: dict):
        print("search_course", course_filters)
        with handle_s3_errors():
            courses_objects_list = self.s3.list_objects(Bucket=settings.COURSE_BUCKET)
        courses_list = []
        if (
            "Contents" not in courses_objects_list
        ):  # If no courses, the list should be empty.
            return {"courses_list": courses_list}
        for courses_object in courses_objects_list["Contents"]:
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
    compare_course = dict(
        (k, v)
        for k, v in course.items()
        if k in course_filters and course_filters[k] is not None
    )
    course_filters = dict(
        (k, v) for k, v in course_filters.items() if k in course and v is not None
    )
    # final check
    if compare_course == course_filters and date_in_range:
        return True
    return False
