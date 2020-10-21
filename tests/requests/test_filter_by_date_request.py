import datetime

from app.requests.filter_by_date_request import FilterByDateRequest


def test_create_course_request():
    """
    When a NewCourseRequest is instantiated,
    the resulting object should have correct attribute values.
    """
    from_date = datetime.datetime.now()
    to_date = datetime.datetime.now()
    request = FilterByDateRequest(
        from_date=from_date,
        to_date=to_date,
    )

    assert request.from_date == from_date
    assert request.to_date == to_date
