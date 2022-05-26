from dbm import _Database
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

con.
    