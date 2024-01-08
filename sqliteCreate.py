import sqlite3

conn = sqlite3.connect('users.db')
c = conn.cursor()

# Crear tabla
c.execute('''CREATE TABLE users (username text, password text)''')

# Insertar un usuario
c.execute("INSERT INTO users VALUES ('admin','password')")

# Guardar los cambios y cerrar
conn.commit()
conn.close()