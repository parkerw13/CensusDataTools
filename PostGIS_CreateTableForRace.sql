CREATE TABLE bay_area_race.alameda_race_acs_2018
(
    geoid_census character varying(25) NOT NULL,
    geo_name character varying(250) NOT NULL,
    geo_join character varying(15) NOT NULL,
    total_pop integer NOT NULL,
    white integer NOT NULL,
	prct_white numeric(6,2) NOT NULL,
    black integer NOT NULL,
	prct_black numeric(6,2) NOT NULL,
    am_indian_nat_alaska integer NOT NULL,
	prct_am_indian_nat_alaska numeric(6,2) NOT NULL,
    asian integer NOT NULL,
	prct_asian numeric(6,2) NOT NULL,
    nat_hawaiian_pac_island integer NOT NULL,
	prct_nat_hawiian_pac_island numeric(6,2) NOT NULL,
    some_other integer NOT NULL,
	prct_some_other numeric(6,2) NOT NULL,
    two_or_more integer NOT NULL,
	prct_two_or_more numeric(6,2) NOT NULL,
    hispanic_latino integer NOT NULL,
	prct_hispanic_latino numeric(6,2) NOT NULL,
    total_minority integer NOT NULL,
    percent_minority numeric(6, 2) NOT NULL,
	majority_population character varying(40) NOT NULL,
	percent_of_pop_majority_pop numeric(6, 2) NOT NULL,
    PRIMARY KEY (geoid_census)
);

ALTER TABLE bay_area_race.alameda_race_acs_2018
    OWNER to postgres;
