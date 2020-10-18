import json
from typing import Any

import boto3

from app.config import settings
from app.domain.entities.course import Course
from app.repositories.course_repo import CourseRepo


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
        try:
            courses_objects_list = self.s3.list_objects(Bucket=settings.COURSE_BUCKET)
        except Exception as exception:
            raise exception
        courses_list = []
        if (
            "Contents" not in courses_objects_list
        ):  # If no courses, the list should be empty.
            return {"courses_list": courses_list}
        for courses_object in courses_objects_list["Contents"]:
            try:
                courses_object = self.s3.get_object(
                    Key=courses_object["Key"], Bucket=settings.COURSE_BUCKET
                )
            except Exception as exception:
                raise exception
            course = vars(Course(**json.loads(courses_object["Body"].read().decode())))
            if filters_match(course, course_filters):
                courses_list.append({"Course": course})
        return {"courses_list": courses_list}


def filters_match(course, course_filters):
    compare_course = dict(
        (k, v)
        for k, v in course.items()
        if k in course_filters and course_filters[k] is not None
    )
    course_filters = dict((k, v) for k, v in course_filters.items() if v is not None)
    if compare_course == course_filters:
        return True
    return False
