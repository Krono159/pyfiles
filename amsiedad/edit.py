from copyreg import constructor
from re import T
import pymysql
try:
    con = pymysql.connect(host = 'localhost',
    user='root', password='',db='libros')
    try:
        with con.cursor() as owo:
            consulta = "UPDATE librowos SET status = %s WHERE id = %s"
            new_status = 'prestado'
            new_id = 1
            owo.execute(consulta,(new_status,new_id))
            con.commit()
    finally:
        con.close()
except(pymysql.err.OperationalError,pymysql.err.InternalError) as e:
    print('error! que paso? esto es todo lo que sabemos:  ',e)