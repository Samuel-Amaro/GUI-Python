from Model_Dados import ModelBeneficiario

class ControleBeneficiario():
    def __init__(self):
        self.objBenef = ModelBeneficiario.ModeloBeneficiario()
        super().__init__()
    
    """
       # METODO QUE FAZ AS VALIDAÇÃO DE CADASTRO PARA UM BENEFICIARIO;
         - CAMPOS OBRIGATORIOS QUE DEVEM SER PREENCHIDOS:
           - id; - telefone; - cpf; - endereço; - bairro; - abrangencia; - moradores_casa; - nome;
         - CAMPOS NÃO OBRIGATORIOS NO CADASTRO DO BENEFICIARIO:
           - nis(so se tiver); - rg(caso não possua cpf);
    """
    def controlerSetInsertBeneficiario(self,novoBeneficiario : ModelBeneficiario.ModeloBeneficiario):
        self.objBenef = novoBeneficiario;
        if(self.objBenef.getFone != "" and self.objBenef.getCpf != "" and self.objBenef.getEndereco != "" and (self.objBenef.getBairro != "" and self.objBenef.getBairro != "ESCOLHA UM LOCAL") and (self.objBenef.getAbrangencia != "" and self.objBenef.getAbrangencia != "ESCOLHA A ABRANGÊNCIA") and self.objBenef.getQtdCasa > 0 and self.objBenef.getNome != ""):
           return True; 
        else:
            return False;
    
    """
     - ESTE METODO FAZ AS VERIFICAÇÕES DE CAMPOS DO CADASTRO DO BENEFICIARIO;
     - FAZ A VALIDAÇÃO DO SUA ATUALIZAÇÃO PARA VER SE ESTA TUDO CORRETO;
     - E VERIFICA SE TODOS OS CAMPOS OBRIGATORIOS ESTÃO PRENCHIDOS;
    """
    def controlerAtualizaCadBenef(self,modelBenef : ModelBeneficiario.ModeloBeneficiario):
        if(modelBenef == None):
           print("----------------------------------------")
           print("Não pode Atualizar um beneficiario vazio");
           print("----------------------------------------")
        else:
            # verifica se os campos estão com dados 
            if(modelBenef.getFone != "" and modelBenef.getNis != "" and (modelBenef.getAbrangencia != "" and modelBenef.getAbrangencia != "ESCOLHA A ABRANGÊNCIA") and (modelBenef.getBairro != "" and modelBenef.getBairro != "ESCOLHA UM LOCAL") and modelBenef.getEndereco != "" and modelBenef.getNome != "" and modelBenef.getQtdCasa > 0):
               return True;
            else:
               return False;


    
