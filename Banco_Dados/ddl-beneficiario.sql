CREATE TABLE beneficiario (
    id_beneficiario_pk    INTEGER       PRIMARY KEY AUTOINCREMENT
                                        NOT NULL,
    telefone              VARCHAR (15)  NOT NULL,
    cpf                   VARCHAR (11)  NOT NULL,
    nis                   VARCHAR (25),
    endereco              VARCHAR (200) NOT NULL,
    bairro                VARCHAR (150) NOT NULL,
    abrangencia           VARCHAR (50)  NOT NULL
                                        CHECK ('ZONA URBANA' OR 
                                               'ZONA RURAL'),
    qtd_pessoas_mora_casa INTEGER       NOT NULL,
    rg                    VARCHAR (10),
    nome                  VARCHAR (250) NOT NULL
);