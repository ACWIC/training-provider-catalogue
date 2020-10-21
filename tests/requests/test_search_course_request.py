import datetime

from app.requests.search_course_request import SearchCourseRequest


def test_create_course_request():
    """
    When a NewCourseRequest is instantiated,
    the resulting object should have correct attribute values.
    """
    from_date = datetime.datetime.now()
    to_date = datetime.datetime.now().now()
    request = SearchCourseRequest(
        industry_standards="Police Check",
        competency="top rated",
        location="Sydney",
        from_date=from_date,
        to_date=to_date,
        availability=True,
    )

    assert request.industry_standards == "Police Check"
    assert request.competency == "top rated"
    assert request.location == "Sydney"
    assert request.from_date == from_date
    assert request.to_date == to_date
    assert request.availability is True
