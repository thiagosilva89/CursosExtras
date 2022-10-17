#IMPORTANDO ESTRUTURA APP FLASK
from app import app
from flask import Flask, render_template, url_for, request, redirect
import os
 
#IMPORTANDO BIBLIOTECA
import sqlite3

#DEFININDO COMUNICAÇÃO COM BANCO.
conn = sqlite3.connect('enterprise.db')



if __name__ == 'main':
    port = int(os.getenv('PORT'), '5000')
    app.run(host='0.0.0.0', port=port)


@app.route('/index', methods=['POST'])
def my_form():
    if request.method == 'POST':
     cursor = conn.cursor()
     guest_sala = request.form.get('sala')
     guest_computador = request.form.get('computador')
     guest_descricao = request.form.get('descricao')
	    
     try:
            cursor.execute("""INSERT INTO tasks(room, computer, description) VALUES (?,?,?),""",(guest_sala, guest_computador, guest_descricao))
    
            #COMITANDO OS DADOS    
            conn.commit()
            return redirect('/')
     except:
            return render_template('index.html')

#DEFINNINDO CURSOR 

