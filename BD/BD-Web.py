from flask import Flask, render_template, request
import pymysql.cursors


# Creando a conexão com o Bando de Dados -> importante já ter ele salvo.
host = 'localhost'
user = 'root'
password = 'password'
#Definindo o Banco de Dados a ser Usado
database = 'Deputados'
# Estabelecendoa conexão
connection = pymysql.connect(host=host, user=user, password=password, database=database,cursorclass=pymysql.cursors.DictCursor)
# Fechando Conexão


app = Flask(__name__)


@app.route('/')
def deputados():
    with connection.cursor() as cursor:
        query_args = []
        if request.args.get("search"):
            sql = "SELECT * FROM `deputados` WHERE LOWER(`nome`) LIKE LOWER(%s) ORDER BY `nome` ASC"
            search = "%{}%".format(request.args["search"])
            query_args = [search]
        else:
            sql = "SELECT * FROM `deputados` ORDER BY `nome` ASC"
        cursor.execute(sql, query_args)
        deputados = cursor.fetchall()

    return render_template("deputados.html", deputados=deputados, search=request.args.get("search"))



if __name__ == '__main__':
    app.run(debug = True)