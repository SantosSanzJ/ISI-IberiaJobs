Create Table Trabajos(
	ID BIGINT NOT NULL,
    Posicion varchar(256),
	Sueldo INT,
    TiempoExperiencia Double,
    Jornada varchar(256),
    Idiomas varchar(256),
    Descripcion varchar(4096),
    EsEspanol boolean,
    PRIMARY KEY (ID)
);
DROP table Trabajos;
Select * FROM Trabajos;

CREATE TABLE Stats(
	Keyword varchar(256),
    FrecuenciaES INT,
    FrecuenciaUSA INT,
    PRIMARY KEY(Keyword)
);

DROP TABLE STATS;
SELECT * FROM Stats;
