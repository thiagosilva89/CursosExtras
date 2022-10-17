#ANTES INSTALAR BIBLIOTECA  pip install sqlite3
#IMPORTANDO  SQLLITE3
from app import app
import sqlite3

#CRIANDO CONEXÃO COM BD
conn = sqlite3.connect('enterprise.db')

#DEFININDO CURSOR DB
cursor = conn.cursor()

#CRIANDO TABELA SQL ESSE COMANDO EXECUTA SOMENTE UMA VEZ PARA CRIAR APÓS ESSA EXECUÇÃO COLOCAR EM COMMETN
cursor.execute("""
               
    CREATE TABLE "tasks" 
    (
	    "id"	INTEGER NOT NULL,
	    "room"	TEXT NOT NULL,
	    "computer"	TEXT NOT NULL,
	    "description"	TEXT NOT NULL,
	    PRIMARY KEY("id" AUTOINCREMENT)
    );
""")

#print("table create sucess")

#FECHANDO COMUNICAÇÃO COM BANCO.
conn.close