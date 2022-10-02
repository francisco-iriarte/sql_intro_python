#!/usr/bin/env python

'''
SQL Introducción [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import sqlite3

# https://extendsclass.com/sqlite-browser.html


def create_schema():

    # Conectarnos a la base de datos
    # En caso de que no exista el archivo se genera
    # como una base de datos vacia
    conn = sqlite3.connect('secundaria.db')

    # Crear el cursor para poder ejecutar las querys
    c = conn.cursor()

    # Ejecutar una query
    c.execute("""
                DROP TABLE IF EXISTS estudiante;
            """)

    # Ejecutar una query
    c.execute("""
            CREATE TABLE estudiante(
                [id] INTEGER PRIMARY KEY AUTOINCREMENT,
                [name] TEXT NOT NULL,
                [age] INTEGER NOT NULL,
                [grade] INTEGER,
                [tutor] TEXT
            );
            """)

    # Para salvar los cambios realizados en la DB debemos
    # ejecutar el commit, NO olvidarse de este paso!
    conn.commit()

    # Cerrar la conexión con la base de datos
    conn.close()


def fill():
    
    # Llenar la tabla de la secundaria con al menos 5 estudiantes
    # Cada estudiante tiene los posibles campos:
    # id --> este campo es auto incremental por lo que no deberá completarlo
    # name --> El nombre del estudiante (puede ser solo nombre sin apellido)
    # age --> cuantos años tiene el estudiante
    # grade --> en que año de la secundaria se encuentra (1-6)
    # tutor --> nombre de su tutor
    conn = sqlite3.connect('secundaria.db')
    c = conn.cursor()

    alumnos = [('Aguilera Silvia Itati', 12, 2, 'Percara Estela'),
               ('Blumaagen Milton', 17, 7, 'Blumaagen Dario Javier'),
               ('Demczuk Claudia Beatriz', 13, 3,'Munitz Iriel Esperanza'),
               ('Ruiz Diaz Sonia', 14, 4,'Lugrin Ana María'),
               ('Vianna Germán Ignacio', 14, 4,'Vianna Ismael'),
               ]

    c.executemany("""
        INSERT INTO estudiante (name, age, grade, tutor)
        VALUES (?,?,?,?);""", alumnos)
    # Se debe utilizar la sentencia INSERT.
    # Observar que hay campos como "grade" y "tutor" que no son obligatorios
    # en el schema creado, puede obivar en algunos casos completar esos campos
    conn.commit()

    conn.close()

def fetch():
    print('Comprobemos su contenido, ¿qué hay en la tabla?')
    # Utilizar la sentencia SELECT para imprimir en pantalla
    # todas las filas con todas sus columnas
    # Utilizar fetchone para imprimir de una fila a la vez
    conn = sqlite3.connect('secundaria.db')
    c = conn.cursor()
    c.execute('SELECT * FROM estudiante')

    datos_todos = c.fetchall()
    print(datos_todos)
    #conn.close()

    # Utilizar fetchone para imprimir de una fila a la vez
    conn = sqlite3.connect('secundaria.db')
    c = conn.cursor()
    c.execute('SELECT * FROM estudiante')

    while True:
        linea = c.fetchone()
        if linea is None:
            break
        print(linea)
    #    conn.close()
    #
    #
def search_by_grade():
    
    # Utilizar la sentencia SELECT para imprimir en pantalla
    # aquellos estudiantes que se encuentra en en año "grade"
    print('Operación búsqueda por grado!')
    grado = int(input('Ingrese el grado a buscar: '))
    # De la lista de esos estudiantes el SELECT solo debe traer
    # las siguientes columnas por fila encontrada:
    # id / name / age
    conn = sqlite3.connect('secundaria.db')
    c = conn.cursor()
    datos = c.fetchone()
    print(grado)
    print(datos)
    c.execute('SELECT id, name, age FROM estudiante WHERE grade = ?', (grado, ))
    datos = c.fetchall()
    print(datos)
    while True:
        linea = c.fetchone()
        if linea is None:
            break
        print(linea)
    conn.close()

def insert_new_student():
    print('                ')
    print('                ')
    print('Nuevos ingresos!')
    print('----------------')
    print('ingresar un nuevo estudiante')
    new_student = input('Ingrese el nombre: ')
    new_age = input('Ingrese la edad: ') 
    # Utilizar la sentencia INSERT para ingresar nuevos estudiantes
    # a la secundaria
    conn = sqlite3.connect('secundaria.db')
    c = conn.cursor()
    values = [new_student, new_age]

    c.execute("""
        INSERT INTO estudiante (name, age)
        VALUES (?,?);""", values)
    datos = c.fetchone()
    print(datos)
    # Para salvar los cambios realizados en la DB 
    # debemos ejecutar el commit
    datos = c.fetchall()
    print(datos)
    while True:
        linea = c.fetchone()
        if linea is None:
            break
        print(linea)
    conn.commit()
    # Cerrar la conexión con la base de datos
    conn.close()  

def modify(id, name):
    print('Modificando la tabla')
    # Utilizar la sentencia UPDATE para modificar aquella fila (estudiante)
    # cuyo id sea el "id" pasado como parámetro,
    # modificar su nombre por "name" pasado como parámetro


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    create_schema()   # create and reset database (DB)
    fill()
    fetch()

    # grade = 3
    # search_by_grade(grade)

    
    search_by_grade()
    
    
    insert_new_student()
    #['You', 16]
    # insert(new_student)
    
    #name = '¿Inove?'
