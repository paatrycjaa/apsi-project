-- MySQL



CREATE TABLE administratorzy (
    uzytkownik_id INTEGER NOT NULL
)
;

ALTER TABLE administratorzy ADD CONSTRAINT administrator_pk PRIMARY KEY ( uzytkownik_id );

CREATE TABLE czlonkowie_komisji (
    uzytkownik_id INTEGER NOT NULL
)
;

ALTER TABLE czlonkowie_komisji ADD CONSTRAINT czlonek_komisji_pk PRIMARY KEY ( uzytkownik_id );

CREATE TABLE decyzje (
    decyzja_id                        INTEGER NOT NULL,
    data                              DATETIME NOT NULL,
    uzasadnienie                      VARCHAR(1000),
    pomysl_pomysl_id                  INTEGER NOT NULL, 
-- SQLINES DEMO *** me length exceeds maximum allowed length(30) 
    rodzaj_decyzji_rodzaj_decyzji_id  VARCHAR(100) NOT NULL,
    czlonek_komisji_uzytkownik_id     INTEGER NOT NULL
)
;

ALTER TABLE decyzje ADD CONSTRAINT decyzja_pk PRIMARY KEY ( decyzja_id );

CREATE TABLE oceny (
    ocena_id                  INTEGER NOT NULL,
    data                      DATETIME NOT NULL,
    ocena_liczbowa            INTEGER,
    opis                      VARCHAR(1000),
    pomysl_pomysl_id          INTEGER NOT NULL,
    uzytkownik_uzytkownik_id  INTEGER NOT NULL
)
;

ALTER TABLE oceny ADD CONSTRAINT ocena_pk PRIMARY KEY ( ocena_id );

CREATE TABLE pomysly (
    pomysl_id                           INTEGER NOT NULL,
    tematyka                            VARCHAR(200) NOT NULL,
    opis                                VARCHAR(2000) NOT NULL,
    data_dodania                        DATETIME NOT NULL,
    data_ostatniej_edycji               DATETIME,
    planowane_korzysci                  VARCHAR(1000),
    planowane_koszty                    TINYINT,
    ocena_wazona                        DOUBLE, 
-- SQLINES DEMO *** me length exceeds maximum allowed length(30) 
    ustawienia_oceniania_ustawienia_id  INTEGER NOT NULL,
    status_pomyslu_status               VARCHAR(50) NOT NULL,
    uzytkownik_uzytkownik_id            INTEGER NOT NULL
)
;

ALTER TABLE pomysly ADD CONSTRAINT pomysl_pk PRIMARY KEY ( pomysl_id );

CREATE TABLE posty (
    post_id                   INTEGER NOT NULL,
    tytul                     VARCHAR(200) NOT NULL,
    tresc                     VARCHAR(1000) NOT NULL,
    watek_watek_id            INTEGER NOT NULL,
    uzytkownik_uzytkownik_id  INTEGER NOT NULL,
    data_dodania              DATETIME NOT NULL
)
;

ALTER TABLE posty ADD CONSTRAINT post_pk PRIMARY KEY ( post_id );

CREATE TABLE rodzaje_decyzji (
    rodzaj_decyzji_id VARCHAR(100) NOT NULL
)
;

ALTER TABLE rodzaje_decyzji ADD CONSTRAINT rodzaj_decyzji_pk PRIMARY KEY ( rodzaj_decyzji_id );

CREATE TABLE slowa_kluczowe (
    slowo_kluczowe_id  VARCHAR(50) NOT NULL,
    pomysl_pomysl_id   INTEGER NOT NULL
)
;

ALTER TABLE slowa_kluczowe ADD CONSTRAINT slowo_kluczowe_pk PRIMARY KEY ( slowo_kluczowe_id );

CREATE TABLE statusy_pomyslow (
    status VARCHAR(50) NOT NULL
)
;

ALTER TABLE statusy_pomyslow ADD CONSTRAINT status_pomyslu_pk PRIMARY KEY ( status );

CREATE TABLE ustawienia_oceniania (
    ustawienia_id  INTEGER NOT NULL,
    klucz          VARCHAR(100) NOT NULL,
    wartosc        CHAR(1) NOT NULL,
    opis           VARCHAR(200)
)
;

ALTER TABLE ustawienia_oceniania ADD CONSTRAINT ustawienia_oceniania_pk PRIMARY KEY ( ustawienia_id );

