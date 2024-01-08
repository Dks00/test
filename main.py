from flask import Flask, request, render_template, redirect, url_for
import subprocess

result = subprocess.run(["python", "./sqliteCreat.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

app = Flask(__name__)

# Ruta para la página principal
@app.route('/')
def index():
    return render_template('login.html')

# Ruta para manejar el login
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Aquí deberías verificar el username y password con la base de datos
    # Por ahora, lo dejaremos como un placeholder
    if username == "admin" and password == "password":
        return redirect(url_for('success'))
    else:
        return redirect(url_for('index'))

# Ruta que se muestra si el login es exitoso
@app.route('/success')
def success():
    return 'Logged in successfully'

if __name__ == '__main__':
    app.run(debug=True)
