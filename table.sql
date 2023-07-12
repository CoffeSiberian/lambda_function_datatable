CREATE TABLE datos (
    rut CHAR(40) NOT NULL UNIQUE PRIMARY KEY,
    nombre CHAR(50) NOT NULL,
    apellido CHAR(50) NOT NULL,
    celular INTEGER(10) NOT NULL,
    eva3 FLOAT(10,2)
);