CREATE TABLE uzytkownicy (
    uzytkownik_id  INTEGER NOT NULL,
    imie           VARCHAR(100) NOT NULL,
    nazwisko       VARCHAR(100) NOT NULL,
    sso            VARCHAR(50) NOT NULL
)
;

ALTER TABLE uzytkownicy ADD CONSTRAINT uzytkownik_pk PRIMARY KEY ( uzytkownik_id );

CREATE TABLE watki (
    watek_id      INTEGER NOT NULL,
    temat         VARCHAR(200) NOT NULL,
    data_dodania  DATETIME
)
;

ALTER TABLE watki ADD CONSTRAINT watek_pk PRIMARY KEY ( watek_id );

CREATE TABLE zalaczniki (
    zalacznik_id  INTEGER NOT NULL,
    nazwa_pliku   VARCHAR(200) NOT NULL,
    data_dodania  DATETIME NOT NULL,
    rozmiar       INTEGER
)
;

ALTER TABLE zalaczniki ADD CONSTRAINT zalacznik_pk PRIMARY KEY ( zalacznik_id );

CREATE TABLE zalaczniki_pomyslow (
    zalacznik_id      INTEGER NOT NULL,
    pomysl_pomysl_id  INTEGER NOT NULL
)
;

ALTER TABLE zalaczniki_pomyslow ADD CONSTRAINT zalacznik_pomysłu_pk PRIMARY KEY ( zalacznik_id );

CREATE TABLE zalaczniki_postow (
    zalacznik_id  INTEGER NOT NULL,
    post_post_id  INTEGER NOT NULL
)
;

ALTER TABLE zalaczniki_postow ADD CONSTRAINT zalacznik_posta_pk PRIMARY KEY ( zalacznik_id );

CREATE TABLE zwykli_uzytkownicy (
    uzytkownik_id INTEGER NOT NULL
)
;

ALTER TABLE zwykli_uzytkownicy ADD CONSTRAINT zwykly_uzytkownik_pk PRIMARY KEY ( uzytkownik_id );

ALTER TABLE administratorzy
    ADD CONSTRAINT administrator_uzytkownik_fk FOREIGN KEY ( uzytkownik_id )
        REFERENCES uzytkownicy ( uzytkownik_id )
            ON DELETE CASCADE
    NOT DEFERRABLE;

ALTER TABLE czlonkowie_komisji
    ADD CONSTRAINT czlonek_komisji_uzytkownik_fk FOREIGN KEY ( uzytkownik_id )
        REFERENCES uzytkownicy ( uzytkownik_id )
            ON DELETE CASCADE
    NOT DEFERRABLE;

ALTER TABLE decyzje
    ADD CONSTRAINT decyzja_czlonek_komisji_fk FOREIGN KEY ( czlonek_komisji_uzytkownik_id )
        REFERENCES czlonkowie_komisji ( uzytkownik_id )
    NOT DEFERRABLE;

ALTER TABLE decyzje
    ADD CONSTRAINT decyzja_pomysl_fk FOREIGN KEY ( pomysl_pomysl_id )
        REFERENCES pomysly ( pomysl_id )
    NOT DEFERRABLE;

ALTER TABLE decyzje
    ADD CONSTRAINT decyzja_rodzaj_decyzji_fk FOREIGN KEY ( rodzaj_decyzji_rodzaj_decyzji_id )
        REFERENCES rodzaje_decyzji ( rodzaj_decyzji_id )
    NOT DEFERRABLE;

ALTER TABLE oceny
    ADD CONSTRAINT ocena_pomysl_fk FOREIGN KEY ( pomysl_pomysl_id )
        REFERENCES pomysly ( pomysl_id )
            ON DELETE CASCADE
    NOT DEFERRABLE;

ALTER TABLE oceny
    ADD CONSTRAINT ocena_uzytkownik_fk FOREIGN KEY ( uzytkownik_uzytkownik_id )
        REFERENCES uzytkownicy ( uzytkownik_id )
    NOT DEFERRABLE;

ALTER TABLE pomysly
    ADD CONSTRAINT pomysl_status_pomyslu_fk FOREIGN KEY ( status_pomyslu_status )
        REFERENCES statusy_pomyslow ( status )
    NOT DEFERRABLE;

