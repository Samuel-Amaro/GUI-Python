from View import ViewSecretariaSocial
import View.Interface_Principal as tela
from tkinter import ttk
from tkinter import tix
from tkinter import *
from Banco_Dados import conexaoBanco
from Dao import dao_Beneficiario


if __name__ == "__main__":
    tela.TelaPrincipal()
    c = conexaoBanco.conexaoBancoDados()
    c.ddlBanco()