import imp
import pymysql
try:
    con = pymysql.connect(host = 'localhost',
    user='root', password='',db='libros')
    try:
        with con.cursor() as cursor:
            isbna=input('ingrese ISBN del libro: \t')
            tituloa = input('ingrese titulo del libro: \t')
            autora = input('ingrese nombre del autor:\t')
            anyoa = input('ingrese año de publicacion del libro:\t')
            disponiblea = input('el libro esta disponible o prestado? \t')
            consulta = "INSERT INTO librowos (isbn,titulo,autor,anyo,status) VALUES(%s,%s,%s,%s,%s);"
            cursor.execute(consulta,(isbna,tituloa,autora,anyoa,disponiblea))
        con.commit()
    finally:
        con.close
except(pymysql.err.OperationalError,pymysql.err.InternalError) as e:
    print('error! que paso? esto es todo lo que sabemos:  ',e)