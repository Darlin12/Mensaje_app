from app import app

def test_hello():
    # Crear un cliente de prueba para la aplicación Flask
    client = app.test_client()

    # Realizar una solicitud GET a la ruta principal
    response = client.get('/')

    # Validar el código de estado de la respuesta
    assert response.status_code == 200

    # Validar el contenido de la respuesta como texto
    expected_message = "¡Hola, bienvenido a mi aplicación web!"
    assert expected_message in response.data.decode('utf-8')  # Decodifica bytes a cadena UTF-8
