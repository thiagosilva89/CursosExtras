# IMPORTANDO BIBLIOTECA FLASK
from flask import Flask


#ESTRUTURA PADRÃO PARA DEFINIÇÃO APP DENTRO DO FLASK
app = Flask(__name__)

#INSTANCIANDO APP PARA IMPORTAR AS ROUTES QUE ESTÁ EM OUTRA APLICAÇÃO CRIADA NA MESMA ESTRUTURA DO APP.
from app import routes