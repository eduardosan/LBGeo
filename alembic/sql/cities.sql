--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: cities; Type: TABLE; Schema: public; Owner: root; Tablespace: 
--

--CREATE TABLE cities (
--    id integer NOT NULL,
--    name character varying(255) NOT NULL,
--    lat double precision,
--    lng double precision,
--    state_id integer,
--    slug character varying(255) NOT NULL
--);

--
-- Name: cities_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('cities_id_seq', 5736, true);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY cities ALTER COLUMN id SET DEFAULT nextval('cities_id_seq'::regclass);


--
-- Data for Name: cities; Type: TABLE DATA; Schema: public; Owner: root
--

--COPY cities (id, name, lat, lng, state_id, slug) FROM stdin;
--\.

--
-- Name: index_cities_on_slug; Type: INDEX; Schema: public; Owner: root; Tablespace: 
--

CREATE UNIQUE INDEX index_cities_on_slug ON cities USING btree (slug);


--
-- PostgreSQL database dump complete
--

