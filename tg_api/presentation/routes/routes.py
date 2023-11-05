from typing import List

from fastapi import APIRouter, Depends
from tg_api.presentation.dependencies import application_container

from tg_api.domain.queries import (
    StatesCountByRegion,
    SchoolsWithRestrictedServicesByCity,
    PrivateHighSchoolsByRegion,
    AverageNumberOfSchoolsPerCityInRegion,
    CityWithTheLargestNumberOfHigherEducationSchool,
    StateWithConcentrationOfPrivateElementarySchools,
    NumberOfHigherEducationSchoolsInEachCity,
)

router = APIRouter()


@router.get("/states_count_by_region/", response_model=List[StatesCountByRegion])
async def get_states_count_by_region(dependencies=Depends(application_container)):
    states = await dependencies.queries_repository.states_count_by_region()

    return states


@router.get(
    "/restricted_services_with_schools_by_municipalities/",
    response_model=List[SchoolsWithRestrictedServicesByCity],
)
async def get_schools_with_restricted_services_by_municipalities(
    page:int = 1,
    dependencies=Depends(application_container),
):
    schools = (
        await dependencies.queries_repository.schools_with_restricted_services_by_municipalities(page)
    )

    return schools


@router.get(
    "/private_high_schools_by_region/",
    response_model=List[PrivateHighSchoolsByRegion],
)
async def get_private_high_schools_by_region(
    page:int = 1,
    dependencies=Depends(application_container),
):
    schools = (
        await dependencies.queries_repository.private_high_schools_by_region(page)
    )

    return schools


@router.get(
    "/average_number_of_schools_per_city_in_region/",
    response_model=List[AverageNumberOfSchoolsPerCityInRegion],
)
async def get_average_number_of_schools_per_city_in_region(
    dependencies=Depends(application_container),
):
    regions = (
        await dependencies.queries_repository.average_number_of_schools_per_city_in_region()
    )

    return regions


@router.get(
    "/city_with_the_largest_number_of_higher_education_school/",
    response_model=List[CityWithTheLargestNumberOfHigherEducationSchool],
)
async def get_city_with_the_largest_number_of_higher_education_school(
    dependencies=Depends(application_container),
):
    cities = (
        await dependencies.queries_repository.city_with_the_largest_number_of_higher_education_school()
    )

    return cities

@router.get(
    "/state_with_concentration_of_private_elementary_schools/",
    response_model=List[StateWithConcentrationOfPrivateElementarySchools],
)
async def get_state_with_concentration_of_private_elementary_schools(
    dependencies=Depends(application_container),
):
    states = (
        await dependencies.queries_repository.state_with_concentration_of_private_elementary_schools()
    )

    return states

@router.get(
    "/number_of_higher_education_schools_in_each_city/",
    response_model=List[NumberOfHigherEducationSchoolsInEachCity],
)
async def get_number_of_higher_education_schools_in_each_city(
    page:int = 1,
    dependencies=Depends(application_container),
):
    cities = (
        await dependencies.queries_repository.number_of_higher_education_schools_in_each_city(page)
    )

    return cities
