from tkinter import *

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
          self.widgetLabels()
          self.estilizarLabels()
          self.fluxoTexto()
          self.optionMenu()
          
      
     """
        * METODO QUE CRIA OS WIDGETS LABELS - ROTULO;
          - CRIA LABELS PARA OS OUTROS COMPONENTES, SÃO LABELS INFORMATIVAS;
     """
     def widgetLabels(self):
         self.lblTipoBeneficio = Label(self.conteinerAbaSecretaria,text="Tipo de Beneficio")
         self.lblTipoBeneficio.place(relx=0.01,rely=0.05,relheight=0.10)


     """
      * ESTE METODO APLICA ESTILO NOS LABELS
        - METODO RESPONSAVEL POR FAZER A ESTILIZAÇÃO DO WIDGET LABEL
        - cor de fundo, fonte, tamanho da fonte, espaço interno da label e alinhamento do texto
     """ 
     def estilizarLabels(self): 
          self.lblTipoBeneficio.configure(bg="#BAD0D9",font=("arial",9,"bold"))         
         

     """
      * ESTE METODO CRIA  O WIDGET OPTION MENU

        - ESTE WIDGET E RESPONSAVEL POR LISTAR AS OPÇÕES DE TIPO DE BENEFICIO;
     """
     def optionMenu(self):
        self.listOpcoesTipoBeneficio = ["SELECIONE O TIPO DE BENEFICIO","ALIMENTICIO","SAUDE","MATERIAL","SOCIAL","FINANCEIRO","SAUDE MENTAL","AUXILIO EMEGERCIAL"]
        self.txtOpMenuTipoBeneficio.set(self.listOpcoesTipoBeneficio[0])
        self.opTipoBeneficio = OptionMenu(self.conteinerAbaSecretaria,self.txtOpMenuTipoBeneficio,*self.listOpcoesTipoBeneficio)
        self.opTipoBeneficio.place(relx=0.01,rely=0.18,relwidth=0.33,relheight=0.10)
     """
      * ESTE METODO CRIA O FLUXO DE TEXTO

        - METODO RESPONSAVEL POR CONTROLAR TODO O FLUXO DE TEXTO DE ENTRADA E SAIDA DOS WIDGETS, USANDO O STRING VAR DAS CAIXAS;
     """
     def fluxoTexto(self):
        self.txtOpMenuTipoBeneficio = StringVar()

     
