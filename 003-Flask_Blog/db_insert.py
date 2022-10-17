#IMPORTANDO BIBLIOTECA
import sqlite3

#DEFININDO COMUNICAÇÃO COM BANCO.
conn = sqlite3.connect('enterprise.db')

#ESTRUTURA DO BANCO CRIADO.
""" 	"id"	INTEGER NOT NULL,
	    "room"	TEXT NOT NULL,
	    "computer"	TEXT NOT NULL,
	    "description"	TEXT NOT NULL,
	    PRIMARY KEY("id" AUTOINCREMENT) """
     
     
     
""" #EXEMPLO DE INPUT DOS DADOS ATRAVES DE UMA LISTA
chamados = [
    {"room":"302", "computer":"G151804", "description": "MOUSE COM CABO ROMPIDO."}
    {"room":"402", "computer":"SL01FAS", "description": "TECLADO DANIFICADO."}
    {"room":"322", "computer":"H1923-A", "description": "COMPUTADOR NÃO LIGA."}
    ]

 """

#DEFINNINDO CURSOR 
cursor = conn.cursor()
test = True
if test == True:
    cursor.execute("""      
        INSERT INTO tasks
        (
            room,
            computer,
            description
        )
        VALUES ('456', 'AasdsadDFGG-A', 'FALHsadadsasA NO MOUSE')
    """
    )
    
#COMITANDO OS DADOS    
conn.commit()


cursor.execute("SELECT * FROM tasks")
print(cursor.fetchall())

#CLOSE CONNECTION
conn.close()
