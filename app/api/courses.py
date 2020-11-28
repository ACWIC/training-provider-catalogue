from datetime import datetime
from typing import List, Optional

from fastapi import APIRouter, HTTPException, Query

from app.repositories.s3_course_repo import S3CourseRepo
from app.use_cases import filter_by_availability as fba
from app.use_cases import filter_by_competency as fbc
from app.use_cases import filter_by_date as fbd
from app.use_cases import filter_by_location as fbl
from app.use_cases import filter_by_standards as fbs
from app.use_cases import search_course as sc

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
    This is a public, read-only API that allows Aged Care Provider (employer) to:\n
    - search for courses meeting various criteria, so they can organise training for staff.\n
    - see what industry standards the training provider supports\n\n
    It is part of the interface standard because it allows employers to\n
    federate search results from multiple training providers.\n
    He can filter on the basis of:\n
    **industry_standards** courses thats meet 1 or more IndustryStandards designations
       eg Police Check, drivers licence, etc \n
    **competency** courses thats meet 1 or more competencies\n
    **location** specified location where the courses are being offered  \n
    **from_date** first date of the date range, courses will be offered in \n
    **to_date** last date of the date range, courses will be offered in\n
    **availability** courses that are currently active / available with vacancies for students \n
    """
    inputs = {
        "industry_standards": industry_standards,
        "competency": competency,
        "location": location,
        "from_date": from_date,
        "to_date": to_date,
        "availability": availability,
    }
    use_case = sc.SearchCourse(course_repo=course_repo)
    response = use_case.execute(inputs)
    if bool(response) is False:  # If request failed
        raise HTTPException(status_code=response.type.value, detail=response.message)
    return response


@router.get("/search_course_by_standards/")
def search_course_by_standards(
    industry_standards: Optional[List[str]] = Query(None),
):
    """
    Aged Care Provider (employer) can filter courses on the basis of:\n
    **industry_standards** courses thats meet 1 or more IndustryStandards designations
       eg Police Check, drivers licence, etc \n
    """
    inputs = {
        "industry_standards": industry_standards,
    }
    use_case = fbs.FilterCourseByStandards(course_repo=course_repo)
    response = use_case.execute(inputs)
    if bool(response) is False:  # If request failed
        raise HTTPException(status_code=response.type.value, detail=response.message)
    return response


@router.get("/search_course_by_competency/")
def search_course_by_competency(
    competency: Optional[List[str]] = Query(None),
):
    """
    Aged Care Provider (employer) can filter courses on the basis of:\n
    **competency** courses thats meet 1 or more competencies\n
    """
    inputs = {
        "competency": competency,
    }
    use_case = fbc.FilterCourseByCompetency(course_repo=course_repo)
    response = use_case.execute(inputs)
    if bool(response) is False:  # If request failed
        raise HTTPException(status_code=response.type.value, detail=response.message)
    return response


@router.get("/search_course_by_location/")
def search_course_by_location(
    location: Optional[str] = None,
):
    """
    Aged Care Provider (employer) can filter courses on the basis of:\n
    **location** specified location where the courses are being offered  \n
    """
    inputs = {
        "location": location,
    }
    use_case = fbl.FilterCourseByLocation(course_repo=course_repo)
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
    Aged Care Provider (employer) can filter courses on the basis of:\n
    **from_date** first date of the date range, courses will be offered in \n
    **to_date** last date of the date range, courses will be offered in\n
    """
    inputs = {
        "from_date": from_date,
        "to_date": to_date,
    }
    use_case = fbd.FilterCourseByDate(course_repo=course_repo)
    response = use_case.execute(inputs)
    if bool(response) is False:  # If request failed
        raise HTTPException(status_code=response.type.value, detail=response.message)
    return response


@router.get("/search_course_by_availability/")
def search_course_by_availability(
    availability: Optional[bool] = None,
):
    """
    Aged Care Provider (employer) can filter courses on the basis of:\n
    **availability** courses that are currently active / available with vacancies for students \n
    """
    inputs = {
        "availability": availability,
    }
    use_case = fba.FilterCourseByAvailability(course_repo=course_repo)
    response = use_case.execute(inputs)
    if bool(response) is False:  # If request failed
        raise HTTPException(status_code=response.type.value, detail=response.message)
    return response
