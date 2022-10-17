from app import app
from flask import Flask, render_template, url_for, redirect
from flask import request
#IMPORTANDO BIBLIOTECA
import sqlite3

conn = sqlite3.connect('enterprise.db')

#DEFININDO CAMINHO DA PAGINA HOME
@app.route('/')


###############################################################
#DEFININDO CAMINHO DA PAGINA INDEX
@app.route('/index', methods=['GET','POST'])  # type: ignore

def index(): #FUNÇÃO INDEX
    if request.method == 'POST':
        getsala = request.form.get('sala')
        getcomputador = request.form.get('computador')
        getdescricao = request.form.get('descricao')
               
        print("SALA -", getsala)
        print("COMPUTADOR -",getcomputador)
        print("DESCRICAO -",getdescricao)
        
        conn = sqlite3.connect('enterprise.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tasks(room, computer, description )
            VALUES (?,?,?)""", (getsala, getcomputador, getdescricao)) #INSTRUÇÃO INPUT BD.
        conn.commit() #COMITANDO OS DADOS
        conn.close() #FECHANDO BANCO  

    else:
        print("SEM ENTRADA NO METODO POST")
        
    return render_template("index.html") #RECARREGA PÁGINA INDEX
################################################################

#chamando rota contatos
@app.route('/admin')
def admin():
    pagina = "Contatos"
    return render_template("admin.html", pagina = pagina)