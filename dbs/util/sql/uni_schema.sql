
/*
DROP DATABASE uni;
*/

/* 
DROP TABLE hoeren;
DROP TABLE voraussetzen;
DROP TABLE pruefen;
DROP TABLE vorlesungen;
DROP TABLE studenten;
DROP TABLE assistenten;
DROP TABLE professoren; 
*/

create database uni;

\c uni;

CREATE TABLE studenten
       (MatrNr         INTEGER,
        Name           VARCHAR(30),
        Semester       INTEGER
        );

CREATE TABLE professoren
       (PersNr         INTEGER,
        Name           VARCHAR(30),
        Rang           CHAR(2),
        Raum           INTEGER
        );

CREATE TABLE assistenten
       (PersNr         INTEGER,
        Name           VARCHAR(30),
        Fachgebiet     VARCHAR(30),
        Boss           INTEGER
        );

CREATE TABLE vorlesungen
       (VorlNr         INTEGER,
        Titel          VARCHAR(30),
        SWS            INTEGER,
        gelesenVon     INTEGER
        );

CREATE TABLE hoeren
       (MatrNr         INTEGER,
        VorlNr         INTEGER
        );

CREATE TABLE voraussetzen
       (Vorgänger     INTEGER,
        Nachfolger     INTEGER
        );

CREATE TABLE pruefen
       (MatrNr         INTEGER,
        VorlNr         INTEGER,
        PersNr         INTEGER,
        Note           NUMERIC
        );
