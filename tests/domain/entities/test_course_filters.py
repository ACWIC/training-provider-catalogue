import datetime

from app.domain.entities.course_filters import CourseFilters


def test_course_init():
    """
    Ensure the course filters data matches constructor values
    """
    from_date = datetime.datetime.now()
    to_date = datetime.datetime.now().now()

    course_filters = CourseFilters(
        industry_standards=["Police Check", "Security check"],
        competency=["top rated", "experienced"],
        location="Sydney",
        from_date=from_date,
        to_date=to_date,
        availability=True,
    )

    assert course_filters.industry_standards == ["Police Check", "Security check"]
    assert course_filters.competency == ["top rated", "experienced"]
    assert course_filters.location == "Sydney"
    assert course_filters.from_date == from_date
    assert course_filters.to_date == to_date
    assert course_filters.availability is True
