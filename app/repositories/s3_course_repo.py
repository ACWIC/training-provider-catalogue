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
        with handle_s3_errors():
            self.s3 = boto3.client("s3", **settings.s3_configuration)

    def search_course(self, course_filters: CourseFilters):
        course_filters = course_filters.dict()
        with handle_s3_errors():
            courses_objects_list = self.s3.list_objects(Bucket=settings.COURSE_BUCKET)
        courses_list = []
        for courses_object in courses_objects_list.get("Contents", []):
            with handle_s3_errors():
                courses_object = self.s3.get_object(
                    Key=courses_object["Key"], Bucket=settings.COURSE_BUCKET
                )
            course = Course(**json.loads(courses_object["Body"].read().decode())).dict()
            if filters_match(course, course_filters.copy()):
                courses_list.append({"Course": course})
        return {"courses_list": courses_list}


def filters_match(course: dict, course_filters: dict):
    # if course start_date is in a specific range
    date_in_range = if_dates_in_range(course, course_filters)
    # if course filter (list)  is subset of course (list)
    subset = if_subset_competency_or_standard(course, course_filters)
    course_filters["competency"] = None
    course_filters["industry_standards"] = None
    # Keep only those keys that are mutual in both
    # course and course_filters and are not None
    compare_course = {
        k: v for (k, v) in course.items() if course_filters.get(k) is not None
    }
    course_filters = dict(
        (k, v) for k, v in course_filters.items() if k in course and v is not None
    )
    # final check
    if compare_course == course_filters and date_in_range and subset:
        return True
    return False


def if_subset_competency_or_standard(course: dict, course_filters: dict):
    if (
        course_filters["competency"] is None
        and course_filters["industry_standards"] is None
    ):
        return True
    subset = False
    if course_filters["competency"] is not None:
        for competency in course_filters["competency"]:
            if competency in course["competency"]:
                subset = True
        if not subset or course_filters["industry_standards"] is None:
            return subset
    subset = False
    for standard in course_filters["industry_standards"]:
        if standard in course["industry_standards"]:
            subset = True
            break
    return subset


def if_dates_in_range(course: dict, course_filters: dict):
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
    return date_in_range
