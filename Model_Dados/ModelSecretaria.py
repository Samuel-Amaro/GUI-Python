"""
 * CLASSE DE MODELO DO BANCO DE DADOS

  - ESTA CLASSE MODELA A TABELA DO BANCO DE DADOS - tabela: secretaria_social
  - todos os campos criados nessa tabela, são de acordo com o banco de dados

"""
class ModelSecretariaSocial:
    # metodo inicializador costrutor 
    def __init__(self):
         self._idSecretaria = -1
         self._dataHora = ""
         self._tipoBeneficio = ""
         self._descricaoBeneficio = ""
         self._localForneceBeneficio = ""
         self._servidorResponsavel = ""

    # metodos acessores de atributos

    @property
    def getIdSecretaria(self):
        return self._idSecretaria
    def setIdSecretaria(self,id):
        self._idSecretaria = id
    @property
    def getDataHora(self):
        return self._dataHora
    def setDataHora(self,dataHora):
        self._dataHora = dataHora
    @property
    def getTipoBeneficio(self):
        return self._tipoBeneficio
    def setTipoBeneficio(self,tipoBeneficio):
        self._tipoBeneficio = tipoBeneficio
    @property
    def getDescricacaoBeneficio(self):
        return self._descricaoBeneficio
    def setDescricaoBeneficio(self,descricaoBeneficio):
        self._descricaoBeneficio = descricaoBeneficio
    @property
    def getLocalForneceBeneficio(self):
        return self._localForneceBeneficio
    def setLocalForneceBeneficio(self,localForneceBeneficio):
        self._localForneceBeneficio = localForneceBeneficio
    @property
    def getServidorResponsavel(self):
        return self._servidorResponsavel
    def setServidorResponsavel(self,servidorResponsavel):
        self._servidorResponsavel = servidorResponsavel

