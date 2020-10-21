from app.requests.filter_by_location_request import FilterByLocationRequest


def test_create_course_request():
    """
    When a NewCourseRequest is instantiated,
    the resulting object should have correct attribute values.
    """
    request = FilterByLocationRequest(
        location="Sydney",
    )

    assert request.location == "Sydney"
