from flask import Flask, render_template

app = Flask(__name__)

#Criar a primeira pagina do site
#route para criar caminho depois do seu dominio
@app.route("/")

#função o que vocÊ quer exibir naquela página.


#função o que vocÊ quer exibir naquela página.
def homepage(): 
    return render_template("homepage.html")


def contatos(): 
    return render_template("contatos.html")
#colocar site no ar
if __name__ == "__main__":
    app.run(debug=True)

