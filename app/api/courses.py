from datetime import datetime
from typing import List, Optional

from fastapi import APIRouter, HTTPException, Query

from app.repositories.s3_course_repo import S3CourseRepo
from app.use_cases.filter_by_availability import FilterCourseByAvailabilty
from app.use_cases.filter_by_competency import FilterCourseByCompetency
from app.use_cases.filter_by_date import FilterCourseByDate
from app.use_cases.filter_by_location import FilterCourseByLocation
from app.use_cases.filter_by_standards import FilterCourseByStandards
from app.use_cases.search_course import SearchCourse

router = APIRouter()
course_repo = S3CourseRepo()


@router.get("/search_course/")
def search_course(
    industry_standards: Optional[List[str]] = Query(None),
    competency: Optional[List[str]] = Query(None),
    location: Optional[str] = None,
    from_date: Optional[datetime] = None,
    to_date: Optional[datetime] = None,
    availability: Optional[bool] = None,
):
    """
    <p>
    This is a public, read-only API that allows Aged Care Provider (employer) to:\n
    the employer is able to:
    <ul>
      <li>search for courses meeting various criteria, so they can organise training for staff.</li>
      <li>see what industry standards the training provider supports</li>
    </ul>
    \n
    It is part of the interface standard because it allows employers to\n
    federate search results from multiple training providers.\n
    He can filter on the basis of:\n
    <ul>
      <li><b>industry_standards</b>, courses thats meet 1 or more IndustryStandards designations
       eg Police Check, drivers licence, etc </li>
      <li><b>competency</b>, courses thats meet 1 or more competencies</li>
      <li><b>location</b>, specified location where the courses are being offered  </li>
      <li><b>from_date</b>, first date of the date range, courses will be offered in </li>
      <li><b>to_date</b>, last date of the date range, courses will be offered in</li>
      <li><b>availability</b>, courses that are currently active / available with vacancies for students </li>
    </ul>
    \n
    </p>
    """
    inputs = {
        "industry_standards": industry_standards,
        "competency": competency,
        "location": location,
        "from_date": from_date,
        "to_date": to_date,
        "availability": availability,
    }
    use_case = SearchCourse(course_repo=course_repo)
    response = use_case.execute(inputs)
    if bool(response) is False:  # If request failed
        raise HTTPException(status_code=response.type.value, detail=response.message)
    return response


@router.get("/search_course_by_standards/")
def search_course_by_standards(
    industry_standards: Optional[List[str]] = Query(None),
):
    """
    <p>
    Aged Care Provider (employer) can filter courses on the basis of:\n
    <ul>
      <li><b>industry_standards</b>, courses thats meet 1 or more IndustryStandards designations
       eg Police Check, drivers licence, etc </li>
    </ul>
    \n
    </p>
    """
    inputs = {
        "industry_standards": industry_standards,
    }
    use_case = FilterCourseByStandards(course_repo=course_repo)
    response = use_case.execute(inputs)
    if bool(response) is False:  # If request failed
        raise HTTPException(status_code=response.type.value, detail=response.message)
    return response


@router.get("/search_course_by_competency/")
def search_course_by_competency(
    competency: Optional[List[str]] = Query(None),
):
    """
    <p>
    Aged Care Provider (employer) can filter courses on the basis of:\n
    <ul>
      <li><b>competency</b>, courses thats meet 1 or more competencies</li>
    </ul>
    \n
    </p>
    """
    inputs = {
        "competency": competency,
    }
    use_case = FilterCourseByCompetency(course_repo=course_repo)
    response = use_case.execute(inputs)
    if bool(response) is False:  # If request failed
        raise HTTPException(status_code=response.type.value, detail=response.message)
    return response


@router.get("/search_course_by_location/")
def search_course_by_location(
    location: Optional[str] = None,
):
    """
    <p>
    Aged Care Provider (employer) can filter courses on the basis of:\n
    <ul>
      <li><b>location</b>, specified location where the courses are being offered  </li>
    </ul>
    \n
    </p>
    """
    inputs = {
        "location": location,
    }
    use_case = FilterCourseByLocation(course_repo=course_repo)
    response = use_case.execute(inputs)
    if bool(response) is False:  # If request failed
        raise HTTPException(status_code=response.type.value, detail=response.message)
    return response


@router.get("/search_course_by_date/")
def search_course_by_date(
    from_date: Optional[datetime] = None,
    to_date: Optional[datetime] = None,
):
    """
    <p>
    Aged Care Provider (employer) can filter courses on the basis of:\n
    <ul>
      <li><b>from_date</b>, first date of the date range, courses will be offered in </li>
      <li><b>to_date</b>, last date of the date range, courses will be offered in</li>
    </ul>
    \n
    </p>
    """
    inputs = {
        "from_date": from_date,
        "to_date": to_date,
    }
    use_case = FilterCourseByDate(course_repo=course_repo)
    response = use_case.execute(inputs)
    if bool(response) is False:  # If request failed
        raise HTTPException(status_code=response.type.value, detail=response.message)
    return response


@router.get("/search_course_by_availability/")
def search_course_by_availability(
    availability: Optional[bool] = None,
):
    """
    <p>
    Aged Care Provider (employer) can filter courses on the basis of:\n
    <ul>
      <li><b>availability</b>, courses that are currently active / available with vacancies for students </li>
    </ul>
    \n
    </p>
    """
    inputs = {
        "availability": availability,
    }
    use_case = FilterCourseByAvailabilty(course_repo=course_repo)
    response = use_case.execute(inputs)
    if bool(response) is False:  # If request failed
        raise HTTPException(status_code=response.type.value, detail=response.message)
    return response
