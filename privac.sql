--
-- PostgreSQL database dump
--

-- Dumped from database version 10.9
-- Dumped by pg_dump version 10.9

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: msgs; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.msgs (
    mid text NOT NULL,
    uid_from integer,
    uid_to integer,
    msg_text text,
    read_status integer,
    mtime integer,
    ftype text,
    fname text,
    fcontent text,
    furl text
);


ALTER TABLE public.msgs OWNER TO postgres;

--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    uid integer,
    user_name text
);


ALTER TABLE public.users OWNER TO postgres;

--
-- Data for Name: msgs; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.msgs (mid, uid_from, uid_to, msg_text, read_status, mtime, ftype, fname, fcontent, furl) FROM stdin;
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (uid, user_name) FROM stdin;
\.


--
-- Name: msgs msgs_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.msgs
    ADD CONSTRAINT msgs_pkey PRIMARY KEY (mid);


--
-- PostgreSQL database dump complete
--

