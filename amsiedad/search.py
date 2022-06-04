import pymysql

try:
    con = pymysql.connect(host = 'localhost',
    user='root', password='',db='libros')
    try:
        with con.cursor() as cursor:
            print('por que desea consultar? \n1: id\n2: isbn\n3: titulo\n4: autor\n5: año\n6: estado\n7: todos')
            choice = input('')
            if choice == '1':
                aid = input('ingrese el id del libro:   ')
                if aid == '':
                    print('error de ingreso de datos, vuelva a ejecutar el programa.')
                else:
                    consulta = "SELECT id,isbn,titulo,autor,anyo,status FROM librowos WHERE id = %s"
                    cursor.execute(consulta%(aid))
                    libros = cursor.fetchall()

                    for librowos in libros:
                        print(librowos)
            elif choice == '2':
                aisbn = input('ingrese el isbn del libro:   ')
                if aisbn == '':
                    print('error de ingreso de datos, vuelva a ejecutar el programa.')
                else:
                    consulta = "SELECT id,isbn,titulo,autor,anyo,status FROM librowos WHERE isbn = %s"
                    cursor.execute(consulta%(aisbn))
                    libros = cursor.fetchall()

                    for librowos in libros:
                        print(librowos)
            elif choice == '3':
                atitle = input('ingrese el titulo del libro:   ')
                if atitle == '':
                    print('error de ingreso de datos, vuelva a ejecutar el programa.')
                else:
                    consulta = "SELECT id,isbn,titulo,autor,anyo,status FROM librowos WHERE titulo = %s"
                    cursor.execute(consulta%(atitle))
                    libros = cursor.fetchall()

                    for librowos in libros:
                        print(librowos)
            elif choice == '4':
                avar = input('ingrese el autor del libro:   ')
                if avar == '':
                    print('error de ingreso de datos, vuelva a ejecutar el programa.')
                else:
                    consulta = "SELECT id,isbn,titulo,autor,anyo,status FROM librowos WHERE autor = %s"
                    cursor.execute(consulta%(avar))
                    libros = cursor.fetchall()

                    for librowos in libros:
                        print(librowos)
            elif choice == '5':
                avar = input('ingrese el año del libro:   ')
                if avar == '':
                    print('error de ingreso de datos, vuelva a ejecutar el programa.')
                else:
                    consulta = "SELECT id,isbn,titulo,autor,anyo,status FROM librowos WHERE anyo = %s"
                    cursor.execute(consulta%(avar))
                    libros = cursor.fetchall()
                    for librowos in libros:
                        print(librowos)
            elif choice == '6':
                print('modulo deshabilitado')

            elif choice == '7' :
                cursor.execute("SELECT * FROM librowos")
                libros = cursor.fetchall()

                for librowos in libros:
                    print(librowos)
            else:
                print('dato invalido, se mostraran todos los libros registrados')
                cursor.execute("SELECT * FROM librowos")
                libros = cursor.fetchall()

                for librowos in libros:
                    print(librowos)
    finally:
        con.close()
except(pymysql.err.OperationalError,pymysql.err.InternalError) as e:
    print('error! que paso? esto es todo lo que sabemos:  ',e)