from unittest import mock

from fastapi.testclient import TestClient

from app.domain.entities.course import Course
from app.main import app
from app.responses import FailureType, ResponseFailure, ResponseSuccess, SuccessType
from tests.test_data.course_data_provider import CourseDataProvider

test_data = CourseDataProvider()
client = TestClient(app)


@mock.patch("app.use_cases.search_course.SearchCourse")
def test_search_course_success(use_case):
    message = "The course has been fetched from the server."
    use_case().execute.return_value = ResponseSuccess(
        value=test_data.sample_course,
        message=message,
    )

    data = test_data.sample_search_course_dict
    response = client.get("/search_course", params=data)
    json_result = response.json()
    course = Course(**json_result.get("value"))

    use_case().execute.assert_called_with(data)
    assert response.status_code == SuccessType.SUCCESS.value
    assert course == test_data.sample_course
    assert json_result.get("message") == message


@mock.patch("app.use_cases.search_course.SearchCourse")
def test_search_course_failure(use_case):
    message = "Error"
    use_case().execute.return_value = ResponseFailure.build_from_resource_error(
        message=message,
    )

    data = test_data.sample_search_course_dict
    response = client.get("/search_course", params=data)

    assert response.status_code == FailureType.RESOURCE_ERROR.value
    assert response.json() == {"detail": "RESOURCE_ERROR: " + message}


@mock.patch("app.use_cases.filter_by_standards.FilterCourseByStandards")
def test_search_course_by_standards_success(use_case):
    message = "The course has been fetched from the server."
    use_case().execute.return_value = ResponseSuccess(
        value=test_data.sample_course,
        message=message,
    )

    data = test_data.sample_by_standards_dict
    response = client.get("/search_course_by_standards", params=data)
    json_result = response.json()
    course = Course(**json_result.get("value"))

    use_case().execute.assert_called_with(data)
    assert response.status_code == SuccessType.SUCCESS.value
    assert course == test_data.sample_course
    assert json_result.get("message") == message


@mock.patch("app.use_cases.filter_by_standards.FilterCourseByStandards")
def test_search_course_by_standards_failure(use_case):
    message = "Error"
    use_case().execute.return_value = ResponseFailure.build_from_resource_error(
        message=message,
    )

    data = test_data.sample_by_standards_dict
    response = client.get("/search_course_by_standards", params=data)

    assert response.status_code == FailureType.RESOURCE_ERROR.value
    assert response.json() == {"detail": "RESOURCE_ERROR: " + message}


@mock.patch("app.use_cases.filter_by_competency.FilterCourseByCompetency")
def test_search_course_by_competency_success(use_case):
    message = "The course has been fetched from the server."
    use_case().execute.return_value = ResponseSuccess(
        value=test_data.sample_course,
        message=message,
    )

    data = test_data.sample_by_competency_dict
    response = client.get("/search_course_by_competency", params=data)
    json_result = response.json()
    course = Course(**json_result.get("value"))

    use_case().execute.assert_called_with(data)
    assert response.status_code == SuccessType.SUCCESS.value
    assert course == test_data.sample_course
    assert json_result.get("message") == message


@mock.patch("app.use_cases.filter_by_competency.FilterCourseByCompetency")
def test_search_course_by_competency_failure(use_case):
    message = "Error"
    use_case().execute.return_value = ResponseFailure.build_from_resource_error(
        message=message,
    )

    data = test_data.sample_by_competency_dict
    response = client.get("/search_course_by_competency", params=data)

    assert response.status_code == FailureType.RESOURCE_ERROR.value
    assert response.json() == {"detail": "RESOURCE_ERROR: " + message}


@mock.patch("app.use_cases.filter_by_location.FilterCourseByLocation")
def test_search_course_by_location_success(use_case):
    message = "The course has been fetched from the server."
    use_case().execute.return_value = ResponseSuccess(
        value=test_data.sample_course,
        message=message,
    )

    data = test_data.sample_by_location_dict
    response = client.get("/search_course_by_location", params=data)
    json_result = response.json()
    course = Course(**json_result.get("value"))

    use_case().execute.assert_called_with(data)
    assert response.status_code == SuccessType.SUCCESS.value
    assert course == test_data.sample_course
    assert json_result.get("message") == message


@mock.patch("app.use_cases.filter_by_location.FilterCourseByLocation")
def test_search_course_by_location_failure(use_case):
    message = "Error"
    use_case().execute.return_value = ResponseFailure.build_from_resource_error(
        message=message,
    )

    data = test_data.sample_by_location_dict
    response = client.get("/search_course_by_location", params=data)

    assert response.status_code == FailureType.RESOURCE_ERROR.value
    assert response.json() == {"detail": "RESOURCE_ERROR: " + message}


@mock.patch("app.use_cases.filter_by_date.FilterCourseByDate")
def test_search_course_by_date_success(use_case):
    message = "The course has been fetched from the server."
    use_case().execute.return_value = ResponseSuccess(
        value=test_data.sample_course,
        message=message,
    )

    data = test_data.sample_by_date_dict
    response = client.get("/search_course_by_date", params=data)
    json_result = response.json()
    course = Course(**json_result.get("value"))

    use_case().execute.assert_called_with(data)
    assert response.status_code == SuccessType.SUCCESS.value
    assert course == test_data.sample_course
    assert json_result.get("message") == message


@mock.patch("app.use_cases.filter_by_date.FilterCourseByDate")
def test_search_course_by_date_failure(use_case):
    message = "Error"
    use_case().execute.return_value = ResponseFailure.build_from_resource_error(
        message=message,
    )

    data = test_data.sample_by_date_dict
    response = client.get("/search_course_by_date", params=data)

    assert response.status_code == FailureType.RESOURCE_ERROR.value
    assert response.json() == {"detail": "RESOURCE_ERROR: " + message}


@mock.patch("app.use_cases.filter_by_availability.FilterCourseByAvailability")
def test_search_course_by_availability_success(use_case):
    message = "The course has been fetched from the server."
    use_case().execute.return_value = ResponseSuccess(
        value=test_data.sample_course,
        message=message,
    )

    data = test_data.sample_by_availability_dict
    response = client.get("/search_course_by_availability", params=data)
    json_result = response.json()
    course = Course(**json_result.get("value"))

    use_case().execute.assert_called_with(data)
    assert response.status_code == SuccessType.SUCCESS.value
    assert course == test_data.sample_course
    assert json_result.get("message") == message


@mock.patch("app.use_cases.filter_by_availability.FilterCourseByAvailability")
def test_search_course_by_availability_failure(use_case):
    message = "Error"
    use_case().execute.return_value = ResponseFailure.build_from_resource_error(
        message=message,
    )

    data = test_data.sample_by_availability_dict
    response = client.get("/search_course_by_availability", params=data)

    assert response.status_code == FailureType.RESOURCE_ERROR.value
    assert response.json() == {"detail": "RESOURCE_ERROR: " + message}
