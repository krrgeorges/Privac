--
-- PostgreSQL database dump
--

-- Dumped from database version 10.9
-- Dumped by pg_dump version 10.9
CREATE DATABASE privac;

\c privac;

CREATE TABLE msgs (
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


CREATE TABLE users (
    uid integer,
    user_name text
);

--
-- PostgreSQL database dump complete
--

