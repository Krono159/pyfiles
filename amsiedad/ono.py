import pymysql

try:
    uwu = pymysql.connect(host = 'localhost',
    user='root', password='',db='libros')
    try:
        with uwu.cursor() as owo: 
            print('recuerde usar el ID del libro para borrarlo de la base de datos. para consultar, vaya a search.py')
            owont = "DELETE FROM librowos WHERE ID = %s"
            del_id = input('que registro desea borrar?\t')
            owo.execute(owont,(del_id))
            uwu.commit()
            print('se ha borrado el registro #',del_id," de la base de datos")
    finally:
        uwu.close()
except(pymysql.err.OperationalError,pymysql.err.InternalError) as e:
    print('error! que paso? esto es todo lo que sabemos:  ',e)