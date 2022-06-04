from copyreg import constructor
from re import T
import pymysql
try:
    con = pymysql.connect(host = 'localhost',
    user='root', password='',db='libros')
    try:
        with con.cursor() as owo:
            consulta = "UPDATE librowos SET status = %s WHERE id = %s"
            c = input('En que estado esta el libro ahora?\n1: prestado\n2: disponible\n3: perdido\n4: en reparacion\n5: dañado\n6: irreparable\n')
            if c == '1':
                new_status = 'prestado'
            elif c == '2':
                new_status = 'disponible'
            elif c == '3':
                new_status = 'perdido'
            elif c == '4':
                new_status = 'en reparacion'
            elif c == '5':
                new_status = 'dañado pendiente de reparacion'
            elif c == '6':
                new_status = 'dañado, irreparable'
            else:
                raise(pymysql.OperationalError)
            new_id = 1
            owo.execute(consulta,(new_status,new_id))
            con.commit()
    finally:
        con.close()
except(pymysql.err.OperationalError,pymysql.err.InternalError) as e:
    if e != '':
        print('error! que paso? esto es todo lo que sabemos:  ',e)
    else:
        print('error! no sabemos que paso')