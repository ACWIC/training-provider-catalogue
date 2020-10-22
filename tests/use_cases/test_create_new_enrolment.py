"""
These tests evaluate (and document) the business logic.
"""
from unittest import mock
from uuid import uuid4

from app.domain.entities.enrolment_authorisation import EnrolmentAuthorisation
from app.repositories.enrolment_repo import EnrolmentRepo
from app.requests.enrolment_requests import NewEnrolmentRequest
from app.use_cases.create_new_enrolment import CreateNewEnrolment


def test_create_new_enrolment_authorisation_success():
    """
    When creating a new enrollment authorisation,
    if everything goes according to plan,
    the response type should be "200-Success".
    """
    repo = mock.Mock(spec=EnrolmentRepo)
    enrolment = EnrolmentAuthorisation(uuid=uuid4(), course_id="123", student_id="abc")
    repo.save_enrolment.return_value = enrolment

    request = NewEnrolmentRequest(course_id="123", student_id="abc")
    use_case = CreateNewEnrolment(enrolment_repo=repo)
    response = use_case.execute(request)

    assert response.type == "200-Success"


def test_create_new_enrolment_authorisation_failure():
    """
    When creating a new enrollment authorisation,
    if there is some kind of error,
    the response type should be "404-Resource Error".
    """
    repo = mock.Mock(spec=EnrolmentRepo)

    repo.save_enrolment.side_effect = Exception()
    request = NewEnrolmentRequest(course_id="123", student_id="abc")
    use_case = CreateNewEnrolment(enrolment_repo=repo)
    response = use_case.execute(request)

    assert response.type == "404-Resource Error"
