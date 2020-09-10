CREATE TABLE bay_area_race.alameda_block_group_race_2018
AS
SELECT * FROM bay_area_race.ca_block_groups JOIN bay_area_race.alameda_race_acs_2018
	ON ca_block_groups.geoid = alameda_race_acs_2018.geo_join;
