"""
These tests evaluate the interaction with the backing PaaS.
The are testing the encapsulation of the "impure" code
(in a functional sense),
the repos should return pure domain objects
of the appropriate type.
"""
from unittest.mock import patch

# from app.repositories.course_repo import CourseRepo
import app.repositories.course_repo
from app.config import settings
from app.repositories.s3_course_repo import S3CourseRepo, filters_match
from tests.test_data.course_data_provider import CourseDataProvider


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
    course_id = CourseDataProvider().sample_course_id
    repo = S3CourseRepo()
    settings.COURSE_BUCKET = "some-bucket"
    course = CourseDataProvider().sample_course_dict
    request = CourseDataProvider().sample_search_course_request_dict

    boto_client.return_value.list_objects = list_objects_sample_content
    json_loads.return_value = course
    courses_list = repo.search_course(request)

    assert courses_list == {
        "courses_list": [{"Course": CourseDataProvider().sample_course_dict}]
    }

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
    course = CourseDataProvider().sample_course_dict
    request = CourseDataProvider().sample_search_course_request_dict1

    boto_client.return_value.list_objects = list_objects_sample_content_empty
    json_loads.return_value = course
    courses_list = repo.search_course(request)

    assert courses_list == {"courses_list": []}


def test_filters_match():
    course = CourseDataProvider().sample_course_dict
    course_filters = CourseDataProvider().sample_search_course_request_dict
    course_filters1 = CourseDataProvider().sample_search_course_request_dict1

    assert filters_match(course, course_filters)
    assert not filters_match(course, course_filters1)


def test_course_repo():
    assert (
        "search_course" in app.repositories.course_repo.CourseRepo.__abstractmethods__
    )


def list_objects_sample_content(Bucket):
    return {
        "Contents": [
            {
                "course_id": CourseDataProvider().sample_course_id,
                "bucket": Bucket,
                # "prefix": Prefix,
                "Key": CourseDataProvider().sample_course_id + ".json",
            }
        ]
    }


def list_objects_sample_content_empty(Bucket):
    return {}
