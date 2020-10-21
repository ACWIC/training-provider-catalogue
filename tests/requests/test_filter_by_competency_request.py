from app.requests.filter_by_competency_request import FilterByCompetencyRequest


def test_create_course_request():
    """
    When a NewCourseRequest is instantiated,
    the resulting object should have correct attribute values.
    """
    request = FilterByCompetencyRequest(
        competency="top rated",
    )

    assert request.competency == "top rated"
