from tg_api.domain.queries import (
    StatesCountByRegion,
    SchoolsWithRestrictedServicesByCity,
    PrivateHighSchoolsByRegion,
    AverageNumberOfSchoolsPerCityInRegion,
    CityWithTheLargestNumberOfHigherEducationSchool,
    StateWithConcentrationOfPrivateElementarySchools,
    NumberOfHigherEducationSchoolsInEachCity,
)
from tg_api.infrastructure.repository.raw_queries import (
    MODEL_BY_REGIONS_AND_COUNT_STATES,
    MODEL_BY_SCHOOLS_WITH_RESTRICTED_SERVICES_BY_MUNICIPALITIES,
    MODEL_BY_PRIVATE_HIGH_SCHOOLS_BY_REGION,
    MODEL_BY_AVERAGE_NUMBER_OF_SCHOOLS_PER_CITY_IN_REGION,
    MODEL_BY_CITY_WITH_THE_LARGEST_NUMBER_OF_HIGHER_EDUCATION_SCHOOL,
    MODEL_BY_STATE_WITH_CONCENTRATION_OF_PRIVATE_ELEMENTARY_SCHOOLS,
    MODEL_BY_NUMBER_OF_HIGHER_EDUCATION_SCHOOLS_IN_EACH_CITY,
)


class QueriesRepository:
    def __init__(self, database) -> None:
        self._database = database

    async def states_count_by_region(self) -> StatesCountByRegion:
        result = await self._database.fetch_all(query=MODEL_BY_REGIONS_AND_COUNT_STATES)
        return self.__result_dataset_to_model(result, StatesCountByRegion)

    async def schools_with_restricted_services_by_municipalities(
        self,
        page:int,
    ) -> SchoolsWithRestrictedServicesByCity:
        offset = (page - 1) * 100
        result = await self._database.fetch_all(
            query=MODEL_BY_SCHOOLS_WITH_RESTRICTED_SERVICES_BY_MUNICIPALITIES,
            values={"limit": 100, "offset": offset}
        )
        return self.__result_dataset_to_model(
            result, SchoolsWithRestrictedServicesByCity
        )
    
    async def private_high_schools_by_region(
        self,
        page:int,
    ) -> PrivateHighSchoolsByRegion:
        offset = (page - 1) * 100
        result = await self._database.fetch_all(
            query=MODEL_BY_PRIVATE_HIGH_SCHOOLS_BY_REGION,
            values={"limit": 100, "offset": offset}
        )
        return self.__result_dataset_to_model(
            result, PrivateHighSchoolsByRegion
        )
    
    async def average_number_of_schools_per_city_in_region(
        self,
    ) -> AverageNumberOfSchoolsPerCityInRegion:
        result = await self._database.fetch_all(
            query=MODEL_BY_AVERAGE_NUMBER_OF_SCHOOLS_PER_CITY_IN_REGION
        )
        return self.__result_dataset_to_model(
            result, AverageNumberOfSchoolsPerCityInRegion
        )
    
    async def city_with_the_largest_number_of_higher_education_school(
        self,
    ) -> CityWithTheLargestNumberOfHigherEducationSchool:
        result = await self._database.fetch_all(
            query=MODEL_BY_CITY_WITH_THE_LARGEST_NUMBER_OF_HIGHER_EDUCATION_SCHOOL,
        )
        return self.__result_dataset_to_model(
            result, CityWithTheLargestNumberOfHigherEducationSchool
        )
    
    async def state_with_concentration_of_private_elementary_schools(
        self,
    ) -> StateWithConcentrationOfPrivateElementarySchools:
        result = await self._database.fetch_all(
            query=MODEL_BY_STATE_WITH_CONCENTRATION_OF_PRIVATE_ELEMENTARY_SCHOOLS,
        )
        return self.__result_dataset_to_model(
            result, StateWithConcentrationOfPrivateElementarySchools
        )
    
    async def number_of_higher_education_schools_in_each_city(
        self,
        page:int,
    ) -> NumberOfHigherEducationSchoolsInEachCity:
        offset = (page - 1) * 100
        result = await self._database.fetch_all(
            query=MODEL_BY_NUMBER_OF_HIGHER_EDUCATION_SCHOOLS_IN_EACH_CITY,
            values={"limit": 100, "offset": offset}
        )
        return self.__result_dataset_to_model(
            result, NumberOfHigherEducationSchoolsInEachCity
        )

    def __result_dataset_to_model(self, data, model_type):
        result = []
        for item in data:
            result.append(model_type(**item))

        return result
