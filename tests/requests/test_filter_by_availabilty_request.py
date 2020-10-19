from app.requests.filter_by_availabilty_request import FilterByAvailabilityRequest


def test_create_course_request():
    """
    When a NewCourseRequest is instantiated,
    the resulting object should have correct attribute values.
    """
    request = FilterByAvailabilityRequest(
        availability=True,
    )

    assert request.availability is True
