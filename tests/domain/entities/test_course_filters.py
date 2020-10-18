import datetime

from app.domain.entities.course_filters import CourseFilters


def test_course_init():
    """
    Ensure the course filters data matches constructor values
    """
    date = datetime.datetime.now()

    course = CourseFilters(
        industry_standards="Police Check",
        competency="top rated",
        location="Sydney",
        date=date,
        availability=True,
    )

    assert course.industry_standards == "Police Check"
    assert course.competency == "top rated"
    assert course.location == "Sydney"
    assert course.date == date
    assert course.availability is True
