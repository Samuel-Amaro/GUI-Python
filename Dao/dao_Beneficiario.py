from Banco_Dados import conexaoBanco
from Banco_Dados.conexaoBanco import *
import Banco_Dados
from Model_Dados import ModelBeneficiario


"""
 # ESSA CLASSE FICA RESPONSAVEL POR EXECUTAR OS COMANDOS SQL, RELACIONADO AO BENEFICIARIO;
   - OS DML,DQL,ETC....
"""
class daoBeneficiarioCrud():
    def __init__(self):
        self.objConexao = conexaoBanco.conexaoBancoDados()
        self.conexaoDb = self.objConexao.conectarBanco()
        self.resultadoSql = None;
        super().__init__()
    
    """
     # METODO QUE CADASTRA(INSERI UM BENEFICIARIO NA TABELA DO BANCO DE DADOS);
       - FAZ UM INSERT NA TABELA BENEFICIARIO;
    """
    def insertBeneficiario(self, novoBeneficiario : ModelBeneficiario):
        # se objeto for vazio(null)
        if(novoBeneficiario is None):
           print("Não se pode inserir um beneficiario Vazio");
           return False;
        else:
                if(novoBeneficiario.getNis is None and novoBeneficiario.getRg is None):        
                        print("campos nulos")
                        return False;
                else:
                        try:
                            self.cursorSql = self.conexaoDb.cursor()
                            self.cursorSql.execute("""INSERT INTO beneficiario_social(telefone,cpf,nis,endereco,bairro,abrangencia,qtd_pessoas_mora_casa,rg,nome)  VALUES(?,?,?,?,?,?,?,?,?)""",(novoBeneficiario.getFone,novoBeneficiario.getCpf,novoBeneficiario.getNis,novoBeneficiario.getEndereco,novoBeneficiario.getBairro,novoBeneficiario.getAbrangencia,novoBeneficiario.getQtdCasa,novoBeneficiario.getRg,novoBeneficiario.getNome))
                            self.conexaoDb.commit()
                            self.objConexao.desconectarBanco()
                            return True;
                        except Error as identifier:
                            print("OCORREU UM ERRO AO INSERIR BENEFICIARIO NO BANCO DE DADOS "  + Error)
                            return False;
    """
     # METODO QUE BUSCA TODOS OS BENEFICIARIOS CADASTRADOS NA TABELA BENEFICIARIO DO BANCO DE DADOS;
    """
    def selectBeneficiarios(self):
        try:
            self.cursorSql = self.conexaoDb.cursor()
            self.cursorSql.execute("SELECT * FROM beneficiario_social ORDER BY nome ASC;")
            self.resultadoSql = self.cursorSql.fetchall()
            self.objConexao.desconectarBanco()
            return self.resultadoSql
        except Error as identifier:
            print("OCORREU UM ERRO AO BUSCAR BENEFICIARIOS CADASTRADOS");
                