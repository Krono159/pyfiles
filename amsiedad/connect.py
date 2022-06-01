import imp
from operator import truediv


import pymysql

try:
    con = pymysql.connect(host = 'localhost',
    user='root', password='',db='libros')
    try:
        with con.cursor() as cursor: 
            cursor.execute ("SELECT id,isbn,titulo,anyo FROM libros")
            libros = cursor.fetchall()

            for libros in libros:
                print(libros)
    finally:
        con.close()
except(pymysql.err.OperationalError,pymysql.err.InternalError) as e:
    print('error! que paso? esto es todo lo que sabemos:  ',e)