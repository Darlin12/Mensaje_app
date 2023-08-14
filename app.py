from flask import Flask

# Crea una instancia de la aplicación Flask
app = Flask(__name__)

# Ruta de la página principal
@app.route('/')
def hello():
    return "¡Hola, bienvenido a mi aplicación web!"

# Inicia el servidor cuando se ejecuta el script
if __name__ == '__main__':
    app.run()
