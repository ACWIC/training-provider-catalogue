"""
These tests evaluate (and document) the business logic.
"""
from unittest import mock

from app.repositories.course_repo import CourseRepo
from app.use_cases.search_course import SearchCourse
from tests.test_data.course_data_provider import CourseDataProvider


def test_search_course_success():
    """
    When searching a course,
    if everything goes according to plan,
    the response type should be "200-Success".
    """
    repo = mock.Mock(spec=CourseRepo)
    course = CourseDataProvider().sample_course
    request = CourseDataProvider().sample_search_course
    use_case = SearchCourse(course_repo=repo)

    repo.search_course.return_value = course
    response = use_case.execute(request)

    assert response.type == "200-Success"


def test_search_course_success_empty():
    """
    When searching a course,
    if everything goes according to plan,
    the response type should be "200-Success".
    """
    repo = mock.Mock(spec=CourseRepo)
    request = CourseDataProvider().sample_search_course
    use_case = SearchCourse(course_repo=repo)

    repo.search_course.return_value = {"courses_list": []}
    response = use_case.execute(request)

    assert response.type == "200-Success"


def test_search_course_failure():
    """
    When searching a course,
    if there is some kind of error,
    the response type should be "404-Resource Error".
    """
    repo = mock.Mock(spec=CourseRepo)
    request = CourseDataProvider().sample_search_course
    use_case = SearchCourse(course_repo=repo)
    repo.search_course.side_effect = Exception()

    response = use_case.execute(request)

    assert response.type == "404-Resource Error"
