"""
These tests evaluate the interaction with the backing PaaS.
The are testing the encapsulation of the "impure" code
(in a functional sense),
the repos should return pure domain objects
of the appropriate type.
"""
from unittest.mock import patch

import app.repositories.course_repo
from app.config import settings
from app.repositories.s3_course_repo import (
    S3CourseRepo,
    filters_match,
    if_dates_in_range,
    if_subset_competency_or_standard,
)
from tests.test_data.course_data_provider import CourseDataProvider

test_data = CourseDataProvider()


@patch("boto3.client")
def test_s3_initialisation(boto_client):
    """
    Ensure the S3CourseRepo makes a boto3 connection.
    """
    S3CourseRepo()
    boto_client.assert_called_once()


@patch("json.loads")
@patch("boto3.client")
def test_search_course(boto_client, json_loads):
    """
    Ensure the S3CourseRepo returns an object with OK data
    and that an appropriate boto3 put call was made.
    """
    course_id = test_data.sample_course_id
    repo = S3CourseRepo()
    settings.COURSE_BUCKET = "some-bucket"
    course = test_data.sample_course_dict
    request = test_data.sample_search_course

    boto_client.return_value.list_objects = list_objects_sample_content
    json_loads.return_value = course
    courses_list = repo.search_course(request)

    assert courses_list == {"courses_list": [{"Course": test_data.sample_course_dict}]}

    boto_client.return_value.get_object.assert_called_once_with(
        Key=f"{course_id}.json",
        Bucket="some-bucket",
    )


@patch("json.loads")
@patch("boto3.client")
def test_search_course_empty_list(boto_client, json_loads):
    """
    Ensure the S3CourseRepo returns an object with OK data
    and that an appropriate boto3 put call was made.
    """
    repo = S3CourseRepo()
    settings.COURSE_BUCKET = "some-bucket"
    course = test_data.sample_course_dict
    request = test_data.sample_search_course

    boto_client.return_value.list_objects = list_objects_sample_content_empty
    json_loads.return_value = course
    courses_list = repo.search_course(request)

    assert courses_list == {"courses_list": []}


def test_filters_match():
    course = test_data.sample_course_dict
    course_filters = test_data.sample_search_course_dict
    course_filters1 = test_data.sample_search_course_dict1

    assert filters_match(course, course_filters)
    assert not filters_match(course, course_filters1)


def test_if_dates_in_range():
    course = test_data.course_start_date_in_range
    course_filters = test_data.course_filters_start_date_in_range
    assert if_dates_in_range(course, course_filters)
    course_filters = test_data.course_filters_start_date_none
    assert if_dates_in_range(course, course_filters)
    course = test_data.course_start_date_not_in_range
    course_filters = test_data.course_filters_start_date_in_range
    assert not if_dates_in_range(course, course_filters)


def test_if_subset_competency_or_standard():
    course = test_data.course_standards_competency_subset
    course_filters = test_data.course_filters_standards_competency_subset
    assert if_subset_competency_or_standard(course, course_filters)
    course = test_data.course_standards_subset
    course_filters = test_data.course_filters_standards_subset
    assert not if_subset_competency_or_standard(course, course_filters)
    course_filters = test_data.course_filters_standards_none
    assert if_subset_competency_or_standard(course, course_filters)
    course = test_data.course_standards_not_subset
    course_filters = test_data.course_filters_standards_not_subset
    assert not if_subset_competency_or_standard(course, course_filters)


def test_course_repo():
    assert (
        "search_course" in app.repositories.course_repo.CourseRepo.__abstractmethods__
    )


def list_objects_sample_content(Bucket):
    return {
        "Contents": [
            {
                "course_id": test_data.sample_course_id,
                "bucket": Bucket,
                # "prefix": Prefix,
                "Key": test_data.sample_course_id + ".json",
            }
        ]
    }


def list_objects_sample_content_empty(Bucket):
    return {}
