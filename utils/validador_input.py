"""
 # ESTA CLASSE FAZ VALIDAÇÕES DE ENTRADA DE TEXTO
"""
class validadorEntradaTexto:
      def __init__(self):
            self.textoCaixa = ""
            super().__init__()
    
      """
       # ESTE METODO FAZ A VALIDAÇÃO DE ENTRADA DE DADOS DE CODIGO ID;
         - A CAIXA DE TEXTO CODIGO SO PODE RECEBER VALORES NUMERICOS DE NO MAXIMO DUAS CASAS ISSO E DEZENA CENTENA OU MILHAR;
         - NÃO PODE RECEBER ENTRADA DE TIPO STRING;
         - A CAIXA DE TEXTO CODIGO SO PODE RECEBER ATE DOIS NUMEROS INTEIROS;
      """  
      def valida_codigo_id(self,text):
         self.textoCaixa = text 
         try:
               #print("oque tem no text input: %s " % (self.textInput))
               # se caixa de texto estiver vazia
               if(self.text.isdigit()):
                  return True;
                  try:
                      # converte o texto para numero
                      valor_numerico = int(text)
                  except ValueError as i:
                         print(i)
                         return False;
                  finally:
                           return 0 <= valor_numerico <= 100;
               else:
                     print("NÃO PODE TRATAR A ENTRADA DE TEXTO SE A CAIXA NÃO ESTIVER VAZIA")
                     return False;  
         except AttributeError as identifier:
            print("-"*30)
            print(f"ERRO AO VALIDAR ENTRADA DA CAIXA DE TEXTO ID: {identifier}")
            return False;
              
