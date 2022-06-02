import imp
from operator import truediv


import pymysql

try:
    con = pymysql.connect(host = 'localhost',
    user='root', password='',db='libros')
    try:
        with con.cursor() as cursor: 
            cursor.execute ("SELECT id,isbn,titulo,anyo,status FROM librowos")
            libros = cursor.fetchall()

            for librowos in libros:
                print(librowos)
    finally:
        con.close()
except(pymysql.err.OperationalError,pymysql.err.InternalError) as e:
    print('error! que paso? esto es todo lo que sabemos:  ',e)