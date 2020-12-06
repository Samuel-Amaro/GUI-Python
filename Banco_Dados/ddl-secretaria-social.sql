CREATE TABLE secretaria_social (
    id_secretaria_pk     INTEGER       PRIMARY KEY AUTOINCREMENT
                                       NOT NULL,
    data_hora            DATETIME      NOT NULL,
    tipo_beneficio       VARCHAR (200) NOT NULL,
    descricao_beneficio  TEXT          NOT NULL,
    scfv_solicitado      VARCHAR (100),
    servidor_responsavel VARCHAR (50)  NOT NULL
);