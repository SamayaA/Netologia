CREATE TABLE IF NOT EXISTS public.genre
(
    id integer NOT NULL DEFAULT nextval('genre_id_seq'::regclass),
    title character varying(50) COLLATE pg_catalog."default",
    CONSTRAINT genre_pkey PRIMARY KEY (id),
    CONSTRAINT genre_title_key UNIQUE (title)
)

TABLESPACE pg_default;

ALTER TABLE public.genre
    OWNER to neto202109090;

CREATE TABLE IF NOT EXISTS public.performer
(
    id integer NOT NULL DEFAULT nextval('performer_id_seq'::regclass),
    name character varying(50) COLLATE pg_catalog."default",
    genreid integer,
    CONSTRAINT performer_pkey PRIMARY KEY (id),
    CONSTRAINT performer_name_key UNIQUE (name),
    CONSTRAINT performer_genreid_fkey FOREIGN KEY (genreid)
        REFERENCES public.genre (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE public.performer
    OWNER to neto202109090;

CREATE TABLE IF NOT EXISTS public.album
(
    id integer NOT NULL DEFAULT nextval('album_id_seq'::regclass),
    title character varying(50) COLLATE pg_catalog."default",
    release_date date,
    performerid integer,
    CONSTRAINT album_pkey PRIMARY KEY (id),
    CONSTRAINT album_performerid_fkey FOREIGN KEY (performerid)
        REFERENCES public.performer (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE public.album
    OWNER to neto202109090;

CREATE TABLE IF NOT EXISTS public.track
(
    id integer NOT NULL DEFAULT nextval('track_id_seq'::regclass),
    title character varying(50) COLLATE pg_catalog."default",
    duration numeric,
    albumid integer,
    CONSTRAINT track_pkey PRIMARY KEY (id),
    CONSTRAINT track_albumid_fkey FOREIGN KEY (albumid)
        REFERENCES public.album (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE public.track
    OWNER to neto202109090;