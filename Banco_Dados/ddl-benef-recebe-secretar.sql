CREATE TABLE beneficiario_recebe_secretaria (
    id_beneficiario INTEGER REFERENCES beneficiario (id_beneficiario_pk) 
                            NOT NULL,
    id_secretaria   INTEGER REFERENCES secretaria_social (id_secretaria_pk) 
                            NOT NULL
);
