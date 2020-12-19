from tkinter import *
from tkinter import messagebox
from Model_Dados import ModelBeneficiario
from Dao import dao_Beneficiario
from Controller import controler_Beneficiario

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
        self.beneficiarioSelecionado = ();
        self.beneficiarioAlterar = ();
        self.controlaBeneficiario = controler_Beneficiario.ControleBeneficiario()
        super().__init__()
     
    """
          # FUNÇÃO QUE LIMPA OS CAMPOS DE ENTRADA DE TEXTO DO USUARIO;
           - LIMPA TODAS AS INFORMAÇÕES DO USUARIO;
           - TODAS INFORMAÇÕES DIGITADAS EM CAIXA DE TEXTO, OU ESCOLHIDAS NO WIDGET, VÃO SER LIMPADAS E FICAR EM BRANCO;
           - VAI LIMPAR O FORMULARIO;
           - LIMPAR TODAS OS INPUT DO USUARIO
    """
    def limparCampos(self):
          self.estadoCaixasTexto("ATIVADO")
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
        - esses dados são add em um obejto de tipo beneficiario, e esses objeto e mandado para a camada de controle, para fazer as validações e persistencias antes de enviar para o banco de dados
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
            print("----------------------------")
            print("Beneficiario Cadastrado com sucesso")
            print("----------------------------")
            messagebox.showinfo("CADASTRO EFETUADO","CADASTRO FEITO COM SUCESSO, Clique no Botão Atualizar!")
            self.limparCampos()
         else:
             print("----------------------------")
             print("Beneficiario Não cadastrado")
             print("----------------------------")
             messagebox.showwarning("CADASTRO NÃO EFETUADO","PREENCHA OS CAMPOS OBRIGATORIOS!")
             self.limparCampos()
    
    """
     # METODO QUE MOSTRA CLIENTES QUE ESTÃO CADASTRADOS NA TABELA DE BENEFICIARIOS DO BANCO DE DADOS
      - faz a busca no banco de dados de todos os clientes cadastrados;
      - retorna a lista com todos os clientes cadastrados na tabela;
      - cada item dessa lista e add, na tree view da interface do usuario, para o usuario ver todos os beneficiarios cadastrados no banco de dados;
    """
    def beneficiariosCadastrados(self):
        self.tViewCli.delete(*self.tViewCli.get_children())
        self.daoBen = dao_Beneficiario.daoBeneficiarioCrud()
        self.listaBeneficiarios = self.daoBen.selectBeneficiarios()
        if(self.listaBeneficiarios == None):
           print("-------------------------------------------")
           print("Lista Vazia, sem beneficiarios cadastrados;")
           print("-------------------------------------------")
        else:
            for linha in self.listaBeneficiarios:
                self.tViewCli.insert("",END,values=linha)
    """
     # ESTE METODO VAI OBTER UM REGISTRO SELECIONADO DA TREE VIEW
       - este metodo busca os valores de um item selecionado na treee view;
       - obtem os valores do registro, e retorna esses valore em um obejto de tipo beneficirio;
       - busca o registro, obtem os valores, e retorna um obejto setado com os valores;
    """
    def obterItemSelecionadoTreeView(self):
      try:
        # obtem o item selecionado da tree view
           self.beneficiarioSelecionado = self.tViewCli.selection();
           #print(self.beneficiarioSelecionado)
           self.beneficiario = ModelBeneficiario.ModeloBeneficiario()
           # obtem os valores do registro selecionado da tree view, retorna um tupla com todos os valores
           self.beneficiarioAlterar = self.tViewCli.item(self.beneficiarioSelecionado,"values")
           # criando um obejto beneficiario, com novos valores, esses valores são do registro selecionado pelo usuario da tree view
           # acesso cada valor do registro usando a indexação da tupla, e setando esses valores na tree view
           self.beneficiario.setId(self.beneficiarioAlterar[0]); #id
           self.beneficiario.setFone(self.beneficiarioAlterar[1]); #telefone
           self.beneficiario.setCpf(self.beneficiarioAlterar[2]) # cpf
           self.beneficiario.setNis(self.beneficiarioAlterar[3]) # nis
           self.beneficiario.setEndereco(self.beneficiarioAlterar[4]) # endereço
           self.beneficiario.setBairro(self.beneficiarioAlterar[5]) # local
           self.beneficiario.setAbrangencia(self.beneficiarioAlterar[6]) # abrangencia
           self.beneficiario.setQtdCasa(self.beneficiarioAlterar[7]) # moradores casa
           self.beneficiario.setRg(self.beneficiarioAlterar[8]) # rg
           self.beneficiario.setNome(self.beneficiarioAlterar[9]) # nome   
           print(self.beneficiario)
           return self.beneficiario;
      except IndexError as identifier:
              print("-" * 30)
              print("SELECIONE UM BENEFICIARIO")
              return None;
           
    
    """ 
     # este metodo e chamado quando um clique em um item da tree view acontece;
       - quando um evento de clique em um item da tree view acontece, esse metodo e chamado;
       - esse metodo vai setar nas caixas de texto, o item selecionado;
       - vai mostrar nas caixas os valores selecionados;
       - o registro selecionado na tree view, vai ter seus valores mostrados nas caixas de texto, atraves, desse metodo, esse metodo vai pegar o item selecionado da tree view, e popular as caixas de texto da view, com os valores do registro selecionado;
       - esse metodo esta associado a um evento, ao evento ser executado, a resposta do evento, sera esse metodo, por isso tem um parametro event, porque o metodo e uma respota a um evento; no caso o evento tem que ser um duplo clique do mouse do botão esquer(<Double-1>)       
    """
    def cliqueSelecionaTreeView(self,event):
        self.beneficiario = ModelBeneficiario.ModeloBeneficiario()
        self.beneficiario = self.obterItemSelecionadoTreeView()
        if(self.beneficiario == None):
          print("Obejto Vazio, não tem como popular a caixa de texto");
        else:
            self.vTxtCodigo.set(self.beneficiario.getId)
            self.vTxtNome.set(self.beneficiario.getNome)
            self.vTxtCpf.set(self.beneficiario.getCpf)
            self.vTxtLocal.set(self.beneficiario.getBairro)
            self.vTxtAbrangencia.set(self.beneficiario.getAbrangencia)
            self.vTxtTelefone.set(self.beneficiario.getFone)
            self.vTxtQtdCasa.set(self.beneficiario.getQtdCasa)
            self.vTxtEndereco.set(self.beneficiario.getEndereco)
            # CAIXA DE TEXTO ID E CPF, NÃO PODEM TER SEU CONTEUDO ALTERADO
            self.estadoCaixasTexto('DESATIVADO')       
    
    """
       # METODO QUE CONGIGURA O ESTADO DE UMA CAIXA DE TEXTO;
         - de acordo com o estado pedido, a caixa vai ser desativada, sem poder editar o conteudo, e sem poder copiar o texto;
         - depois a caixa pode ser ativada e fazer tudo que se pode fazer normalmente;
    """
    def estadoCaixasTexto(self,estado = "ATIVADO" or "DESATIVADO"):
         if(estado == "ATIVADO"):
            self.txtCodigo.configure(state=NORMAL)
            self.txtCpf.configure(state=NORMAL)
         else:  
            self.txtCodigo.configure(state=DISABLED)
            self.txtCpf.configure(state=DISABLED)

    """
     # METODO QUE VAI ATUALIZAR UM CADASTRO DE UM BENEFICIARIO
       - recebe os dados do cadastro, faz validação do cadastro e manda para o banco de dados;
       - obtem os dados da caixa de texto, usando o controle de variaveis de fluxo, das caixas de texto;
       - esses dados obtidos das caixas de texto, são armazenados num novo obejto beneficiario, para ser encaminhado para a camada dao, do banco de dados para ver se vai poder atualizar o cadastro do beneficiario ou não;
    """
    def atualizarCadBenf(self):
        self.beneficiario = ModelBeneficiario.ModeloBeneficiario();
        self.daoBen = dao_Beneficiario.daoBeneficiarioCrud();
        #algum campo vazio
        try:
            self.beneficiario.setNome(self.vTxtNome.get())
            self.beneficiario.setBairro(self.vTxtLocal.get())
            self.beneficiario.setAbrangencia(self.vTxtAbrangencia.get())
            self.beneficiario.setEndereco(self.vTxtEndereco.get())
            self.beneficiario.setFone(self.vTxtTelefone.get())
            self.beneficiario.setNis(None)
            self.beneficiario.setRg(None)
            self.beneficiario.setId(self.vTxtCodigo.get())
            self.beneficiario.setCpf(self.vTxtCpf.get())
            self.beneficiario.setQtdCasa(self.vTxtQtdCasa.get())
            if(self.daoBen.daoAtualizarCadBeneficiario(self.beneficiario)):
                  print("--------------------------------------");
                  print("BENEFICIARIO ATUALIZADO COM SUCESSO!")
                  print("--------------------------------------");
                  messagebox.showinfo("ATUALIZAÇÃO DE CADASTRO","ATUALIZAÇÃO DE CADASTRO EFETUADA COM SUCESSO!")
                  # CAIXA DE TEXTO VOLTA SER EDITAVEL
                  self.estadoCaixasTexto("ATIVADO")
                  # LIMPA CAMPOS DO FORMULARIO
                  self.limparCampos()
            else:
                  print("--------------------------------------");
                  print("BENEFICIARIO NÃO ATUALIZADO!")
                  print("--------------------------------------");
                  messagebox.showwarning("ATUALIZAÇÃO EM PENDENCIA","PARA ATUALIZAR O CADASTRO PREENCHA OS CAMPOS DE CADASTRO OBRIGATORIOS!")  
        except TclError as identifier:
             print("-"*30)
             print("Campos obrigatorios na atualizaçaõ estão vazios")
             print("--------------------------------------");
             print("BENEFICIARIO NÃO ATUALIZADO!")
             print("--------------------------------------");
             messagebox.showwarning("ATUALIZAÇÃO EM PENDENCIA","PARA ATUALIZAR O CADASTRO PREENCHA OS CAMPOS DE CADASTRO OBRIGATORIOS!") 
        
    
    """
     # este metodo deleta um beneficiario, que foi selecionado na tree view;
    """
    def deletarBeneficiario(self,respostaUsuario):
        self.beneficiario = ModelBeneficiario.ModeloBeneficiario()
        self.beneficiario = self.obterItemSelecionadoTreeView()
        self.daoBen = dao_Beneficiario.daoBeneficiarioCrud();
        if(self.daoBen.daoDeleteBeneficiario(self.beneficiario,respostaUsuario)):
          print("-"*30)
          print("BENEFICIARIO DELETADO COM SUCESSO")
          messagebox.showinfo("BENEFICIARIO DELETADO","BENEFICIARIO SELECIONADO FOI DELETADO COM SUCESSO, ATUALIZE A LISTA, CLICANDO NO BOTÃO ATUALIZAR!")
          self.limparCampos()
          return True
        else:
          print("-"*30)
          print("BENEFICIARIO NÃO DELETADO")
          messagebox.showwarning("ATENÇÃO","ESCOLHA UM BENEFICIARIO PARA SER EXCLUIDO")
          self.limparCampos()            
          return False
    

    """
     # METODO QUE TEM A FUNÇAÕ DE ENCERRAR O SISTEMA;
    """
    def sairSistema(self):
        self.telaPrincipal.destroy()

    
    """
     # ESTE METODO BUSCA UM CADASTRO DE UM BENEFICIARIO, DE ACORDO COM O NOME INFORMADO, NA CAIXA DE TEXTO, DO NOME;
       - vou tratar esse nome e fazer a busca do beneficiario, e verificar se eles existe, e se existe, mostra ele na tree view destacada para o usuario;
    """
    def buscarBeneficiario(self):
        self.controlaBeneficiario = controler_Beneficiario.ControleBeneficiario()
        if(self.controlaBeneficiario.controlerBuscaBenefi(self.vTxtNome.get())):
           self.daoBen = dao_Beneficiario.daoBeneficiarioCrud()
           self.listaBeneficiarios = self.daoBen.daoBuscaBenef(self.vTxtNome.get());
           # não retornou nenhum beneficiario
           if(self.listaBeneficiarios == None):
              print("-------------------------------------------")
              print("Não encontrou beneficiario com esse Nome;")
              print("-------------------------------------------")
              messagebox.showerror("BUSCA BENEFICIARIO","NÃO EXISTE BENEFICIARIO {%s} CADASTRADO NO SISTEMA" % (self.vTxtNome.get()))
           else:
                # nome do beneficiario e valido mas não existe no banco
                if(self.listaBeneficiarios == []):
                   print("-"*30)
                   print("NÃO EXISTE BENEFICIARIOS COM ESSE NOME")
                   print("-"*30)
                   messagebox.showerror("BUSCA BENEFICIARIO","NÃO EXISTE BENEFICIARIO {%s} CADASTRADO NO SISTEMA" % (self.vTxtNome.get()))
                   self.limparCampos()
                else:
                    # se beneficiario existe, MOSTRA  ele na tree view
                    self.limparCampos()
                    self.tViewCli.delete(*self.tViewCli.get_children())
                    for linha in self.listaBeneficiarios:
                        self.tViewCli.insert("",END,values=linha)
                    messagebox.showinfo("BENEFICIARIO ENCONTRADO","BENEFICIARIOS ENCONTRADOS, OLHE NA LISTA ABAIXO O RESULTADO DE SUA PESQUISA!")       
        else:
          print("-"*30)
          print("DIGITE UM NOME VALIDO PARA FAZER A BUSCA")
          print("-"*30)
          messagebox.showerror("ERRO NA BUSCA","DIGITE UM NOME DE BENEFICIARIO VALIDO, PARA REALIZAR A BUSCA NO SISTEMA")


    