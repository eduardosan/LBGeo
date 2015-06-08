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
-- Name: states; Type: TABLE; Schema: public; Owner: root; Tablespace: 
--

--CREATE TABLE states (
--    id integer NOT NULL,
--    name character varying(30) NOT NULL,
--    short_name character varying(4),
--    country_id integer,
--    slug character varying(255) NOT NULL
--);


--
-- Name: states_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('states_id_seq', 27, true);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY states ALTER COLUMN id SET DEFAULT nextval('states_id_seq'::regclass);


--
-- Data for Name: states; Type: TABLE DATA; Schema: public; Owner: root
--

--COPY states (id, name, short_name, country_id, slug) FROM stdin;
--\.


--
-- Name: index_states_on_slug; Type: INDEX; Schema: public; Owner: root; Tablespace: 
--

CREATE UNIQUE INDEX index_states_on_slug ON states USING btree (slug);


--
-- PostgreSQL database dump complete
--
