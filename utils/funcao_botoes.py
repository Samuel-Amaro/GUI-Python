from tkinter import *
from Model_Dados import ModelBeneficiario
from Dao import dao_Beneficiario

"""
 # CLASSE QUE FICA RESPONSAVEL POR FAZER AÇÕES DO BOTÃO;
   - CADA METODO PERTENCE A UM BOTÃO;
   - CADA METODO EXECECUTA UMA TAREFA DE UM BOTÃO;
   - CADA METODO ESTÁ ASSOCIADO A UM BOTÃO, LIGANDO ENTRE ELES UM EVENTO;
"""
class functionBtn():

    def __init__(self):
        self.beneficiario = ModelBeneficiario.ModeloBeneficiario();
        self.daoBen = dao_Beneficiario.daoBeneficiarioCrud();
        self.listaBeneficiarios = None;
        super().__init__()
     
    """
          # FUNÇÃO QUE LIMPA OS CAMPOS DE ENTRADA DE TEXTO DO USUARIO;
           - LIMPA TODAS AS INFORMAÇÕES DO USUARIO;
           - TODAS INFORMAÇÕES DIGITADAS EM CAIXA DE TEXTO, OU ESCOLHIDAS NO WIDGET, VÃO SER LIMPADAS E FICAR EM BRANCO;
           - VAI LIMPAR O FORMULARIO;
           - LIMPAR TODAS OS INPUT DO USUARIO
    """
    def limparCampos(self):
          self.txtCodigo.delete(0,END);
          self.txtNome.delete(0,END);
          self.txtTelefone.delete(0,END);
          self.txtCpf.delete(0,END);
          self.txtEndereco.delete(0,END);
          self.txtLocal.set("ESCOLHA UM LOCAL")
          self.txtAbrangencia.set("ESCOLHA A ABRANGÊNCIA")
          #self.txtQtdCasa.set(1);
    
    """
      # FUNÇÃO QUE RECEBE DADOS DO FORMULARIO E FAZ CADASTRO DO BENEFICIARIO NO BANCO; 
        - recebe dados das caixas de texto que o usuario digitou;
        - recebe dados dos widgets graficos que o usuario manipulou;
    """
    def cadastrarBeneficiario(self):
         self.beneficiario = ModelBeneficiario.ModeloBeneficiario();
         self.daoBen = dao_Beneficiario.daoBeneficiarioCrud();
        # obtem dados do usuario e armazenado num objeto do tipo beneficiario
         self.beneficiario.setId(self.txtCodigo.get()) #id
         self.beneficiario.setNome(self.txtNome.get()) # nome
         self.beneficiario.setFone(self.txtTelefone.get()) # telefone
         self.beneficiario.setCpf(self.txtCpf.get()) # cpf
         self.beneficiario.setEndereco(self.txtEndereco.get()) # endereço
         self.beneficiario.setBairro(self.txtLocal.get()) # bairro/local
         self.beneficiario.setAbrangencia(self.txtAbrangencia.get()) # abrangencia
         self.beneficiario.setQtdCasa(int(self.txtQtdCasa.get())) # qtd reside casa 
         self.beneficiario.setRg("");
         # mandando para o banco de dados
         resultado = self.daoBen.insertBeneficiario(self.beneficiario)
         if(resultado):
            print("Usuario inserido com sucesso")
         else:
             print("Usuario não inserido")
    
    """
     # METODO QUE MOSTRA CLIENTES QUE ESTÃO CADASTRADOS NA TABELA DE BENEFICIARIOS DO BANCO DE DADOS
    """
    def beneficiariosCadastrados(self):
        self.tViewCli.delete(*self.tViewCli.get_children())
        self.daoBen = dao_Beneficiario.daoBeneficiarioCrud()
        self.listaBeneficiarios = self.daoBen.selectBeneficiarios()
        for linha in self.listaBeneficiarios:
            self.tViewCli.insert("",END,values=linha)