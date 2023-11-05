MODEL_BY_REGIONS_AND_COUNT_STATES = """\
SELECT 
    r.name_region AS region_name,
    COUNT(s.code_state) AS states_amount
FROM public.regions r
LEFT JOIN public.states s ON r.code_region = s.code_region
GROUP BY r.name_region;
"""

MODEL_BY_SCHOOLS_WITH_RESTRICTED_SERVICES_BY_MUNICIPALITIES = """\
SELECT 
    sc.name_school AS school_name, 
    m.name_muni AS city_name
FROM public.schools sc
JOIN public.municipalities m ON sc.code_muni = m.code_muni
WHERE sc.urban = 'Urbana' AND sc.service_restriction IS NOT NULL
LIMIT :limit OFFSET :offset;
"""

MODEL_BY_PRIVATE_HIGH_SCHOOLS_BY_REGION = """\
SELECT
    sc.name_school AS school_name,
    r.name_region AS region_name
FROM public.schools sc
JOIN public.states s ON sc.code_state = s.code_state
JOIN public.regions r ON s.code_region = r.code_region
WHERE sc.government_level = 'Privada' AND sc.education_level like 'Ensino Médio'
LIMIT :limit OFFSET :offset;
"""

MODEL_BY_AVERAGE_NUMBER_OF_SCHOOLS_PER_CITY_IN_REGION = """\
SELECT 
    r.name_region AS region_name, 
    AVG(school_count) AS average_schools
FROM (
    SELECT m.code_state, COUNT(sc.code_school) AS school_count
    FROM public.municipalities m
    LEFT JOIN public.schools sc ON m.code_muni = sc.code_muni
    GROUP BY m.code_state
) AS schools_per_state
JOIN public.states s ON schools_per_state.code_state = s.code_state
JOIN public.regions r ON s.code_region = r.code_region
GROUP BY r.name_region;
"""

MODEL_BY_CITY_WITH_THE_LARGEST_NUMBER_OF_HIGHER_EDUCATION_SCHOOL = """\
SELECT
    m.name_muni AS city_name,
    COUNT(sc.code_school) AS college_count
FROM public.municipalities m
LEFT JOIN public.schools sc ON m.code_muni = sc.code_muni
WHERE sc.education_level like '%Educação Profissional%'
GROUP BY m.name_muni
ORDER BY college_count DESC
LIMIT 1;
"""

MODEL_BY_STATE_WITH_CONCENTRATION_OF_PRIVATE_ELEMENTARY_SCHOOLS = """\
SELECT 
    s.name_state AS name_state, 
    COUNT(sc.code_school) AS elementary_school_count
FROM public.states s
LEFT JOIN public.schools sc ON s.code_state = sc.code_state
where sc.education_level like '%Ensino Fundamental%' AND sc.government_level = 'Privada'
GROUP BY s.name_state
ORDER BY elementary_school_count DESC;
"""

MODEL_BY_NUMBER_OF_HIGHER_EDUCATION_SCHOOLS_IN_EACH_CITY = """\
SELECT
    m.name_muni AS city_name,
    COUNT(sc.code_school) AS college_count
FROM public.municipalities m
LEFT JOIN public.schools sc ON m.code_muni = sc.code_muni
WHERE sc.education_level like '%Educação Profissional%'
GROUP BY m.name_muni
ORDER BY college_count DESC
LIMIT :limit OFFSET :offset;
"""