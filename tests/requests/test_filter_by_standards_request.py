from app.requests.filter_by_standards_request import FilterByStandardsRequest


def test_create_course_request():
    """
    When a NewCourseRequest is instantiated,
    the resulting object should have correct attribute values.
    """
    request = FilterByStandardsRequest(industry_standards="Police Check")

    assert request.industry_standards == "Police Check"
