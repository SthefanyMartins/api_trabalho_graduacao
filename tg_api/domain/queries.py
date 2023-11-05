from pydantic import BaseModel


class StatesCountByRegion(BaseModel):
    region_name: str
    states_amount: int


class SchoolsWithRestrictedServicesByCity(BaseModel):
    school_name: str
    city_name: str


class PrivateHighSchoolsByRegion(BaseModel):
    school_name: str
    region_name: str


class AverageNumberOfSchoolsPerCityInRegion(BaseModel):
    region_name: str
    average_schools: float


class CityWithTheLargestNumberOfHigherEducationSchool(BaseModel):
    city_name: str
    college_count: int

class StateWithConcentrationOfPrivateElementarySchools(BaseModel):
    name_state: str
    elementary_school_count: float

class NumberOfHigherEducationSchoolsInEachCity(BaseModel):
    city_name: str
    college_count: int