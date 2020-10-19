import datetime

from app.requests.filter_by_date_request import FilterByDateRequest


def test_create_course_request():
    """
    When a NewCourseRequest is instantiated,
    the resulting object should have correct attribute values.
    """
    date = datetime.datetime.now()
    request = FilterByDateRequest(
        date=date,
    )

    assert request.date == date
