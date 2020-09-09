CREATE TABLE public."AlamedaRaceACS2018"
(
    geoid_census character varying(25) NOT NULL,
    geo_name character varying(250) NOT NULL,
    geo_join character varying(15) NOT NULL,
    total_pop integer NOT NULL,
    white integer NOT NULL,
    black integer NOT NULL,
    am_indian_nat_alaska integer NOT NULL,
    asian integer NOT NULL,
    nat_hawaiian_pac_island integer NOT NULL,
    some_other integer NOT NULL,
    two_or_more integer NOT NULL,
    hispanic_latino integer NOT NULL,
    total_minority integer NOT NULL,
    percent_minority numeric(6, 2) NOT NULL,
    PRIMARY KEY (geoid)
);

ALTER TABLE public."AlamedaRaceACS2018"
    OWNER to postgres;