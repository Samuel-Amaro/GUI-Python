from Banco_Dados import conexaoBanco
from Banco_Dados.conexaoBanco import *
import Banco_Dados
from Model_Dados import ModelBeneficiario
from Controller import controler_Beneficiario
from sqlite3 import IntegrityError,OperationalError,ProgrammingError

"""
 # ESSA CLASSE FICA RESPONSAVEL POR EXECUTAR OS COMANDOS SQL, RELACIONADO AO BENEFICIARIO;
   - OS DML,DQL,ETC....
"""
class daoBeneficiarioCrud():
    def __init__(self):
        self.objConexao = conexaoBanco.conexaoBancoDados()
        self.conexaoDb = self.objConexao.conectarBanco()
        self.resultadoSql = None;
        self.controleBene = controler_Beneficiario.ControleBeneficiario()
        super().__init__()
    
    """
     # METODO QUE CADASTRA(INSERI UM BENEFICIARIO NA TABELA DO BANCO DE DADOS);
       - FAZ UM INSERT NA TABELA BENEFICIARIO;
    """
    def insertBeneficiario(self, novoBeneficiario : ModelBeneficiario.ModeloBeneficiario):
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
                            if(self.controleBene.controlerSetInsertBeneficiario(novoBeneficiario)):
                                self.cursorSql = self.conexaoDb.cursor()
                                self.cursorSql.execute("""INSERT INTO beneficiario_social(telefone,cpf,nis,endereco,bairro,abrangencia,qtd_pessoas_mora_casa,rg,nome)  VALUES(?,?,?,?,?,?,?,?,?)""",(novoBeneficiario.getFone,novoBeneficiario.getCpf,novoBeneficiario.getNis,novoBeneficiario.getEndereco,novoBeneficiario.getBairro,novoBeneficiario.getAbrangencia,novoBeneficiario.getQtdCasa,novoBeneficiario.getRg,novoBeneficiario.getNome))
                                self.conexaoDb.commit()
                                self.objConexao.desconectarBanco()
                                return True;
                            else:
                                return False;
                        except IntegrityError as identifier:
                            print("Usuario existente no banco de dados, não se pode add, que ja esta cadastrado: {%s}" % (identifier))
                            self.objConexao.desconectarBanco()
                            return False;
    """
     # METODO QUE BUSCA TODOS OS BENEFICIARIOS CADASTRADOS NA TABELA BENEFICIARIO DO BANCO DE DADOS;
       - retorna uma tupla com todos os registros de beneficiarios cadastrados;
       - retorna uma lista com os registros dos beneficiarios cadastrados
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
            self.objConexao.desconectarBanco()    
    
    
    """
     # ESTE METODO ATUALIZA UM CADASTRO EXISTENTE DE UM BENEFICIARIO
      - recebe um obejto beneficiario com informações existentes, e faz atualização;
    """
    def daoAtualizarCadBeneficiario(self,modelCadastroBen : ModelBeneficiario.ModeloBeneficiario):
        if(modelCadastroBen == None):
           print("----------------------------------------")
           print("Não pode Atualizar um beneficiario vazio");
           return False;
        else:
            if(self.controleBene.controlerSetInsertBeneficiario(modelCadastroBen)):
                try:
                    self.cursorSql = self.conexaoDb.cursor()
                    self.cursorSql.execute("""UPDATE beneficiario_social SET telefone = ?,nis = ?,endereco = ?,bairro = ?,abrangencia = ?,qtd_pessoas_mora_casa = ?,rg = ?,nome = ? WHERE id_beneficiario_pk = ?;""",(modelCadastroBen.getFone,modelCadastroBen.getNis,modelCadastroBen.getEndereco,modelCadastroBen.getBairro,modelCadastroBen.getAbrangencia,
                    modelCadastroBen.getQtdCasa,modelCadastroBen.getRg,modelCadastroBen.getNome,modelCadastroBen.getId))
                    self.conexaoDb.commit()
                    self.objConexao.desconectarBanco()
                    return True;
                except OperationalError as identifier:
                    print("------------------------------------------------")
                    print("Ocorreu um erro inesperado ao fazer atualização!: {%s}" % (identifier))
                    print("------------------------------------------------")
                    self.objConexao.desconectarBanco()
                    return False;
                except ProgrammingError as identifier:
                    print("------------------------------------------------")
                    print("Ocorreu um erro inesperado ao fazer atualização!: {%s}" % (identifier))
                    print("------------------------------------------------")
                    self.objConexao.desconectarBanco()
                    return False;
            else:
                print("---------------------------------------")
                print("ATUALIZAÇÃO DE CADASTRO NÃO AUTORIZADA! campos obrigatorios vazios!")
                print("----------------------------------------")
                return False;
    

    """
     # ESTE METODO TEM A TAREFA DE EXCLUIR UM BENEFICIARIO
    """
    def daoDeleteBeneficiario(self,beneficExcluido : ModelBeneficiario.ModeloBeneficiario,respostaUsuario):
        if(beneficExcluido == None):
           print("----------------------------------------")
           print("SELECIONAR UM BENEFICIARIO PARA SER EXCLUIDO");
           print("-" * 30)
           return False;
        else:
            if(self.controleBene.controlerDeleteBeneficiario(respostaUsuario)):
                 try:
                     self.cursorSql = self.conexaoDb.cursor()
                     self.cursorSql.execute("""DELETE FROM beneficiario_social WHERE id_beneficiario_pk = ?;""",(beneficExcluido.getId));
                     self.conexaoDb.commit()
                     self.objConexao.desconectarBanco()
                     return True;
                 except Error as r:
                    print("-"*30)
                    print("OCORREU UM ERRO AO DELETAR BENEFICIARIO: {%s}" % (r))
                    return False;
            else:
                print("-"*30)
                print("Usuario não excluido")
                print("-"*30)

    
    """
     # ESTE METODO FAZ A BUSCA DE UM BENEFICIARIO NO BANCO DE DADOS;
       - A BUSCA TEM COMO REQUISITO O NOME DO BENEFICIARIO, PODE SER NOME COMPLETO,
       PRIMERIO NOME, OU SO AS LETRAS INICIAIS;
       - A BUSCA VAI SER EFETUADA USANDO OPERADORES DE TEXT DO BANCO DE DADOS, ILIKE E %,
       PARA QUE VENHA TODOS OS CADASTRADOS QUE SEJA REALMENTE DO NOME INFORMADO, OU PARECIDO;
    """
    def daoBuscaBenef(self,textSearch):
        try:
            self.cursorSql = self.conexaoDb.cursor();
            self.cursorSql.execute("""SELECT * FROM beneficiario_social WHERE nome LIKE '%s%%' 
            """ % (textSearch))
            self.resultadoSql = self.cursorSql.fetchall()
            self.objConexao.desconectarBanco()
            return self.resultadoSql;
        except ValueError as identifier:
            print("-"*30)
            print("OCORREU UM ERRO AO BUSCA BENEFICIARIO {%s}" % (identifier))
            print("-"*30)
            return None;
        except OperationalError as e:
            print("-"*30)
            print("OCORREU UM ERRO AO BUSCA BENEFICIARIO {%s}" % (e))
            print("-"*30)
            return None;
