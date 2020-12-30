from tkinter import *
from tkinter import ttk

"""
 * CLASSE QUE E RESPONSAVEL POR COSTRUIR OS WIDGETS GRAFICOS DA ABA SECRETARIA SOCIAL;
   - A CLASSE VIEWSECRETARIA HERDA TUDO DA CLASSE INTERFACE PRINCIPAL;
"""
class ViewSecretaria:
     """
       * METODO COSTRUTOR INICIALIZADOR DA CLASSE ViewSecretaria
     """
     def __init__(self,conteiner):
          self.conteinerAbaSecretaria = conteiner;  
          self.estilizarConteiner()  
          self.widgetLabels()
          self.estilizarLabels()
          self.fluxoTexto()
          self.optionMenu()
          self.estilizarWidgetOptionMenu()
          self.widgetCaixaTexto()
          self.estilizarWidgetText()
          self.widgetButtons()
          self.estilizarWidgetButtons()
          self.estilizarWidgetComboBox()
          self.widgetComboBox()

     """
      * ESTILIZANDO O CONTEINER;
        - ADD um cor de fundo ao conteiner;
     """     
     def estilizarConteiner(self):
         self.conteinerAbaSecretaria.configure(bg="#525252")

     """
        * METODO QUE CRIA OS WIDGETS LABELS - ROTULO;
          - CRIA LABELS PARA OS OUTROS COMPONENTES, SÃO LABELS INFORMATIVAS;
          - espaço entre uma label e uma widget de 0.3%
          - espaço entre um widget e uma nova label 0.5%
     """
     def widgetLabels(self):
         self.lblTipoBeneficio = Label(self.conteinerAbaSecretaria,text="Tipo de Beneficio")
         self.lblTipoBeneficio.place(relx=0.01,rely=0.05,relheight=0.10)
         self.lblDescricaoBeneficio = Label(self.conteinerAbaSecretaria,text="Descrição do Beneficio")
         self.lblDescricaoBeneficio.place(relx=0.01,rely=0.37,relheight=0.10)
         self.lblLocalBeneficio = Label(self.conteinerAbaSecretaria,text="Local Disponibilizara o beneficio")
         self.lblLocalBeneficio.place(relx=0.46,rely=0.20,relheight=0.12)
         self.lblServidorResponsavel = Label(self.conteinerAbaSecretaria,text="Servidor Responsavel")
         self.lblServidorResponsavel.place(relx=0.46,rely=0.54,relheight=0.12)


     """
      * ESTE METODO APLICA ESTILO NOS LABELS
        - METODO RESPONSAVEL POR FAZER A ESTILIZAÇÃO DO WIDGET LABEL
        - cor de fundo, fonte, tamanho da fonte, espaço interno da label e alinhamento do texto
     """ 
     def estilizarLabels(self): 
          self.lblTipoBeneficio.configure(bg="#BAD0D9",font=("arial",9,"bold"))         
          self.lblDescricaoBeneficio.configure(bg="#BAD0D9",font=("arial",9,"bold"))
          self.lblLocalBeneficio.configure(bg="#BAD0D9",font=("arial",9,"bold"))
          self.lblServidorResponsavel.configure(bg="#BAD0D9",font=("arial",9,"bold"))

     """
      * ESTE METODO CRIA  O WIDGET OPTION MENU

        - ESTE WIDGET E RESPONSAVEL POR LISTAR AS OPÇÕES DE TIPO DE BENEFICIO;
     """
     def optionMenu(self):
        self.listOpcoesTipoBeneficio = ["SELECIONE O TIPO DE BENEFICIO","ALIMENTICIO","SAUDE","MATERIAL","SOCIAL","FINANCEIRO","SAUDE MENTAL","AUXILIO EMEGERCIAL"]
        self.txtOpMenuTipoBeneficio.set(self.listOpcoesTipoBeneficio[0])
        self.opTipoBeneficio = OptionMenu(self.conteinerAbaSecretaria,self.txtOpMenuTipoBeneficio,*self.listOpcoesTipoBeneficio)
        self.opTipoBeneficio.place(relx=0.01,rely=0.20,relwidth=0.40,relheight=0.12)
        self.listOpcoesLocal = ["SELECIONE O LOCAL QUE DISPONIBILIZARA O BENEFICIO","CRAS-I","CRAS-II","SCFV VILA VERDE","SCFV PRAÇA CÉUS","SCFV JARDIM OLIVEIRA","SCFV SETOR SUL","CREAS","CASA DAS HORTENCIAS","CENTRO POP","SECRETARIA DESENVOLVIMENTO SOCIAL E TRABALHO"]
        self.txtOpMenuLocalBeneficio.set(self.listOpcoesLocal[0])
        self.opLocalBeneficio = OptionMenu(self.conteinerAbaSecretaria,self.txtOpMenuLocalBeneficio,*self.listOpcoesLocal)
        self.opLocalBeneficio.place(relx=0.46,rely=0.37,relwidth=0.53,relheight=0.12)


     """
      * ESTE METODO CRIA O FLUXO DE TEXTO

        - METODO RESPONSAVEL POR CONTROLAR TODO O FLUXO DE TEXTO DE ENTRADA E SAIDA DOS WIDGETS, USANDO O STRING VAR DAS CAIXAS;
     """
     def fluxoTexto(self):
        self.txtOpMenuTipoBeneficio = StringVar()
        self.txtInputOutputDescriBenef = StringVar()
        self.txtOpMenuLocalBeneficio = StringVar()
        self.txtInputOutputServidorResponsavel = StringVar()
     
     """
      * ESTE METODO ESTILIZA O COMPONENTE OPTION MENU
        
         - as opções de estilização do widget estão especificadas abaixo:
         - opção relief - add um estilo de borda ao componente;
         - opção borderwidth - add uma largura a borda;
         - font - fonte,tamanho,peso;
         - background = cor de fundo ao desenhar widget na tela;
         - foregound - cor do conteudo ao desenhar widget na tela;
         - activebackground - cor de fundo ao passar o mouse por cima do widget;
         - activeforeground - cor do conteudo ao passar o mouse por cima do widget;
         - highlightcolor - Especifica a cor a ser usada para o retângulo de destaque transversal que é desenhado ao redor do widget quando ele tem o foco de entrada;
         - highlightthickness - Especifica um valor não negativo indicando a largura do retângulo de destaque a ser desenhado ao redor do widget quando ele tem o foco de entrada;
     """
     def estilizarWidgetOptionMenu(self):
         self.opTipoBeneficio.configure(relief="raised",borderwidth=4,font=("Helvetica",9,"bold"),background="black",foreground="white",activebackground="black",activeforeground="white",highlightcolor="white",highlightthickness=2)
         self.opLocalBeneficio.configure(relief="raised",borderwidth=4,font=("Helvetica",9,"bold"),background="black",foreground="white",activebackground="black",activeforeground="white",highlightcolor="white",highlightthickness=2)


     """
       * ESTE METODO CRIA UM WIDGET CAIXA DE TEXTO

        - CRIA UM WIDGET DE TIPO CAIXA DE TEXTO, PARA RECEBER UM INPUT TEXT do usuario;
        - self.conteinerAbaSecretaria, o text esta dentro dessa aba de frame(conteiner)
        - textvariable=self.txtInputOutputDescriBenef - controla o fluxo de entrada e saida de texto
     """
     def widgetCaixaTexto(self):
        self.txtDescricaoBeneficio = Text(self.conteinerAbaSecretaria)
        self.txtDescricaoBeneficio.place(relx=0.01,rely=0.52,relwidth=0.40,relheight=0.45)

     
     """
      * ESTE METODO ESTILIZA O WIDGET TEXT

       - a estilização do componente TEXT
       - add uma borda de efeito 3D - relief="raised"
       - ao usuario digitar o texto dentro do componente o texto deve seguir essas opções de fonte - font=("arial",9,"bold")
     """
     def estilizarWidgetText(self):
         self.txtDescricaoBeneficio.configure(relief="raised",borderwidth=4,font=("arial",12,"bold"))


     """
      * ESTE METODO CRIA UM WIDGET DE TIPO BUTTON

       - o widget de tipo button e responsavel por fazer açoes, no formulario;
       - btnCadastrarBeneficio : cadastra um beneficio, obtem os dados do formulario e manda para as outras camadas do projeto para poder enviar e armazenar no banco de dados;
       - btnAtualizarBeneficio : atualiza um beneficio ja existente, que exista no banco de dados;
       - btnExcluirBeneficio : exclui um beneficio ja existente;
       - 
     """
     def widgetButtons(self):
         self.btnCadastrarBeneficio = Button(self.conteinerAbaSecretaria,text="Cadastrar Beneficio")
         self.btnCadastrarBeneficio.place(relx=0.22,rely=0.01,relwidth=0.19,relheight=0.13)
         self.btnAtualizarBeneficio = Button(self.conteinerAbaSecretaria,text="Atualizar Beneficio")
         self.btnAtualizarBeneficio.place(relx=0.46,rely=0.01,relwidth=0.19,relheight=0.13)
         self.btnExcluirBeneficio = Button(self.conteinerAbaSecretaria,text="Excluir Beneficio")
         self.btnExcluirBeneficio.place(relx=0.65,rely=0.01,relwidth=0.19,relheight=0.13)

     
     """
      * ESTE METODO ESTILIZA OS BOTÕES;
       
        - activebackground : ao usuario clicar no botão, muda a cor de fundo do botão;
        - relief : especifica um tipo de borda 3d ao widget, neste caso e um tipo de borda afundado;
        - borderwidth : largura da borda 3d desenhada;
        - activeforeground : cor do texto do botão ao clicar nele;
        - font : configura uma fonte, o tamanho e o peso da fonte do botão;
        - highlightbackground : Especifica a cor a ser exibida na região de destaque transversal quando o widget não tem o foco de entrada;
        - background : cor de fundo do botão;
        - foreground - cor do texto do botão;
        - highlightcolor : Especifica a cor a ser usada para o retângulo de destaque transversal que é desenhado ao redor do widget quando ele tem o foco de entrada;
        - highlightthickness : Especifica um valor não negativo indicando a largura do retângulo de destaque a ser desenhado ao redor do widget quando ele tem o foco de entrada;

     """
     def estilizarWidgetButtons(self):
        self.btnCadastrarBeneficio.configure(activebackground="#C2C2C2",relief="sunken",activeforeground="black",borderwidth=4,font=("TimesNewRoman",9,"bold"),highlightbackground="white",background="#1F1F1F",foreground="white",highlightcolor="white",highlightthickness=2)
        self.btnAtualizarBeneficio.configure(activebackground="#C2C2C2",relief="raised",activeforeground="black",borderwidth=4,font=("TimesNewRoman",9,"bold"),highlightbackground="white",background="#1F1F1F",foreground="white",highlightcolor="white",highlightthickness=2)
        self.btnExcluirBeneficio.configure(activebackground="#C2C2C2",relief="sunken",activeforeground="black",borderwidth=4,font=("TimesNewRoman",9,"bold"),background="#1F1F1F",foreground="white",highlightcolor="white",highlightthickness=2)

    
     """
      * ESTE METODO CRIA UM WIDGET COMBO BOX

        - cria o widget que vai mostrar a lista de servidores responsavel;
        - cria o widget combobox com os servidores que pertecem a secretaria social;
        - opções ao cria o widget:
        - textvariable : controla fluxo de entrada e saida do combobox;
        - value : mostra a lista de opções dos servidores;
        - justify="center" : a cada opção escolhida no combo box, quando tiver dentro do widget vai ficar alinhada dentro da caixa ao centro;
        - state="readonly" : deixa o widget com o estado de somente leitura, usuario não pode modificar;
        - style : define um estilo para o widget;

     """
     def widgetComboBox(self):
        self.listServidoresResponsaveis = ["ESCOLHA UM SERVIDORE RESPONSAVEL PELO BENEFICIO","SOLANGE - CHEFE","SINEUMA - CORDENADORA","ELISANGELA - ADMINISTRATIVO","MARCIA - ARTICULAÇÃO","GEOVANA - PSICOLOGA","LETICIA - ARTICULAÇÃO","PAULA FABIANE - ASSISTENTE SOCIAL ZONA RURAL","ANA PAULA - ASSISTENTE SOCIAL ZONA RURAL","MARIA JOSE - ASSISTENTE SOCIAL ZONA URBANA","LIVIA - ASSISTENTE SOCIAL ZONA URBANA","CAROLINE MARQUES - SECRETARIA GERAL","CAROL - COMUNICAÇÃO","GUILHERME - RH","GUILHERME 2 - RH","MARY - RH","CARLA - RH","IVONE - GERENCIADORA DE ESTOQUE","DANIELA - BOLSA FAMILIA"]
        self.cbServidor = ttk.Combobox(self.conteinerAbaSecretaria,value=self.listServidoresResponsaveis,textvariable=self.txtInputOutputServidorResponsavel,justify="center",state="readonly",style="TCombobox")
        self.cbServidor.place(relx=0.46,rely=0.71,relwidth=0.53,relheight=0.12)
        self.cbServidor.set("ESCOLHA UM SERVIDORE RESPONSAVEL PELO BENEFICIO")

     """
      * ESTE METODO ESTILIZA O COMBO BOX

       - cria uma objeto de estilo do ttk style para estilizar componentes do ttk;
       - dar as configurações de estilo informando o nome da classe de estilo pertecente ao widget ao estilizar, no caso o nome da classe de estilo para estilizar o combo box e Tcombobox, seguido de suas opções de estilização;
       - bordercolor : cor da borda do widget;
       - selectbackground : seleciona uma cor de fundo para o primeiro plano, ao selecionar o elemento, dentro do combobox;
       - selectforeground : selcionar uma cor do texto ao selecionar um elemento do combobox;
     """
     def estilizarWidgetComboBox(self):
         estiloComboBox = ttk.Style()
         estiloComboBox.configure("TCombobox",selectbackground="#1F1F1F",bordercolor="white",selectforeground="white")
