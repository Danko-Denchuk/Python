import sqlite3, datetime


string_text = input('Write something')
entero = input('Input a number')
floatable = input('Input a decimal')

try: entero = int(entero)
except ValueError:
    print('No es un entero')
    exit()
try: floatable = float(floatable) or int(floatable)
except ValueError:
    print('No es un decimal')
    exit()

# Connect to the db

conn = sqlite3.connect('connect.odb')
consulta = conn.cursor()

# Argument values

args = (string_text, entero, floatable, datetime.datetime.today())

# Consulta

sql = """
INSERT INTO test(string_text, entero, floatable, fecha)
VALUES(?, ?, ?, ?)
"""
if (consulta.execute(sql, args)):
    print("Registro guardado con exito")
else:
    print("No hay suerte")

consulta.close()
conn.commit()
conn.close()
