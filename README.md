# GUI-Python
Projeto de exemplo que usa o pyhton tkinter, uma GUI python aplicada, a um problema real, projeto envolve uso de banco de dados, e consumo de algumas API,
e bibliotecas externas proprias do python
# Ferramentas Necessarias
  * [Python versão 3.9.0](https://www.python.org/)
  * [Tkinter](https://docs.python.org/pt-br/3/library/tkinter.ttk.html)
  * Editor de Código;
  * [API-SQLite3 Python](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.fetchall);
# Tkinter
Para utilizar o python tkinter basta istalar a versão mais recente do python, 
e seguir as importações a seguir em seu projeto e tera todos os widgets disponiveis no tkinter para usar em seu projeto  
  ```
  from tkinter import *
  from tkinter import ttk
  ```
## Istalar Sqlite3 usando gerenciador de pacotes pip
```
 pip install sqlite3-api
```
## API SQLite3 No Python
```
 from sqlite3 import *
```
## Banco-Dados
 * Modelo logico do banco de dados que deve ser implementado;
 * [Modelo-Logico-Db](https://github.com/Samuel-Amaro/GUI-Python/blob/main/Documentacao/Banco-Dados/modelo-logico-banco.pdf)
 
## Executavel do Projeto
  * Para se criar o executavel do projeto usa-se o [pyinstaller](https://www.pyinstaller.org/)
  ```
   pip install pyinstalle
   # para criar  o .exe no seu SO
   # no terminal execute
   pyinstaller yourprogram.py
  ```
  * Compativel com Windows 10;
  * Não e Multiplataforma;
  * O Executavel e compativel somente em SO em que ele foi gerado(No caso Windows 10);
  * [Executavel de teste do Projeto](https://github.com/Samuel-Amaro/GUI-Python/tree/main/dist)
  
## Prototipos Interface

 * **Prototipo Interface Beneficiario**
 
 
 ![Prototipo Beneficiario](https://github.com/Samuel-Amaro/GUI-Python/blob/main/Documentacao/Prototipos-Interface-GUI/0001.jpg)
