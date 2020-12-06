
"""
 # ESTA CLASSE SIMULA O TABELA DO BANCO DE DADOS;
   - ELA SERVE PARA PODER ARMAZENAR E MANIPULAR OS DADOS DO USUARIO;
   - PODE MODIFICAR ALTERAR OS DADOS, ADD NOVOS ETC...
   - E O MODELO DA CLASSE BENEFICIARIO;
   - MODELO DA TABELA DO BANCO DE DADOS;
   - (_) indica que atributo e privado
"""
class ModeloBeneficiario():
      # costrutor inicializador da classe
      def __init__(self):
            
            self._nome = None;
            self._id_beneficiario = None;
            self._telefone = None;
            self._cpf = None;
            self._nis = None;
            self._endereco = None;
            self._bairro = None;
            self._abrangencia = None;
            self._qtd_pessoa_casa = None;
            self._rg = None;

      # metodos especiais acessores de atributos
      @property
      def getId(self):
            return self._id_beneficiario;
      def setId(self,id : int):
            self._id_beneficiario = id;
      @property
      def getFone(self) -> str:
           return self._telefone;
      def setFone(self,pTelefone : str):
            self._telefone = pTelefone;
      @property 
      def getCpf(self) -> str:
            return self._cpf;
      def setCpf(self,pCpf : str):
            self._cpf = pCpf;
      @property
      def getNis(self) -> str:
          return self._nis;
      def setNis(self,pNis : str):
           self._nis = pNis;
      @property
      def getEndereco(self) -> str: 
           return self._endereco;
      def setEndereco(self,pEndereco : str):
           self._endereco = pEndereco;
      @property
      def getBairro(self) -> str:
          return self._bairro;
      def setBairro(self,pBairro : str):
            self._bairro = pBairro;
      @property
      def getAbrangencia(self) -> str:
          return self._abrangencia;
      def setAbrangencia(self,pAbrangencia : str):
          self._abrangencia = pAbrangencia;
      @property
      def getQtdCasa(self) -> int:
          return self._qtd_pessoa_casa;
      def setQtdCasa(self,pQtdPessCasa : int):
           self._qtd_pessoa_casa = pQtdPessCasa;
      @property
      def getRg(self) -> str:
          return self._rg;
      def setRg(self,pRg : str):
            self._rg = pRg;  
      @property
      def getNome(self) -> str:
          return self._nome;
      def setNome(self,pNome : str):
           self._nome = pNome;
                
      
            