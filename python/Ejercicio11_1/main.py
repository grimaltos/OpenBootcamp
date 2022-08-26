import sqlite3
import os

con = sqlite3.connect('./Ejercicio11_1/personal.db')

def crear_tabla(con, consulta):
    cursor = con.cursor()
    cursor.execute(consulta)
    con.commit()
    return '---- Tabla creada ----'

def insertar_alumno(con, datos):
    cursor = con.cursor()
    sql = 'INSERT INTO Alumnos (id, nombre, apellido) VALUES (?, ?, ?)'
    cursor.execute(sql, datos)
    con.commit()
    return '---- Alumno guardado ----'

def listar_tabla(con):
    cursor = con.cursor()
    sql = 'SELECT * FROM Alumnos'
    cursor.execute(sql)
    records = cursor.fetchall()
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nListado de alumnos")
    for row in records:
        print(row[0], row[1], row[2])
    os.system("pause")
    os.system('cls' if os.name == 'nt' else 'clear')

def buscar_alumno(con, alumno):
    cursor = con.cursor()
    sql = f'SELECT * FROM Alumnos WHERE nombre LIKE \'%{alumno}%\''
    cursor.execute(sql)
    records = cursor.fetchall()
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nResultado de la busqueda")
    for row in records:
        print(row[0], row[1], row[2])
    os.system("pause")
    os.system('cls' if os.name == 'nt' else 'clear')


while(True):
    print('Seleccione que desea hacer:')
    print('1. Crear tabla Alumnos')
    print('2. Insertar datos alumno')
    print('3. Buscar alumno')
    print('4. Listar tabla Alumnos')
    print('5. Salir')
    opcion = 0
    while opcion < 1 or opcion > 5:
        opcion = int(input('Opción: '))
    match opcion:
        case 1:
            sql_tabla = "CREATE TABLE IF NOT EXISTS Alumnos (id INT NOT NULL, nombre CHAR(255) NOT NULL, apellido CHAR(255) NOT NULL);"
            os.system('cls' if os.name == 'nt' else 'clear')
            print(crear_tabla(con, sql_tabla))

        case 2:
            idalumno = int(input('Introduce el id del alumno: '))
            nombrealumno = input('Introduce el nombre del alumno: ')
            apellidoalumno = input('Introduce el apellido del alumno: ')
            datos = (idalumno, nombrealumno, apellidoalumno)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(insertar_alumno(con, datos))

        case 3:
            busquedaalumno = input('Introduce el nombre del alumno a buscar: ')
            buscar_alumno(con,busquedaalumno)

        case 4:
            listar_tabla(con)
        case 5:
            con.close()
            break

