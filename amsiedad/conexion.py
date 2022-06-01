import pymysql
try:
    con = pymysql.connect(host = 'localhost',
    user='root', password='',db='libros')
    print('base de datos conectada')
    try:
        with con.cursor() as cursor:
            consulta = "INSERT INTO libros (isbn,titulo,anyo) VALUES(%s,%s,%s);"
            cursor.execute(consulta,('','',''))
    finally:
        con.close()
except(pymysql.err.OperationalError,pymysql.err.InternalError) as e:
    print('error! que paso? esto es todo lo que sabemos:  ',e)