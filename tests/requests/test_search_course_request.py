import datetime

from app.requests.search_course_request import SearchCourseRequest


def test_create_course_request():
    """
    When a NewCourseRequest is instantiated,
    the resulting object should have correct attribute values.
    """
    date = datetime.datetime.now()
    request = SearchCourseRequest(
        industry_standards="Police Check",
        competency="top rated",
        location="Sydney",
        date=date,
        availability=True,
    )

    assert request.industry_standards == "Police Check"
    assert request.competency == "top rated"
    assert request.location == "Sydney"
    assert request.date == date
    assert request.availability is True
