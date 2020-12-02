""" 
        # como posicionar um elemento widget relativamente em relação a outro widget
        #posicão relativa do conteiner
        # relx e rely estão na faixa de 0.0 ~ 1.0 
        #  É a percentagem relativa da posição do widget para o tamanho da janela.
        # relx = para dar uma margem(um pad espaço interno entre os elementos) horizontal, da esquerda para direita
        # rely = para dar uma margen vertical(um pad um espaço interno entre os elementos), de cima para baixo
        # relwidth = define largura relativa do widget em relação a % total que quer ocupar
        # relheight = define altura relativa do widget em relação a % total que quer ocupar
        # 0.5 = 50% de largura da janela o widget sera posicionado
"""

from tkinter import ttk
from tkinter import *


"""
 # CLASSE QUE COSTROE A TELA PRINCIPAL DO PROJETO;
"""
class TelaPrincipal:
     """
      # METODO COSTRUTOR(INICIALIZADOR DA CLASSE);
       - VAI CHAMAR TODAS AS FUNÇÕES QUE COSTROEM A CLASSE, COMPONENTE POR COMPONENTE, QUE DA VIDA A CLASSE;
       - CADA METODO CHAMADO PERTENCE A UM WIDGET QUE VAI SER MOSTRADO NA TELA PRINCIPAL;
     """
     def __init__(self,nomeTela):
          self.telaPrincipal = nomeTela
          self.definirTelaInicial()
          self.conteinerFrames()
          self.botoes()
          self.labels_informativas()
          self.caixaEntradaTexto()
          self.comboBox()
          self.spinBox()
          self.estilizarBotoes()
          self.estilizarLabels()
          self.treeViewClientes()
          self.telaPrincipal.mainloop()
          super().__init__()
     """
      # DEFINE AS CONFIGURAÇÕES BASICAS DA TELA PRINCIPAL
        - TITULO;
        - TAMANHO;
        - TAMANHO MAXIMO QUE PODE ATINGIR;
        - TAMANHO MINIMO QUE PODE ALCANÇAR;
        - PERMITINDO A RESPONSIVIDADE NA TELA;
        - ADD UMA CONFIGURAÇÃO DE ESTILIZAÇÃO DE COR DE FUNDO
     """     
     def definirTelaInicial(self):
          self.telaPrincipal.title("CADASTRO CLIENTES")
          self.telaPrincipal.configure(background="#243340")
          self.telaPrincipal.geometry("700x500")
          self.telaPrincipal.resizable(True,True)
          self.telaPrincipal.maxsize(900,700)
          self.telaPrincipal.minsize(600,500)
     """
      # METODO QUE CRIA CONTEINER DE AGRUPAMENTO PARA A TELA PRINCIPAL;
       - CRIA O CONTEINER 1 COM CONFIGURAÇÕES DE POSICIONAMENTO RELATIVAS EM RELAÇÃO A JANELA, PARA TER UM RESPONSIVIDADE;
       - CRIA O CONTEINER 2 COM AS MESMAS CONFIGURAÇÕES DO CONTEINER 1, SO QUE COM POSICIONAMENTO DIFERENTE DENTRO DA TELA;
     """     
     def conteinerFrames(self):
        self.conteinerTop = Frame(self.telaPrincipal,bd=4,background="#BAD0D9",highlightbackground="#54778C",highlightthickness=2)
        self.conteinerTop.place(relx=0.02,rely=0.020,relwidth=0.96,relheight=0.46)
        self.conteinerBotton = Frame(self.telaPrincipal,bg="#BAD0D9",bd=4,highlightbackground="#54778C",highlightthickness=2)
        self.conteinerBotton.place(relx=0.02,rely=0.50,relwidth=0.96,relheight=0.48)
     """
      # CRIA BOTÕES QUE VÃO DAR AÇÃO PARA A INTERFACE, VÃO PERMITIR INTERAÇÃO COM O USUARIO;
       - BOTÃO DE CADASTRAR COM POSICIONAMENTO RELATIVO AO CONTEINER;
       - BOTÃO DE ALTERAR COM POSICIONAMENTO RELATIVO AO CONTEINER;
       - BOTÃO DE APAGAR COM POSICIONAMENTO RELATIVO AO CONTEINER;
       - BOTÃO DE LIMPAR COM POSICIONAMENTO RELATIVO AO CONTEINER;
       - BOTÃO DE ALTERAR COM POSICIONAMENTO RELATIVO AO CONTEINER;
     """    
     def botoes(self):
          self.btn_limpar_campos_formualario = Button(self.conteinerTop,text="Limpar Campos")
          self.btn_limpar_campos_formualario.place(relx=0.2,rely=0.02,relwidth=0.16,relheight=0.10)
          self.btn_cadastrar = Button(self.conteinerTop,text="Cadastrar")
          self.btn_cadastrar.place(relx=0.36,rely=0.02,relwidth=0.12,relheight=0.10)
          self.btn_buscar = Button(self.conteinerTop,text="Buscar")
          self.btn_buscar.place(relx=0.6,rely=0.02,relwidth=0.10,relheight=0.10)
          self.btn_alterar = Button(self.conteinerTop,text="Alterar")
          self.btn_alterar.place(relx=0.70,rely=0.02,relwidth=0.10,relheight=0.10)
          self.bnt_apagar = Button(self.conteinerTop,text="Apagar")
          self.bnt_apagar.place(relx=0.8,rely=0.02,relwidth=0.10,relheight=0.10)
     
     """
      # CRIA WIDGETS INFORMATIVOS PARA O USUARIO;
        - CRIA LABELS PARA WIDGETS DE INPUTS DE ENTRADA DE TEXTO DO USUARIO;
        - CADA CAIXA DE TEXTO, DE INPUT, VAI TER UMA RESPECTIVA LABEL, INFORMATIVA;
        - LABEL INFORMATIVA PARA A CAIXA DE ENTRADA DE TEXTO(INPUT), DIZENDO QUE E O CODIGO DO USUARIO, DE ACORDO COM O BANCO DE DADOS;
        - LABEL INFORMATIVA DA CAIXA DE TEXTO NOME;
        - LABEL INFORMATIVA DA CAIXA DE TEXTO TELEFONE;
        - LABEL INFORMATIVA DO COMBOBOXBAIRRO BAIRRO;
        - LABEL INFORMATIVA DA CAIXA DE TEXTO CPF;
        - LABEL INFORMATIVA DO COMBO BOX ABRANGENCIA;
        - LABEL INFORMATIVA DE ENDEREÇO;
        - LABEL INFORMATIVA QUANTIDADE PESSOAS RESIDEM NA CASA;
     """
     def labels_informativas(self):
         self.lbl_codigo = Label(self.conteinerTop,text="Código")
         self.lbl_codigo.place(relx=0.03,rely=0.02,relwidth=0.10) 
         self.lbl_nome = Label(self.conteinerTop,text="Nome")
         self.lbl_nome.place(relx=0.03,rely=0.25)
         self.lbl_telefone = Label(self.conteinerTop,text="Telefone")
         self.lbl_telefone.place(relx=0.03,rely=0.50)
         self.lbl_local = Label(self.conteinerTop,text="Local")
         self.lbl_local.place(relx=0.32,rely=0.50)
         self.lbl_cpf = Label(self.conteinerTop,text="CPF")
         self.lbl_cpf.place(relx=0.6,rely=0.25)
         self.lbl_abrangencia = Label(self.conteinerTop,text="Abrangência")
         self.lbl_abrangencia.place(relx=0.6,rely=0.50)
         self.lbl_endereco = Label(self.conteinerTop,text="Endereço")
         self.lbl_endereco.place(relx=0.03,rely=0.75)
         self.lbl_qtd_casa = Label(self.conteinerTop,text="Quantidade Pessoas Residem Na Casa")
         self.lbl_qtd_casa.place(relx=0.6,rely=0.75)
     
     """
      # METODO QUE CRIA AS CAIXAS DE TEXTO, PARA O USUARIO, DIGITAR ENTRADA DE TEXTO;
       - USUARIO DIGITA INFOMRAÇÕES NAS CAIXAS DE TEXTO, E O PROGRAMADRO TRATA ESSAS ENTRADAS DE TEXTO;
       - SÃO CAIXAS DE TEXTO QUE SO ACEITAM UMA LINHA DE TEXTO, NÃO SE PODE QUEBRAR LINHA DENTRO DESSAS CAIXA DE TEXTO;
       - CAIXA DE TEXTO DO CODIGO DO CADASTRO DO USUARIO DE ACORDO COM O BANCO DE DADOS;
       - CAIXA DE TEXTO PARA USUARIO DIGITAR SEU NOME COMPLETO;
       - CAIXA DE TEXTO PARA USUARIO DIGITAR SEU TELEFONE;
       - CAIXA DE TEXTO PARA USUARIO DIGITAR SEU CPF;
       - CAIXA DE TEXTO PARA USUARIO DIGITAR SEU ENDEREÇO;
     """
     def caixaEntradaTexto(self):
         self.txtCodigo = Entry(self.conteinerTop) 
         self.txtCodigo.place(relx=0.03,rely=0.12,relwidth=0.10,relheight=0.10)
         self.txtNome= Entry(self.conteinerTop)
         self.txtNome.place(relx=0.03,rely=0.35,relwidth=0.54,relheight=0.10)
         self.txtTelefone = Entry(self.conteinerTop)
         self.txtTelefone.place(relx=0.03,rely=0.60,relwidth=0.25,relheight=0.10)
         self.txtCpf = Entry(self.conteinerTop)
         self.txtCpf.place(relx=0.6,rely=0.35,relwidth=0.30,relheight=0.10)
         self.txtEndereco = Entry(self.conteinerTop)
         self.txtEndereco.place(relx=0.03,rely=0.85,relwidth=0.54,relheight=0.10)

     
     """
      # CRIA UM JCOMBO BOX, PARA PODER SE TER VARIAS OPÇÕES DE ESCOLHA PADRONIZADAS PARA TODO CADASTRO DE UM CLIENTE;
       - O CLIENTE VAI PODER ESCOLHER QUAL BAIRRO ELE MORA, DE ACORDO COM TODAS AS OPÇÕES DISPONIVEIS NO COMBOBOX;
       - CLIENTE ESCOLHE O TIPO DE ABRANGENCIA QUE ELE MORA, SE E EM ZONA RURAL, OU ZONA URBANA;
     """
     def comboBox(self):
          self.lista_bairros = ["ESCOLHA UM LOCAL","SETOR SUL","BOSQUE II","BOSQUE I","VILA VERDE","FORMOSINHA"]
          self.txtLocal = ttk.Combobox(self.conteinerTop,value=self.lista_bairros)
          self.txtLocal.place(relx=0.32,rely=0.60,relwidth=0.25,relheight=0.10)
          # setando uma opção padrão para o bairro
          self.txtLocal.set("ESCOLHA UM LOCAL")
          self.lista_abrangencia = ["ESCOLHA A ABRANGÊNCIA","ZONA URBANA","ZONA RURAL"];
          self.txtAbrangencia = ttk.Combobox(self.conteinerTop,value=self.lista_abrangencia)
          self.txtAbrangencia.place(relx=0.6,rely=0.60,relwidth=0.30,relheight=0.10)
          # setando uma opção padrão para o combo box
          self.txtAbrangencia.set("ESCOLHA A ABRANGÊNCIA")
     
     """
      # NESTE METODO SE TRATA DO WIDGET SPIN BOX;
       - USUARIO VAI TER OPÇÕES DE INCREMENTAR E DECREMENTAR OPÇÕES DE VALORES INTEIROS;
       - ONDE USUARIO TERA QUE INFORMAR A QUANTIDADE DE PESSOAS QUE MORA NA SUA CASA;
     """
     def spinBox(self):
          self.txtQtdCasa = Spinbox(self.conteinerTop,from_=1,to=15)
          self.txtQtdCasa.place(relx=0.6,rely=0.85,relwidth=0.10,relheight=0.10)
          
     """
      # METODO QUE APLICA ESTILIZAÇÃO MODERNA NOS BOTÕES DA TELA PRINCIPAL;
       - somente configurações da borda do botão e da fonte e do tamanho da fonte;
     """     
     def estilizarBotoes(self): 
          self.btn_limpar_campos_formualario.configure(border=2,font=("arial",9,"normal"))
          self.bnt_apagar.configure(border=2,font=("arial",9,"normal"))
          self.btn_alterar.configure(border=2,font=("arial",9,"normal"))
          self.btn_buscar.configure(border=2,font=("arial",9,"normal"))
          self.btn_cadastrar.configure(border=2,font=("arial",9,"normal"))
     
     """
      # METODO QUE TERA A FUNÇÃO DE APLICAR UMA ESTILIZAÇÃO MODERNA NAS LABELS DA TELA PRINCIPAL;
       - SOMENTE APLICAR UMA COR DE FUNDO NA LABEL, E UMA COR DE FONTE;
       - configurando uma cor de fundo, e uma cor de fonte, e o tamanho da fonte;
     """
     def estilizarLabels(self):
          self.lbl_codigo.configure(bg="#BAD0D9",font=("arial",9,"bold"))
          self.lbl_nome.configure(bg="#BAD0D9",font=("arial",9,"bold"))
          self.lbl_cpf.configure(bg="#BAD0D9",font=("arial",9,"bold"))
          self.lbl_endereco.configure(bg="#BAD0D9",font=("arial",9,"bold"))
          self.lbl_qtd_casa.configure(bg="#BAD0D9",font=("arial",9,"bold"))
          self.lbl_local.configure(bg="#BAD0D9",font=("arial",9,"bold"))
          self.lbl_telefone.configure(bg="#BAD0D9",font=("arial",9,"bold"))
          self.lbl_abrangencia.configure(bg="#BAD0D9",font=("arial",9,"bold"))
     
     """
      # METODO QUE CRIA A LISTA DE CLIENTES CADASTRADOS NO SISTEMA, PARA FICAR DISPONIVEL PARA VISUALIZAÇÃO DO CLIENTE;
        - ESSA LISTA CONTERA DADOS DE TODOS OS CLIENTES;
        - TODOS OS DADOS DE CADA CLIENTE FICARA DISPONIVEL EM CADA LINHA DA TREE VIEW;
        - USUARIO PODERA VER CLIENTES CADASTRADOS;
        - PODERA SELECIONAR CLIENTES ATRAVES DA TREEVIEW;
        - PODERAR DELETAR CLIENTES ATRAVES DA TREE VIEW;
     """
     def treeViewClientes(self):
         self.tViewCli = ttk.Treeview(self.conteinerBotton,columns=("col0","col1","col2","col3","col4","col5","col6","col7"),show="headings")
         self.tViewCli.column("col0",minwidth=0,width=5) # coluna id
         self.tViewCli.column("col1",minwidth=0,width=150) # coluna nome
         self.tViewCli.column("col2",minwidth=0,width=30) # cpf
         self.tViewCli.column("col3",minwidth=0,width=30) # telefone
         self.tViewCli.column("col4",minwidth=0,width=50) # local
         self.tViewCli.column("col5",minwidth=0,width=50) # abrangencia(zona rural,urbana)
         self.tViewCli.column("col6",minwidth=0,width=75) # endereço
         self.tViewCli.column("col7",minwidth=0,width=5) # qtd pessoa residem na casa
         self.tViewCli.heading("col0",text="Código")
         self.tViewCli.heading("col1",text="Nome")
         self.tViewCli.heading("col2",text="CPF")
         self.tViewCli.heading("col3",text="Telefone")
         self.tViewCli.heading("col4",text="Local")
         self.tViewCli.heading("col5",text="Abrangência")
         self.tViewCli.heading("col6",text="Endereço")
         self.tViewCli.heading("col7",text="Qtd Pessoa Na Casa")
         self.tViewCli.place(relx=0.01,rely=0.01,relwidth=0.95,relheight=0.95)

     """
      # METODO QUE DEFINE BARRA DE ROLAGENS NA HORIZONTAL E NA VERTICAL;
        - BARRA DE ROLAGENS PARA A TREE VIEW, PORQUE PODE ACONTECER DE NÃO CONSEGUIR VISUALIZAR INFORMAÇÕES;
        - A BARRA DE ROLAGENS PERMITE PERCORRER TODA A TREE VIEW NA HORIZONTAL E VERTICAL, VISUALIZANDO TODAS INFORMAÇÕES;
     """
     def barraRolagens(self):         


