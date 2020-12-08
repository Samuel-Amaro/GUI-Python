from sqlite3 import *
from sqlite3 import Error
"""
 # ESSA CLASSE FAZ CONEXÃO COM O BANCO DE DADOS;
   - FAZ CONEXÃO COM O BANCO DE DADOS SQLIT3;
   - PERMITINDO USAR TABELAS E CAMPOS DO BANCO DE DADOS;
"""
class conexaoBancoDados():
    # costrutor inicializador
    def __init__(self):
        self.conexao = None
        self.cursoSql = None
        super().__init__()
    """
     # METODODO QUE SE CONECTA AO BANCO DE DADOS;
    """
    def conectarBanco(self):
        try:
             # SE CONECTA AO BANCO
             self.conexao = connect('db_secretaria_social.db')
             self.cursoSql = self.conexao.cursor()
             print("---------------------------")
             print("Banco conectado com Sucesso")
             print("---------------------------")
             return self.conexao;
        except Error as e:
            print("Ocorreu um erro ao se conectar ao banco de dados" + e)
    """
     # METODO QUE SE DESCONECTA DO BANCO DE DADOS
    """
    def desconectarBanco(self):
        # fecha o banco de dados e faz desconexão
        self.conexao.close()
        print("----------------------------------")
        print("BANCO DE DADOS DESCONECTADO")
        print("----------------------------------")
    """
     # METODO QUE MONTA A  ESTRUTURA DO BANCO DE DADOS;
       - CRIA OS DDL DO BANCO DE DADOS;
       - CRIA TABELA BENEFICIARIO
    """
    def ddlBanco(self):
        self.conectarBanco();
        #self.cursoSql.execute("""DROP TABLE beneficiario_social;""")
        #print("Apagou tabela")
        self.cursoSql.execute("""CREATE TABLE IF NOT EXISTS beneficiario_social(
                                  id_beneficiario_pk INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                  telefone VARCHAR(15) NOT NULL,
                                  cpf VARCHAR(11) UNIQUE NOT NULL,
                                  nis VARCHAR (25),
                                  endereco VARCHAR(200) NOT NULL,
                                  bairro VARCHAR (150) NOT NULL,
                                  abrangencia VARCHAR (50)  NOT NULL,
                                  qtd_pessoas_mora_casa INTEGER NOT NULL,
                                  rg VARCHAR (10),
                                  nome VARCHAR (250) NOT NULL); 
        """);
        self.cursoSql.execute("""CREATE TABLE IF NOT EXISTS secretaria_social(
                                     id_secretaria_pk INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                     data_hora DATETIME NOT NULL,
                                     tipo_beneficio VARCHAR (200) NOT NULL,
                                     descricao_beneficio TEXT NOT NULL,
                                     scfv_solicitado VARCHAR (100),
                                     servidor_responsavel VARCHAR (50) NOT NULL);
        """)
        self.cursoSql.execute("""CREATE TABLE IF NOT EXISTS beneficiario_recebe_secretaria (
                                    id_beneficiario INTEGER REFERENCES beneficiario (id_beneficiario_pk) NOT NULL,
                                    id_secretaria   INTEGER REFERENCES secretaria_social (id_secretaria_pk) NOT NULL); 
        """)
        self.conexao.commit()
        self.desconectarBanco()
        print("-------------------")
        print("DDL DO BANCO CRIADO")
        print("-------------------")

    