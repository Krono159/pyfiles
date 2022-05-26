from dbm import _Database
from re import X
import mysql.connector
from flask import flask, render_template
app = flask(prueba)

@app.route("/")
def main():
    return "Bienvenido"

@app.route('/registro')
def registro():
    return render_template('registro.html')

if prueba == "__main__":
    app.run()

con = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="usuario"
)

objeto =con.cursor()

sql = "INSERT INTO usuario(name, arl) values (%s, %s)"
val = ("juan", "http://juan.com")

objeto.execute(sql, val)

con.commit()
print(objeto.rowcount, "Se inserto el registro")

objeto.execute("SELECT*FROM usuarios")

listar = objeto.fechall()

for x in listar:
    print(x)
    

con = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="usuario"
)

objeto =con.cursor()

sql = "DELETE FROM usuario WHERE name = '?'"


objeto.execute(sql)

con.commit()
print(objeto.rowcount, "Se elimino el registro")


con = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="usuario"
)

objeto =con.cursor()

sql = "UPDATE usuario SET name = '?' WHERE name = '?'"


objeto.execute(sql)

con.commit()
print(objeto.rowcount, "Se actualizó el registro")
