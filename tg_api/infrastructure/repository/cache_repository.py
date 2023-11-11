import json
from typing import List

from pydantic import BaseModel
from tg_api.domain.queries import (
    StatesCountByRegion,
    SchoolsWithRestrictedServicesByCity,
    PrivateHighSchoolsByRegion,
    AverageNumberOfSchoolsPerCityInRegion,
    CityWithTheLargestNumberOfHigherEducationSchool,
    StateWithConcentrationOfPrivateElementarySchools,
    NumberOfHigherEducationSchoolsInEachCity,
)


class CacheRepository:
    def __init__(self, redis) -> None:
        self._redis = redis

    async def set_states_count_by_region(self, states_count: List[StatesCountByRegion]):
        await self._redis.set(
            "states_count_by_region", self.__serialize_list_of_models(states_count)
        )

    async def get_states_count_by_region(self):
        response = await self._redis.get("states_count_by_region")
        if not response:
            return

        return self.__deserialize_list_of_models(response, StatesCountByRegion)

    async def set_schools_with_restricted_services_by_municipalities(
        self, page:int, schools_list: List[SchoolsWithRestrictedServicesByCity]
    ):
        await self._redis.set(
            f"schools_with_restricted_services_by_municipalities_{page}",
            self.__serialize_list_of_models(schools_list),
        )

    async def get_schools_with_restricted_services_by_municipalities(self, page:int):
        response = await self._redis.get(
            f"schools_with_restricted_services_by_municipalities_{page}"
        )
        if not response:
            return

        return self.__deserialize_list_of_models(
            response, SchoolsWithRestrictedServicesByCity
        )

    async def set_private_high_schools_by_region(
        self, page:int, schools_list: List[PrivateHighSchoolsByRegion]
    ):
        await self._redis.set(
            f"private_high_schools_by_region_{page}",
            self.__serialize_list_of_models(schools_list),
        )

    async def get_private_high_schools_by_region(self, page:int):
        response = await self._redis.get(
            f"private_high_schools_by_region_{page}"
        )
        if not response:
            return

        return self.__deserialize_list_of_models(
            response, PrivateHighSchoolsByRegion,
        )
    
    async def set_average_number_of_schools_per_city_in_region(
        self, regions_list: List[AverageNumberOfSchoolsPerCityInRegion]
    ):
        await self._redis.set(
            "average_number_of_schools_per_city_in_region",
            self.__serialize_list_of_models(regions_list),
        )

    async def get_average_number_of_schools_per_city_in_region(self):
        response = await self._redis.get(
            "average_number_of_schools_per_city_in_region"
        )
        if not response:
            return

        return self.__deserialize_list_of_models(
            response, AverageNumberOfSchoolsPerCityInRegion,
        )
    
    async def set_city_with_the_largest_number_of_higher_education_school(
        self, cities_list: List[CityWithTheLargestNumberOfHigherEducationSchool]
    ):
        await self._redis.set(
            "city_with_the_largest_number_of_higher_education_school",
            self.__serialize_list_of_models(cities_list),
        )

    async def get_city_with_the_largest_number_of_higher_education_school(self):
        response = await self._redis.get(
            "city_with_the_largest_number_of_higher_education_school"
        )
        if not response:
            return

        return self.__deserialize_list_of_models(
            response, CityWithTheLargestNumberOfHigherEducationSchool,
        )
    
    async def set_state_with_concentration_of_private_elementary_schools(
        self, states_list: List[StateWithConcentrationOfPrivateElementarySchools]
    ):
        await self._redis.set(
            "state_with_concentration_of_private_elementary_schools",
            self.__serialize_list_of_models(states_list),
        )

    async def get_state_with_concentration_of_private_elementary_schools(self):
        response = await self._redis.get(
            "state_with_concentration_of_private_elementary_schools"
        )
        if not response:
            return

        return self.__deserialize_list_of_models(
            response, StateWithConcentrationOfPrivateElementarySchools,
        )
    
    async def set_number_of_higher_education_schools_in_each_city(
        self, 
        page:int, 
        cities_list: List[NumberOfHigherEducationSchoolsInEachCity]
    ):
        await self._redis.set(
            f"number_of_higher_education_schools_in_each_city_{page}",
            self.__serialize_list_of_models(cities_list),
        )

    async def get_number_of_higher_education_schools_in_each_city(
        self, 
        page:int
    ):
        response = await self._redis.get(
            f"number_of_higher_education_schools_in_each_city_{page}"
        )
        if not response:
            return

        return self.__deserialize_list_of_models(
            response, NumberOfHigherEducationSchoolsInEachCity,
        )
    
    async def set_states_count_by_region_with_ttl(self, states_count: List[StatesCountByRegion]):
        await self._redis.incr("states_count_by_region_counting_key")
        await self._redis.set(
            "states_count_by_region", self.__serialize_list_of_models(states_count)
        )

    async def get_states_count_by_region_with_ttl(self):
        response = await self._redis.get("states_count_by_region")
        if not response:
            return

        counting_key = await self._redis.get(
            "states_count_by_region_counting_key"
        )
        if int(counting_key) < 100:
            await self._redis.incr("states_count_by_region_counting_key")
        else:
            await self._redis.delete("states_count_by_region_counting_key")
            set_states_count_by_region_with_ttl(
                self.__deserialize_list_of_models(
                    response, 
                    StatesCountByRegion
                )
            )
        
        return self.__deserialize_list_of_models(response, StatesCountByRegion)
    
    async def set_schools_with_restricted_services_by_municipalities_with_ttl(
        self,
        page:int,
        schools_count: List[SchoolsWithRestrictedServicesByCity]
    ):
        await self._redis.incr(
            f"schools_with_restricted_services_by_municipalities_{page}_counting_key"
        )
        await self._redis.set(
            f"schools_with_restricted_services_by_municipalities_{page}", 
            self.__serialize_list_of_models(schools_count)
        )

    async def get_schools_with_restricted_services_by_municipalities_with_ttl(
        self,
        page:int
    ):
        response = await self._redis.get(
            f"schools_with_restricted_services_by_municipalities_{page}"
        )
        if not response:
            return

        counting_key = await self._redis.get(
            f"schools_with_restricted_services_by_municipalities_{page}_counting_key"
        )
        if int(counting_key) < 100:
            await self._redis.incr(
                f"schools_with_restricted_services_by_municipalities_{page}_counting_key"
            )
        else:
            await self._redis.delete(
                f"schools_with_restricted_services_by_municipalities_{page}_counting_key"
            )
            set_schools_with_restricted_services_by_municipalities_with_ttl(
                self.__deserialize_list_of_models(
                    response,
                    page,
                    SchoolsWithRestrictedServicesByCity
                )
            )
        
        return self.__deserialize_list_of_models(
            response, 
            SchoolsWithRestrictedServicesByCity
        )
    
    async def set_private_high_schools_by_region_with_ttl(
        self, 
        page:int, 
        schools_count: List[PrivateHighSchoolsByRegion]
    ):
        await self._redis.incr(
            f"private_high_schools_by_region_{page}_counting_key"
        )
        await self._redis.set(
            f"private_high_schools_by_region_{page}_counting_key", 
            self.__serialize_list_of_models(schools_count)
        )

    async def get_private_high_schools_by_region_with_ttl(self, page:int):
        response = await self._redis.get(
            f"private_high_schools_by_region_{page}"
        )
        if not response:
            return

        counting_key = await self._redis.get(
            f"private_high_schools_by_region_{page}_counting_key"
        )
        if int(counting_key) < 100:
            await self._redis.incr(
                f"private_high_schools_by_region_{page}_counting_key"
            )
        else:
            await self._redis.delete(
                f"private_high_schools_by_region_{page}_counting_key"
            )
            set_schools_with_restricted_services_by_municipalities_with_ttl(
                self.__deserialize_list_of_models(
                    response, 
                    PrivateHighSchoolsByRegion
                )
            )
        
        return self.__deserialize_list_of_models(
            response, 
            PrivateHighSchoolsByRegion
        )
    
    async def set_average_number_of_schools_per_city_in_region_with_ttl(
        self, 
        regions_count: List[AverageNumberOfSchoolsPerCityInRegion]
    ):
        await self._redis.incr(
            "average_number_of_schools_per_city_in_region_counting_key"
        )
        await self._redis.set(
            "average_number_of_schools_per_city_in_region",
            self.__serialize_list_of_models(regions_count)
        )

    async def get_average_number_of_schools_per_city_in_region_with_ttl(self):
        response = await self._redis.get(
            "average_number_of_schools_per_city_in_region"
        )
        if not response:
            return

        counting_key = await self._redis.get(
            "average_number_of_schools_per_city_in_region_counting_key"
        )
        if int(counting_key) < 100:
            await self._redis.incr(
                "average_number_of_schools_per_city_in_region_counting_key"
            )
        else:
            await self._redis.delete(
                "average_number_of_schools_per_city_in_region_counting_key"
            )
            set_average_number_of_schools_per_city_in_region_with_ttl(
                self.__deserialize_list_of_models(
                    response, 
                    AverageNumberOfSchoolsPerCityInRegion
                )
            )
        
        return self.__deserialize_list_of_models(response, StatesCountByRegion)
    
    async def set_city_with_the_largest_number_of_higher_education_school_with_ttl(
        self, 
        cities_count: List[CityWithTheLargestNumberOfHigherEducationSchool]
    ):
        await self._redis.incr(
            "city_with_the_largest_number_of_higher_education_school_counting_key"
        )
        await self._redis.set(
            "city_with_the_largest_number_of_higher_education_school",
            self.__serialize_list_of_models(cities_count)
        )

    async def get_city_with_the_largest_number_of_higher_education_school_with_ttl(self):
        response = await self._redis.get(
            "city_with_the_largest_number_of_higher_education_school"
        )
        if not response:
            return

        counting_key = await self._redis.get(
            "city_with_the_largest_number_of_higher_education_school_counting_key"
        )
        if int(counting_key) < 100:
            await self._redis.incr(
                "city_with_the_largest_number_of_higher_education_school_counting_key"
            )
        else:
            await self._redis.delete(
                "city_with_the_largest_number_of_higher_education_school_counting_key"
            )
            set_city_with_the_largest_number_of_higher_education_school_with_ttl(
                self.__deserialize_list_of_models(
                    response, 
                    CityWithTheLargestNumberOfHigherEducationSchool
                )
            )
        
        return self.__deserialize_list_of_models(response, StatesCountByRegion)
    
    async def set_state_with_concentration_of_private_elementary_schools_with_ttl(
        self, 
        states_count: List[StateWithConcentrationOfPrivateElementarySchools]
    ):
        await self._redis.incr(
            "state_with_concentration_of_private_elementary_schools_counting_key"
        )
        await self._redis.set(
            "state_with_concentration_of_private_elementary_schools",
            self.__serialize_list_of_models(states_count)
        )

    async def get_state_with_concentration_of_private_elementary_schools_with_ttl(self):
        response = await self._redis.get(
            "state_with_concentration_of_private_elementary_schools"
        )
        if not response:
            return

        counting_key = await self._redis.get(
            "state_with_concentration_of_private_elementary_schools_counting_key"
        )
        if int(counting_key) < 100:
            await self._redis.incr(
                "state_with_concentration_of_private_elementary_schools_counting_key"
            )
        else:
            await self._redis.delete(
                "state_with_concentration_of_private_elementary_schools_counting_key"
            )
            set_state_with_concentration_of_private_elementary_schools_with_ttl(
                self.__deserialize_list_of_models(
                    response, 
                    StateWithConcentrationOfPrivateElementarySchools
                )
            )
        
        return self.__deserialize_list_of_models(response, StatesCountByRegion)
    
    async def set_number_of_higher_education_schools_in_each_city_with_ttl(
        self, 
        page:int, 
        cities_count: List[NumberOfHigherEducationSchoolsInEachCity]
    ):
        await self._redis.incr(
            f"number_of_higher_education_schools_in_each_city_{page}_counting_key"
        )
        await self._redis.set(
            f"number_of_higher_education_schools_in_each_city_{page}", 
            self.__serialize_list_of_models(cities_count)
        )

    async def get_number_of_higher_education_schools_in_each_city_with_ttl(self, page:int):
        response = await self._redis.get(
            f"number_of_higher_education_schools_in_each_city_{page}"
        )
        if not response:
            return

        counting_key = await self._redis.get(
            f"number_of_higher_education_schools_in_each_city_{page}_counting_key"
        )
        if int(counting_key) < 100:
            await self._redis.incr(
                f"number_of_higher_education_schools_in_each_city_{page}_counting_key"
            )
        else:
            await self._redis.delete(
                f"number_of_higher_education_schools_in_each_city_{page}_counting_key"
            )
            set_number_of_higher_education_schools_in_each_city_with_ttl(
                self.__deserialize_list_of_models(
                    response, 
                    NumberOfHigherEducationSchoolsInEachCity
                )
            )
        
        return self.__deserialize_list_of_models(
            response, 
            NumberOfHigherEducationSchoolsInEachCity
        )
    
    async def flushall(self):
        await self._redis.flushall()
    
    def __serialize_list_of_models(self, model_list: List[BaseModel]):
        return json.dumps(model_list, default=lambda x: x.model_dump())

    def __deserialize_list_of_models(self, data: str, model_type):
        model_list = json.loads(data)

        return [model_type(**item) for item in model_list]