ALTER TABLE pomysly
    ADD CONSTRAINT pomysl_ustawienia_oceniania_fk FOREIGN KEY ( ustawienia_oceniania_ustawienia_id )
        REFERENCES ustawienia_oceniania ( ustawienia_id )
    NOT DEFERRABLE;

ALTER TABLE pomysly
    ADD CONSTRAINT pomysl_uzytkownik_fk FOREIGN KEY ( uzytkownik_uzytkownik_id )
        REFERENCES uzytkownicy ( uzytkownik_id )
    NOT DEFERRABLE;

ALTER TABLE posty
    ADD CONSTRAINT post_uzytkownik_fk FOREIGN KEY ( uzytkownik_uzytkownik_id )
        REFERENCES uzytkownicy ( uzytkownik_id )
    NOT DEFERRABLE;

ALTER TABLE posty
    ADD CONSTRAINT post_watek_fk FOREIGN KEY ( watek_watek_id )
        REFERENCES watki ( watek_id )
            ON DELETE CASCADE
    NOT DEFERRABLE;

ALTER TABLE slowa_kluczowe
    ADD CONSTRAINT slowo_kluczowe_pomysl_fk FOREIGN KEY ( pomysl_pomysl_id )
        REFERENCES pomysly ( pomysl_id )
    NOT DEFERRABLE;

ALTER TABLE zalaczniki_pomyslow
    ADD CONSTRAINT zalacznik_pomysłu_pomysl_fk FOREIGN KEY ( pomysl_pomysl_id )
        REFERENCES pomysly ( pomysl_id )
    NOT DEFERRABLE;

ALTER TABLE zalaczniki_pomyslow
    ADD CONSTRAINT zalacznik_pomysłu_zalacznik_fk FOREIGN KEY ( zalacznik_id )
        REFERENCES zalaczniki ( zalacznik_id )
            ON DELETE CASCADE
    NOT DEFERRABLE;

ALTER TABLE zalaczniki_postow
    ADD CONSTRAINT zalacznik_posta_post_fk FOREIGN KEY ( post_post_id )
        REFERENCES posty ( post_id )
    NOT DEFERRABLE;

ALTER TABLE zalaczniki_postow
    ADD CONSTRAINT zalacznik_posta_zalacznik_fk FOREIGN KEY ( zalacznik_id )
        REFERENCES zalaczniki ( zalacznik_id )
            ON DELETE CASCADE
    NOT DEFERRABLE;

-- SQLINES DEMO *** ength exceeds maximum allowed length(30) 
ALTER TABLE zwykli_uzytkownicy
    ADD CONSTRAINT zwykly_uzytkownik_uzytkownik_fk FOREIGN KEY ( uzytkownik_id )
        REFERENCES uzytkownicy ( uzytkownik_id )
            ON DELETE CASCADE
    NOT DEFERRABLE;

-- SQLINES DEMO *** minator Value found for FK Administrator_Uzytkownik_FK - constraint trigger for Arc FKArc_1 cannot be generated 

-- SQLINES DEMO *** minator Value found for FK Zwykly_uzytkownik_Uzytkownik_FK - constraint trigger for Arc FKArc_1 cannot be generated 

-- SQLINES DEMO *** minator Value found for FK Czlonek_komisji_Uzytkownik_FK - constraint trigger for Arc FKArc_1 cannot be generated

-- SQLINES DEMO *** minator Column found in Arc FKArc_2 - constraint trigger for Arc cannot be generated 

-- SQLINES DEMO *** minator Column found in Arc FKArc_2 - constraint trigger for Arc cannot be generated



-- SQLINES DEMO *** per Data Modeler Summary Report: 
-- 
-- SQLINES DEMO ***                        16
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***                        34
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO *** DY                      0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***  TYPE                   0
-- SQLINES DEMO ***  TYPE                   0
-- SQLINES DEMO ***  TYPE BODY              0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO *** EGMENT                  0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO *** ED VIEW                 0
-- SQLINES DEMO *** ED VIEW LOG             0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***                         0
-- 
-- SQLINES DEMO ***                         0
-- SQLINES DEMO ***                         0
-- 
-- SQLINES DEMO ***                         0
-- 
-- SQLINES DEMO ***                         0
-- SQLINES DEMO *** A                       0
-- SQLINES DEMO *** T                       0
-- 
-- SQLINES DEMO ***                         8
-- SQLINES DEMO ***                         0
