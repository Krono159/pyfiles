import imp
from operator import truediv


import pymysql

try:
    uwu = pymysql.connect(host = 'localhost',
    user='root', password='',db='libros')
    try:
        with uwu.cursor() as owo: 
            owont = "DELETE FROM librowos WHERE ID = %s"
            del_id = '1'
            owo.execute(owont,(del_id))
            uwu.commit()

    finally:
        uwu.close()
except(pymysql.err.OperationalError,pymysql.err.InternalError) as e:
    print('error! que paso? esto es todo lo que sabemos:  ',e)