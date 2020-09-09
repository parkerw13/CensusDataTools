CREATE TABLE public."alameda_block_group_race_2018"
AS
SELECT * FROM public."CA_BlockGroup" JOIN public."AlamedaRaceACS2018"
	ON "CA_BlockGroup".geoid = "AlamedaRaceACS2018".geo_join;