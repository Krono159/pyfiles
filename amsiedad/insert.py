import pymysql
try:
    con = pymysql.connect(host = 'localhost',
    user='root', password='',db='libros')
    try:
        with con.cursor() as cursor:
            consulta = "INSERT INTO libros (isbn,titulo,anyo) VALUES(%s,%s,%s);"
            cursor.execute(consulta,('9789875452114','La serpiente y el mar','2005'))
        con.commit()
    finally:
        con.close
except(pymysql.err.OperationalError,pymysql.err.InternalError) as e:
    print('error! que paso? esto es todo lo que sabemos:  ',e)